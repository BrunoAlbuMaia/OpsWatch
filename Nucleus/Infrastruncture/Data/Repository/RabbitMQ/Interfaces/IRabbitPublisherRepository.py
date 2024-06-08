from abc import ABC,abstractmethod


class IRabbitPublisherRepository(ABC):
    @abstractmethod 
    async def enviar_mensagem(self,mensagem:str):
        pass