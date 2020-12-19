# UML (UNIFIED MODELING LANGUAGE)

A picture is worth a thousand words  
general-purpose, developmental, modeling language in the field of software engineering, that is intended to provide a standard way to visualize the design of a system.  

## Structural UML diagrams
* Class diagram
* Package diagram
* Object diagram
* Component diagram
* Composite structure diagram
* Deployment diagram
*	
## Behavioral UML diagrams
* 	Activity diagram
* 	Sequence diagram
* 	Use case diagram
* 	State diagram
* 	Communication diagram
* 	Interaction overview diagram
* 	Timing diagram


## Notation
Object. A specific entity or concept that has meaning in an application domain.
Class. A definition of a set of potential objects that have the same data, behavior, and relationships.
Attribute. A data value defined in a class and held within an object that has meaning within the application domain.
Behavior. A service defined in a class and provided by an object.
Method. The implementation of a behavior in an object-oriented programming language.
Association. A "peer-to-peer" relationship between classes.
Aggregation. A "whole/part" relationship between classes.
			Car <>-------> Wheel      
Inheritance. A "generalization/specialization" relationship between classes.

Cardinality/Multiplicity. The minimum and maximum number of objects that participate in an association or aggregation. The common (interesting) ones are 0..*, 0..1, 1..*, and 1..1

Polymorphism. The ability to send a message to an object without knowing its specific class.

class diagrams notation (uml)

    * OBJECT
        A specific entity or concept that has meaning in an application domain.

    * CLASS
        A definition of a set of potential objects that have the same data, behavior, and relationships.

    * ATTRIBUTE
        A data value defined in a class and held within an object that has meaning within the application domain.

    * BEHAVIOR
        A service defined in a class and provided by an object.

    * METHOD
        The implementation of a behavior in an object-oriented programming language.

    * ASSOCIATION
        A ------- B
        A and B can call each other    
        A "peer-to-peer" relationship between classes.

    * INHERITANCE
        A ◄------ B
        A "generalization/specialization" relationship between classes.

    * AGGREGATION
        A ------- B
        A "whole/part" relationship between classes.

    * CARDINALITY/MULTIPLICITY
        The minimum and maximum number of objects that participate in an association or aggregation. The common (interesting) ones are 0..*, 0..1, 1..*, and 1..1

    * POLYMORPHISM
        The ability to send a message to an object without knowing its specific class.

# Inheritence vs Composition vs aggregation

    inheritence 
        is inheriting from a base class 
    composition 
        is allowing properties of your classes to be filled, e.g. MyCompany.Person. 
        A own an instance of B. B cannot exists without A
    aggregation
        A reference an instance of B. B survive if A is disposed

    Most of the time you will use composition, and DI you get to use it via Setter injection, or constructor injection which then fill properties.

## Resources

* http://www.tutorialspoint.com/uml/uml_overview.htm
* https://www.smartdraw.com/uml-diagram/
* https://www.youtube.com/watch?v=OkC7HKtiZC0
