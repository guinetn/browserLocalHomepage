## EVENT DRIVEN ARCHITECTURE

https://docs.nestjs.com/microservices/basics
https://www.enterpriseintegrationpatterns.com/patterns/messaging/index.html

Connect devices using a publish/subscribe model
Necessary steps to collect, clean, define, store, and analyze data.

business is powered by applications that run in diverse environments (on-premises, datacenters, field offices, manufacturing floors, retail stores), lacking of compatibility and connectivity between these environments forces your
applications to interact via tightly-coupled synchronous request/reply interactions, individually customized batch-oriented ETL processes, or even bespoke integration = slow responses and stale data. 

For an enterprise to be real-time, events must be streamed between the app and microservices that process them so insights can be gleaned and decisions can be made fast. To become more responsive and to take advantage of new technologies (cloud, IoT, microservices, etc.), your enterprise architecture needs to support real-time, event-driven interactions.

Every business process is basically a series of events. An event can be described as a change notification. These changes can have a variety of forms, but all have the common structure of an action that has occurred on an object. Event-driven architecture is just a way of building enterprise IT systems that lets loosely coupled applications and microservices produce and consume these events.

With event-driven architecture, applications and microservices talk through events or event adapters. Events are routed among these applications in a publish/subscribe manner according to subscriptions that indicate their interest in all manner of topics,

An event-driven architecture will depend on decomposing flows into microservices, and putting in place a runtime fabric that lets the microservices talk to each other in a publish/subscribe, one-to-many, distributed fashion


Event-Driven Applications 
- publish and subscribe to events
- are topic and taxonomy aware
- are real-time

Having an eventing platform in place (even the most basic pieces of it) allows your first project to leverage it as microservices and events start to come online and communicate with each other, rather than via REST, resulting in a distributed monolith.

- Event Broker 
  An event broker is the fundamental runtime component for event routing in a publish/ subscribe, low latency, and guaranteed delivery manner. Applications and microservices are decoupled from each other and communicate via the event broker. Events are published to the event broker via topics following a topic hierarchy (or taxonomy), correspondingly subscribed to by one or more applications or microservices, or analytics engines or data lakes.

  An ideal event broker uses open protocols and APIs to avoid vendor lock-in. With open standards, you have the flexibility of choosing the appropriate event broker provider over time. Think about the independence TCP/IP gave to customers choosing networking gear - open standards made the internet happen. By leveraging the open source community, it's easier to create on-the-fly changes, and you're not stuck having to consult closed documentation or sit in a support queue.

- Event Mesh
An event mesh is a network of event brokers that dynamically routes events between applications no matter where they are deployed - on-premises or in any cloud or event at loT edge locations. Just like the internet is made possible by routers converging routing tables, the event mesh converges topic subscriptions with various optimizations for distributed event streaming.

- Event Portal
An event portal ~ just like an API portal - is your design and runtime view into your event mesh. An event portal gives architects an easy GUI-based tool to define and design events in a governed manner, and offers them for use by publishers and subscribers. Once you have defined events, you can design microservices or applications in the event portal and choose which events they will consume and produce by browsing and searching the event catalog.
As your events get defined, they are enlisted in an event catalog for discovery. An event catalog gives you 's more of a documentation step, sibility into your events. Although this will help to visualize and describe the events that you're able to process. When building out the system for more event sources and different ways to consume them, the catalog is a great reference to know what's already been built so you can avoid duplication of effort.

- Event Taxonomy
 
Topic routing is the lifeblood of an event-driven architecture. Topics are metadata of events; tags of the form a/b/c - just like an HTTP URL or a File Path ~ which describe the event. The event broker understands topics and can route events based on who subscribed to them, including wildcard subscriptions. As you start your event-driven architecture journey, itâ€™s important to pay attention to Asolid topic taxonomy - setting up a topic naming convention early on and governing i taxonomy is probably the most important design investment you will make, so itâ€™s best not to take shortcuts here. Having a good taxonomy will significantly help with event routing, and the conventions will be obvious to application developers. For more on topic hierarchy best practices, visit: bit ly/topic-hierarchy

Because events from the publisher (microservice, application, legacy-to-event adapter) have topics as metadata, consumers can use it to subscribe to events.
Event             Topic
New Order         order/init/1.1/icecream/udders/rumraisin/sg/lazada
Validated Order   order/valid/1.1/icecream/udders/rumraisin/sg/lazada
Order Shipment    order/shipped/1.1/icecream/udders/rumraisin/sg/lazada


Topic subscriptions would be:
* Consume and validate all orders of version 1.1 and publish the order valid message: order/init/1.1/>
* Consume and process all valid orders for ice cream originating in Singapore: order/valid/*/icecream/*/*/sg/*
* Allorders no matter what stage, category, location: order/>

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
download.page(api/architecture/architecture_event_driven/event_sourcing_streaming.md)
download.page(api/architecture/architecture_event_driven/mqtt.md)
download.page(api/architecture/architecture_event_driven/nats.md)
download.page(api/architecture/architecture_event_driven/kafka.md)
download.page(assets/books/data/db_streaming_ksqldb.md)
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

## SAMPLES

- https://itnext.io/how-to-build-an-event-driven-asp-net-core-microservice-architecture-e0ef2976f33f
- https://itnext.io/how-to-use-database-sharding-and-scale-an-asp-net-core-microservice-architecture-22c24916590f
- https://docs.ksqldb.io/en/latest/tutorials/event-driven-microservice