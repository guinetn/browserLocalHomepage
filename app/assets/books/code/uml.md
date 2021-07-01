# UML (UNIFIED MODELING LANGUAGE)

A picture is worth a thousand words  
Software Modeling language providing a standard way to visualize the design of a system.  

## Tools

https://yuml.me

## Structural UML diagrams
* Class diagram
describes structure of an object-oriented system by showing classes/classes relationships
* Package diagram
Presenting structure and dependencies between sub-systems or modules
* Object diagram
* Component diagram
Simplified view of a large system. Classifying groups of classes into components supports the interchangeability and reuse of code.
* Composite structure diagram
* Deployment diagram
To visualize the static aspect of physical nodes and their relationships and to specify their details for construction.
## Behavioral UML diagrams
* 	Activity diagram
Similar to a business work flow diagram or simply a flowchart with much richer semantics.
* 	Sequence diagram
Describes an interaction among a set of objects participated in a collaboration (or scenario), arranged in a chronological order
* 	Use case diagram
* 	State diagram
Model the dynamic behavior of individual class objects, use cases, and entire systems
* 	Communication diagram
* 	Interaction overview diagram
* 	Timing diagram


## Notation
		  
Inheritance
A "generalization/specialization" relationship between classes.

Cardinality/Multiplicity
The minimum and maximum number of objects that participate in an association or aggregation. The common (interesting) ones are 0..*, 0..1, 1..*, and 1..1

Polymorphism
The ability to send a message to an object without knowing its specific class.

CLASS DIAGRAMS NOTATION (UML)

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
        A ◊------> B
        Car ◊----> Wheel    
        A "whole/part" relationship between classes.

    * CARDINALITY/MULTIPLICITY
        The minimum and maximum number of objects that participate in an association or aggregation. The common (interesting) ones are 0..*, 0..1, 1..*, and 1..1

    * POLYMORPHISM
        The ability to send a message to an object without knowing its specific class.

◯  interface
A ────────▶ B
A ────────→ B
A --------▶ B
A ◆───────▶ B

A ◀──────── B
A ←──────── B
A ◀-------- B
A ◀-------◆ B

A ◀──────▶ B
A ◀------▶ B

A ◆------- B  
A ◊-------- B
A ------- B

[Customer]->[Order]               // Association
[Customer]<>->[Order]             // Aggregation
[Customer]++->[Order]             // Composition
[Customer]1-0..1>[Order]          // Cardinality
[Customer]1-0..orders 1>[Order]   // Assoc Labels
[Customer]-.-[note: DAO]          // Notes
[Customer]^[Member]               // Inheritance
[Customer|name;address|save()]    // Properties
[≪IDisposable≫;Customer]         // Interface
[Customer|var arr［］ ]            // Brackets
[Customer {bg:green}]             // Colour


see oop page



## Resources

* https://online.visual-paradigm.com/fr/diagrams/tutorials/
* http://www.tutorialspoint.com/uml/uml_overview.htm
* https://www.smartdraw.com/uml-diagram/
* https://www.youtube.com/watch?v=OkC7HKtiZC0
