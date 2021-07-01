# OOP - OBJECT ORIENTED PROGRAMMING

## OOP PRINCIPLES

The 3 OOP pillars: Encapsulation, Inheritance, Polymorphism

### Entities and relationship

#### Entity
A person, place, car, anything that `can be represented as an object `

#### Entity Relationship
Relationship defines the `dependency that entities share` amongst each other.

#### One-One Relationship
#### One-Many Relationship
a record in One object can be associated or related to Many objects

#### Many-Many Relationship
### OBJECT
A specific entity or concept that has meaning in an application domain.

### Abstraction / Interface: be general, not specific
Showing only the functionality (hiding the internal details)
'abstract' modifier indicates the incomplete implementation. 

Representation of essential features a class must have without including background details (code) or explanation
To make a program progressively more general and less specific
Metaphors about objects instead of writing lines of functional code

### CLASS
A definition of a set of potential objects that have the same data, behavior, and relationships.

* Is class antipattern ?       
Inheritance is not the core of object oriented programming, and it is commonly overrated because it creates more harm than help and should only used in certain situations
“Classical Inheritance is Obsolete: How to Think in Prototypal OO”
https://medium.com/javascript-scene/common-misconceptions-about-inheritance-in-javascript-d5d9bab29b0a
https://medium.com/javascript-scene/how-to-fix-the-es6-class-keyword-2d42bb3f4caf
https://ericleads.wordpress.com/2013/02/11/fluent-javascript-three-different-kinds-of-prototypal-oo/

Gang of Four’s advice: “Favor object composition over class inheritance”

#### Access modifiers
public
private 
protected
internal
protected internal
    
#### Sealed class
Cannot be inherited
They cannot inherit from any class except Object. 

####  Static class
Cannot contain an instance constructor
        
####  Abstract class
Abstraction: showing only the functionality (hiding the internal details)
'abstract' modifier indicates the incomplete implementation 
Incomplete class that contains at least one abstract methods (without body)
		 
* can have abstract methods
* can have constructors/destructors		
* cannot be inherited by structures
* cannot support multiple inheritance
* cannot be instantiated: if you have an abstract class with concrete methods then it can be subclassed and the subclass can then be instantiated.

Usage
- cannot be instantiated. Need its child class(es) to fill out the tasks. 
designed to be subclassed
- provide common functionality across a set of related classes while also allowing default method implementations

wpf
```c#    
public abstract class BindableBase : INotifyPropertyChanged 
{
    implemented ...
}
public abstract class ViewModelBase : BindableBase
{

}
public class BookViewModel : ViewModelBase, IDisposable
```

EF

####  Abstract method 
Declaration only
Method that is declared, but not implemented in the code (no body)	
### ATTRIBUTE
A data value defined in a class and held within an object that has meaning within the application domain.

### BEHAVIOR
A service defined in a class and provided by an object.

### METHOD
The implementation of a behavior in an object-oriented programming language.

### ASSOCIATION
A --- B
A and B can call each other    
A "peer-to-peer" relationship between classes.

### INHERITANCE
B ---► A
A "generalization ► specialization" relationship between classes.

Is inheriting from a base class 
Relationships between objects: "An apple is a Fruit"

```c++
class Fruit  { // superclass… }
class Apple : Fruit { // subclass… }
```

L'héritage est un mécanisme de transmission des caractéristiques d'une classe (ses attributs et méthodes) vers une sous-classe. Une classe peut être spécialisée en d'autres classes, afin d'y ajouter des caractéristiques spécifiques ou d'en adapter certaines. Plusieurs classes peuvent être généralisées en une classe qui les factorise, afin de regrouper les caractéristiques communes d'un ensemble de classes.

Ainsi, la spécialisation et la généralisation permettent de construire des hiérarchies de classes. L'héritage peut être simple ou multiple. L'héritage évite la duplication et encourage la réutilisation.

If you don’t have a feature but someone actually uses it
To reuse/extend a class. If you just want to reuse a class, use composition (over inheritance)

See Prototype design pattern

### INHERITANCE FORMS
    
    see uml page
    feature of some object-oriented computer programming languages 
    is inheriting from a base class 

    * Single Inheritance
        
        When a class extends another one class 
        A is a parent class of B and B would be  a child class of A
        
        A ───▶ B				

    * Multiple inheritance 

        A ──┐			   	   
            ├───▶ C
        B ──┘

        an object or class can inherit characteristics and features from more than one parent object or parent class.
        Increased complexity
        Semantic ambiguity often summarized as the diamond problem: confusion when two base classes implement a method with the same name.
        Not being able to explicitly inherit multiple times from a single class.

        Multiple Inheritance is very rarely used in software projects. Using Multiple inheritance often leads to problems in the hierarchy. This results in unwanted complexity when further extending the class.
        Most of the new OO languages like Small Talk, Java, C# do not support Multiple inheritance. 
        Multiple Inheritance is supported in C++

    * Multilevel inheritance 
    
        A ───▶ B ───▶ C

        where one can inherit from a derived class, thereby making this derived class the base class for the new class.        	
        C is subclass or child class of B and B is a child class of A

    * Hierarchical Inheritance

                        ___ classes B,C D inherits the same class A
                        /	
                ┌────▶ B
        A ────├────▶ C
        \	  └────▶ D				
            \
            A is parent class (or base class) of B,C & D
            One class is inherited by many sub classes. 	    			    				 

    * Hybrid Inheritance

        a combination of Single and Multiple inheritance. Ex: diamond  


