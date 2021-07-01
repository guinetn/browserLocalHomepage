# WCF

For distributed service-oriented applications
WCF can create, host, consume and secure services
Enables applications to communicate whether they are on the same computer, across the Internet, or on different application platforms.
Developers focus on their implementation rather than communication protocols and low level messaging details. Implement services in a unified way regardless of the wire protocol or message format used to communicate 
Combines .NET Remoting, Distributed Transactions, Message Queues and Web Services into a single programming model and also support interoperability with other processes.

## WCF Architecture
![WCF Architecture](assets/books/dotnet/tools/assets/wcf_architecture.png)

## FEATURES

* Service Orientation
Applications use services to send and receive data (benefit of loose-coupling)
Client can connect to hosted services as long as the client meets the service contract requirements.

* Interoperability
WCF supports interoperability with multiple web services specifications and implements a number of web services protocols. WCF provides support for 
- Web services (WS) infrastructure protocols through channels 
- Web services application protocols through the contracts feature
Interoperability for application protocols is accomplished through 
- XML Schema description language 1.0 (XSD) 
- Web Services Description Language (WSDL) 1.1. 
Some of the major protocols/specifications include HTTP 1.1, SOAP 1.1, SOAP 1.2 Core, XML, WSDL 1.1, XOP etc.

* Multiple Message Patterns
WCF supports multiple patterns for exchanging messages from one endpoint to other endpoint. 
* request/reply message pattern
common pattern
one endpoint sends data request to second endpoint 
second endpoint replies to the request
* one-way message pattern
first endpoint sends a message to second endpoints and do not expect the reply from the second endpoint. 
* Duplex exchange pattern 
two endpoints establish a connection and send data back and forth just like an instant messaging program.

* Service Metadata
WCF supports service metadata publishing using industry standards formats such as 
- WSDL
- XML Schema
- WS-Policy
This metadata can be published over HTTP or HTTPs and client applications use this metadata to generate or configure service clients who can communicate with the WCF services.

* Data Contracts
.NET classes representing a data entity with properties that belong to the data entity
These classes are used to exchange data between WCF services and clients. 
WCF service architecture automatically generates the metadata from these classes that allows clients to send and receive data.
 
* Security
WCF supports messages encryption to protect data privacy using well-known standards such as 
- SSL
- WS-SecureConversation
It also supports authentication to prevent unauthorized access to services from users or client applications.

* Multiple Transports and Encodings
WCF supports several built-in transport protocols and encodings for messages communication. On the World Wide Web, messages are text encoded in SOAP format and send over HTTP. Other supported options are using TCP, Named pipes or MSMQ. Furthermore, messages can be encoded as text or optimized binary format which can be send efficiently using the MTOM standard. WCF also allows you to create your own custom transport or encoding if none of the built-in option suits your need.

* Transactions
WCF supports three different transaction models. You can use WS-AtomixTransactions, the APIs in the System.Transactions namespace and Microsoft Distributed Transaction Coordinator.

* AJAX and REST Support
To support the modern Web 2.0 technologies such as REST, JSON, ATOM etc. WCF can be configured to process the data in plain XML format without wrapping it in SOAP envelope.

* Extensibility
If you are running short of options or existing built-in features doesn’t fulfill your needs, WCF provides you many extensibility entry points to customize the behavior of a service according to your application requirements.
 
## CONCEPTS

***Endpoints - ABC***
A resource on the network to which clients can send messages
Messages are formatted according to the contract on which both client and service are agreed
All the communication takes place through those endpoints

A WCF service can expose multiple endpoints to its clients, each endpoint is defined by an address, binding, contract (informations required to communicate with clients)

![](assets/books/dotnet/tools/assets/wcf_abc.jpg)


A service endpoint must define the ABCs of WCF to expose its capabilities on the network
- Define endpoints in code
>ServiceHost.AddServiceEndpoint()
- Define endpoints in configuration files

***Address - where***
Location to which the messages must be send by the client to start the communication with the WCF service. 
- HTTP: http://webserver/webservice 
- TCP: net.tcp://webserver:8080/webservice
 
***Binding - how***
Specifies how client will communicate with the service
Defines binding elements (lowest level binding element is the transport base protocol to be used: HTTP, Named Pipes, TCP, MSMQ...). 
Encoding element: type of encoding to be used: Text, Binary, MTOM
Other elements: security, transaction, reliable messaging capability...

