# DEPENCY INJECTION - IOC Inversion  Of Control

Software application design rule: loosely coupled = greater reusability, maintainability,  testability. 

Dependency Injection (DI) reduces the coupling between classes and moves the binding of abstraction and concrete implementation out of the dependent class. 

DI creates loosely coupled classes. The Dependency Injection (DI) pattern uses a builder object to initialize objects and provide the required dependencies to the object, meaning that it allows developers to "inject" a dependency from outside the class. There are four ways of achieving the Dependency Injection.

![](assets/chapters/dotnet/assets/di/di.jpg)

![](assets/chapters/dotnet/assets/di/di-host.png)
Strongly Coupling the Client to the Logging Service Implementation

![](assets/chapters/dotnet/assets/di/di-host-2.png)
Decoupling the Client/Library from the Specific Logging Implementation via Dependency Injection

![](assets/chapters/dotnet/assets/di/di-sequence-diagram.png)
![](assets/chapters/dotnet/assets/di/di-unit-testing.png)

![](assets/chapters/dotnet/assets/di/di-unit-tests-host.png)
Unit Testing with Dependency Injection so a Mock Type Instance Can Be Used
 
 
 
 
 
* Remove the dependency between two objects
* Style of wiring objects together
* DI containers improve the composition of whole object graphs
* Ideal for mocking: common need for dependency injection is in unit tests 

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

You can also use other design patterns, such as the Factory or Publisher/Subscriber patterns, to reduce the dependency between components.

## IOC - inversion of control

Pattern of decoupling the actual instance returned

A way to apply the Dependency Inversion Principle, mechanism that allows your higher-level components to depend on abstraction rather than the concrete implementation of lower-level components.
Hollywood Principle. This name comes from the Hollywood cinema industry, where, after an audition for an actor role, usually the director says, don't call us, we'll call you.

Using DI, we are inverting the control of object creation from a dependent object to an injector/caller which will take care of creating the instance.

Rather than the client determining what is instantiated, as it does when explicitly invoking the constructor with the new operator, dependency injection determines what will be returned.  Dependency injection registers an association between the type requested by the client (generally an interface) and the type that will be returned.  Furthermore, dependency injection generally determines the lifetime of the type returned, specifically, whether there will be a single instance shared between all requests for the type, a new instance for every request, or something in between.


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
* CONSTRUCTOR INJECTION
with this approach, you create an instance of your dependency and pass it as an argument to the constructor of the dependent class.
* Method Injection - INTERFACE BASED INJECTION
in this case, you create an instance of your dependency and pass it to a specific method of the dependent class.
* SETTER/PROPERTY INJECTION 
this approach allows you to assign the instance of your dependency to a specific property of the dependent class.

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






## Dependency Injection Design Pattern

A dependency describes the relationship among entities
To remove the dependencies between the objects: class decoupling

technique in which an object receives other objects that it depends on. These other objects are called dependencies. ... The "injection" refers to the passing of a dependency (a service) into the object (a client) that would use it.

A design pattern used to implement IoC
Moves the dependencies to the interface of components.
Reduce the cohesion or coupling amongst the components in an application.

Makes a class independent of its dependencies by decoupling the usage of an object from its creation
Move the creation and binding of the dependent objects outside of the class that depends on them

allows a service to be used/injected in a way that is completely independent of any client consumption. ... Dependency injection separates the creation of a client's dependencies from the client's behavior, which allows program designs to be loosely coupled

* When: if tight coupling of object implementations

* Benefits
Injections reduce the amount you have to code (and hence, debug), facilitating the creation of better apps and a smoother development process

Helps class decoupling. 
make simple to manage dependencies between objects that makes it easier to break coherent functionality off into its own contract. Code become more modularized. 
Increases reusability of the code and improves code maintainability and testing.

* Downsides 
increases code complexity, usually by increasing the number of classes, which is not always beneficial. Generally, the benefit of decoupling makes each task simpler to read and understand, but increases the complexity of orchestrating the more complex tasks.
a higher learning curve. To understand how a project uses dependency injection, a developer needs to understand both the dependency injection pattern and the specific framework.

* Types of dependency injection

### constructor injection
https://dotnettutorials.net/lesson/dependency-injection-design-pattern-csharp/

### method injection
### property/setter injection
https://dotnettutorials.net/lesson/setter-dependency-injection-design-pattern-csharp/

### Interface-based injection

## IOC - Inversion of control 

Normal control sequence would be the object finds the objects it depends on by itself and then calls them.
Implementations are passed into an object through constructors/setters/service lookups

Program delegates control to someone else who will drive the flow IOC (Inversion of control) is a general parent term while DI (Dependency injection) is a subset of IOC
 
## C# Dependency Injection containers

In the past, we were using libraries and frameworks (Autofac,Unity...) to implement Dependency Injection in our projects but Dependency injection is now part of .NET Core.
.NET Core comes with a built-in IoC Container that simplifies Dependency Injection management.

