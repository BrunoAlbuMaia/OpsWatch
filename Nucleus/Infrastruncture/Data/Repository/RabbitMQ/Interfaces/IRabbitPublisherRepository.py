from abc import ABC,abstractmethod


class IRabbitPublisherRepository(ABC):
    @abstractmethod 
    async def enviar_mensagem(self,destino:str,mensagem:str):
        pass