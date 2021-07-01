### SOLID

a guideline to write maintainable, expandable and easy to understand code
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

***S - SINGLE RESPONSIBILITY PRINCIPLE***
"A class should have one and only one responsibility".
Each responsibility is an axis of change.
Code becomes coupled if classes have more than one responsibility.

***O - OPENED CLOSED PRINCIPLE***
"Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification"
- [Strategy Pattern to the rescue](https://itnext.io/how-we-avoided-if-else-and-wrote-extendable-code-with-strategy-pattern-256e34b90caf)
- Decorator design pattern

This principle is to keep the existing code from breaking when you implement new features.
* Open if you can extend it, and produce a subclass and do whatever you want with it—add new methods or fields, override base behavior, etc.
* Closed if it's 100% ready to be used by other classes—its interface is clearly defined and won’t be changed in the future

***L - LISKOV SUBSTITUTION PRINCIPLE***
"Subtypes must be substitutable for their base types."
This is polymorphism. just a way of ensuring that inheritance is used correctly.

***I - INTERFACE SEGREGATION PRINCIPLE***
"Clients should not be forced to depend upon interfaces that they do not use."
A class don't have to implement not needed methods from an interface to implement: Share functionality among many interfaces.
If a class wants to implement the interface, it has to implement all of the methods, some of which may not be needed by that
class at all. So, doing this also introduces unnecessary complexity, and reduces maintainability or robustness in the system.
The Interface Segregation principle ensures that Interfaces are developed so that each of them have their own responsibility
and thus they are specific, easily understandable, and re-usable.

***D - DEPENDENCY INVERSION PRINCIPLE***
Depend on abstractions, not on concrete objects
High level modules should not depend upon low level modules

    BAD
       
        Employee class 
            // Have to persist to XML and a database
            ToXML() Break single responsibility principle
            ToDB()  Break single responsibility principle
            To(saveMethod)  Hard-coding a set of devices = Break Open Closed principle

    GOOD
       
        DataWriter abstract class 
            |___ class XMLDataWriter
            |___ class DbDataWriter

        class EmployeeWriter  
            Save(DataWriter)
                    |___ Output method depend upon abstractions not concrete classes
                        The dependencies have been inverted. 
                        Now we can create new types of ways for Employee data to be written   

## more

- https://towardsdatascience.com/5-principles-to-write-solid-code-examples-in-python-9062272e6bdc