#### Spring.NET
Spring.NET is one of the popular open source frameworks for Dependency Injection. Spring.NET supports .NET 4.0, .NET Client Profile 3.5 and 4.0, Silverlight 4.0 and 5.0, and Windows Phone 7.0 and 7.1
#### Castle Windsor
http://www.castleproject.org/projects/windsor/
Castle Windsor is a mature Inversion of Control Container available for .NET and Silverlight. The current version is 4.0, released in July 2017. Castle Windsor could be downloaded from GitHub or NuGet. The advantages of using Castle Windsor is that it is completem it understands decorators, and its very well documented.
#### Unity
http://unitycontainer.org/articles/introduction.html
The Unity Application Block (Unity) is a lightweight, extensible dependency injection container which is relatively more complicated and obtrusive code. Unity uses a container and XML data. It has strong XML support and works with WPF applications. It's free under the Microsoft public license. Unity addresses the issues faced by developers engaged in component-based software engineering. Unity also includes the Interception container extension, which allows developers to inject exception management, logging, or even your own custom code between the caller and the called.
#### Structure Map
StructureMap is a Dependency Injection tool for .NET that can be used to improve the architectural qualities of an object-oriented system by reducing the mechanical costs of good design techniques. It's released under the permissive Apache 2 OSS license. It's free, and a developer can download, modify, or redistribute StructureMap.
#### Autofac
https://autofac.org/
https://autofaccn.readthedocs.io/en/latest/
Autofac is an Inversion of Control (IOC) container for Microsoft .NET C#, versions 3.0 and above. Licensed under MIT, it manages the dependencies among classes so that applications stay easy to change as they grow in size and complexity.
#### Ninject
An open source, ultra-lightweight, and universal dependency injection framework for .NET, Mono, .NET Compact Framework, and Silverlight. It is licensed under Apache 2. Ninject helps you use the technique of dependency injection to break your applications into loosely coupled, highly-cohesive components, and then glue them back together in a flexible manner.

## .Net core Dependency Injection

.NET Core comes with a built-in IoC Container that simplifies Dependency Injection management.

All Framework services (Configuration, Logging, Routing...) are now registered in a built-in DI Container and provided to us as services wherever we need them. 
1. Register all services (dependencies) when the application starts 
2. These services will be injected and resolved at runtime

***Microsoft.Extensions.DependencyInjection.Abstractions NuGet package***
|___IServiceCollection 
 |___ exposes a System.IService­Provider
    |____ GetService<TService>
    TService type parameter identifies the type of the service to retrieve (generally an interface)
    So application code obtains an instance: ILoggingFactory loggingFactory = serviceProvider.GetService<ILoggingFactory>();

To obtain an instance of the service provider on which to invoke GetService:
1. Instantiate ServiceCollection’s default constructor
2. Register the type you want the service to provide


***IServiceCollection***
Standard way to use Dependency Injection in .NET Core applications
Interface used to register all the services to resolve and inject later in our application
Startup.ConfigureServices() gives access to the instance of IServiceCollection as a parameter
https://docs.microsoft.com/fr-fr/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection

***IServiceProvider***
This interface is used to resolve service instances by actually looking up what interface belongs to what concrete implementation and carry out the creation.

## Console DI

https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-usage

Registering and Requesting an Object from Dependency Injection
```cs
public class Host
{
    public static void Main()
    {
        IServiceCollection serviceCollection = new ServiceCollection();
 
        ConfigureServices(serviceCollection);
        Application application = new Application(serviceCollection);
 
        // Run
        // ...
    }
 
    static private void ConfigureServices(IServiceCollection serviceCollection)
    {
        ILoggerFactory loggerFactory = new Logging.LoggerFactory(); 
        serviceCollection.AddInstance<ILoggerFactory>(loggerFactory);
    }
}
 
public class Application
{
    public IServiceProvider Services { get; set; }
    public ILogger Logger { get; set; }
 
    public Application(IServiceCollection serviceCollection)
    {
        ConfigureServices(serviceCollection);
        Services = serviceCollection.BuildServiceProvider();
        Logger = Services.GetRequiredService<ILoggerFactory>()
                .CreateLogger<Application>();
        Logger.LogInformation("Application created successfully.");
 
    }
         
    public void MakePayment(PaymentDetails paymentDetails)
    {
        Logger.LogInformation(
            $"Begin making a payment { paymentDetails }");
        IPaymentService paymentService = 
            Services.GetRequiredService<IPaymentService>();
 
        // ...
    }
 
    private void ConfigureServices(IServiceCollection serviceCollection)
    {
        serviceCollection.AddSingleton<IPaymentService, PaymentService>();
    }
}
public class PaymentService: IPaymentService
{
    public ILogger Logger { get; }
 
    public PaymentService(ILoggerFactory loggerFactory)
    {
 
        Logger = loggerFactory?.CreateLogger<PaymentService>();
        if(Logger == null)
        {
            throw new ArgumentNullException(nameof(loggerFactory));
        }
         
        Logger.LogInformation("PaymentService created");
    }
}
```

