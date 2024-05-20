from pydantic import BaseModel


class JobsEntity(BaseModel):
    nrServidorId:int
    jsonConfig:str
    dtCriacao:str
    dtAtualizacao:str
    usuarioCriacao:str
    usuarioAlteracao:str
    