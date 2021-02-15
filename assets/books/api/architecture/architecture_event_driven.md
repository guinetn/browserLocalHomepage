## EVENT DRIVEN ARCHITECTURE

https://docs.nestjs.com/microservices/basics

connect devices using a publish/subscribe model

Dispatch some data with different computation times to different destinations:
- a broker
- a simple job queue
- plethora of battle-tested solutions out there
- Apache Kafka
- RabbitMQ 
- Redis
- solid AWS SNS/SQS combination where topics can be defined on SNS with Lambdas or SQS enqueuing triggered at each message received. Why? Because why not, it gives solid performances and near unlimited scalability for just some bucks per month, with low to none maintenance costs beside your business logic; something to consider if you already have a part or your entire backend hosted on AWS.

Sometimes though it can be an overkill or all we need is just a prototype, a proof of concept, in those cases a simple microservice can do well enough with little costs: https://codepr.github.io/posts/asyncio-pubsub/ ***





RabbitMQ and Kafka are very often used for asynchronous messaging for inter-service communication. Services communicating by exchanging messages over messaging channels.

Advantages of Message-Based Systems are:

The sender only needs to know the location of the message broker, not the addresses of all possible receivers.
It’s possible to have multiple receivers for a message.
We can easily add new receivers without any changes in the sender.
Messages can be queued, ensuring delivery after a receiver has been down.
In short, senders and receivers are decoupled from each other.
When you build a system of microservices, you can end up with many, many services. Coordinating communications between all these services can be tricky.


SNS - Amazon Simple Notification Service 
https://aws.amazon.com/sns/

SQS - Amazon Simple Queue Service
https://aws.amazon.com/sqs/
 
download.page(data/db_nosql_redis.md)
download.page(api/architecture/architecture_event_driven/mqtt.md)
download.page(api/architecture/architecture_event_driven/nats.md)
download.page(api/architecture/architecture_event_driven/kafka.md)
download.page(api/architecture/architecture_event_driven/rabbitmq.md)
download.page(api/grpc.md)
download.page(api/architecture/architecture_event_driven/ipc-on-linux.md)

## Azure Event Hubs
https://azure.microsoft.com/services/event-hubs/
Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions of events per second and stream them to multiple consumers. This lets you process and analyze the massive amounts of data produced by your connected devices and applications. Once Event Hubs has collected the data, you can retrieve, transform, and store it using any real-time analytics provider, such as Azure Stream Analytics, or with batching/storage adapters.