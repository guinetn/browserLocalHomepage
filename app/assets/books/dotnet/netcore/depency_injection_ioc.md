# DEPENCY INJECTION - IOC Inversion  Of Control

A software design rule: ***loosely coupled objects*** = greater reusability, maintainability, testability
The 'D' pillar in SOLID principles, which is "Dependency Inversion Principle":
- High-level modules should not depend on low-level modules. Both should depend on abstractions
- Abstractions should not depend on details. Details should depend on abstractions

- Reduces the coupling between classes
- Moves the binding of abstraction and concrete implementation out of the dependent class
- DI pattern uses a builder object to initialize objects and provide the required dependencies to the object, meaning that it allows developers to "inject" a dependency from outside the class. 
- There are four ways of achieving the Dependency Injection.

* Remove the dependency between two objects
* Style of wiring objects together
* DI containers improve the composition of whole object graphs
* Ideal for mocking: common need for dependency injection is in unit tests 

![](assets/books/dotnet/assets/di/di.jpg)

![](assets/books/dotnet/assets/di/di-host.png)
Strongly Coupling the Client to the Logging Service Implementation

![](assets/books/dotnet/assets/di/di-host-2.png)
Decoupling the Client/Library from the Specific Logging Implementation via Dependency Injection

![](assets/books/dotnet/assets/di/di-sequence-diagram.png)
![](assets/books/dotnet/assets/di/di-unit-testing.png)

![](assets/books/dotnet/assets/di/di-unit-tests-host.png)
Unit Testing with Dependency Injection so a Mock Type Instance Can Be Used
 
## What is dependency? 

There is a dependency when HighLevelModule depends directly on LowLevelModule and this does not follow the "D" of SOLID, this creates a direct and tightly coupled relationship between the two. 

Inheritance creates a strongly coupled link:
```cs
public class Address { }                // The low-level module
public class Customer: Address {}       // The high-level module
```

Object composition, using instance variables that are references to other objects,
denotes an ownership "is-a-part-of" relationship between objects → strongly coupled
```cs
public class Address { }
public class Customer
{
    Address address;
    public Customer() { address = new Address(); }
}
```

Objects aggregation is a bit less coupled and gives us a clue to be less coupled
```cs
public class Customer
{
    Address address;
    public Customer(Address c) { this.address = c; }
}
```
### How to remove dependency between two classes?

"Dependency Inversion Principle":
- High-level modules should not depend on low-level modules. Both should depend on abstractions
- ***Abstractions*** should not depend on details. Details should depend on abstractions

***Define an interface (=contract,abstraction) and share it*** with any object dependant of it

Define a contract for Address and share this contract to 
- both Address and Customer classes
- and any other class which are dependent on Address.

App now depend on the abstraction of Address rather than on concrete class Address

```cs
public interface IAddress { }

// Share the contract
public class Address : IAddress { }  // LowLevelModule needs to be abstracted. Done with IAddress

public class Customer                // HighLevelModule will depends on the abstraction of LowLevelModule
{
    IAddress address;               // reference to IAddress interface not concrete class Address
    public Customer()
    {
        address = new Address();   // Problem: still depends on Address in it's constructor as it is instantiated in the constructor
    }
}
```

* What is the solution?

***Move the instantiation of class Address to some other class which will take care of creating the instance***. This way there is no dependency between Customer and Address. 
***This process of moving LowLevelModule (IAddress) instantiation from inside to outside of the class is called inversion***.

HighLevelModule will solely depend on IAddress abstraction so we can't have any ` new LowLevelModule() ` inside the HighLevelModule class. LowLevelModule has to be ` injected ` into HighLevelModule class from the caller context. 

Using DI, we are inverting the control of object creation from a dependent object to an injector/caller which will take care of creating the instance.

```cs
public interface IAddress { }

// Share the contract
public class Address : IAddress { }

public class Customer
{
    IAddress address;               // reference to IAddress interface not concrete class Address
    public Customer(IAddress address)
    {
        this.address = address;
    }
}
```

In this program there is no dependency between Class Customer and Address: Instance of Address is created somewhere in main program and passed to the constructor as a parameter. This is called "constructor injection". There is another way called property injection or method injection.

This can be better handled using dependency injection.

## Dependency injection - DI

DI allow to substitute different concrete class implementations at runtime. This allow testing easier

* The DI 3 elements
- Contract: IAddress
- Consumer (class Customer here) that declares its dependencies (Address) as contracts 
- Injector, which creates instances of concrete classes. There are lots of injectors available in the market like NInject, Microsoft unity, DoNetCore built-in…

You can also use other design patterns to reduce the dependency between components
- Factory
- Publisher/Subscriber

## Abstraction Methods

1. Using an Interface: provide an abstraction
2. Using an Abstract Class: provide some shared implementation details between two or more classes
3. Using a Delegate: provides an abstraction for one particular method or function

