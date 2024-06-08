from abc import ABC,abstractmethod


class IRabbitConsumerRepository(ABC):
    @abstractmethod 
    def iniciar_consumidor(self,target_consumer):
        pass