https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53
The problem with object-oriented languages is they’ve got all this implicit environment that they carry around with them. You wanted a banana but what you got was a gorilla holding the banana and the entire jungle.


Composition and aggregation are two types of association which is used to represent relationships between two classes

### COMPOSITION (OWN): "is-a-part-of"

is allowing properties of your classes to be filled, e.g. MyCompany.Person. 
A own an instance of B. B cannot exists without A
Gang of Four’s advice on this point: “Favor object composition over class inheritance”

Composition denotes an ownership "is-a-part-of" relationship between objects using instance variables that are references to other objects
Parent owns child entity so child entity can't exist without parent entity

```c++
class Fruit  { // superclass… }
class Apple { // subclass… 
    private Fruit;
    public Apple()  { 
        fruit = new Fruit(); // Parent owns child entity, child can't exist without parent
    }
}
```

well-known object-oriented design principle which is: 
***favour object composition over class inheritance***

Class inheritance is said to break encapsulation as the implementation of a parent class is been exposed to their subclasses. Class inheritance also creates a tied coupling between the classes and stablishes a dependency in the system. These dependencies can cause problems when the parent class gets an internal modification as it is impacting all its subclasses.
Class decoupling in a system will give you flexibility when adding new functionality or existing code gets rewritten.

Object composition is based on a “has a” relationship whereas Class inheritance is based on “is a” relation.
object composition there are less dependencies in terms of implementation as the objects been reused keep their interfaces.

Ideally you shouldn’t have to create new components to achieve code reusability. If objects are well-designed, you should be able to get all the functionality you need by assembling existing objects through object composition.
http://treeindev.net/article/object-composition-class-inheritance

### AGGREGATION: "Has-A"
A ◊------> B
Car ◊----> Wheel    
A "whole/part" relationship between classes.

A reference an instance of B. B survive if A is disposed
Parent and child entity maintain "Has-A" relationship but both can also exist independently

A classes relation saying that one class instances are components of the other class
Define objects made of others objects

```c++

class Fruit  { // superclass… }
class Apple { // subclass… 
    private Fruit fruit = null;
    public Apple(Fruit fruit) 
    {
        this.Fruit = fruit;
    }
}
Fruit f = new Fruit();
Apple a = new Apple(f);
```

# Inheritence vs Composition vs aggregation

Establishing relationships between classes: inheritance or composition
Favor composition over inheritance is a design principle that gives the design higher flexibility
>Most of the time you will use composition, and DI you get to use it via Setter injection, or constructor injection which then fill properties.
Overuse of inheritance leads to thickly layered programs that destroy transparency
>Some languages, notably Go, use type composition exclusively



#### Class or not Class?

Gang of Four’s advice on this point: “Favor object composition over class inheritance”

Classes should achieve polymorphic behavior and code reuse by their composition (by containing instances of other classes that implement the desired functionality) rather than inheritance from a base or parent class
1. Create interfaces representing the system's behaviors (Give OO Polymorphic behavior)
2. Implement classes using interfaces 
3. Add these classes to business domain classes as needed
Business domain classes may all be base classes without any inheritance at all
Any business domain class that contains a reference to the interface can easily support any implementation of that interface and the choice can even be delayed until run time

##### PRO
    Favor composition over inheritance is a design principle that gives the design higher flexibility
    Overuse of inheritance leads to thickly layered programs that destroy transparency
    Some languages, notably Go, use type composition exclusively

##### CON
    methods provided by individual components may have to be implemented in the derived type, even if they are only forwarding methods. In contrast, inheritance does not require all of the base class's methods to be re-implemented within the derived class. Rather, the derived class only need to implement (override) the methods having different behavior than the base class methods. This can require significantly less programming effort if the base class contains many methods providing default behavior and only a few of them need to be overridden within the derived class.




### CARDINALITY/MULTIPLICITY
The minimum and maximum number of objects that participate in an association or aggregation. The common (interesting) ones are 0..*, 0..1, 1..*, and 1..1

### ENCAPSULATION    
Restrict access to some of the objects components: protect variables from unwanted change
Wrapping up of data and functions in to a single unit is known as encapsulation.
Methods/properties act as an interface.

L'encapsulation consiste à masquer les détails d'implémentation d'un objet, en définissant une interface. L'interface est la vue externe d'un objet, elle définit les services accessibles (offerts) aux utilisateurs de l'objet.

L'encapsulation facilite l'évolution d'une application, car elle stabilise l'utilisation des objets : on peut modifier l'implémentation des attributs d'un objet sans modifier son interface, et donc la façon dont l'objet est utilisé.

L'encapsulation garantit l'intégrité des données, car elle permet d'interdire, ou de restreindre, l'accès direct aux attributs des objets.

### POLYMORPHISM

Exhibiting different behaviors in different contexts.
The ability to send a message to an object without knowing its specific class.
Ex: virtual functions, function and operator overloading.

Le polymorphisme représente la faculté d'une méthode à pouvoir s'appliquer à des objets de classes différentes. Le polymorphisme augmente la généricité, et donc la qualité, du code.


