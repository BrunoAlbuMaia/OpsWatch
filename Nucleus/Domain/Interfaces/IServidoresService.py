
from abc import ABC,abstractmethod
from Domain.Entities.ServidoresEntity import ServidoresEntity


class IServidoresService(ABC):
    @abstractmethod
    async def consultar(self,flAtivo=None):
        pass
    @abstractmethod
    async def registrar(self,dados:ServidoresEntity):
        pass

    @abstractmethod
    async def atualizar(self,dados:ServidoresEntity):
        pass
    