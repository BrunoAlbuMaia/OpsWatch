import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')))
import json
from decouple import config
from typing import Dict,Any

from Domain.Entites.jobEntity import Job
from Infrastruncture.Data.Repository.Json.Interfaces.IJobsRepository import IJobsRepository

class JobsRepository(IJobsRepository):
    file_path = config('file_pathJOBS')

    async def get_dados(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    async def get_dados_by_id(self, job_id:int):
        with open(self.file_path, 'r',encoding='utf-8') as f:
            data = json.load(f)
            for job in data['jobs']:
                if job['id'] == job_id:
                    return job
        return None  # Retorna None se não encontrar nenhum job com o ID especificado
    
    async def registrar_job(self,dados:Dict[str,Any]):
        try:
            # Ler os dados JSON atuais
            with open(self.file_path, 'r') as f:
                servico = json.load(f)
            
            # Obter o último ID usado
            last_id = max(job['id'] for job in servico['jobs']) if servico['jobs'] else 0
            
            # Gerar novo ID sequencial
            novo_id = last_id + 1
            
            # Adicionar novo job com o novo ID
            novo_job = {**dados, 'id': novo_id}
            servico['jobs'].append(novo_job)
            
            # Escrever os dados atualizados de volta no arquivo
            with open(self.file_path, 'w') as f:
                json.dump(servico, f, indent=4)
            
            return novo_job
        except Exception as ex:
            return str(ex)

    async def update_dados(self, dados: Dict[str, Any]):
        try:
            with open(self.file_path, 'r') as f:
                servico = json.load(f)
            
            # Atualiza os dados com base no mapeamento entre os campos JSON e os campos da classe ConfigEntity
            for job in servico['jobs']:
                if job['id'] == dados['id']:
                    for campo, valor in dados.items():
                        if campo in job:
                            job[campo] = valor

            with open(self.file_path, 'w') as f:
                json.dump(servico, f, indent=4)
            
            return await self.get_dados_by_id(job['id'])
        except Exception as ex:
            return str(ex)
