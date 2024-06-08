
from abc import ABC,abstractmethod
from typing import Dict,Any
from Domain.Entites.jobEntity import Job


class IJobsService(ABC):

    @abstractmethod
    async def consultar_configuracao(self):
        pass
    
    @abstractmethod
    async def consultar_jobs_id(self, id):
        pass

    @abstractmethod
    async def atualizar_configuracao(self, job):
       pass

    @abstractmethod
    async def inserir_job(self,job:Dict[str,Any]):
        pass

    @abstractmethod
    async def consumindo_mensagem(self):
        pass