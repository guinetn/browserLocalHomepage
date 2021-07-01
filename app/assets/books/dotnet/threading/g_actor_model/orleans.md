# orleans

Frameworks to build cloud native applications on dotnet. Any kind of distributed apps. Model "grains' to model app.


Open source actor framework
an actor framework? → popular .net actor framework is AKKA.net (event sourcing)
  
An Orleans application consists of 
  
***Grains*** (interfaces + implementations)
The “virtual actors” and/or “primitives” that are described in the actor model definition 
Are objects containing logic that is to be distributed. Each individual grain is guaranteed to operate in a single-threaded execution model as to greatly simplify the programming, and avoid race conditions. The grains are written in an asynchronous manner, and are intended for very fast running operations
***Silos*** Host
where your “grains” are kept. A silo can contain many grain types, as well as many instantiations of those types, depending on your needs.
***Clusters***
a collection of silos. This allows for the “scale out” portion of Orleans.
***Clients***

>dotnet new console -n Kritner.OrleansGettingStarted.Client
dotnet new console -n Kritner.OrleansGettingStarted.SiloHost
dotnet new classlib -n Kritner.OrleansGettingStarted.GrainInterfaces
dotnet new classlib -n Kritner.OrleansGettingStarted.Grains

download.code(https://gist.githubusercontent.com/Kritner/dbba6369cf381ee5f3cae7f75131584b/raw/6840bee0f623f8362bcccec2655dbc706e69d6c8/Program.cs)

- https://dotnet.github.io/orleans
- https://dotnet.github.io/orleans/Documentation/index.html
- https://getakka.net/ 
- https://medium.com/swlh/getting-started-with-microsoft-orleans-882cdac4307f
- https://channel9.msdn.com/Shows/On-NET/Setting-up-Observability-in-Orleans