|PREDEFINED BINDINGS|Description|
|---|---|
|BasicHttpBinding  |	Basic Web service communication. No security by default|
|WSHttpBinding  |	Web services with WS-* support. Supports transactions|
|WSDualHttpBinding  |	Web services with duplex contract and transaction support|
|NetMsmqBinding  |	Communication between WCF applications by using queuing. Supports transactions|
|NetNamedPipeBinding  |	Communication between WCF applications on same computer. Supports duplex contracts and transactions|
|NetPeerTcpBinding  |	Communication between computers across peer-to-peer services. Supports duplex contracts|
|NetTcpBinding  |	Communication between WCF applications across computers. Supports duplex contracts |and transactions|

***Contract - What***
Agreement between two or more parties for common understanding 
Platform-neutral and standard way of describing what the service does
Contracts are mapped to interfaces which describe the list of operations exposed to the clients 
from a particular endpoint. 

Types of contracts supported

- Operation Contract
Defines the signature and the list of parameters to be passed in and out of those operations.
```cs
[OperationContract] 
double AddNumbers(double a, double b);
```

- Service Contract
Defines the service that holds multiple operation contracts and act as a single functional unit.
Method signatures of the service and usually defined as an interface

```cs
[ServiceContract] 
public interface ICalculator 
{ 
   [OperationContract] 
   double AddNumbers(double a, double b); 
 
   [OperationContract] 
   double DivideNumbers(double a, double b); 
 
   [OperationContract] 
   void FormatNumbers(double a); 
}
```

- Data Contract
Describes the data to be passed between the service and client and the way to serialize that data
Defines the external format of the data passed to and from the service operations. 
It defines the structure and types of data exchanged and can map the CLR type to an XML Schema. 
It can also define how the data will be serialized over a network.
```cs
[DataContract] 
public class ComplexNumber 
{ 
   [DataMember] public int RealNumber { get; set; } 
   [DataMember] public int BaseNumber { get; set; } 
}
```

- Message contract 
defines the default SOAP message format provided by the WCF runtime for communication between client and service 
and it can be customized to meet your requirements. 

- Policy and bindings
Define the conditions required to communicate with a service such as transport protocol HTTP or TCP, 
an encoding, security requirement etc.


***Service Runtime***
Contains the runtime behaviors of the service that occur only during the actual operation of the service
|||
|---|---|
|Throttling Behavior |Controls how many messages are processed and can be configured if the demand of the service increased|
|Error Behavior |Specifies what occurs when an internal error occurs on the service. This allows you to configure what information is communicated to the client when any exception occurs|
|Metadata Behavior |Tells how and whether metadata is available to outside world|
|Instance Behavior |Specified how many instance of the service has to be created while running. For example, a singleton specified only one instance to process all messages|
|Transaction Behavior |Enables the rollback of transacted operations if a failure occurs|
|Dispatched Behavior |Controls how a message is processed by the WCF infrastructure|


## 1. SERVICE CONTRACT 
Specifies operations the service will expose to its clients. 
An operation is just like a web service method that can be called by outside world.

Creating a service contract:
ICalculator.cs 
```cs
[ServiceContract] 
public interface ICalculator 
{ 
   [OperationContract] 
   double Add(double n1, double n2); 
 
   [OperationContract] 
   double Subtract(double n1, double n2); 
 
   [OperationContract] 
   double Multiply(double n1, double n2); 
 
   [OperationContract] 
   double Divide(double n1, double n2); 
}
```

## 2. SERVICE IMPLEMENTATION 

Implementing the contract: 
CalculatorService.cs 
```cs
public class CalculatorService : ICalculator 
{ 
   public double Add(double n1, double n2) 
   { 
      return n1 + n2; 
   } 
   ...
}
```

## 3. WCF SERVICE HOSTING

WCF services cannot listen to incoming clients requests unless it is not hosted. You can host service in 
- IIS - Internet Information Service 
provides number of advantages if a service used HTTP as protocol. IIS hosting option is integrated with ASP.NET and used the features these technologies offer such as process recycling, idle shutdown, process health monitoring and message-based activation. This is preferred solution for hosting web service applications that must be highly available and highly scalable.
- Windows Activation Service (WAS)
WAS is the new process activation mechanism that ships with IIS 7.0 and available for the Windows Server 2008 or Windows 7. In addition to HTTP based communication, WCF can also use WAS to provide message-based activation over other protocols, such as TCP and named pipes.
- Self-Hosting (console, Windows Application)
 WCF service can be self-hosted as a managed console, Windows Forms or WPF application. It is very flexible option because it requires the least infrastructure to deploy. You need to embed the code inside the managed application to create and open an instance of the ServiceHost to make service available. Services hosted like this are very useful during development because you can easily debug and get trace information to find out what is happening inside the application.
