from abc import ABC, abstractmethod
from typing import Dict,Any
from Domain.Entities.ServidoresEntity import ServidoresEntity

class IServidoresRepository:
    @abstractmethod
    async def registrar(self,dados:ServidoresEntity):
        pass
    @abstractmethod
    async def atualizar(self,dados:ServidoresEntity):
        pass
    