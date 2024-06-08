from abc import ABC, abstractmethod
from Domain.Entities.DescricaoEntity import DescricaoEntity


class IDescricaoRepository(ABC):
    
    @abstractmethod
    async def consultar(self):
        pass

    @abstractmethod
    async def consultar_chave(self,chave:str):
        pass

    @abstractmethod
    async def registrar(self,descricao:DescricaoEntity):
        pass

    @abstractmethod
    async def atualizar(self,descricao:DescricaoEntity):
        pass
    @abstractmethod
    async def excluir(self,nrDescriptionId:int):
        pass