# GRPC


Open source high performance RPC (remote procedure call) framework
It is based on HTTP/2, Protocol Buffers and other modern standard-based technologies. 
Supported by many programming languages, including .NET.
https://gRPC.io
Efficiently connect services 
Pluggable support for load balancing, tracing, health checking, authentication. 
To connect devices, mobile apps/browsers to backend services
Uses protocol buffers by default.
 
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