from Infrastruncture.Data.Repository.RabbitMQ.Interfaces import IRabbitPublisherRepository
from Infrastruncture.Data.Context.dbSessionRabbit import DbSessionRabbitMQ
import pika
from datetime import timezone
from decouple import config
from datetime import datetime
import logging

class RabbitPublisherRepository(IRabbitPublisherRepository):
    def __init__(self, rabbit: DbSessionRabbitMQ) -> None:
        self._rabbit = rabbit

    async def enviar_mensagem(self, mensagem: str):
        channel = self._rabbit.connect()
        try:
            ipServidor: str = config('headersConsumidorJobs').replace('_agenteJobs', '')

            headers_agente = {
                "message_type": "http",
                "sender": "apiagente",
                "ip": ipServidor,
                "timestamp": f'{datetime.now(timezone.utc).isoformat()}Z',
                "destinatary": "apicentralizador",
            }

            # Publicar a mensagem com o cabeçalho target_consumer
            channel.basic_publish(
                exchange=config('exchange'),
                routing_key='',
                body=mensagem,
                properties=pika.BasicProperties(
                    headers=headers_agente,
                    delivery_mode=2  # Tornar a mensagem persistente
                )
            )

            return 'Mensagem Enviada'
        except Exception as ex:
            logging.error(f"Erro ao enviar mensagem: {str(ex)}")
            raise
        finally:
            self._rabbit.close_connection(channel)
