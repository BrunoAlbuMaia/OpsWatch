import time
from typing import Type,Dict,Any
from Domain.Interfaces.IJobsService import IJobsService
from Infrastruncture.Data.Repository.Interfaces.IJobsRepository import IJobsRepository
import json
import requests as rs


class JobsService(IJobsService):
    def __init__(self,jobRepository: Type[IJobsRepository]) -> None:
        self._job = jobRepository
    
    async def consultarUrl(self, url: str):
        try:
            resultado = await self._job.consultarUrl(url)
            return resultado
        except Exception as ex:
            raise Exception(str(ex))
    
    async def consultarIp(self,nmIpServidor:str):
        try:
            resultado = await self._job.consultarIp(nmIpServidor)
            return json.loads(resultado['jsonConfig'])
        except Exception as ex:
            raise Exception(str(ex))
        
    async def consultarId(self,nmIpServidor:str,jobId:int):
        try:
            resultado = await self._job.consultarIp(nmIpServidor)
            json_resultado = json.loads(resultado['jsonConfig'])
            for item in json_resultado:
                if item.get('id') == jobId:
                    # Encontrou o dicionário com 'id' igual a 1
                    return item
            else:
                # Se o loop terminar sem encontrar o dicionário
                raise Exception(f"Nenhum Job com 'id' igual a {jobId} encontrado")
            
        except Exception as ex:
            raise Exception(str(ex))
    
    async def registrarAPI(self, nmIpServidor: str, dados:str):
        try:
            
           
            headers = {
                "Content-Type": "application/json"
            }

            response = rs.post('http://'+nmIpServidor+'/Jobs/api/jobs', json=dados,headers=headers)
            if response.status_code == 200:
                return True
            else:
                raise Exception(f"Nao foi possivel enviar esse JOB para o servidor. Status code: {response.status_code}")
            
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizarAPI(self, nmIpServidor: str, dados:str):
        try:
            
           
            headers = {
                "Content-Type": "application/json"
            }

            response = rs.patch('http://'+nmIpServidor+'/Jobs/api/jobs', json=dados,headers=headers)
            if response.status_code == 200:
                return True
            else:
                raise Exception(f"Nao foi possivel enviar esse JOB para o servidor. Status code: {response.status_code}")
            
        except Exception as ex:
            raise Exception(str(ex))

    async def atualizar(self, url: str, dados: str):
        try:
            resultado = await self._job.atualizar(url,dados)
        except Exception as ex:
            pass
  