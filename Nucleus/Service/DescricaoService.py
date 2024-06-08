from Domain.Interfaces.IDescricacaoService import IDescricacaoService
from Domain.Entities.DescricaoEntity import DescricaoEntity
from Infrastruncture.Data.Repository.SqlServer.Interfaces.IDescricaoRepository import IDescricaoRepository


class DescricaoService(IDescricacaoService):
    def __init__(self,repository:IDescricaoRepository):
        self._repo = repository

    async def consultar_descricoes(self):
        return await self._repo.consultar()
    
    async def consultar_descricoes_chave(self, nmChavePlugin):
        return await self._repo.consultar_chave(nmChavePlugin)
    
    async def registrar_descricao(self, description: DescricaoEntity):
        return await self._repo.registrar(description)
    
    async def atualizar_descricao(self, description: DescricaoEntity):
        return await self._repo.atualizar(description)
    
    async def excluir_descricao(self, nrDiscriptionId:int)-> bool:
        return await self._repo.excluir(nrDiscriptionId)
    