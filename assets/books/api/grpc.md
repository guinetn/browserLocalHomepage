# GRPC


Open source high performance RPC (remote procedure call) framework that can run in any environment (.NET…)
It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication.
It is based on HTTP/2, Protocol Buffers and other modern standard-based technologies. 

https://gRPC.io
https://github.com/grpc/grpc-node

Efficiently connect services 
Pluggable support for load balancing, tracing, health checking, authentication. 
To connect devices, mobile apps/browsers to backend services
Uses protocol buffers by default.
 
Like many RPC systems, gRPC is based on the concept of defining a service in terms of functions (methods) that can be called remotely. For each method, you define the parameters and return types. Services, parameters, and return types are defined in .proto files using Google's open source language-neutral protocol buffers mechanism.

With the gRPC transporter, Nest uses .proto files to dynamically bind clients and servers to make it easy to implement remote procedure calls, automatically serializing and deserializing structured data.





### protocol buffers
https://developers.google.com/protocol-buffers/docs/overview 

Ex: In IA, ONNX est écrit en protocol buffers (protobufs). Il existe un compilateur officiel protobufs pour Go. Cet outil permet de générer les fonctions de désérialisation, qui vont convertir le binaire ONNX en un objet Go. [onnx-go](https://github.com/owulveryck/onnx-go)

### gRPC Web
 a JS client library that supports the same API as gRPC-Node to access a gRPC service. Due to browser limitation, the Web client library implements a different protocol than the native gRPC protocol. This protocol is designed to make it easy for a proxy to translate between the protocols as this is the most likely deployment model.
https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md

## More
interserviceCommunication: Sample code to compare performance of http/1.1, http/2 and gRPC
- https://itnext.io/effectively-communicate-between-microservices-de7252ba2f3c
- https://github.com/abhinavdhasmana/interserviceCommunication
- https://auth0.com/blog/implementing-microservices-grpc-dotnet-core-3/
- https://medium.com/@waelkdouh/microfrontends-with-blazor-webassembly-b25e4ba3f325
- https://michaelscodingspot.com/rest-vs-grpc-for-asp-net/