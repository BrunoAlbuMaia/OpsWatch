from fastapi.websockets import WebSocket
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from functools import partial
import json

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


    async def start_consumidor(self):
        return await self.jobService.consumindo_mensagem()
    # async def websocket_job(self,websocket:WebSocket,connection):
    #     try:
            
    #         resultado = await self.obter_configuration()
    #         # print(f"Received message: {data}")
    #         jobs_str = json.dumps(resultado['jobs'], indent=4)
    #         return jobs_str
    #     except Exception as ex:
    #         raise Exception(str(ex))
        


   

    