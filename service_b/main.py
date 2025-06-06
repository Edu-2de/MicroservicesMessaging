from fastapi import FastAPI
import pika
import threading
import os
import time

app = FastAPI()
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
QUEUE_NAME = "tasks"
messages = []  # Lista para armazenar tarefas recebidas

def callback(ch, method, properties, body):
    msg = body.decode()
    messages.append(msg)
    print(f"[x] Received task: {msg}")

def start_consumer():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE_NAME, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
            print("[*] Waiting for messages. To exit press CTRL+C")
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError:
            print(" [!] RabbitMQ não disponível, tentando novamente em 5 segundos...")
            time.sleep(5)

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_consumer, daemon=True)
    thread.start()

@app.get("/")
def read_root():
    return {"message": "Service B is running and listening for tasks!"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": messages}