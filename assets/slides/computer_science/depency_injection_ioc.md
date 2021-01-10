# DEPENCY INJECTION - IOC Inversion  Of Control

* Remove the dependency between two objects
* Style of wiring objects together
* DI containers improve the composition of whole object graphs
* Ideal for mocking

  ## What is dependency?
  public class Address { }
  public class Customer
  {
      Address address;
      public Customer() { address = new Address(); }
  }

 ## Remove dependency between two classes?

  Define an interface and share it with any object dependant of it

  1. Define a contract for Address and share this contract to both Address and 
  
  Customer classes
     and any other class which are dependent on Address.
     App now depend on the abstraction of Adresss rather than on concrete class.

    // contract for Address
    public interface IAddress  { }

    public class Address : IAddress { }

    public class Customer
    {
        IAddress address;               // reference to IAddress interface not concrete class Address
        public Customer()
        {
            address = new Address();   // Problem: still depends on Address in it's constructor as it is instantiated in the constructor
        }
    }


In the above the program we can see there is no dependency between Class Customer and Address. Instance of Customer is created in main program and passed to the constructor as a parameter.  This is called constructor injection. There is another way called property injection.


Then what is the solution?
We will move the instantiation of class Address to some other class which will take care of creating the instance. By this way there is no dependency between Customer and Address.  This can be better handled using dependency injection.

What is dependency injection?
With dependency injection, you can substitute different concrete class implementations at runtime.

There should be 3 elements for DI(dependency injection).
A dependent consumer (in our case class Customer)
Declaration of dependencies as contractors (Address is dependency and IAddress is the contract)
Injector, which creates instances of concrete classes ( in our explanation , we referred to this as  some other class ) . There are lots of injectors available in the market like Ninject, Microsoft unity ….

## What is inversion of control?
As I said, I will be considering DI for explaining IoC. Using DI, we are inverting the control of object creation from a dependent object to an injector/caller which will take care of creating the instance.

public interface IAddress
{
}
public class Address: IAddress
{
}
public class Customer
{
    IAddress address;
    public Customer(IAddress adress)
    {
        this.address = address;
    }
}
class Program
{
    static void Main(string[] args)
    {
        IAddress address = new Address();
        Customer customer = new Customer(address);
    }
}


Three basic type of Dependency Injection
* CONSTRUCTION INJECTION
* SETTER INJECTION 
* INTERFACE BASED INJECTION


# Registering
different ways of registering your classes to Dependency Injection system
# Resolving
Registration informs IOC (Inversion of Control) Container (a.k.a. DI frameowk) about your classes, their dependencies and lifecycles. 
Sometimes, directly resolve your dependency instead of constructor & property injection. 


## OBJECTS LIFESPAN 

* Singleton   
A single instance is created and acts like a singleton.
* Instance    
A new object is created upon each request = specific instance all the time. 
You are responsible for its initial creation.
* Transient   
A new instance is created every time.
* Scoped    
A single instance is created inside the current scope. It is equivalent to Singleton in the current scope.
* Thread
* Pooled
* Per Web Request
