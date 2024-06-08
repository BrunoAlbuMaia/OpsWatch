from abc import ABC, abstractmethod
from typing import Dict,Any
from Domain.Entities.ServidoresEntity import ServidoresEntity

class IServidoresRepository:
    @abstractmethod
    async def consultar(self,flAtivo=None):
        pass
    @abstractmethod
    async def consultar_por_hostname(self,hostname:str):
        pass
    @abstractmethod
    async def registrar(self,dados:ServidoresEntity):
        pass
    @abstractmethod
    async def atualizar(self,dados:ServidoresEntity):
        pass
    