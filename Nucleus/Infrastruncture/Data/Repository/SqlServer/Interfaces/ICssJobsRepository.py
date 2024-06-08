from typing import Any, Dict
from abc import ABC, ABCMeta, abstractmethod


class ICssJobsRepository(ABC):
    @abstractmethod
    async def consultar(self, nrServidorId: int):
        pass
    @abstractmethod
    async def registrar(self,nrServidorId:int,dados:Dict[str,Any]):
        pass
    
    @abstractmethod
    async def apagar(self,nrServidorId:int,nrJobId:int):
        pass