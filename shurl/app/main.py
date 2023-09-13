import json
import logging

import pika
from app.token_generator import generate_token
from fastapi import FastAPI, HTTPException

from app.db import get_stats
from app.exceptions import TokenAlreadyExistError, TokenNotFoundError
from models import UrlRequest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI(
    title="Shurl",
    description="Url shortener",
    version="0.0.2",
    contact={
        "name": "pacifikus",
        "email": "masterkristall@gmail.com",
    },
    docs_url="/docs",
    redoc_url=None,
)


def send_to_rabbit(token: str, url: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='host.docker.internal',
            port=5672,
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='generated_tokens', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='generated_tokens',
        body=json.dumps({
            "token": token,
            "original_url": url,
        }),
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    logger.info(f'Token {token} has been sent to RabbitMQ')
    connection.close()


@app.post(
    "/get_token",
    summary="Generate token by url",
)
def create_token(url_request: UrlRequest) -> dict:
    try:
        token = generate_token(
            url=url_request.original_url,
            custom_alias=url_request.custom_alias,
        )
        send_to_rabbit(token, url_request.original_url)
    except TokenAlreadyExistError:
        raise HTTPException(
            status_code=400,
            detail="Custom alias token already exists",
        )
    else:
        return {"token": token}


@app.get(
    "/stats/{token}",
    summary="Get clicks stats by token",
)
def get_token_stats(token: str) -> dict:
    try:
        return {token: get_stats(token)}
    except TokenNotFoundError:
        raise HTTPException(status_code=404, detail="Token not found")
