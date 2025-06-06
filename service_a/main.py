from fastapi import FastAPI, Request
import pika
import os

app = FastAPI()

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
QUEUE_NAME = "tasks"

def publish_message(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )
    connection.close()

@app.get("/")
def read_root():
    return {"message": "Service A is running!"}

@app.post("/send-task")
async def send_task(request: Request):
    data = await request.json()
    task = data.get("task", "default task")
    publish_message(task)
    return {"status": "sent", "task": task}