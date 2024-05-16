import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from Application.program import DependencyContainer
from Domain.Entites.jobEntity import Job
scheduler = AsyncIOScheduler()

class ConfigurarServidorController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.__configService = self.injection.configService

    async def configurar_servidor_automaticamente(self):
        return await self.__configService.configurar_servidor_automaticamente()
        

