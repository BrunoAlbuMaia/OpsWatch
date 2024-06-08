
import asyncio
import websockets
from typing import List

from functools import partial
import logging
from Application.program import DependencyContainer
from Domain.Entities.ServidoresEntity import ServidoresEntity
class ServidoresController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.servidorService = self.injection.servidorService
        self.reconnect_interval = 5
        self.check_interval = 10
        self.connections = {}

    async def consultar(self,flAtivo=None):
        try:
            return await self.servidorService.consultar()
        except Exception as ex:
            raise Exception(str(ex))
    async def registrar(self,dados: ServidoresEntity):
        try:
            return await self.servidorService.registrar(dados)
        except Exception as ex:
            raise Exception(str(ex))
        




    async def connect_to_websocket(self, servidor: dict):
        url = servidor['urlWebsocketServidor']
        while True:
            try:
                async with websockets.connect(url) as websocket:
                    logging.info(f"Conexão estabelecida com o servidor WebSocket: {url}")
                    self.connections[url] = websocket
                    try:
                        while True:
                            response = await websocket.recv()
                            logging.info(f"Mensagem recebida de {url}: {response}")

                            if not servidor['flAtivo']:
                                resultado = ServidoresEntity(**servidor)
                                resultado.flAtivo = True
                                await self.servidorService.registrar(resultado)

                    except websockets.exceptions.ConnectionClosed as e:
                        logging.warning(f"Conexão encerrada pelo servidor {url}: {e}")
                        break  # Sai do loop para reconectar e consultar a tabela novamente
                    except Exception as e:
                        logging.error(f"Erro durante a recepção de mensagens WebSocket de {url}: {e}")
                        break  # Sai do loop para reconectar e consultar a tabela novamente
            except Exception as e:
                logging.error(f"Erro na conexão WebSocket com {url}: {e}")

            resultado = ServidoresEntity(**servidor)
            if resultado.flAtivo:
                resultado.flAtivo = False
                await self.servidorService.registrar(resultado)

            logging.info(f"Tentando reconectar a {url} em {self.reconnect_interval} segundos...")
            await asyncio.sleep(self.reconnect_interval)
            break  # Sai do loop de reconexão para consultar a tabela novamente

    async def check_for_new_servers(self):
        while True:
            try:
                servidores = await self.servidorService.consultar()
                for servidor in servidores:
                    url = servidor['urlWebsocketServidor']
                    if url not in self.connections or self.connections[url].closed:
                        # Criar uma nova conexão se o URL não estiver no dicionário de conexões ou se a conexão estiver fechada
                        asyncio.create_task(self.connect_to_websocket(servidor))
            except Exception as e:
                logging.error(f"Erro ao consultar servidores: {e}")
            await asyncio.sleep(self.check_interval)

    async def start(self):
        # Inicia a tarefa de verificação de novos servidores em background
        asyncio.create_task(self.check_for_new_servers())
        # Mantém o loop de eventos rodando para que as conexões e a verificação continuem
        while True:
            await asyncio.sleep(3600)  # Mantém a execução indefinidamente
