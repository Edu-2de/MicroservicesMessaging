# MicroservicesMessaging

A Python project demonstrating microservices architecture with asynchronous messaging using FastAPI and RabbitMQ. Includes two independent services communicating through message queues, showcasing queue patterns and scalable design.

## Initial structure

- `service_a/`: First microservice (producer)
- `service_b/`: Second microservice (consumer)
- `docker-compose.yml`: Orchestrates the services and RabbitMQ