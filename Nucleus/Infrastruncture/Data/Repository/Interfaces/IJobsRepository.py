from abc import ABC, abstractmethod
from typing import Dict,Any
from Domain.Entities.JobsEntity import JobsEntity

class IJobsRepository:
    @abstractmethod
    async def consultarUrl(self,url:str):
        pass
    
    @abstractmethod
    async def consultarIp(self,nmIpServidor:str):
        pass

    @abstractmethod
    async def registrarJson(self,dados:JobsEntity):
        pass

    @abstractmethod
    async def atualizar(self,url:str,dados: str):
        pass
