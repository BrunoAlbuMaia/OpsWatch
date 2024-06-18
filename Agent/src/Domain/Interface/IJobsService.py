
from abc import ABC,abstractmethod
from typing import Dict,Any
from Domain.Entites.jobEntity import Job


class IJobsService(ABC):

    @abstractmethod
    async def jobs(self):
        pass
    
    @abstractmethod
    async def job_id(self, id):
        pass

    @abstractmethod
    async def atualizar(self, job):
       pass

    @abstractmethod
    async def registrar(self,job:Dict[str,Any]):
        pass

    @abstractmethod
    async def enviar_mensagem(self):
        pass