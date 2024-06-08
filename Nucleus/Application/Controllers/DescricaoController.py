
from Application.program import DependencyContainer
from Domain.Entities.DescricaoEntity import DescricaoEntity
class DescricaoController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.descricaoService = self.injection.descricaoService

    async def consultar(self):
        try:
            return await self.descricaoService.consultar_descricoes()
        except Exception as ex:
            raise Exception(str(ex))
        
    async def consultar_chave(self,nmChavePlugin:str):
        try:
            return await self.descricaoService.consultar_descricoes_chave(nmChavePlugin)
        except Exception as ex:
            raise Exception(str(ex))
    
    async def registrar(self,descricao:DescricaoEntity):
        try:
            return await self.descricaoService.registrar_descricao(descricao)
        except Exception as ex:
            raise Exception(str(ex))
    
    async def atualizar(self,descricao:DescricaoEntity):
        try:
            return await self.descricaoService.atualizar_descricao(descricao)
        except Exception as ex:
            raise Exception(str(ex))
    
    async def excluir(self,nrDescricaoId:int):
        try:
            return await self.descricaoService.excluir_descricao(nrDescricaoId)
        except Exception as ex:
            raise Exception(str(ex))
        