from Infrastruncture.Data.Repository.RabbitMQ.Interfaces.IRabbitConsumerRepository import IRabbitConsumerRepository
from Infrastruncture.Data.Context.dbSessionRabbit import DbSessionRabbitMQ
from decouple import config
import threading
from typing import Callable
class RabbitConsumerRepository(IRabbitConsumerRepository):
    def __init__(self,rabbit:DbSessionRabbitMQ):
        self._rabbit = rabbit

    def iniciar_consumidor(self,target_consumer, callback: Callable[[str], None]):
        def __minha_chamada(ch, method, properties, body):
            message_target_consumer  = properties.headers.get('apicentralizador') ## Isso deve ser fixo pois ele vai receber sempre no headers informando que e do centralizador
            if message_target_consumer  == target_consumer: 
                print(f" [x] Consumer 1 Received: {body}")
                callback(body)


        channel = self._rabbit.connect()
        try:
            channel.queue_declare(queue='my_queue', durable=True)

            channel.basic_consume(queue='my_queue',
                                auto_ack=True,
                                on_message_callback=__minha_chamada)
            channel.start_consuming()
        except Exception as ex:
            # sourcery skip: raise-specific-error
            raise Exception(str(ex)) from ex