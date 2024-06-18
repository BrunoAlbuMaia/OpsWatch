from pydantic import BaseModel
from typing import Dict,Any,List

class ConfigDBEntity(BaseModel):
    usuario:str
    senha:str
    database:str
    serve:str

class ProcEntity(BaseModel):
    nome:str
    parametros:list[dict]

class DetalhesEntity(BaseModel):
    tempExecucao:str = '* * * * *'
    ultExecucao:str
    navegador:str
    proc:ProcEntity
    configDB:ConfigDBEntity

class AutomacaoWebEntity(BaseModel):
    id:int
    nomeJOB:str
    tipo:str = 'automacao_web'
    status:bool
    detalhes:DetalhesEntity
    comandos_web: List[Dict[str, Any]] 