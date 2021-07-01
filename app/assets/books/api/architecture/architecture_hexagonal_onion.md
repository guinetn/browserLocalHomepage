## HEXAGONAL ARCHITECTURE - Ports and Adapters

Software design pattern to develop applications that are highly maintainable. Idea: the fastest we apply changes to a system, the better (reduces the amount of technical depth in a system).  
Core business logic talks to other (Database, Queues, files, HTTP, FTP, NOSQL…) through a contract
Every channel has to implement that contract/interface to talking with our software
This decouple business domain from technical framework (for testing purposes)

Sometimes called "Port and Adapter" or "Onion architecture"
2005 Alistair Cockburn 


### Benefits

1. Easily incorporates any channel (Database, Queues, files, HTTP, FTP, NOSQL…)
2. Software easily tested with mocks as just need to implement the contracts.
3. Adding new requirements means plugging it, or implementing the contracts.
4. Proper separation of concern.
5. Maintains IOC as Higher level and lower level talking through contract.


# ARCHITECTURE ONION

2008 Jeffrey Palermo

Evolution of the Ports and Adapters Architecture
Externalize infrastructure and write adapter code so that the infrastructure does not become tightly coupled.
- [Onion Architecture In .Net 5](https://github.com/JayKrishnareddy/OnionArchitecture)

To construct applications in the context of better testability, practicality, constancy. Onion Architecture tends to the difficulties confronted with 3-tier and n-tier architectures and gives an answer for normal issues.   
Onion design layers associate with one another by utilizing the Interfaces.

### Layers

Hexagonal Architecture pattern in based on three main layers that connect to each other using ports and adapters. This design pattern allows for applications to keep a single code base while serving requests from multiple inputs.  
Layers are independent from each other. The key principle of the pattern is that inner layers are not aware of their outer layers. This ensures that the core business logic of your application is not affected by any of the external services.  
The object-oriented classes on each layer are going to define interfaces in order to model the data types and their dependencies. Then, the required objects are passed in using dependency injection at run time.

The number of ports that a layer expose is not fixed. Each layer can define a different set of ports than its relatives.

- inner layers expose the Ports configuration  
- outer layers connect to them via Adapters

## Domain layer (Domain Model)
The very centre of the Model, this layer can have dependencies only on itself. It represents the Entities of the Business and the Behaviour of these Entities. It exists at the center part of the Onion architecture where it consists of all application domain entities which are nothing but database models

## Framework layer (Domain Services)
This layer contains the implementation of the behaviour contracts defined in the Model layer.

## Application layer (Services)
This layer is the bridge between external infrastructure and the domain layers. The domain layers often need information or functionality in order to complete business functionality, however they should not directly depend on these. Instead, the application layer needs to depend on the the contracts defined in the Domain Services layer.

This layer is used to communicate between the Repository layer and Main Project where it consists of exposable APIs. The Service layer also could hold business logic for an entity. In this layer, the service interfaces are kept separate from their implementation for loose coupling and also the separation of concerns.

## Repository Layer
Middle layer between the services and Model objects   
This layer maintain all the Database migrations and application Data context object  
Interfaces that will consist of data access pattern of reading and write operations involving a database.

## UI Layer
The UI is nothing but a front-end application that will communicate with this API.

## External Services
Databases, Messaging systems, Notification systems, User Interface, etc.

PROS
Onion Architecture layers are associated through interfaces. Implantations are given during run time.
Application engineering is based on top of an area model.
All outer reliance, similar to data set admittance and administration calls, are addressed in outside layers.
No conditions of the Internal layer with outer layers.
Couplings are towards the middle.
Adaptable and feasible and convenient design.
No compelling reason to make normal and shared activities.
Can be immediately tried in light of the fact that the application center doesn’t rely upon anything.

CONS
Difficult to comprehend for amateurs, expectation to absorb information included. Modelers generally jumble up parting obligations between layers.
Intensely utilized interfaces

## More 

- http://treeindev.net/article/hexagonal-architecture