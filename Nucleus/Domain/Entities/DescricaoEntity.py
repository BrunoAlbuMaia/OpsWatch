from pydantic import BaseModel

class DescricaoEntity(BaseModel):
    nrDescriptionId:int
    nmChavePlugin:str
    nmJsonPlugin:str
    descricao:str