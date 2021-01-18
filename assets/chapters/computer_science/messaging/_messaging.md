# MESSAGING

RabbitMQ and Kafka are very often used for asynchronous messaging for inter-service communication. Services communicating by exchanging messages over messaging channels.

Advantages of Message-Based Systems are:

The sender only needs to know the location of the message broker, not the addresses of all possible receivers.
It’s possible to have multiple receivers for a message.
We can easily add new receivers without any changes in the sender.
Messages can be queued, ensuring delivery after a receiver has been down.
In short, senders and receivers are decoupled from each other.
When you build a system of microservices, you can end up with many, many services. Coordinating communications between all these services can be tricky.

::::
download.md(assets/slides/computer_science/messaging/rabbitmq.md)
::::
download.md(assets/slides/computer_science/messaging/kafka.md)
::::