## BDD (BEHAVIOUR-DRIVEN DEVELOPMENT)

méthodologie agile proposée par Dan North pour aller au delà du TDD
Extends TDD by writing test cases in a natural language in combination with Domain Driven Design to describe the purpose 
and benefit of code before writing it.



 	Objectif: améliorer la compréhension et la collaboration du métier, du Product Owner, des développeurs, des testeurs et de
 	toute autre partie prenante pertinente en les rassemblant autour d’un langage commun : le Gherkin.
	BDD suggests that 
		unit test names be whole sentences starting with a conditional verb ("should" in English for example) and should be written in order of business value. 
		Acceptance tests should be written using the standard agile framework of a user story: 
			"Being a [role/actor/stakeholder] 
			I want a [feature/capability] yielding a [benefit]". 
			Acceptance criteria should be written in terms of scenarios and implemented in classes: 
				Given [initial context], 
				when [event occurs], 
				then [ensure some outcomes] .

			 	| Etant donné que ‘contexte initial’
				| Quand ‘un événement’
				| Alors ‘un certain résultat’
                
Main components of DDD are: Entity, Value Object, Aggregate, Service and Repository.

* Entity 		An object that has an identity- it is unique within the system, like Customer, Employee etc.

* Value Object 	An object that has no identity within the system like Rate, State etc.
                Note: A value object can become an entity depending on the situation.
                Value Type ça va pouvoir vous permettre d’exprimer votre domaine mais aussi d’avaler une grosse partie de la complexité dans votre code.
                Un Value Type c’est ce qu’ils sont qui compte, pas qui ils sont.

                les billets…10 € Ce qui est important c’est la valeur pas les identités. 
                Alors sauf, si mon domaine : je suis banque de France ou banque fédérale 
                mon domaine c’est de suivre la traçabilité des billets. 
                Dans ce cas là, les 10€ ne sont plus un Value Type mais c’est une entité, quelque chose dont je vais 
                vouloir suivre l’identité à travers le temps (numéro dessus, Mon domaine c’est ça)

* Aggregate: 	An aggregate root is a special kind of entity that consumers refer to directly. 
                All consumers of the aggregate root are called as aggregate. 
                The aggregate root guarantees the consistency of changes being made within the aggregate.

* Service 		A service is a way of dealing with actions, operations and activities within your application.

* Repository 	A repository is responsible to store and to retrieve your data. 
                It is not a concern how and where data will be persist. So, it can be SQL server, oracle, xml, text file or anything else. 
                Repository is not a Data Access Layer but it refers to a location for storage, often for safety or preservation.                
                
                
