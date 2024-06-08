
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

    async def ativar_consumidorJobs(self):
        return await self.jobService.consumindo_mensagem()