from abc import ABC, abstractmethod
from Domain.Entities.DescricaoEntity import DescricaoEntity
class IDescricacaoService(ABC):
    @abstractmethod
    async def consultar_descricoes(self):
        pass

    @abstractmethod
    async def consultar_descricoes_chave(self,nmChavePlugin):
        pass

    @abstractmethod
    async def registrar_descricao(self,description:DescricaoEntity):
        pass

    @abstractmethod
    async def atualizar_descricao(self,description:DescricaoEntity):
        pass

    @abstractmethod
    async def excluir_descricao(self,nrDiscriptionId) -> bool:
        pass
