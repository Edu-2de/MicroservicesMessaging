from fastapi import FastAPI
import pika
import threading
import os

app = FastAPI()

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
QUEUE_NAME = "tasks"

def callback(ch, method, properties, body):
    print(f"[x] Received task: {body.decode()}")  # Aqui você pode colocar qualquer lógica de processamento

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    print("[*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_consumer, daemon=True)
    thread.start()

@app.get("/")
def read_root():
    return {"message": "Service B is running and listening for tasks!"}