***Interface***
```cs
public interface IAction
{
  void Play();
}

public class LowLevelModule: IAction
{
  public LowLevelModule() { } 
  public void Play() {  }
}

public class HighLevelModule
{
  private readonly IAction _action;
  public HighLevelModule(IAction action)
  {
    _action = action;
  }

  public void Run()
  {
    _action.Play();
  }
}
```

***Abstract class***
Change the interface into an abstract class
Use abstract classes if there is a shared implementation detail. For example when HighLevelModule can use either LowLevelModule or AnotherLowLevelModule and these both classes share implementation detail then use an abstract class as a base class for both. 
```cs
public abstract class ActionBase
{
  public abstract void Play();
}

public class LowLevelModule: ActionBase
{
  protected LowLevelModule() { }  
  public override void Play() { }
}

public class HighLevelModule
{
  private readonly ActionBase _action;
  public HighLevelModule(ActionBase action)
  {
    _action = action;
  }

  public void Run()
  {
    _action.Play();
  }
}
```

***Delegate***
You can abstract a method or a function using a delegate
Generic delegates: Func<T>, Action<T>
Not Generic delegates: Action

With generic delegates there is no need to create a type (interface or class) for the dependencies
Simply use any methods or functions from the caller context or from anywhere else

```cs
public class Caller
{ 
  public void CallerMethod()
  {
    var module = new HighLevelModule(PlaySong);
    …    
  }

  // Method injected into HighLevelModule
  public void PlaySong() { }
}

public class HighLevelModule
{
  private readonly Action _action;
  public HighLevelModule(Action action)
  {
    _action = action;
  }

  public void Run()
  {
    _action();
  }
}
```

Using your own delegate:
```cs
public delegate void MyOperation();

public class Caller
{ 
  public void CallerMethod()
  {
    var module = new HighLevelModule(PlaySong);
    …
  }

  // Method injected into HighLevelModule
  public void PlaySong() { }
}

public class HighLevelModule
{
  private readonly MyOperation _action;
  public HighLevelModule(MyOperation action)
  {
    _action = action;
  }

  public void Run()
  {
    _action();
  }
}
```

## Dependency Inversion Methods

### 1. Using Dependency Injection

Dependency is injected to a class via its public members: 

- Contructor Injection: Dependency is injected into the class's constructor

```cs
public interface IAddress { }

// Share the contract
public class Address : IAddress { }

public class Customer
{
    IAddress address;               // reference to IAddress interface not concrete class Address
    public Customer(IAddress address)
    {
        this.address = address;
    }
}
```

- Method Injection: Dependency is injected into a method

```cs
public class Customer
{
    private readonly IOperation _operationOne;
    private readonly IOperation _operationTwo;    
    public Customer(IOperation operationOne, IOperation _operationTwo) { 
       _operationOne = operationOne;
       _operationTwo = operationTwo;        
    }
    public void Run()
    {
        _operationOne.Play();
        _operationTwo.Play();
    }
}
```

- Setter Injection: Dependency is injected into a set property

```cs
public interface IAddress { }
public class Customer
{
    IAddress address  { get; set; }; 
    public Customer() { }
    public void Run() { address.GetCity(); }
}
```

- Events Injection

Only for delegate type injection in a subscription/notificatin model
The caller will subscribe a delegate to the class that implements the event, and there can be multiple subscribers. Injecting events via constructor not common. 
The delegate must return void

```cs
public class Caller
{ 
  public void CallerMethod()
  {
    var module = new HighLevelModule();
    module.SendEvent += ShowMessage; // event injection can be performed after the object construction
    …
  }

  // Method injected into HighLevelModule
  public void ShowMessage() { }
}

public class HighLevelModule
{
  public event Action SendEvent = delegate {};

  public void Call()
  {
    SendEvent();
  }
}
```

- index properties, fields... any public member

### 2. Using Global States

Dependency is not injected but retrieved from a global state from inside the class
The dependency itself can be injected into the global states and later accessed from inside the class
Global states to invert dependencies is not recommended, as it makes dependencies less obvious, and hides them inside the class.

```cs
public class Helper
{
    // Global states can be properties, methods, fields. Underlying value has public setter and getter
    // Setter and getter can be in the form of methods instead of properties
    public static IOperation GlobalStateOperation { get; set;}
}

public class HighLevelModule
{
    public void Call()
    {
        Helper.GlobalStateOperation.Send();
    }
}

public class Caller
{
    public void CallerMethod()
    {
        Helper.GlobalStateOperation = new LowLevelModule();

        var highLevelModule = new HighLevelModule();
        highLevelModule.Call();
    }
}
```
### 3. Using Indirection

Dependency is not injected but you pass an object that is capable of creating the implementation of the abstraction for you. This means you create another dependency for the class.

Use indirection sparingly. Service Locator Pattern, is seen as anti-pattern nowadays. However from time to time, you may need to use a factory object to create the dependencies. Try to stay clear from using Indirection, unless it is proven necessary.

The type of object you pass into the class can be:

- Registry/Container object

Using a register/container, you need to register the implementation class before you can query it

If you use a register (Service Locator Pattern) then you can query the register to return an implementation of an abstraction. Register the implementation first from outside the class

