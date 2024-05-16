import time
from typing import Type,Dict,Any
from Domain.Interfaces.IJobsService import IJobsService
from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository



class JobsService(IJobsService):
    def __init__(self,jobRepository: Type[IJobsRepository]) -> None:
        self._job = jobRepository
    
    async def consultar(self, nrServidorId: int):
        try:
            resultado = await self._job.consultar(nrServidorId=nrServidorId)
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
    
    async def consultarId(self, nrServidorId: int, jobId: int):
        try:
            pass
        except Exception as ex:
            raise Exception(str(ex))
    
    async def registrar(self, nrServidorId: int, dados: Dict[str, Any]):
        try:
            pass
        except Exception as ex:
            pass
    
    async def atualizar(self, nrServidorId: int, dados: Dict[str, Any]):
        try:
            pass
        except Exception as ex:
            pass
  