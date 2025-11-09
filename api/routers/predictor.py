from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pika
import uuid
import json
import os
import time

router = APIRouter()

# Modelo de datos para la petición
class PlayerState(BaseModel):
    current_items: list[str]
    player_status: dict
    context: str = ""

# Configuración de RabbitMQ
RABBIT_HOST = os.getenv("RABBIT_HOST")
RABBIT_USER = os.getenv("RABBIT_USER")
RABBIT_PASS = os.getenv("RABBIT_PASS")

# Variables globales para conexión y canal
connection = None
channel = None

def get_rabbitmq_channel():
    """Crea conexión y canal a RabbitMQ si no existen"""
    global connection, channel
    if channel and connection and connection.is_open:
        return channel

    # Retry mientras RabbitMQ no esté listo
    for _ in range(20):
        try:
            credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
            )
            channel = connection.channel()
            channel.queue_declare(queue='prediction_requests')
            channel.queue_declare(queue='prediction_responses')
            print("Conectado a RabbitMQ correctamente")
            return channel
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ no está listo, esperando 3 segundos...")
            time.sleep(3)
    raise HTTPException(status_code=503, detail="No se pudo conectar a RabbitMQ")


@router.post("")
def recommend(state: PlayerState):
    ch = get_rabbitmq_channel()  # conexión lazy
    correlation_id = str(uuid.uuid4())
    payload = state.dict()
    payload["request_id"] = correlation_id
    payload_bytes = json.dumps(payload).encode()

    # Publicar request
    ch.basic_publish(
        exchange='',
        routing_key='prediction_requests',
        properties=pika.BasicProperties(
            reply_to='prediction_responses',
            correlation_id=correlation_id
        ),
        body=payload_bytes
    )

    # Esperar respuesta indefinidamente (polling simple)
    for method_frame, properties, body in ch.consume('prediction_responses'):
        if body and properties.correlation_id == correlation_id:
            ch.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
