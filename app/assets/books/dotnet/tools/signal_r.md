# SignalR

Real-time web functionality enables server-side code to push content to clients instantly
Real-time update notification (chat, any refresh needed,...replace long polling) 
Historically it was tied to ASP.NET Core but the protocol is open and implementable in any language.

SignalR provides an API for creating server-to-client remote procedure calls (RPC). The RPCs call JavaScript functions on clients from server-side .NET Core code.

SignalR uses Websockets to push messages between the clients and the server for real-time updates. If for some reason Websockets are not available, then it will fall back to other transport mechanisms.

WebSocket: HTML5 API for bi-directional communication between the browser and server. 
A stateful protocol 

![](assets/books/dotnet/tools/assets/websockets.png)
SignalR uses encryption + digital signature to protect the connection token. 
For each request, the server validates the contents of the token to ensure that the request is coming from the specified user.

ASP.NET Core SignalR is an open-source library that simplifies adding real-time web functionality to apps. Real-time web functionality enables server-side code to push content to clients instantly. ... Dashboards and monitoring apps

https://www.nuget.org/packages/Microsoft.AspNet.SignalR/

SignalR Hubs API enables you to call methods on connected clients from the server. ... In the client code, you define methods that are called from the serve

* SignalR backplane 
connects multiple servers

* SignalR Hub
High-level API to call methods on connected clients from the server. 
- In the server code: methods called by the client
- In the client code: methods that are called from the server
SignalR takes care of everything behind the scenes that makes real-time client-to-server and server-to-client communications possible.

Hubs call client-side code by sending messages that contain the name and parameters of the client-side method. Objects sent as method parameters are deserialized using the configured protocol. The client tries to match the name to a method in the client-side code. When the client finds a match, it calls the method and passes to it the deserialized parameter data.

To create a hub in your code, you need to create a class that inherits from the Hub class and then you can create public methods in the Hub. These public methods can be called from connected clients. In the example below when any connected client will call the SendMessage method then the method will broadcast the user and message parameters values to all the clients connected to this Hub.

## More

- https://speakerdeck.com/davidfowl/signalr-deep-dive
- https://docs.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-5.0
- https://github.com/davidfowl/WorkersWithSignalR

- https://github.com/davidfowl/signalr-ports 
Simplifies adding real-time web functionality to apps
- signalr-go-server
- signalr-node-server

- https://github.com/davidfowl/NdcLondon2020/tree/master/talk1
- https://www.ezzylearning.net/tutorial/display-live-sports-updates-using-asp-net-core-signalr