- Windows Service
WCF service can also be hosted as a Windows Service so that it is under control of the Service Control Manager (SCM). Similar to the self-hosting option, some hosting code needed to be written as part of the application. The lifetime of the service is controlled by the operating system which is better option for long running WCF services.


Each one of these options gives you some advantages and disadvantages.

Ex: Console Application 'ConsoleHost'
1. Add a reference to System.ServiceModel
2. Right click on the project's "References" folder under the project in Solution Explorer
Add a reference to the CalculatorServiceLibrary
3. Define an endpoint
Endpoint = address, binding, contract (informations required to communicate with clients)
A service endpoint must define the ABCs of WCF to expose its capabilities on the network
- Define endpoints in code
>ServiceHost.AddServiceEndpoint()
- Define endpoints in configuration files

![](assets/books/dotnet/tools/assets/wcf_metadata_exchange.jpg)

Program.cs of the host
When running 
- on Windows Vista and later operating systems, the service must be run with administrator privileges
- Visual Studio with Administrator privileges, ConsoleHost application will also run with Administrator privileges
 
```cs
class Program 
{ 
   static void Main(string[] args) 
   { 
      ServiceHost host = null; 
      try { 
        Uri baseAddress = new Uri("http://localhost:8000/CalculatorService/");   // Creating base address  
        host = new ServiceHost(typeof(CalculatorService), baseAddress);   // Creating ServiceHost instance  
        host.AddServiceEndpoint(typeof(ICalculator), new BasicHttpBinding(), "");  // Adding service endpoint 
        // basicHttpBinding is compliant and interoperable with most systems that implement XML Web Services
        
        ServiceMetadataBehavior smb = new ServiceMetadataBehavior();   // Enable metadata exchange 
        /* WCF Metadata 
        Say how to communicate with a service
        Clients request metadata of a running service to learn about their endpoints + message formats required
        At design time, clients send a request message defined by the WS-MetadataExchange standard and receive WSDL in return. The WSDL can be used by the client to define a proxy class and configuration file that will later be used at runtime to communicate with the service */
 
        smb.HttpGetEnabled = true; 
        host.Description.Behaviors.Add(smb); 
          
        host.AddServiceEndpoint(typeof(IMetadataExchange), MetadataExchangeBindings.CreateMexHttpBinding(), "mex");  // Adding MEX endpoint 
        /*MEX endpoints
        By default, WCF services do not expose a MEX endpoint: nobody can query the service to find out how to communicate with it. 
        WCF makes it easy to expose a MEX endpoint so that clients can communicate properly with services. You can add it either in code or in configuration. 
        In code above, MEX endpoint is added with IMetadataExchange contract, HTTP protocol for transport and “mex” as the address. Because the address is specified as a relative address, the base address of the service is used as the prefix, so the full address is http://localhost:8000/CalculatorService/mex
        */
 
        host.Open(); // Start service 
 
        Console.WriteLine("The service is ready."); 
        Console.WriteLine("Press to terminate service.");          
        Console.ReadLine();
 
        host.Close(); // Shutdown service (if user press Enter key) 
      } 
      catch (CommunicationException ce) { 
         Console.WriteLine("An exception occurred: {0}", ce.Message); 
         host.Abort(); 
      } 
   } 
} 
```
http://localhost:8000/CalculatorService/mex
http://localhost:8000/CalculatorService

WCF Service Client

## 4. WCF SERVICE CLIENT

Create a client that can access the service
- Use code to program the client using the rich WCF API (more control over service invocation)
- Use tools to generate a proxy class + configuration file 

Ex: Console Application 'ConsoleClient'
1. Add a reference to System.ServiceModel
2. Right click on the project's "References" folder under the project in Solution Explorer
Add a reference to the CalculatorServiceLibrary

Client must know the service's ABCs to access its capabilities

```cs
class Program 
{ 
   static void Main(string[] args) 
   { 
      ChannelFactory myChannelFactory = 
         new ChannelFactory( 
            new BasicHttpBinding(), 
            new EndpointAddress("http://localhost:8000/CalculatorService/")); 
 
      ICalculator client = myChannelFactory.CreateChannel(); 
      double result = client.Add(5, 6); 
 
      Console.WriteLine("Calling Service..."); 
      Console.WriteLine(result); 
      Console.WriteLine(); 
      Console.ReadLine(); 
   } 
}
```


## More 
- https://www.ezzylearning.net/tutorial/programming-wcf-services
- https://www.ezzylearning.net/tutorial/introducing-windows-communication-foundation-wcf
- https://www.ezzylearning.net/tutorial/programming-wcf-services
