from pydantic import BaseModel

class ServidoresEntity(BaseModel):
    nrServidorId: int
    nmServidor: str
    nmIpServidor: str
    nmDescricao: str
    urlWebsocketServidor: str
    urlWebSocketJobs:str
    flAtivo: bool
