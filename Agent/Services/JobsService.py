import contextlib
from typing import Type,Dict,Any
import threading
from Domain.Interface.IJobsService import IJobsService
from Infrastruncture.Data.Repository.Json.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.RabbitMQ.Interfaces import IRabbitConsumerRepository,IRabbitPublisherRepository
import json
import asyncio

class JobsService(IJobsService):
    
    def __init__(self,jobRepository: Type[IJobsRepository],rabbitConsumerRepository: Type[IRabbitConsumerRepository],rabbitPublishRepository:Type[IRabbitPublisherRepository]) -> None:

        self.__jobRepository = jobRepository
        self.__rabbitConsumerRepository = rabbitConsumerRepository
        self.__rabbitPublishRepository = rabbitPublishRepository
        self.__consumer_thread = None
    
    async def consultar_jobs_id(self, id):
        return await self.__jobRepository.get_dados_by_id(job_id=id)
    
    async def consultar_configuracao(self):
        return await self.__jobRepository.get_dados()
    
    async def atualizar_configuracao(self, dados:Dict[str,Any]):
        resultado_id,resultado_json = await self.__jobRepository.update_dados(dados)
        serialize_str = json.dumps(resultado_json['jobs'])
        notificar_centralizador = await self.__rabbitPublishRepository.enviar_mensagem(serialize_str)
        return True
    
    async def inserir_job(self, job:Dict[str,Any]):
        with contextlib.suppress(Exception):
            pass

    async def consumindo_mensagem(self):
        try:
            if self.__consumer_thread is None or not self.__consumer_thread.is_alive():
                self.__consumer_thread = threading.Thread(target=self.__rabbitConsumerRepository.iniciar_consumidor, args=('apiagente',self.__on_message_received,))
                self.__consumer_thread.start()
                print('Consumer thread started.')
        except Exception as ex:
            raise Exception(str(ex))
        
    def __on_message_received(self, message,ch,method): 
        try:
            mensagemJson =json.loads(message.decode('utf8'))
            asyncio.run(self.__jobRepository.update_dados(mensagemJson))
            # ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as ex:
            ch.basic_nack(delivery_tag=method.delivery_tag)  # Rejeitar a mensagem em caso de erro
            print(f"Error processing message: {str(ex)}")
            raise Exception(str(ex))