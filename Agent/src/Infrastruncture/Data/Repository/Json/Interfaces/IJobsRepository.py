from abc import ABC, abstractmethod
from typing import Dict,Any

class IJobsRepository(ABC):
    @abstractmethod
    async def jobs(self):
        pass
    @abstractmethod
    async def job_id(self,job_id:int):
        pass
    @abstractmethod
    async def registrar(self,dados:Dict[str,Any]):
        pass
    @abstractmethod
    async def atualizar(self,dados: Dict[str, Any]):
        pass
