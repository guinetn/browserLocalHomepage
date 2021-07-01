# API ways of Communication

download.page(api/architecture/architecture_event_driven/_architecture_event_driven.md)

https://docs.nestjs.com/microservices/basics

[ways of Communication](https://michaelscodingspot.com/rest-vs-grpc-for-asp-net/)

[Messaging Patterns](https://www.redhat.com/architect/architectural-messaging-patterns): essential patterns of message exchange architectures and routing methods used in technologies such as Redis, Apache Kafka, RabbitMQ, ZeroMQ, and IBM MQ.

[gRPC](https://grpc.io/)(gRPC Remote Procedure Call) is an open-source remote procedure call system developed by Google. It’s a bit like REST in the way that it provides a way to send requests from a client to a server. But it’s different in many ways

[GraphQL](https://graphql.org/) is a query language for APIs developed by Facebook. It allows the client to ask for exactly the data it needs from the server. This way, you can create just one endpoint on the server that will be extremely flexible and return only the data the client needs. GraphQL is becoming very popular in recent years.

[SignalR](https://github.com/SignalR/SignalR) is a technology that allows for real-time bi-directional communication between server and client. Instead of the client always sending requests to server, SignalR also allows the server to send push notifications to the client. This allows to see real-time updates in web applications. SignalR is extremely popular in ASP.NET.

[TcpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.tcpclient?view=netframework-4.8) and TcpListener (in System.Net.Sockets) provide a low-level connection over TCP. Basically, you’re going to establish a connection and transfer byte arrays. It’s not ideal for a big application where you can use ASP.NET’s controllers and actions to make order in a big API.

[UdpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.udpclient?view=netframework-4.8) provides a way to communicate over UDP protocol. TCP establishes a connection and then sends data, whereas UDP just sends data. TCP makes sure there are no errors in the data, whereas UDP doesn’t. UDP is more effective to transfer data quickly that you don’t care enough for it to be reliable and error-free. Some examples are: Video streaming, Live broadcasts, and Voice over IP (VoIP).

[WCF](https://docs.microsoft.com/en-us/dotnet/framework/wcf/whats-wcf) is an older technology that mostly uses SOAP-based communication between processes. It’s a huge framework that I’m not going to get into except to say that it lost its popularity to REST and JSON payloads.