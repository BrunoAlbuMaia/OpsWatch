
from abc import ABC,abstractmethod
from typing import Dict,Any



class IJobsService(ABC):

    @abstractmethod
    async def consultarUrl(self,url:str):
        pass

    @abstractmethod
    async def consultarIp(self,nmIpServidor:str):
        pass
    @abstractmethod
    async def consultarId(self,nmIpServidor:str,jobId:int):
        pass

    @abstractmethod
    async def registrarAPI(self, nmIpServidor: str, dados:str):
        pass

    @abstractmethod
    async def atualizarAPI(self, nmIpServidor: str, dados:str):
        pass

    @abstractmethod
    async def atualizar(self, url:str,dados:str):
       pass

    @abstractmethod 
    async def consumindo_mensagem(self):
        pass

