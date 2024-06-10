import time
from typing import Type,Dict,Any
from Domain.Interfaces.IJobsService import IJobsService
from Infrastruncture import IJobsRepository, IRabbitPublisherRepository,IRabbitConsumerRepository
import json
import threading
import asyncio
import requests as rs


class JobsService(IJobsService):
    def __init__(self,jobRepository: Type[IJobsRepository],rabbitConsumer:Type[IRabbitConsumerRepository],rabbitPublish: Type[IRabbitPublisherRepository]) -> None:
        self._job = jobRepository
        self._rabbitPublish = rabbitPublish
        self.__rabbitConsumer = rabbitConsumer
        self.__consumer_thread = None

    async def consultarUrl(self, url: str):
        try:
            resultado = await self._job.consultarUrl(url)
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
    
    async def consultarIp(self,nmIpServidor:str):
        try:
            resultado = await self._job.consultarIp(nmIpServidor)
            return json.loads(resultado['jsonConfig'])
        except Exception as ex:
            raise Exception(str(ex))
        
    async def consultarId(self,nmIpServidor:str,jobId:int):
        try:
            resultado = await self._job.consultarIp(nmIpServidor)
            json_resultado = json.loads(resultado['jsonConfig'])
            for item in json_resultado:
                if item.get('id') == jobId:
                    # Encontrou o dicionário com 'id' igual a 1
                    return item
            else:
                # Se o loop terminar sem encontrar o dicionário
                raise Exception(f"Nenhum Job com 'id' igual a {jobId} encontrado")
            
        except Exception as ex:
            raise Exception(str(ex))
    
    async def registrarAPI(self, nmIpServidor: str, dados:str):
        try:
            
           
            headers = {
                "Content-Type": "application/json"
            }

            response = rs.post('http://'+nmIpServidor+'/Jobs/api/jobs', json=dados,headers=headers)
            if response.status_code == 200:
                return True
            else:
                raise Exception(f"Nao foi possivel enviar esse JOB para o servidor. Status code: {response.status_code}")
            
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizarAPI(self, nmIpServidor: str, dados:str):
        '''Sera publicada uma mensagem para esse servidor, porem antes temos que ver se o cara esta ativo la na tabela servidores'''
        try:
            await self._job.consultarIp(nmIpServidor) #verifica esse IP no servidor, se existir o codigo segue, se nao cai no excption
            '''Padrao do consumidor {ip}_agente'''
            destino = f'{nmIpServidor}_agenteJobs'
            mensagem = json.dumps(dados)
            await self._rabbitPublish.enviar_mensagem(destino,mensagem)

            return 'Dados enviado para o agente'
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizar(self, url: str, dados: str):
        try:
            resultado = await self._job.atualizar(url,dados)
        except Exception as ex:
            pass
  
    async def consumindo_mensagem(self):
        try:
            if self.__consumer_thread is None or not self.__consumer_thread.is_alive():
                self.__consumer_thread = threading.Thread(target=self.__rabbitConsumer.iniciar_consumidor, args=('apicentralizador',self.__on_message_received,))
                self.__consumer_thread.start()
                print('Consumer thread started.')
        except Exception as ex:
            raise Exception(str(ex))
        
    def __on_message_received(self, message,ip,ch,method): 
        try:
            mensagem = message.decode('utf8')
            asyncio.run(self._job.atualizar(ip,mensagem))
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as ex:
            raise Exception(str(ex))    