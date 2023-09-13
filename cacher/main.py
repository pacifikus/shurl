import json
import logging

import pika
import redis

redis_client = redis.Redis(host='host.docker.internal', port=6379, decode_responses=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def save_token(token: str, url: str) -> bool:
    return redis_client.set(token, url)


def callback(ch, method, properties, body):
    data = json.loads(body.decode())
    token = data['token']
    url = data['original_url']
    save_token(token, url)
    logger.info(f'Token {token} is saved to Redis')
    ch.basic_ack(delivery_tag=method.delivery_tag)


rabbit_connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='host.docker.internal',
        port=5672,
    )
)
rabbit_channel = rabbit_connection.channel()
rabbit_channel.queue_declare(queue='generated_tokens', durable=True)

rabbit_channel.basic_qos(prefetch_count=1)
rabbit_channel.basic_consume(queue='generated_tokens', on_message_callback=callback)
rabbit_channel.start_consuming()