## AspNetCore DI
```cs
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    { 
        services.AddTransient<IProductService, ProductService>();
        services.AddScoped<ILoggingService, LoggingService>();
        services.AddSingleton<ICacheProvider, CacheProvider>();
    }
}
```

### .NET Core Service Lifetimes
https://docs.microsoft.com/fr-fr/dotnet/api/microsoft.extensions.dependencyinjection.servicelifetime

How long the service will live before it’s being garbage collected

***Singleton***
**A single instance of the service class is created**, stored in memory and shared (reused)
- For services that are expensive to instantiate
- To share state across multiple components
- Consider instance concurrency and thread-safety: instance is created just once and accessed by many consumers

>services.AddSingleton<IProductService, ProductService>(); // register Singleton service

***Scoped***
An **instance of the service class is created once per request**
- Request is the scope
- All middlewares, MVC controllers, etc. that participate in the handling of a single request will get the same instance. A good candidate for a scoped service is an Entity Framework context. 

>services.AddScoped<IProductService, ProductService>(); // register Scoped service

***Transient***
An **instance of the service class is created each time they’re requested** (even in the same request)
- For lightweight, stateless services
- Default choice when you don’t know which lifetime to use because each consumer will get its copy of the service and thread-safety will not be an issue. 

>services.AddTransient<IProductService, ProductService>(); // register Transient service

## .NET Core Dependency Injection Example


## Service Locator design pattern 
Allows decoupling clients of services (described by a public interface) from the concrete class implementing those services. 

The Service Locator is a pattern by which we can reduce the dependency of one object on another that we will see shortly and Dependency injection (DI) is another smart solution for the same problem.


* STRONGLY TYPED SERVICE LOCATOR
ServiceLocator will return a known type

```cs
using System;  
using System.Collections.Generic;  
using System.Linq;  
namespace Client  
{  
    public interface IService  
    {  
        void ExecuteService();  
    }  
    public class LoggingService : IService  
    {  
        public void ExecuteService()  
        {  
            Console.WriteLine("Executing Log Service");  
        }  
    }  
  
    public static class ServiceLocator  
    {  
        public static IService ObjService = null;  
          
        //Service locator function returning strong type   
        public static IService SetLocation(IService tmpser)  
        {  
            if (ObjService == null) return new LoggingService();  
            return ObjService;  
        }  
          
        //Execute service  
        public static void ExecuteService()  
        {  
            ObjService.ExecuteService();  
        }  
    }  
  
    class Program  
    {  
        static void Main(string[] args)  
         {  
           IService svr =  ServiceLocator.SetLocation(new LoggingService());  
           svr.ExecuteService();  
           Console.ReadLine();  
        }  
    }  
} 
```


* GENERIC TYPE SERVICE LOCATOR
Can deal with various types since this is generic in nature

```c#
using System;  
using System.Collections.Generic;  
using System.Text;  
namespace Client  
{  
    public interface IServiceA  
    {  
        void Execute();  
    }  
  
    public class ServiceA : IServiceA  
    {  
        public void Execute()  
        {  
            Console.WriteLine("A service called.");  
        }  
    }  
  
    public interface IServiceB  
    {  
        void Execute();  
    }  
  
    public class ServiceB : IServiceB  
    {  
        public void Execute()  
        {  
            Console.WriteLine("B service called.");  
        }  
    }  
  
    public interface IService  
    {  
        T GetService<T>();  
    }  
    public class ServiceLocator : IService  
    {  
        public Dictionary<object, object> servicecontainer = null;  
        public ServiceLocator()  
        {  
            servicecontainer = new Dictionary<object, object>();  
            servicecontainer.Add(typeof(IServiceA), new ServiceA());  
            servicecontainer.Add(typeof(IServiceB), new ServiceB());  
        }  
        public T GetService<T>()  
        {  
            try  
            {  
                return (T)servicecontainer[typeof(T)];  
            }  
            catch (Exception ex)  
            {  
                throw new NotImplementedException("Service not available.");  
            }  
        }  
    }  
    class Program  
    {  
        static void Main(string[] args)  
         {  
            ServiceLocator loc = new ServiceLocator();  
            IServiceA Aservice =  loc.GetService<IServiceA>();  
            Aservice.Execute();  
  
            IServiceB Bservice = loc.GetService<IServiceB>();  
            Bservice.Execute();  
  
           Console.ReadLine();  
         }  
    }  
} 
```

## More

- https://intellitect.com/net-core-dependency-injection/ ****
- https://github.com/unitycontainer
- https://auth0.com/blog/dependency-injection-in-dotnet-core/ **
- https://www.ezzylearning.net/tutorial/a-step-by-step-guide-to-asp-net-core-dependency-injection
- https://pradeeploganathan.com/dotnet/dependency-injection-in-net-core-console-application/
- https://docs.microsoft.com/en-us/archive/msdn-magazine/2016/june/essential-net-dependency-injection-with-net-core