
## Delegates
A type (delegate name = delegate type) that encapsulate (wrap) a method 
Call him = call a function(s) that can be different
~ function pointer in C/C++ 
Object-oriented, type safe, secure 
 
```cs
public delegate string show(string s, int i);

public delegate double dg(double db);
dg dlg1 = new dg(System.Math.Cos);
double res = dlg1(2.3); // -0.666
dg dlg2 = new dg(System.Math.Sin);
double res2 = dlg2(2.3); // 0.745
```

A delegate is an instance of a delegate type that has references to:
- An instance method of a type and a target object assignable to that type.
    Stores a reference to the method's entry point 
    Stores a reference to an object (target) of type assignable to the type that defined the method
- An instance method of a type, with the hidden this parameter exposed in the formal parameter list (open instance delegate)
    Stores a reference to the method's entry point
    Delegate parameters signature include the hidden 'this' 
    Delegate doesn't have a reference to a target object that must be supplied at delegate invokation
- A static method
    Stores a reference to the method's entry point
- A static method and a target object assignable to the first parameter of the method (closed over its first argument)
    Stores a reference to the method's entry point
    Stores a reference to a target object assignable to the type of the method's first argument. When the delegate is invoked, the first argument of the static method receives the target object.

When a delegate is constructed to wrap an instance method
    the delegate references both the instance and the method. A delegate has no knowledge of the instance type aside from the method it wraps, so a delegate can refer to any type of object as long as there is a method on that object that matches the delegate signature
When a delegate is constructed to wrap a static method
    it only references the method

Derived from 'Delegate' class:
Represents a delegate, which is a data structure that refers to a static method or to a class instance and an instance method of that class.

CLR provides each delegate type with BeginInvoke() and EndInvoke() to enable asynchronous invocation of the delegate


```cs
// 1. DELEGATE TYPE DECLARATION
// Contract that specifies the signature of one or more methods
// A delegate named Del that can encapsulate a method having a string argument and returning void:
public delegate void Del(string message);

// 2. DELEGATE INSTANTIATION 
// * the name of the method the delegate will wrap
// * an anonymous function
public static void DelegateMethod(string message)
{
    Console.WriteLine(message);
}
Del handler = DelegateMethod;

// 3. DELEGATE INVOKATION
handler("Hello World");


public static void MethodWithCallback(int param1, int param2, Del callback)
{
    callback("The number is: " + (param1 + param2).ToString());
}
MethodWithCallback(1, 2, handler);
```

```cs

public delegate String methodDelegate( int myInt );

// Defines some methods to which the delegate can point.
public class class1  {
    // Defines an instance method.
    public String myStringMethod ( int myInt )  { }
    // Defines a static method.
    public static String mySignMethod ( int myInt )  {}
}

mySampleClass c = new class1();
var myD1 = new methodDelegate( c.myStringMethod );
var myD2 = new methodDelegate( class1.mySignMethod );
```
## MulticastDelegate
A delegate with more than one element in its invocation list (a linked list of delegates)

All delegates are MulticastDelegates but for efficiency reasons an invocation list is only created if there is more than one method encapsulated. That is, a delegate that encapsulates a single method stores this method in its Method and Target properties and has a null invocation list.

+= operator    to add a method to the invocation list 
-= operator    to remove methods from the invocation list 
 
greetType DelA = hello;
greetType DelB = goodbye;
greetType DelC;
DelC = DelA + DelB; DelC encapsulates the methods of DelA and DelB.
DelC = DelC - DelA; removes one delegate’s invocation list from another 

Two MulticastDelegates are considered equal if their invocation lists are identical and in the same order.
 
Some static methods defined on the Delegate class such as Combine and Remove which can be used to manipulate arrays of Delegates as well as pairs of Delegates.
 
Delegate[] InvList = DoGreet.GetInvocationList();
foreach (Delegate d in InvList)
    d.DynamicInvoke("Loop");
DynamicInvoke rather than Invoke: reason is that neither Delegate nor MulticastDelegate support an Invoke method. When you use the classes directly in this way the invocation of the method cannot be checked at compile time, hence the need for a “DynamicInvoke”.

var obj = new MethodClass();
Del d1 = obj.Method1;
Del d2 = obj.Method2;
Del d3 = DelegateMethod;

//Both types of assignment are valid.
Del allMethodsDelegate = d1 + d2;
allMethodsDelegate += d3;

