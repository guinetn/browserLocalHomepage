### RABBIT MQ

- https://www.rabbitmq.com/
- https://docs.nestjs.com/microservices/rabbitmq
- https://wanago.io/2020/11/23/api-nestjs-rabbitmq-microservices/

Message broker: a Publish/Subscribe messaging system.
channel
exchanges
topics
bind queues

open-source and lightweight message broker which supports multiple messaging protocols. It can be deployed in distributed and federated configurations to meet high-scale, high-availability requirements. In addition, it's the most widely deployed message broker, used worldwide at small startups and large enterprises.

* Start a RabbitMQ container with admin UI 
docker run -d  -p 15672:15672 -p 5672:5672 --hostname my-rabbit --name some-rabbit rabbitmq:3-management
Browse localhost:15672 
Log in with the username “guest” and the password “guest”
Use the web UI to create an Exchange with the name “user” of type “Fanout” and two queues “user.postservice” and “user.otherservice”. It is important to use the type “Fanout” so that the exchange copies the message to all connected queues.
https://itnext.io/how-to-build-an-event-driven-asp-net-core-microservice-architecture-e0ef2976f33f


amqpUri: Describes how to connect to RabbitMQ
    uri: A uri in the format amqp://{user}:{password}@{host}:{port}/{vhost}. Default uri is amqp://guest:guest@localhost:5672/%2f.
    connectionRetryCount: The retry count for when a connection fails. Default count is 3 retries.
    retryWaitInMilliseconds: The time in milliseconds to wait before retrying to connect again. Default duration is 1000 ms.
    circuitBreakTimeInMilliseconds: The time in milliseconds to keep the circuit broken. Default duration is 60000 ms.
exchange: Describes where messages are sent
    name: The name of the exchange.
    type: The type of the exchange. Can be one of:
        direct (default)
        fanout
        headers
        topic
    durable: Indicates whether the exchange is durable. Default value is false.
queues: Defines general settings for queues
    - highAvailability: Indicates whether all queues should be mirrored across all nodes in the cluster. Default value is false.
    - qosPrefetchSize: Allows you to limit the number of unacknowledged messages on a channel (or connection) when consuming (aka “prefetch count”). Default count is 1.


## more

- https://itnext.io/how-to-build-an-event-driven-asp-net-core-microservice-architecture-e0ef2976f33f
- https://paramore.readthedocs.io/en/latest/RabbitMQConfiguration.html