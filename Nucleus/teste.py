import redis
import time

# Conectando ao servidor Redis
r = redis.Redis(host='192.168.60.222', port=6379, db=0)

# Função para publicar mensagens em um canal específico
def publish_message(channel, message):
    r.publish(channel, message)

# Função para processar mensagens recebidas de um canal
def process_message(message):
    print(f"Mensagem recebida: {message}")

# Função para assinar um canal e processar mensagens recebidas
async def subscribe_channel(channel):
    # Conectando ao servidor Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Criando um objeto de pubsub
    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    # Loop para ouvir mensagens
    for message in pubsub.listen():
        if message['type'] == 'message':
            process_message(message)


# Exemplo de publicação de mensagens
# publish_message('canal-teste', 'TCHAU')

# Exemplo de assinatura de um canal e processamento de mensagens



async def main():
    await subscribe_channel('canal-teste')

# Mantém o programa em execução para receber mensagens
# while True:
#     time.sleep(1)
