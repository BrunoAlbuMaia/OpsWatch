import contextlib
from typing import Type,Dict,Any
import threading
from Domain.Interface.IJobsService import IJobsService
from Infrastruncture.Data.Repository.Json.Interfaces.IJobsRepository import IJobsRepository
from Infrastruncture.Data.Repository.RabbitMQ.Interfaces.IRabbitConsumerRepository import IRabbitConsumerRepository


class JobsService(IJobsService):
    
    def __init__(self,jobRepository: Type[IJobsRepository],rabbitRepository: Type[IRabbitConsumerRepository]) -> None:

        self.__jobRepository = jobRepository
        self.__rabbiRepository = rabbitRepository
        self.__consumer_thread = None
    
    async def consultar_jobs_id(self, id):
        return await self.__jobRepository.get_dados_by_id(job_id=id)
    
    async def consultar_configuracao(self):
        return await self.__jobRepository.get_dados()
    
    async def atualizar_configuracao(self, dados:Dict[str,Any]):
        return await self.__jobRepository.update_dados(dados)
    
    async def inserir_job(self, job:Dict[str,Any]):
        with contextlib.suppress(Exception):
            pass

    async def consumindo_mensagem(self):
        try:
            if self.__consumer_thread is None or not self.__consumer_thread.is_alive():
                self.__consumer_thread = threading.Thread(target=self.__rabbiRepository.iniciar_consumidor, args=('apiagente',self.__on_message_received,))
                self.__consumer_thread.start()
                print('Consumer thread started.')
        except Exception as ex:
            raise Exception(str(ex))
        
    def __on_message_received(self, message):
        # Ação com base na mensagem recebida
        print(f'Message received: {message}')