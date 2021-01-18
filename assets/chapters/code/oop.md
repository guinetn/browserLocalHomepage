# OOP (OBJECT ORIENTED PROGRAMMING) PRINCIPLES

metaphors about objects instead of writing lines of functional code
Abstraction (Interface)
    representation of essential features without including background details or explanation
    Making a program progressively more general and less specific

3 OOP pillars: Encapsulation, Inheritance, Polymorphism

- ENCAPSULATION
    Restrict access to some of the objects components: protect variables from unwanted change
    Wrapping up of data and functions in to a single unit is known as encapsulation.
    Methods/properties act as an interface.

- POLYMORPHISM
    Exhibiting different behaviors in different contexts.
    The ability to send a message to an object without knowing its specific class.
    Ex: virtual functions, function and operator overloading.

- INHERITANCE

    If you don’t have a feature but someone actually uses it
    To reuse/extend a class. If you just want to reuse a class I recommend going with composition.

    * is class antipattern ?
            
        Inheritance is not the core of object oriented programming, and it is commonly overrated because 
        it creates more harm than help and should only used in certain situations
        
        “Classical Inheritance is Obsolete: How to Think in Prototypal OO”

        https://medium.com/javascript-scene/common-misconceptions-about-inheritance-in-javascript-d5d9bab29b0a
        https://medium.com/javascript-scene/how-to-fix-the-es6-class-keyword-2d42bb3f4caf
        https://ericleads.wordpress.com/2013/02/11/fluent-javascript-three-different-kinds-of-prototypal-oo/

        follow the Gang of Four’s advice on this point: “Favor object composition over class inheritance.”

    * INHERITANCE FORMS
        
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


# Abstract class 
    
    Abstraction: showing only the functionality (hiding the internal details)
    'abstract' modifier indicates the incomplete implementation. 
    a class that contains at least one abstract method
    incomplete class (contains abstract methods without body)

    Abstract methods: declaration only
        method that is declared, but not implemented in the code (no body)			 
    
    can have abstract methods
    can have constructors/destructors		
    cannot be inherited by structures
    cannot support multiple inheritance
    cannot be instantiated: if you have an abstract class with concrete methods then it can be subclassed and the subclass can then be instantiated.
    
    Usage
        cannot be instantiated. Need its child class(es) to fill out the tasks. 
        designed to be subclassed
        provide common functionality across a set of related classes while also allowing default method implementations

        wpf: 
        public abstract class BindableBase : INotifyPropertyChanged 
        {
            implemented ...
        }
        public abstract class ViewModelBase : BindableBase
        {

        }
        public class BookViewModel : ViewModelBase, IDisposable

        EF

# Static class
    
    sealed = cannot be inherited
    They cannot inherit from any class except Object. 
    Static classes cannot contain an instance constructor