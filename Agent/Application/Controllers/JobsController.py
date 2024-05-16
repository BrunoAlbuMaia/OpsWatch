from fastapi.websockets import WebSocket
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from functools import partial

from Application.program import DependencyContainer
from Domain.Entites.jobEntity import Job    
scheduler = AsyncIOScheduler()

class JobsController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.jobService = self.injection.jobService
        self.automacaoweb = self.injection.automacaoWeb

    async def obter_jobs_id(self,id):
        return await self.jobService.consultar_jobs_id(id)
    
    async def obter_configuration(self):
        return await self.jobService.consultar_configuracao()
    
    async def cadastrar_job(self,entidade):
        try:
            return await self.jobService.inserir_job(entidade)
        except Exception as ex:
            pass

    async def atualizar_configuration(self,dados):
        resultado = await self.jobService.atualizar_configuracao(dados)
        return resultado

    async def websocket_job(self,websocket:WebSocket,connection):
        try:
            # data = await websocket.receive_text()
            
            resultado = await self.obter_configuration()
            resultado = resultado['jobs']
            # print(f"Received message: {data}")
            return resultado
        except Exception as ex:
            raise Exception(str(ex))

   

    