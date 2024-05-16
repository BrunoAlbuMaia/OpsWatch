import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))


from fastapi import WebSocket
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


from Application.program import DependencyContainer
from Domain.Entites.jobEntity import Job
scheduler = AsyncIOScheduler()

class MonitorarServidorController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.__monitramento = self.injection.monitorarServidorService

    async def monitorar_recursor(self):
        ram = f'{await self.__monitramento.verificar_consumo_ram()}%'
        consumo_cpu = f'{await self.__monitramento.verificar_consumo_cpu()}%'
        disco = await self.__monitramento.verificar_uso_disco()
        connectividade = await self.__monitramento.verificar_conectividade() 

        dicionario ={
            "consumo_ram":ram,
            "consumo_cpu":consumo_cpu,
            "Disco":[disco],
            "conectividade":connectividade
        }
        return dicionario
    async def monitoramentoWebSocket(self,websocket):
        try:

            ram = f'{await self.__monitramento.verificar_consumo_ram()}%'
            consumo_cpu = f'{await self.__monitramento.verificar_consumo_cpu()}%'
            disco = await self.__monitramento.verificar_uso_disco()
            connectividade = await self.__monitramento.verificar_conectividade() 
            dicionario ={
            "consumo_ram":ram,
            "consumo_cpu":consumo_cpu,
            "Disco":[disco],
            "conectividade":connectividade
            }
            # Enviar os dados para o cliente através do WebSocket
            return dicionario
            # Esperar um segundo antes de enviar os próximos dados
            
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
            


