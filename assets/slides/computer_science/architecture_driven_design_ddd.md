## DDD 	Domain Driven Design

https://blog.soat.fr/2016/09/domain-driven-design-ddd-ou-la-conception-pilotee-par-le-domaine/

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