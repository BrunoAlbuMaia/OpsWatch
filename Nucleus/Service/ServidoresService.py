import time
from typing import Type,Dict,Any
from Domain.Entities.ServidoresEntity import ServidoresEntity
from Domain.Interfaces.IServidoresService import IServidoresService
from Infrastruncture.Data.Repository.SqlServer.Interfaces.IServidoresRepository import IServidoresRepository



class ServidoresService(IServidoresService):
    def __init__(self,servidorRepositry: Type[IServidoresRepository]) -> None:
        self.__servidor = servidorRepositry
    
    async def consultar(self,flAtivo=None):
        try:
            resultado = await self.__servidor.consultar(flAtivo)
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
    async def registrar(self,dados: ServidoresEntity):
        try:
            #vamos verificar se esse cara ja existe na nossa base
            resultado = await self.__servidor.consultar_por_hostname(hostname=dados.nmServidor)
            if resultado != None:
                resultado = ServidoresEntity(**resultado)
                resultado_dict = resultado.dict()
                dados_dict = dados.dict()
                
                # Removendo 'nrServidorId' para a comparação
                resultado_dict.pop('nrServidorId', None)
                dados_dict.pop('nrServidorId', None)

                if resultado_dict == dados_dict:
                    raise Exception('Esse agente já está configurado...')
                else:
                   dados.nrServidorId = resultado.nrServidorId
                   return await self.__servidor.atualizar(dados)

            else:
                return await self.__servidor.registrar(dados)
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizar(self,dados:ServidoresEntity):
        try:
            pass
        except Exception as ex:
            pass
    
  