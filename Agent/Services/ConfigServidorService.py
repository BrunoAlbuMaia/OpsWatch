import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import socket
import requests as rs


from decouple import config
from Domain.Entites.ConfigServidorEntity import ConfigServidorEntity
from Domain.Interface.IConfigServidorService import IConfigServidorService
from Infrastruncture.Data.Repository.IConfigServidorRepository import IConfigServidorRepository
from Infrastruncture.Data.Repository.ConfigServidorRepository import ConfigServidorRepository


class ConfigServidorService(IConfigServidorService):
    
    def __init__(self,repository:IConfigServidorRepository = ConfigServidorRepository) -> None:
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
            
            payload = {
                "nrServidorId": 0,
                "nmServidor": hostname,
                "nmIpServidor": ipv4_address,
                "nmDescricao": "",
                "urlWebsocketServidor": f"ws://{ipv4_address}:{config("port")}/Servidores/ws",
                "urlWebSocketJobs": f"ws://{hostname}:{config("port")}/Jobs/ws",
                "flAtivo": True

            }
            headers = {
                "Content-Type": "application/json"
            }

            response = rs.post(self.url, json=payload,headers=headers)
            if response.status_code == 200:
                return True
            else:
                raise Exception(f"Erro ao enviar configuração. Status code: {response.status_code}")
            
        except Exception as ex:
            raise Exception(str(ex))