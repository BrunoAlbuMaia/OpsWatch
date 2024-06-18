from pydantic import BaseModel
from typing import Dict, Any,List,Union

class PreExecProc(BaseModel):
    nomeProc: str
    parametros: List[str]

class PosExecProc(BaseModel):
    nomeProc: str
    parametros: List[str]

class ConfigDB(BaseModel):
    usuario: str
    senha: str
    database: str
    serve: str

class Detalhes(BaseModel):
    tempExecucao: str
    ultAlteracao: str
    caminhoExecutavel: str
    nomeExecutavel: str
    tmpEsperaSegundos: int
    preExecProc: PreExecProc
    posExecProc: PosExecProc
    configDB: ConfigDB
    comandos_pos_fechamento: List[dict]
    comando_pos_abertura: List[dict]

class Job(BaseModel):
    id: int
    nomeJOB: str
    tipo: str
    status: bool
    detalhes: Detalhes

