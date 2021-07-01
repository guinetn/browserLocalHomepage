## CQRS

Separates the read/write operations of a distributed system to increase scalability and security. This model uses commands to write data to persistent storage and queries to locate and fetch the data.
CQRS is best for data-intensive applications like SQL or NoSQL database management systems. It’s also helpful for data-heavy microservice architectures. It’s great for handling stateful applications because the writer/reader distinction helps with immutable states.

CQRS involves splitting an application into two parts internally 
— the command side: ordering the system to update state 
- the query side: that gets information without changing state.
The way event sourcing works with CQRS is to have part of the application that models updates as writes to an event log or Kafka topic.

A command center receives users requests and fetches the data and makes any necessary modifications, saves the data, and notifies the read service. The read service then updates the read model to show the change to the user.

The flow of simple CRUD (Create, Read, Update and Delete) applications can be described using the following steps:
- Controllers layer handles HTTP requests and delegates tasks to the services layer.
- Services layer is where most of the business logic lives.
- Services use repositories / DAOs to change / persist entities.
- Entities act as containers for the values, with setters and getters.
In most cases, for small and medium-sized applications, this pattern is sufficient. However, when our requirements become more complex, the CQRS model may be more appropriate and scalable. 


PRO
- Reduces system complexity by delegating tasks.
- Enforces a clear separation between business logic and validation.
- Helps categorize processes by their job.
- Reduces the number of unexpected changes to shared data.
- Reduces the number of entities that have modifying access to data.
CONS
- Requires constant back-and-forth communication between command and read models.
- Can cause increased latency when sending high-throughput queries.
- No means to communicate between service processes.

COMMAND AND QUERY RESPONSIBILITY SEGREGATION

Segregate operations that read data from operations that update data by using separate interfaces. 
This pattern can maximize performance, scalability, and security; support evolution of the system over time
through higher flexibility; and prevent update commands from causing merge conflicts at the domain level

https://github.com/PacktPublishing/ASP.NET-Core-5-Design-Patterns/tree/main/C14/CQRS

http://cre8ivethought.com/blog/2009/11/12/cqrs--la-greg-young
See sql.md and CloudBestPractices.md

CQRS (Command-Query Reponsability Separation)
    http://www.nicholassuter.com/2013/12/apprenons-ensemble-cqrs-1/
    http://martinfowler.com/bliki/CQRS.html
    https://www.codeproject.com/Articles/5264244/A-Fast-and-Lightweight-Solution-for-CQRS-and-Event

    A pattern in wich 
        the model used to update information 
                is different than 
        the model used to read information
    Beyond the CRUD for sophisticated needs

        Change that CQRS introduces is to split that conceptual model into 
            separate models for update and display,
        which it refers to as Command and Query respectively following the vocabulary of CommandQuerySeparation.


    SÃ©parer DB commandes et requÃªtes (Queries)
    Le systÃ¨me gÃ¨re des EvÃ©nements (Events), alimentÃ©es par â€œquelque choseâ€ qui traite des Commandes: Command Handler
    Les Commandes et les EvÃ©nements sont des messages qui transitent de faÃ§on asynchrone via des tuyaux.
    Les RequÃªtes, elles, sont traitÃ©es en synchrone.

    http://sachabarbs.wordpress.com/distributed-systems/


CQS 		Command Query Separation
every method should either be a command that performs an action, or a query that returns data to the caller, but not both. 
In other words, asking a question should not change the answer.

