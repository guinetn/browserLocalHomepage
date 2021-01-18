# HEXAGONAL ARCHITECTURE 

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

### Layers

## Domain Model
The very centre of the Model, this layer can have dependencies only on itself. It represents the Entities of the Business and the Behaviour of these Entities.

## Domain Services
This layer contains the implementation of the behaviour contracts defined in the Model layer.

## Application Services
This layer is the bridge between external infrastructure and the domain layers. The domain layers often need information or functionality in order to complete business functionality, however they should not directly depend on these. Instead, the application layer needs to depend on the the contracts defined in the Domain Services layer.

## External Services
Databases, Messaging systems, Notification systems, User Interface, etc.