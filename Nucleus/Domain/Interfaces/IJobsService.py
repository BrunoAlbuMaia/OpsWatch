
from abc import ABC,abstractmethod
from typing import Dict,Any



class IJobsService(ABC):

    @abstractmethod
    async def consultar(self,nrServidorId:int):
        pass
    
    @abstractmethod
    async def consultarId(self,nrServidorId:int,jobId:int):
        pass

    @abstractmethod
    async def registrar(self,nrServidorId:int,dados:Dict[str,Any]):
        pass

    @abstractmethod
    async def atualizar(self, nrServidorId:int,dados:Dict[str,Any]):
       pass

