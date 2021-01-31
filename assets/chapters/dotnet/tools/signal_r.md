# SignalR

Real-time update notification (chat, any refresh needed,...replace long polling) 

SignalR provides an API for creating server-to-client remote procedure calls (RPC). The RPCs call JavaScript functions on clients from server-side .NET Core code.

SignalR uses Websockets to push messages between the clients and the server for real-time updates. If for some reason Websockets are not available, then it will fall back to other transport mechanisms.

WebSocket: HTML5 API for bi-directional communication between the browser and server. 
A stateful protocol 

SignalR uses encryption + digital signature to protect the connection token. 
For each request, the server validates the contents of the token to ensure that the request is coming from the specified user.

ASP.NET Core SignalR is an open-source library that simplifies adding real-time web functionality to apps. Real-time web functionality enables server-side code to push content to clients instantly. ... Dashboards and monitoring apps

https://www.nuget.org/packages/Microsoft.AspNet.SignalR/

SignalR Hubs API enables you to call methods on connected clients from the server. ... In the client code, you define methods that are called from the serve

* SignalR backplane 
connects multiple servers


## More

- https://docs.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-5.0
