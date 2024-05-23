import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..')))
import json
from decouple import config
from typing import Dict,Any

from Domain.Entites.jobEntity import Job
from Infrastruncture.Data.Repository.Json.Interfaces.IConfigServidorRepository import IConfigServidorRepository

class ConfigServidorRepository(IConfigServidorRepository):
    file_path = config('file_pathConfig')

    async def get_dados(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    async def update_dados(self, dados: Dict[str, Any]):
        try:
            with open(self.file_path, 'r') as f:
                servico = json.load(f)
            
            for campo, valor in dados.dict().items():
                if campo in servico:
                    servico[campo] = valor

            with open(self.file_path, 'w') as f:
                json.dump(servico, f, indent=4)
            
            return 'Atualizado com sucesso'
        except Exception as ex:
            return str(ex)
