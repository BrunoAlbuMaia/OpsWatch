import contextlib
from typing import Type,Dict,Any
from Domain import IJobsService
from Infrastruncture import IRabbitPublisherRepository,IJobsRepository
import json

class JobsService(IJobsService):
    
    def __init__(self,jobRepository: Type[IJobsRepository],rabbitPublishRepository:Type[IRabbitPublisherRepository]) -> None:
        self.__jobsJson = jobRepository
        self.__rabbitPublishRepository = rabbitPublishRepository

    
    async def job_id(self, id):
        try:
            return await self.__jobsJson.job_id(job_id=id)
        except Exception as ex:
            raise Exception(str(ex))
    
    async def jobs(self):
        try:
            return await self.__jobsJson.jobs()
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizar(self, dados:Dict[str,Any]):
        try:
            await self.__jobsJson.atualizar(dados)
            resultado_json = await self.jobs()
            serialize_str = json.dumps(resultado_json['jobs'])
            return await self.__rabbitPublishRepository.enviar_mensagem(serialize_str)
        except Exception as ex:
            raise Exception(str(ex))
    
    async def registrar(self, job:Dict[str,Any]):
        with contextlib.suppress(Exception):
            pass

    async def enviar_mensagem(self):
        try:
            #Serializa as configurações do JOBS
            jobs_json = await self.jobs()
            jobs_serialize = json.dumps(jobs_json['jobs'])

            #vamos montra a estrutura de envio para o consumidro
            return await self.__rabbitPublishRepository.enviar_mensagem('')
        except Exception as ex:
            raise Exception(str(ex))