from abc import ABC, abstractmethod
from typing import Dict,Any

class IJobsRepository:
    @abstractmethod
    async def consultar(self,nrServidorId:int):
        pass

    @abstractmethod
    async def atualizar(self,nrServidorId:int,dados: Dict[str, Any]):
        pass
