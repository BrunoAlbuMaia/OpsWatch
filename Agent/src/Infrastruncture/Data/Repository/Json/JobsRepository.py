
import json
from decouple import config
from typing import Dict,Any

from Infrastruncture import IJobsRepository

class JobsRepository(IJobsRepository):
    file_path = config('file_pathJOBS')

    async def jobs(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except Exception as ex:
            raise Exception('Não foi possível ler o arquivo de JOBS')
    
    async def job_id(self, job_id:int):
        try:
            with open(self.file_path, 'r',encoding='utf-8') as f:
                data = json.load(f)
                for job in data['jobs']:
                    if job['id'] == job_id:
                        return job
            raise Exception('Esse ID não existe, verifique os IDS disponiveis no endpoint Jobs/api/Jobs')
        except Exception as ex:
            raise Exception(str(ex))
    
    async def registrar(self,dados:Dict[str,Any]):
        try:
            jobs_cadastrados:list = self.jobs()         
            last_id = max(job['id'] for job in jobs_cadastrados['jobs']) if jobs_cadastrados['jobs'] else 0
            novo_id = last_id + 1
            novo_job = {**dados, 'id': novo_id}
            jobs_cadastrados['jobs'].append(novo_job)
            
            with open(self.file_path, 'w') as f:
                json.dump(jobs_cadastrados, f, indent=4)
            
            return novo_job
        except Exception as ex:
            return str(ex)

    async def atualizar(self, dados: Dict[str, Any]):
        try:
            job_id = await self.job_id(dados['id'])

            for job in job_id:
                for campo, valor in dados.items():
                    if campo in job:
                        job[campo] = valor

            with open(self.file_path, 'w') as f:
                json.dump(job_id, f, indent=4)

            return job_id
        except Exception as ex:
            return str(ex)
