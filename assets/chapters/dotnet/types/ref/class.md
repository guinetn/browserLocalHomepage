## Classes

Inherit from a not sealed base class
Other classes can inherit from your class and override class virtual methods
Can implement one or more interfaces.

![](assets/chapters/dotnet/types/ref/class.png)
### abstract class
Has abstract methods: signature definition but no implementation
Abstract classes cannot be instantiated
They can only be used through derived classes that implement the abstract methods.
Class definitions can be split between different source files with 'partial'

### Finalizers / destructors

Perform any necessary final clean-up when a class instance is being collected by the garbage collector.
* Finalizers cannot be defined in structs. They are only used with classes.
* A class can only have one finalizer.
* Finalizers cannot be inherited or overloaded.
* Finalizers cannot be invoked explicitly. They are invoked automatically.
* A finalizer does not take modifiers or have parameters.
* Empty finalizers should not be used (performance) 

An instance becomes eligible for destruction when it is no longer possible for any code to use the instance.
Execution of the destructor for the instance may occur at any time after the instance becomes eligible for destruction.
When an instance is destructed, the destructors in its inheritance chain are called, in order, from most derived to least derived. 

It implicitly calls Finalize() on the base class of the object. 
Finalize is called recursively for all instances in the inheritance chain, from the most-derived to the least-derived.
The programmer has no control over when the finalizer is called; the garbage collector decides when to call it. Finalizers are also called when the program exits. 
Forcing garbage collection with Collect() should be avoided for performance issues.

```cs
public class Destroyer
{
   public override string ToString() => GetType().Name;

   ~Destroyer() => Console.WriteLine($"The {ToString()} destructor is executing.");
}

protected override void Finalize()  
{  
    try  
    {  
        // Cleanup statements...  
    }  
    finally  
    {  
        base.Finalize();  
    }  
}  
```
#### IDisposable
To release unmanaged resources. The garbage collector automatically releases the memory allocated to a managed object when that object is no longer used. However, it is not possible to predict when garbage collection will occur. Furthermore, the garbage collector has no knowledge of unmanaged resources such as window handles, or open files and streams.

You can release your resources before the garbage collector frees the object
Even with this explicit control over resources, the finalizer becomes a safeguard to clean up resources if the call to the Dispose method fails.

Call Dispose() to explicitly release unmanaged resources in conjunction with the garbage collector.

```cs
class BaseClass : IDisposable
{
   // Flag: Has Dispose already been called?
   bool disposed = false;

   // Public implementation of Dispose pattern callable by consumers.
   public void Dispose()
   {
      Dispose(true);
      GC.SuppressFinalize(this);
   }

   // Protected implementation of Dispose pattern.
   protected virtual void Dispose(bool disposing)
   {
      if (disposed)
         return;

      if (disposing) {
         // Free any other managed objects here.
         //
      }

      // Free any unmanaged objects here.
      //
      disposed = true;
   }

   ~BaseClass()
   {
      Dispose(false);
   }
}
```

Subclasses should implement the disposable pattern as follows:
They must override Dispose(Boolean) and call the base class Dispose(Boolean) implementation.
They can provide a finalizer if needed. The finalizer must call Dispose(false).

### Polymorphism

When a derived class inherits from a base class, it gains all the methods, fields, properties, and events of the base class. 

Base classes can implement ***virtual*** methods that derived classes can ***override*** (their own implementation)
* Methods, properties, events, indexers can be virtual
* Fields cannot be virtual

A derived class can override a base class member only if the base class member is declared as virtual or abstract. Derived class has different choices for the behavior of virtual methods:

* Can inherit without overriding it: preserve existing behavior but enabling further derived classes to override the method.
* Can override virtual members in the base class, defining new behavior.
* Can define ***new*** non-virtual implementation of those members that ***hide*** the base class implementations`.

`When a derived class overrides a virtual member, that member is called even when an instance of that class is being accessed as an instance of the base class`
CLR looks the run-time type of the object and invokes that override of the virtual method

`Hidden BASE CLASS MEMBERS may be accessed from client code by casting the instance of the derived class to an instance of the base class`

```cs
public class BaseClass
{
    public virtual void DoWork() { }
    public virtual int WorkProperty { get { return 0; } }
}

public class DerivedClass : BaseClass
{
    public override void DoWork() { }
    public override int WorkProperty { get { return 0; } }
}

public class HideDerivedClass : BaseClass
{
    public new void DoWork() { }
    public new int WorkProperty { get { return 0; } }
}

DerivedClass B = new DerivedClass();
B.DoWork();  // Calls the new method

BaseClass A = (BaseClass)B;
A.DoWork();  // Also calls the new method

HideDerivedClass C = new HideDerivedClass();
C.DoWork();  // Calls the new method
BaseClass A2 = (BaseClass)C;
A2.DoWork();  // Calls the hidden old method
```

#### Stop virtual inheritance

Method DoWork is no longer virtual to any class derived from C. It's still virtual for instances of C, even if they're cast to type B or type A. Sealed methods can be replaced by derived classes by using the new keyword
 
```c#
public class A
{
    public virtual void DoWork() { }
}
public class B : A
{
    public override void DoWork() {
        // Access base class virtual members from derived classes
        base.DoWork();
     }
}
// Stop virtual inheritance
public class C : B
{
    public sealed override void DoWork() { }
}
public class D : C
{
    public new void DoWork() { }
}
```

## Shallow copy

## Deep copy (reference types inside)


public static Object CloneType(Object objtype)
{
    Object lstfinal = new Object();

    using (MemoryStream memStream = new MemoryStream())
    {
        BinaryFormatter binaryFormatter = new BinaryFormatter(null, new StreamingContext(StreamingContextStates.Clone));
        binaryFormatter.Serialize(memStream, objtype); memStream.Seek(0, SeekOrigin.Begin);
        lstfinal = binaryFormatter.Deserialize(memStream);
    }

    return lstfinal;
}

// Private members are not cloned using the JSON method
public static T DeepCopy<T>(this T value)
{
    string json = JsonConvert.SerializeObject(value);

    return JsonConvert.DeserializeObject<T>(json);
}

