from Infrastruncture.Data.Repository.RabbitMQ.Interfaces import IRabbitPublisherRepository
from Infrastruncture.Data.Context.dbSessionRabbit import DbSessionRabbitMQ
import pika
from decouple import config

class RabbitPublisherRepository(IRabbitPublisherRepository):
    def __init__(self,rabbit:DbSessionRabbitMQ) -> None:
        self._rabbit = rabbit
    async def enviar_mensagem(self,destino:str, mensagem: str):
        channel = self._rabbit.connect()
        try:
            # Publicar a mensagem com o cabeçalho target_consumer
            channel.basic_publish(
                exchange=config('exchange'),
                routing_key='', 
                body=mensagem,
                properties=pika.BasicProperties(
                    headers={'apicentralizador':destino},
                    delivery_mode=2  # Tornar a mensagem persistente
                )
            )

            return 'Mensagem Enviada'
        except Exception as ex:
            raise Exception(str(ex)) from ex