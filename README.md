# MicroservicesMessaging

A simple Python project demonstrating microservices communication using **FastAPI** and **RabbitMQ**.

## Structure

- `service_a/`: Producer microservice (sends tasks to RabbitMQ)
- `service_b/`: Consumer microservice (receives tasks from RabbitMQ)
- `docker-compose.yml`: Orchestrates both services and RabbitMQ

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)

### Running the Project

Build and start all services:

```sh
docker compose up --build
```

- RabbitMQ UI: [http://localhost:15672](http://localhost:15672) (user: guest, password: guest)
- Service A: [http://localhost:8000](http://localhost:8000)
- Service B: [http://localhost:8001](http://localhost:8001)

### Sending a Task

On Windows PowerShell:

```powershell
Invoke-WebRequest -Uri "http://localhost:8000/send-task" `
  -Method POST `
  -Body '{"task": "hello from RabbitMQ"}' `
  -ContentType "application/json"
```

Or with curl (if installed):

```sh
curl.exe -X POST -H "Content-Type: application/json" -d "{\"task\": \"hello from RabbitMQ\"}" http://localhost:8000/send-task
```

### Checking Processed Tasks

Check the `service_b` container logs for:

```
[x] Received task: hello from RabbitMQ
```

Or visit [http://localhost:8001/tasks](http://localhost:8001/tasks) to see received tasks.

---
```<!-- filepath: c:\Projects\MicroservicesMessaging\README.md -->
# MicroservicesMessaging

A simple Python project demonstrating microservices communication using **FastAPI** and **RabbitMQ**.

##

- `service_a/`: Producer microservice (sends tasks to RabbitMQ)
- `service_b/`: Consumer microservice (receives tasks from RabbitMQ)
- `docker-compose.yml`: Orchestrates both services and RabbitMQ

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)

### Running the Project

Build and start all services:

```sh
docker compose up --build
```

- RabbitMQ UI: [http://localhost:15672](http://localhost:15672) (user: guest, password: guest)
- Service A: [http://localhost:8000](http://localhost:8000)
- Service B: [http://localhost:8001](http://localhost:8001)

### Sending a Task

On Windows PowerShell:

```powershell
Invoke-WebRequest -Uri "http://localhost:8000/send-task" `
  -Method POST `
  -Body '{"task": "hello from RabbitMQ"}' `
  -ContentType "application/json"
```

Or with curl (if installed):

```sh
curl.exe -X POST -H "Content-Type: application/json" -d "{\"task\": \"hello from RabbitMQ\"}" http://localhost:8000/send-task
```

### Checking Processed Tasks

Check the `service_b` container logs for:

```
[x] Received task: hello from RabbitMQ
```

Or visit [http://localhost:8001/tasks](http://localhost:8001/tasks) to see received tasks.

---