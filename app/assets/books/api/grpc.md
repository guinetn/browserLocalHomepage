# GRPC - Remote Procedure Calls


- https://levelup.gitconnected.com/grpc-how-to-make-effective-unary-calls-4c9fa68cd9d5  to add
- https://medium.com/pragmatic-programmers/what-is-grpc-9df7c8dd0f91

A faster and more effective protocol for sending and receiving data over the wire.
A gRPC service is essentially a group of related RPC endpoints (a group of endpoints needed to solve some problem). Creating a gRPC service involves defining it in protobuf and then compiling your protocol buffers into code comprising the client and server stubs that you then implement. 

Google open source high performance RPC (remote procedure call) framework that can run in any environment (.NET…)
It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication.
It is based on HTTP/2, Protocol Buffers and other modern standard-based technologies. 

Ability to make streaming calls from the client and server side, or Bi-directional streaming. It serializes and deserializes data using Protocol Buffers, and it also provides code generation through the gRPC compiler to currently 11 different languages.
 
- https://gRPC.io
- https://github.com/grpc/grpc-node
- https://developers.google.com/protocol-buffers/docs/overview 
- https://developers.google.com/protocol-buffers/docs/proto3
- https://medium.com/pragmatic-programmers/define-a-grpc-service-e8e20c5589d5

Efficiently connect services 
Pluggable support for load balancing, tracing, health checking, authentication. 
To connect devices, mobile apps/browsers to backend services
Uses protocol buffers by default.
 
Like many RPC systems, gRPC is based on the concept of defining a service in terms of functions (methods) that can be called remotely. For each method, you define the parameters and return types. Services, parameters, and return types are defined in .proto files using Google's open source language-neutral protocol buffers mechanism.

With the gRPC transporter, Nest uses .proto files to dynamically bind clients and servers to make it easy to implement remote procedure calls, automatically serializing and deserializing structured data.

### Protocol Buffers: a data serializer

Makes serializing and deserializing data faster than with JSON format by converting the data to a binary format and compress it, allowing the data to be transmitted using less space, and CPU memory.
.proto files to write the definitions for each message and service requests. The drawback of serializing data using Protocol Buffers is that it’s not human-readable.

* 1. Install the compiler
Protoc compiler to generate the code from a .proto file

- choco install protoc
Software installed to 'C:\ProgramData\chocolatey\lib\protoc\tools'

- NuGet package in Visual Studio. Just go get that.

- https://developers.google.com/protocol-buffers/docs/downloads
protoc-3.15.3-win64.zip

* 2. Install the go plugin for the protoc compiler

The protocol buffer compiler requires the `protoc-gen-go` plugin to generate Go code for for proto2/3 versions of the protocol buffer language. Install it with:
>go get google.golang.org/protobuf/cmd/protoc-gen-go google.golang.org/grpc/cmd/protoc-gen-go-grpc

https://pkg.go.dev/google.golang.org/protobuf/cmd/protoc-gen-go



    

In IA, ONNX est écrit en protocol buffers (protobufs). Il existe un compilateur officiel protobufs pour Go. Cet outil permet de générer les fonctions de désérialisation, qui vont convertir le binaire ONNX en un objet Go. [onnx-go](https://github.com/owulveryck/onnx-go)


### gRPC Web
 a JS client library that supports the same API as gRPC-Node to access a gRPC service. Due to browser limitation, the Web client library implements a different protocol than the native gRPC protocol. This protocol is designed to make it easy for a proxy to translate between the protocols as this is the most likely deployment model.
https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md

## More


- https://github.com/davidfowl/grpc-dotnet
- https://github.com/davidfowl/gRPCSamples
interserviceCommunication: Sample code to compare performance of http/1.1, http/2 and gRPC
- https://itnext.io/effectively-communicate-between-microservices-de7252ba2f3c
- https://github.com/abhinavdhasmana/interserviceCommunication
- https://auth0.com/blog/implementing-microservices-grpc-dotnet-core-3/
- https://medium.com/@waelkdouh/microfrontends-with-blazor-webassembly-b25e4ba3f325
- https://michaelscodingspot.com/rest-vs-grpc-for-asp-net/
- [gRPC in GO](https://levelup.gitconnected.com/grpc-how-to-make-client-streaming-calls-5c731197585)