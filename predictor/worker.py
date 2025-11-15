import pika
import json
import os
import time
import random

RABBIT_HOST = os.getenv("RABBIT_HOST")
RABBIT_USER = os.getenv("RABBIT_USER")
RABBIT_PASS = os.getenv("RABBIT_PASS")

# Lista de items de calidad 4
QUALITY_4_ITEMS = [
    "Brimstone", "Polyphemus", "Sacred Heart", "Godhead",
    "Mega Blast", "Mom's Knife", "The Mind", "The Body",
    "The Soul", "Death's Touch", "Epic Fetus", "Technology"
]

def generate_prediction(payload):
    """
    Devuelve 3 items al azar de calidad 4.
    """
    suggestions = random.sample(QUALITY_4_ITEMS, 3)

    return suggestions
    

# --- Conexión a RabbitMQ ---
connection = None
for _ in range(20):
    try:
        credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
        )
        break
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ no está listo, esperando 3 segundos...")
        time.sleep(3)
else:
    raise RuntimeError("No se pudo conectar a RabbitMQ")

channel = connection.channel()
channel.queue_declare(queue='prediction_requests')
channel.queue_declare(queue='prediction_responses')

print("Worker de predicción listo y escuchando en 'prediction_requests'...")

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f"Recibido request: {payload}")

    # Generar predicción
    prediction = generate_prediction(payload)

    # Publicar respuesta
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        body=json.dumps(prediction)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"Respuesta enviada: {prediction}")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='prediction_requests', on_message_callback=callback)

channel.start_consuming()
