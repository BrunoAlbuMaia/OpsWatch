import pika
from pika.adapters.blocking_connection import BlockingChannel
from decouple import config

class DbSessionRabbitMQ:
    def __init__(self):
        self.rabbit = config('rabbitMQ')

    def connect(self) -> BlockingChannel:
        components = self.rabbit.split(';')
        connection_params = {}
        for component in components:
            key, value = component.split('=')
            connection_params[key] = value

        self.connection_parameters = pika.ConnectionParameters(
            host=connection_params['host'],
            port=connection_params['port'],
            credentials=pika.PlainCredentials(username=connection_params['username'], password=connection_params['password'])
        )
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        
        return self.channel
    
    def declare_queue(self, queue_name):
        return self.channel.queue_declare(queue=queue_name, durable=True)

    def consume(self, queue_name, on_message_callback):
        self.channel.basic_consume(queue=queue_name,
                                auto_ack=True,
                                on_message_callback=on_message_callback)
        self.channel.start_consuming()
    
    def close_connection(self):
        if self.channel:
            self.channel.stop_consuming()
            self.channel.close()
        if self.connection:
            self.connection.close()
        print('[*] Connection closed.')

