import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from abc import ABC, abstractmethod
from typing import Dict,Any

class IJobsRepository:
    @abstractmethod
    async def get_dados(self):
        pass
    @abstractmethod
    async def get_dados_by_id(self,job_id:int):
        pass
    @abstractmethod
    async def registrar_job(self,dados:Dict[str,Any]):
        pass
    @abstractmethod
    async def update_dados(self,dados: Dict[str, Any]):
        pass
