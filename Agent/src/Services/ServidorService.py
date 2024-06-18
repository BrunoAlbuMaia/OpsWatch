import socket
from typing import Type
from decouple import config
from Domain.Entites.ConfigServidorEntity import ConfigServidorEntity
from Domain import IConfigServidorService
from Infrastruncture import IConfigServidorRepository


class ConfigServidorService(IConfigServidorService):
    
    def __init__(self,repository:Type[IConfigServidorRepository]) -> None:
        self.__jobsRepository = repository
        self.url = config("api_centralizador")
        return None
    
    async def consultar_configuracao(self):
        return await self.__jobsRepository.get_dados()
    
    async def atualizar_configuracao(self, dados:ConfigServidorEntity):
        return await self.__jobsRepository.update_dados(dados)
    
    async def configurar_servidor_automaticamente(self):
        try:
            hostname = socket.gethostname()
            ipv4_address = socket.gethostbyname(hostname)
            dados = ConfigServidorEntity(nmServidor=hostname,ipServidor=ipv4_address)
            await self.__jobsRepository.update_dados(dados)
            
            
            
        except Exception as ex:
            return False