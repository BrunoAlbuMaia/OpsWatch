import time
from typing import Type,Dict,Any
from Domain.Entities.ServidoresEntity import ServidoresEntity
from Domain.Interfaces.IServidoresService import IServidoresService
from Infrastruncture.Data.Repository.Interfaces.IServidoresRepository import IServidoresRepository



class ServidoresService(IServidoresService):
    def __init__(self,servidorRepositry: Type[IServidoresRepository]) -> None:
        self.__servidor = servidorRepositry
    

    async def registrar(self,dados: ServidoresEntity):
        try:
            await self.__servidor.registrar(dados)
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizar(self,dados:ServidoresEntity):
        try:
            pass
        except Exception as ex:
            pass
    
  