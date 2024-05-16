
import asyncio
import websockets
from typing import List

from functools import partial

from Application.program import DependencyContainer

class JobsController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.jobService = self.injection.jobService

    async def consultar(self,nrServidorId:int):
        try:
            return await self.jobService.consultar(nrServidorId)
        except Exception as ex:
            raise Exception(str(ex))
        


    async def connect_to_websockets(self,urls: List[str]):
        async def connect_to_websocket(url: str):
            while True:
                try:
                    async with websockets.connect(url) as websocket:
                        print(f"Conexão estabelecida com o servidor WebSocket: {url}")
                        try:
                            while True:
                                response = await websocket.recv()

                                # Gravar no banco de dados aqui
                                print(f"Mensagem do servidor {url}: {response}")
                                
                                #vou verificar nos registro de replicacao para o JOB e registrar o job como concluído
                                print('')


                        except websockets.exceptions.ConnectionClosed:
                            print(f"Conexão encerrada pelo servidor: {url}")
                        except Exception as e:
                            print(f"Erro durante a recepção de mensagens WebSocket de {url}: {e}")


                except Exception as e:
                    print(f"Erro na conexão WebSocket com {url}: {e}")

                print(f"Tentando reconectar a {url} em 5 segundos...")
                await asyncio.sleep(5)

        # Criar uma tarefa assíncrona para cada URL de WebSocket
        await asyncio.gather(*(connect_to_websocket(url) for url in urls))
