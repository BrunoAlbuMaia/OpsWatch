from pydantic import BaseModel
from typing import Dict, Any

class ConfigServidorEntity(BaseModel):
    nmServidor: str
    ipServidor: str
    nrServidorID: int = 0
