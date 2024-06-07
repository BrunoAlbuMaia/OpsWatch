
import asyncio
import websockets
from typing import List

from functools import partial
import json
from Application.program import DependencyContainer

class JobsController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.jobService = self.injection.jobService
        self.servidores = self.injection.servidorService
        self.json_configs = {}

    async def consultarIp(self,nmIpServidor:str):
        try:
            return await self.jobService.consultarIp(nmIpServidor)
        except Exception as ex:
            raise Exception(str(ex))
        
    async def consultarId(self,nmIpServidor:str,jobId:int):
        try:
            return await self.jobService.consultarId(nmIpServidor,jobId)
        except Exception as ex:
            raise Exception(str(ex))
        
    async def registrarAPI(self, nmIpServidor: str, dados:str):   
        try:
            return await self.jobService.registrarAPI(nmIpServidor=nmIpServidor,dados=dados)  
        except Exception as ex:
            raise Exception(str(ex))
    
    async def atualizarAPI(self, nmIpServidor: int, dados:str):
        try:
            return await self.jobService.atualizarAPI(nmIpServidor=nmIpServidor,dados=dados)  
        except Exception as ex:
            raise Exception(str(ex))

    async def connect_to_websockets(self):
        async def connect_to_websocket(url: str):
            
            while True:
                try:
                    async with websockets.connect(url) as websocket:
                        print(f"Conexão estabelecida com o servidor WebSocket: {url}")
                        try:
                            while True:
                                    
                                response = await websocket.recv()
                               

                                if url not in self.json_configs:
                                    self.json_configs[url] = response
                                    await self.jobService.atualizar(url, response)
                                elif response != self.json_configs.get(url):
                                    self.json_configs[url] = response
                                    await self.jobService.atualizar(url, response)
                    
                        except websockets.exceptions.ConnectionClosed:
                            print(f"Conexão encerrada pelo servidor: {url}")
                        except Exception as e:
                            print(f"Erro durante a recepção de mensagens WebSocket de {url}: {e}")


                except Exception as e:
                    print(f"Erro na conexão WebSocket com {url}: {e}")

                print(f"Tentando reconectar a {url} em 5 segundos...")
                await asyncio.sleep(5)

        # Criar uma tarefa assíncrona para cada URL de WebSocket
        urls = await self.servidores.consultar()
        await asyncio.gather(*(connect_to_websocket(url['urlWebSocketJobs']) for url in urls))