IoC container frameworks use a container to wrap up the registry. Register all the dependencies first.

In the early days IoC container frameworks was often implemented as a Global state or Singleton instead of explicitly passing it into a class, and this was now considered as anti-pattern

Using a container

```cs
public interface IOperation
{
  void Play();
}

public class LowLevelModule: IOperation
{
  public LowLevelModule() { }
  public void Play() { }
}

public class HighLevelModule
{
  private readonly Container _container;

  public HighLevelModule(Container container)
  {
    _container = container;
  }

  public void Call()
  {
    IOperation operation = _container.Resolvel<IOperation>();
    operation.Play();
  }
}

public class Caller
{
  public void UsingContainerObject()
  {
     //registry the LowLevelModule as implementation of IOperation
     var register  = new Registry();
     registry.For<IOperation>.Use<LowLevelModule>();

     //wrap-up registry in a container
     var container = new Container(registry);
      
     //inject the container into HighLevelModule
     var highLevelModule = new HighLevelModule(container);
     highLevelModule.Call();     
  }
}
```

- Factory object

 A normal class that returns an abstraction (interface)
 Instantiations are hardcoded in the factory implementation
  
```cs
public interface IOperation
{
  void Play();
}

public class LowLevelModule: IOperation
{
  public LowLevelModule() { }  
  public void Play() { }
}

public interface IModuleFactory
{
   IOperation CreateModule();
}

// Factory object needs to implement the abstraction
public class ModuleFactory: IModuleFactory
{
  public IOperation CreateModule()
  {
      //LowLevelModule is the implementation of the IOperation and it is hardcoded in the factory. 
      return new LowLevelModule();
  }
}

// HighLevelModule needs to depend on the factory abstraction
public class HighLevelModule
{
  private readonly IModuleFactory _moduleFactory;

  public HighLevelModule(IModuleFactory moduleFactory)
  {
    _moduleFactory = moduleFactory;
  }

  public void Run()
  {
    IOperation operation = _moduleFactory.CreateModule();
    operation.Play();
  }
}

public class Caller
{
  public void CallerMethod()
  {
     //create the factory as the implementation of abstract factory
     IModuleFactory moduleFactory = new ModuleFactory();
      
     //inject the factory into HighLevelModule
     var highLevelModule = new HighLevelModule(moduleFactory);   
     highLevelModule.Run();  
  }
}
```

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

https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-usage

```cs

namespace ConsoleDI.Example
{
    public interface ITransientOperation : IOperation { }
    public interface IScopedOperation  : IOperation { }
    public interface ISingletonOperation  : IOperation { }
}


using static System.Guid;
namespace ConsoleDI.Example
{
    public class DefaultOperation : ITransientOperation, IScopedOperation, ISingletonOperation
    {
        public string OperationId { get; } = NewGuid().ToString()[^4..];
    }
}


using System;

namespace ConsoleDI.Example
{
    public class OperationLogger
    {
        private readonly ITransientOperation _transientOperation;
        private readonly IScopedOperation _scopedOperation;
        private readonly ISingletonOperation _singletonOperation;

        public OperationLogger(
            ITransientOperation transientOperation,
            IScopedOperation scopedOperation,
            ISingletonOperation singletonOperation) =>
            (_transientOperation, _scopedOperation, _singletonOperation) =
                (transientOperation, scopedOperation, singletonOperation);

        public void LogOperations(string scope)
        {
            LogOperation(_transientOperation, scope, "Always different");
            LogOperation(_scopedOperation, scope, "Changes only with scope");
            LogOperation(_singletonOperation, scope, "Always the same");
        }            

        private static void LogOperation<T>(T operation, string scope, string message)
            where T : IOperation =>
            Console.WriteLine(
                $"{scope}: {typeof(T).Name,-19} [ {operation.OperationId}...{message,-23} ]");
    }
}

using System;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace ConsoleDI.Example
{
    class Program
    {
        static Task Main(string[] args)
        {
            using IHost host = CreateHostBuilder(args).Build();

            ExemplifyScoping(host.Services, "Scope 1");
            ExemplifyScoping(host.Services, "Scope 2");

            return host.RunAsync();
        }

        static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((_, services) =>
                    services.AddTransient<ITransientOperation, DefaultOperation>()
                            .AddScoped<IScopedOperation, DefaultOperation>()
                            .AddSingleton<ISingletonOperation, DefaultOperation>()
                            .AddTransient<OperationLogger>());

        static void ExemplifyScoping(IServiceProvider services, string scope)
        {
            using IServiceScope serviceScope = services.CreateScope();
            IServiceProvider provider = serviceScope.ServiceProvider;

            OperationLogger logger = provider.GetRequiredService<OperationLogger>();
            logger.LogOperations($"{scope}-Call 1 .GetRequiredService<OperationLogger>()");

            Console.WriteLine("...");

            logger = provider.GetRequiredService<OperationLogger>();
            logger.LogOperations($"{scope}-Call 2 .GetRequiredService<OperationLogger>()");

            Console.WriteLine();
        }
    }
}
```

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
- https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-usage *