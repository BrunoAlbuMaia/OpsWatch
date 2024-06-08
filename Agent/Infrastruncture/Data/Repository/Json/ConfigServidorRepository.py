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
        '''Atualiza o JSON e a variavel de ambiente'''
        try:
            with open(self.file_path, 'r') as f:
                servico = json.load(f)
            
            for campo, valor in dados.dict().items():
                if campo in servico:
                    servico[campo] = valor

            with open(self.file_path, 'w') as f:
                json.dump(servico, f, indent=4)
            

            await self.__update_env_variable('headersConsumidorJobs',f'{servico['ipServidor']}_agente')
            return 'Atualizado com sucesso'
        except Exception as ex:
            return str(ex)


    # Função para atualizar o valor de uma variável no arquivo .env
    async def __update_env_variable(self,variable_name, new_value):
        current_value = config(variable_name)
        
        # Se o valor atual for diferente do novo valor, atualize-o
        if current_value != new_value:
            with open('.env', 'r') as file:
                lines = file.readlines()
            
            with open('.env', 'w') as file:
                for line in lines:
                    # Verifica se a linha contém a variável que queremos atualizar
                    if line.startswith(variable_name):
                        file.write(f"{variable_name}='{new_value}'\n")
                    else:
                        file.write(line)

            print(f"Valor da variável {variable_name} atualizado para {new_value}.")