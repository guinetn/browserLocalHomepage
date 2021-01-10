# CQRS -COMMAND AND QUERY RESPONSIBILITY SEGREGATION

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


    Séparer DB commandes et requêtes (Queries)
    Le système gère des Evénements (Events), alimentées par “quelque chose” qui traite des Commandes: Command Handler
    Les Commandes et les Evénements sont des messages qui transitent de façon asynchrone via des tuyaux.
    Les Requêtes, elles, sont traitées en synchrone.

    http://sachabarbs.wordpress.com/distributed-systems/


CQS 		Command Query Separation
every method should either be a command that performs an action, or a query that returns data to the caller, but not both. 
In other words, asking a question should not change the answer.

