### DDD - Domain Driven Design

https://blog.soat.fr/2016/09/domain-driven-design-ddd-ou-la-conception-pilotee-par-le-domaine/

Centres the business domain at the core of the development. 
Benefit: avoid messy terminology which lead to confusing systems
Origin: 2003 by Eric Evans which stablishes the base for developing using DDD ideas.

The mainstream though on Domain Driven Design is about Entities, Value Objects, Aggregates, Repositories, Services, Factories... all kinds of technical patterns. Because of this, most don't think they need Domain Driven Design because it's complicated for their domain. Why would you need all that "stuff"? Well maybe you don't! In a large system, modeling your domain, defining boundaries, and how they relate is far more important than concerning yourself with if you're using the Repository pattern correctly.

## Domain Driven Design concepts 
Use them ensures that the software is developed to satisfy the needs of a business domain and not the other way around.

- Business domain  
can be anything: health, insurance, economy, advertisement…
- Naming convention and concepts  
should be used when defining classes, interfaces, data models

## keys

* COLLABORATION with domain experts = accurate data models enhancing application's object-oriented mapping  

* Build a UBIQUITOUS LANGUAGE that introduces the domain terminology into the software application that is been developed. clarify terminology by consulting experts. The Ubiquitous language should not be fixed. It needs to evolve and improve over time in order to accommodate for system updates and new software requirements.

## DDD Object Classification

OO application is organised into objects.

### Entities
They represent unique identities which run through time. Their properties might be the same as other entities but they reference is still unique. Examples: Employee, Department, Car, Company, Insurance, etc.

### Value objects
They are usually tinny objects that are defined by the value of their properties. If two objects have the same property values, they are equal. Examples: Date, password, amounts, etc. C# 'record' type

### Service objects
Objects that hold functionality used by other objects to perform a certain task. A running application usually has a single instance of a service object.


## DDD Aggregates pattern 

Pattern grouping domain objects as individual units, a cluster of entities and value objects which are conceptually bound together. 
Aggregates example: a customer order and its purchased products

Aggregates define a set of boundaries that structure the internal object relations and their core domain concepts. Boundaries rules also prevent outside access to the internal object collections and properties of an aggregate. If an object wants to access an entity of an aggregate, then it needs to send the request to the aggregate root object.

Maintain integrity of aggregate root’s internal objects by preventing unwanted data modification of entities and value objects (c# 'record' type).

It is important not to mix aggregate objects with standard collection data as: arrays, sets, maps… Aggregates are objects within the scope of Domain Driven Design.

## DDD Core: Strategic Design → Bounded Context and Context Maps

Ability to define a software system that is aligned with the concepts and needs of its domain business. Strategic Design (strategic modelling) set the base for building up 

- Bounded Context
Difficult for large software systems to defines a unique model that is going to represent the full picture of the core domain. BC divide a large system into individual bounded contexts which can hold their own unique models and unrelated concepts. Bounded Contexts can also define a unique Ubiquitous Language that is scoped within their own context.

- Ubiquitous Language

- Context Maps
Define the relationships between Bounded Contexts in DDD systems. Stablishing boundaries in Bounded Contexts ensure each context is unique and Context Maps help us understand how they relate to each other.
These tools allow domain experts and software engineers to stablish a common ground for building domain models using a terminology that is understandable to all team preventing ambiguity in the language that is been used.


définir une vision et un langage partagés par toutes les personnes impliquées dans la construction d’une application

1. Toute conception métier complexe doit se baser sur un modèle de domaine.
2. Se focaliser en premier sur le cœur de métier et sa logique au lieu des contraintes techniques.

User Stories
  besoins utilisateur à implémenter
  En tant que X je veux Y pour pouvoir Z
Ubiquitous Language

Express model with 	→ 	SERVICES
			

								 			 		→ Access with 	→ REPOSITORIES 		←		
																							↑ 	Access with
													→ Maintain integrity with → 			↑
																					AGGREGATES 	 		
			Express model with 	→	ENTITIES		→ Act as root of 		  → 			↓
																							↓
													→ Encapsulate with → 					↓
																			FACTORIES	← Encapsulate with

			Express model with 	→ 	VALUE OBJECTS   → Encapsulate with →    FACTORIES/AGGREGATES


			isolate domain with 	→ 	Layered architecture


	http://www.codeproject.com/Articles/768664/Introduction-to-ASP-NET-Boilerplate
	http://www.asp.net/mvc/overview/older-versions/getting-started-with-ef-5-using-mvc-4/implementing-the-repository-and-unit-of-work-patterns-in-an-asp-net-mvc-application


	Domain layer
		"Responsible for representing concepts of the business, information about the business situation, and business rules" 
		The core layer is the Domain Layer. 
		Domain Layer defines your Entities, implements your business rules and so on.

	Entities 
		one of the core concepts of DDD. Eric Evans describe it as "An object that is not fundamentally defined by its attributes, but rather 
		by a thread of continuity and identity". So, entities have Id´s and stored in a database.

		public class Task : Entity<long> 			← long primary key type
		{
		    public virtual Person AssignedPerson { get; set; }
		    public virtual string Description { get; set; }
		    public virtual DateTime CreationTime { get; set; }
		    public virtual TaskState State { get; set; }
		    public Task()
		    {
		        CreationTime = DateTime.Now;
		        State = TaskState.Active;
		    }
		}

		
		public class Person : Entity     ← If your Entity´s primary key is int, you may not define primary key type and directly implement IEntity interface
		{
		    public virtual string Name { get; set; }
		}                


## More

- https://www.youtube.com/watch?v=Z_nmvQFc3Es
- http://treeindev.net/article/domain-driven-design
- https://dzone.com/refcardz/getting-started-domain-driven