All three methods are called in order
If the delegate uses reference parameters, the reference is passed sequentially to each of the three methods in turn, and any changes by one method are visible to the next method.

//remove Method1
allMethodsDelegate -= d1;

// copy AllMethodsDelegate while removing d2
Del oneMethodDelegate = allMethodsDelegate - d2;

// Number of methods in a delegate's invocation list:
int invocationCount = d1.GetInvocationList().GetLength(0);




public int hello(string param)
{
 MessageBox.Show("Hello "+param);
 return 1;
}

public int goodbye(string param)
{
 MessageBox.Show("Goodbye " + param);
 return 2;
}

A suitable delegate type is just: delegate int greetType(string param);
Create an instance of MulticastDelegate encapsulating two methods:
greetType DoGreet = hello;
DoGreet += goodbye;
DoGreet += delegate(string param)
{
 MessageBox.Show("Goodbye " + param);
 return 2;
};

Or, more properly if you agree that lambda expressions should be used in preference to  anonymous methods:
DoGreet += (string param)=>
{
 MessageBox.Show("Goodbye " + param);
 return 2;
};
## Asynchronous delegates

Don’t confuse asynchronous delegates with asynchronous methods (starts with Begin or End, such as File.BeginRead/File.EndRead)

Asynchronous delegates 
* let you return data from the thread
* allow any number of typed arguments to be passed in both directions.
* marshal any exception back to the caller. Rethrown on the original thread (or more accurately, the thread that calls EndInvoke)

EndInvoke()
1. Waits for the asynchronous delegate to finish executing if it hasn’t already. 
2. Receives the return value (as well as any ref or out parameters)
3. Throws any unhandled worker exception back to the calling thread

```c#
static void Main()
{
  Func<string, int> method = Work;
  method.BeginInvoke("test", Done, method);
  // ...
  //
}
 
static int Work (string s) { return s.Length; }
 
static void Done (IAsyncResult cookie)
{
  var target = (Func<string, int>) cookie.AsyncState;
  int result = target.EndInvoke(cookie);
  Console.WriteLine ("String length is: " + result);
}
```


## Methods (functions in classes)

https://docs.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/calling-synchronous-methods-asynchronously

### Dynamic method invocation
call a method on some instance

```cs 
public class Foo
{
    public int Bar(int a, int b, bool c) => a + (c ? b : 0);
}
``` 

1. Direct method invocation

``` cs
object fooInstance = new Foo();
fooInstance.Bar(1,2,false);
``` 

2. MethodInfo.Invoke
``` cs
object fooInstance = new Foo();
MethodInfo barMethod = ClassType.GetMethod(nameof(Foo.Bar));
barMethod.Invoke(fooInstance, new[] { (object)1, (object)2, (object)false });
``` 

3. Delegate.DynamicInvoke
``` cs
object fooInstance = new Foo();
MethodInfo barMethod = ClassType.GetMethod(nameof(Foo.Bar));
// wrap MethodInfo in a delegate
var delegateType = Expression.GetDelegateType(typeof(Foo), typeof(int), typeof(int), typeof(bool), typeof(int));
var @delegate = Delegate.CreateDelegate(delegateType, barMethod);
@delegate.DynamicInvoke(new[] { fooInstance, (object)1, (object)2, (object)false });
``` 

4. Func<> invocation
``` cs
object fooInstance = new Foo();

MethodInfo barMethod = ClassType.GetMethod(nameof(Foo.Bar));
var delegateType = Expression.GetDelegateType(typeof(Foo), typeof(int), typeof(int), typeof(bool), typeof(int));
// cast the Delegate to a Func<>
var func = (Func<Foo, int, int, bool, int>)Delegate.CreateDelegate(delegateType, barMethod);
func(fooInstance as Foo, 1, 2, false);
``` 

5. Dynamic cast
``` cs
object fooInstance = new Foo();

dynamic dynamicFoo = fooInstance as dynamic;
dynamicFoo.Bar(1, 2, false);
``` 

download.code(dotnet/types/ref/delegate_standards.md)

download.code(dotnet/types/ref/expression_lambdas.md)

download.code(dotnet/types/ref/closures.md)

## More

- https://www.davideguida.com/dynamic-method-invocation-with-net-core/
- https://www.i-programmer.info/programming/c/870-multicast-delegates-and-events.html