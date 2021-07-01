# C#8 (.NET Core 3.0) #

supported only on frameworks implementing .NET Standard 2.1 (which the .NET Framework will never do)



Readonly members
Default interface methods
Pattern matching enhancements:
Switch expressions
Property patterns
Tuple patterns
Positional patterns
Using declarations
Static local functions
Disposable ref structs
Nullable reference types
Asynchronous streams
Indices and ranges
Null-coalescing assignment
Unmanaged constructed types
Stackalloc in nested expressions
Enhancement of interpolated verbatim strings








## Need Visual Studio 2019 

## CLOUD SCENARIOS
Async enumerables
More patterns in more places
Default interface members
Indices and Ranges

## Increase your productivity
Using statement
Static local functions
Readonly members
Null coalescing assignment
Unmanaged constraint
Interpolated verbatim strings



download.page(dotnet/types/ref/null.md)

download.page(dotnet/threading/b_async_3/iasyncenumerable.md)

download.page(dotnet/threading/b_async_3/async_streams.md)

download.page(dotnet/types/val/range.md)



## DEFAULT METHODS IMPLEMENTATIONS OF INTERFACE MEMBERS

< C# 8
Interface is used to 
    Define the contract to be implemented by the concrete class
    Create a loosely coupled component 
    No body, no modifiers

Once you publish an interface it’s game over: you can’t add members to it without breaking all the existing implementers of it.


C# 8.0 Fix: Default methods
Let you provide a body for an interface member. 
Thus, if somebody doesn’t implement that member (perhaps because it wasn’t there yet when they wrote the code), they will just get the default implementation instead.
Default methods will only work if the class is contextually treated as interfaces if we are not doing that then Default method implementation will not be available for the use
```c#
    interface ILogger
    {
        void Log(LogLevel level, string message);
        void Log(Exception ex) => Log(LogLevel.Error, ex.ToString()); // New overload
    }

    class ConsoleLogger : ILogger
    {
        public void Log(LogLevel level, string message) { ... }
        // Log(Exception) gets default implementation
    }
```

The ConsoleLogger class doesn’t have to implement the Log(Exception) overload of ILogger, because it is declared with a default implementation. Now you can add new members to existing public interfaces as long as you provide a default implementation for existing implementors to use.

Diamond Problem risk (Multiple Inheritance)
    interface first {…}
    interface second:first {…}
    interface third:second {…} ...
    A class implementation of an interface member should always win over a default implementation in an interface, even if it is inherited from a base class. Default implementations are always a fall back only for when the class does not have any implementation of the member at all.        
    Fix: modifiers like private, protected, internal , public and virtual are allowed, By design all the default interfaces methods are made virtual unless we are making them private or sealed, All the members without body are treated as abstract by default making it compulsory to be implemented in the concrete classes.

### When we run above code we can see the following output on the console:

    Abstract virtual method
    Default method
    public Default method
    Virtual Default method
    Apart from this few observations that I come across in this example.
    When we make a method virtual we can override that method in interface itself and we cannot override it in the implementation class.
    When we make one method protected it is available in the inheriting interface rather than implementing class by default the members of the interfaces are abstract which makes it compulsory for the implementing class to implement them properly.

## RECURSIVE PATTERNS
We’re allowing patterns to contain other patterns:
```c#
    IEnumerable<string> GetEnrollees()
    {
        foreach (var p in People)
        {
            // If p is a Student, has not graduated and has a non-null name, we yield return that name
            if (p is Student { Graduated: false, Name: string name }) yield return name;
        }
    }
```

The pattern Student { Graduated: false, Name: string name } checks that the Person is a Student, then applies the constant pattern false to their Graduated property to see if they’re still enrolled, and the pattern string name to their Name property to get their name (if non-null). 
If p is a Student, has not graduated and has a non-null name, we yield return that name.

## SWITCH EXPRESSIONS

"lightweight" version of Switch statements with patterns (C# 7)
```c#
    var area = figure switch 
    {
        Line _      => 0,
        Rectangle r => r.Width * r.Height,
        Circle c    => c.Radius * 2.0 * Math.PI,
        _           => throw new UnknownFigureException(figure)
    };

    static string Display(object o) => o switch
    {
        Point p when p.X == 0 && p.Y == 0 => "origin",
        Point p                           => $"({p.X}, {p.Y})",
        _                                 => "unknown"
    };
```

# TARGET-TYPED NEW-EXPRESSIONS

When you’re creating a new object, the type is often already given from context, so omit the type:

```c#
Point[] ps = { new (1, 4), new (3,-2), new (9, 5) }; // all Points
```

## PLATFORM DEPENDENCIES

Most of the C# 8.0 language features will run on any version of .NET. However, a few of them have platform dependencies.
indexers and ranges all rely on new framework types that will be part of .NET Standard 2.1. 

.NET Core 3.0 as well as Xamarin, Unity and Mono will all implement .NET Standard 2.1, but .NET Framework 4.8 will not. 
This means that the types required to use these features won’t be available when you target C# 8.0 to .NET Framework 4.8.

As always, the C# compiler is quite lenient about the types it depends on. If it can find types with the right names and shapes, it is happy to target them.

Default interface member implementations rely on new runtime enhancements, and we will not make those in the .NET Runtime 4.8 either. So this feature simply will not work on .NET Framework 4.8 and on older versions of .NET.

The need to keep the runtime stable has prevented us from implementing new language features in it for more than a decade. With the side-by-side and open-source nature of the modern runtimes, we feel that we can responsibly evolve them again, and do language design with that in mind. Scott explained in his Update on .NET Core 3.0 and .NET Framework 4.8 that .NET Framework is going to see less innovation in the future, instead focusing on stability and reliability. Given that, we think it is better for it to miss out on some language features than for nobody to get them.




- https://www.codeproject.com/Articles/1265802/New-Features-of-Csharp-8
- https://medium.com/codex/5-methods-that-drastically-shorten-drastically-your-code-in-c-8-0-e7bc1ca1b480