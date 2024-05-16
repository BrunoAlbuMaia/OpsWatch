from Domain.Interface.IJobBaseService import IJobBaseService
from Infrastruncture.Data.Repository.ISQLExecutorRepository import ISQLExecutorRepository

from typing import Dict,Any,Type
import time
import subprocess
import psutil


class JobOpenCloseService(IJobBaseService):
    def __init__(self,repos:Type[ISQLExecutorRepository]) -> None:
        self._repos = repos
        return None

    async def execute_job(self, job:Dict[str,Any]):
        '''É responsável por executar o JOB'''
        try:
            configDetalhes = job['detalhes']

            for _ in range(configDetalhes.get('num_executions', 1)):
                await self.execute_pre_job_actions(configDetalhes)
                await self.execute_application_actions(configDetalhes)
                await self.execute_post_job_actions(configDetalhes)

            print('Job executado com sucesso')
        except Exception as ex:
            raise Exception(str(ex))
    
    async def execute_pre_job_actions(self, config:Dict[str,Any]) -> str:
        # Lógica para executar ações antes do trabalho principal
        try:
            configDB = config['configDB']

            if config['preExecProc'].get('nomeProc','') != '':
                resultado_pre_proc = await self._repos.executar_proc(config['preExecProc']['nomeProc'], 
                config['preExecProc']['parametros'],
                configDB)

            return True
        except Exception as ex:
            raise Exception(str(ex))

    async def execute_application_actions(self, config:Dict[str,Any]) -> str:
        # Lógica para executar o trabalho principal
        try:
            nomeProcesso = config['nomeExecutavel']
            caminhoExecutavel = config['caminhoExecutavel']
            for process in psutil.process_iter(attrs=['pid', 'name']):
                if process.info['name'] == nomeProcesso:
                    process.terminate()  
                    try:
                        process.wait(timeout=5)
                        break
                    except psutil.TimeoutExpired:
                        process.kill()
            time.sleep(config['tmpEsperaSegundos'])
            subprocess.Popen(caminhoExecutavel)

        except Exception as ex:
            raise Exception(str(ex))
        
    async def execute_post_job_actions(self, config:Dict[str,Any]) -> str:
        try:
            configDB = config['detalhes']['configDB']

            if config['posExecProc'].get('nomeProc','') != '':
                resultado_pos_proc = await self._repos.executar_proc(config['postExecProc']['nomeProc'], 
            config ['postExecProc']['parametros'],
            configDB)
            
            return resultado_pos_proc
        except Exception as ex:
            raise Exception(str(ex))

