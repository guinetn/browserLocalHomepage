
## Delegates
A type (delegate name = delegate type) that encapsulate (wrap) a method 
Call him = call a function(s) that can be different
~ function pointer in C/C++ 
Object-oriented, type safe, secure 
 
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


## Methods

https://docs.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/calling-synchronous-methods-asynchronously

## Lambdas

```cs
List<int> elements = new List<int>() { 10, 20, 31, 40 };
int firstOddIndex = elements.FindIndex(x => x % 2 != 0);
Console.WriteLine(firstOddIndex);

elements.Where(v => (int)v > 11).ToArray()
```