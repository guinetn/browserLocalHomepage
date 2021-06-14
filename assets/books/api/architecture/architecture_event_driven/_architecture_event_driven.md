## EVENT DRIVEN ARCHITECTURE

https://docs.nestjs.com/microservices/basics
https://www.enterpriseintegrationpatterns.com/patterns/messaging/index.html

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


! In an event oriented environment the linear flow of actions is often made unclear by the need to pause processing until an event occurs


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
download.page(api/architecture/architecture_event_driven/event_sourcing.md)
download.page(api/architecture/architecture_event_driven/mqtt.md)
download.page(api/architecture/architecture_event_driven/nats.md)
download.page(api/architecture/architecture_event_driven/kafka.md)
download.page(api/architecture/architecture_event_driven/rabbitmq.md)
download.page(api/grpc.md)
download.page(api/architecture/architecture_event_driven/ipc-on-linux.md)
download.page(api/architecture/architecture_event_driven/amazon-sqs.md)
download.page(api/architecture/architecture_event_driven/distributed_task_queue.md)

## Azure Event Hubs
https://azure.microsoft.com/services/event-hubs/
Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions of events per second and stream them to multiple consumers. This lets you process and analyze the massive amounts of data produced by your connected devices and applications. Once Event Hubs has collected the data, you can retrieve, transform, and store it using any real-time analytics provider, such as Azure Stream Analytics, or with batching/storage adapters.


## Message Broker Pub/Sub

[Messaging Patterns](https://www.redhat.com/architect/architectural-messaging-patterns): essential patterns of message exchange architectures and routing methods used in technologies such as Redis, Apache Kafka, RabbitMQ, ZeroMQ, and IBM MQ.

ways to route messages to the proper destination without the originating application being aware of the ultimate destination of the message. 
 
decouple the destination of a message from the sender and maintain central control over the flow of messages

receive messages from multiple senders, determine the correct destination and route the message to the correct channel

Pub-Sub pattern: asynchronous, no blocking lock between sender and receiver
Messages in the Pub-Sub pattern tend to be discrete, containing all the information that a process needs to act upon the data provided.

- A publisher 
>The sender sends the message to the broker and then moves onto other tasks.  
 Sends a message to a topic (~inbox: RabbitMQ Exchange, Kafka Yopic) on a message broker.

- A subscriber 
>The receiver accepts a message at its convenience.   
  binds to the topic and receives messages from the topic in an asynchronous manner

Fanout:   
interested parties will bind (a.k.a, subscribe) to a given topic. Then, when a message is sent to the topic, all subscribers will receive a copy of the message sent to the topic. The message is “fanned out.” 
Twitter = Fanout pattern: One single tweet is sent to all the parties following the person sending the tweet.



https://developer.lightbend.com/docs/akka-platform-guide/concepts/message-driven-event-driven.html