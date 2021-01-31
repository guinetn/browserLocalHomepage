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



## NULLABLE REFERENCE TYPES

    string s = null;
    WriteLine($"The first letter of {s} is {s[0]}"); // "null reference exception"

Nullable reference types feature intends to warn you about null-unsafe behavior in the code. 

    myproject.csproj
        <NullableReferenceTypes>true</NullableReferenceTypes>     turn them on

    mycode.cs
        string? s = null;
        WriteLine($"The first letter of {s} is {s[0]}");                        Warning
        if (s != null) WriteLine($"The first letter of {s} is {s[0]}");         Fix 1
        WriteLine($"The first letter of {s} is {s?[0] ?? '?'}");                Fix 2
                                                    ↓     ↓
                                                    ↓   Null-coalescing operator ??   '?' replaces a null value with the char '?'. Avoid null dereferences
                                                    ↓                                                 
                                            Null conditional indexing operator s?[0]
                                                * avoids the dereference 
                                                * produces a null if s is null (has nullable char?) 

## ASYNC STREAMS (for continuous streams)

The async/await feature of C# 5.0 lets you consume (and produce) asynchronous results in straightforward code, without callbacks:
with C# 5.0 async and await were introduced into the language to simplify using the Task Parallel Library.

    async Task<int> GetBigResultAsync()
    {
        var result = await GetResultAsync();
        if (result > 20) return result; 
        else return -1;
    }
It is not so helpful if you want to consume (or produce) continuous streams of results, such as you might get from an IoT device or a cloud service. 
Async streams are there for that.

## IAsyncEnumerable<T>

Asynchronous version of IEnumerable<T>
The language lets you await foreach over these to consume their elements, and yield return to them to produce elements.

    async IAsyncEnumerable<int> GetBigResultsAsync()
    {
        await foreach (var result in GetResultsAsync())
        {
            if (result > 20) yield return result; 
        }
    }

## NEW TYPE: RANGE [x..y] AND INDICES ^

Index. Used for indexing
An int that counts from the beginning
An int that counts from the the end with a prefix ^

    Index i1 = 3;  // number 3 from beginning
    Index i2 = ^4; // number 4 from end
    int[] a = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    Console.WriteLine($"{a[i1]}, {a[i2]}); // "3, 6"

Range
2 Indexes (one for the start, one for the end)
Written with a x..y range expression
Index with a Range in order to produce a slice:

    var slice = a[i1..i2]; // { 3, 4, 5 }
    MyName.Substring(0, MyName.Length-2)  →  jsonChunk[0..^2]
    foreach (var name in names[1..4])  iterating over names 1 to 4
                                ↓
                            a range expression: 
    Range range = 1..4; 
    foreach (var name in names[range])
    foreach (var name in names[1..^1])
    Range expressions can be open at either or both ends. 
        ..^1 means the same as 0..^1
        1..  means the same as 1..^0
        ..   means the same as 0..^0: beginning to end

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

    IEnumerable<string> GetEnrollees()
    {
        foreach (var p in People)
        {
            // If p is a Student, has not graduated and has a non-null name, we yield return that name
            if (p is Student { Graduated: false, Name: string name }) yield return name;
        }
    }

The pattern Student { Graduated: false, Name: string name } checks that the Person is a Student, then applies the constant pattern false to their Graduated property to see if they’re still enrolled, and the pattern string name to their Name property to get their name (if non-null). 
If p is a Student, has not graduated and has a non-null name, we yield return that name.

## SWITCH EXPRESSIONS

"lightweight" version of Switch statements with patterns (C# 7)

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

# TARGET-TYPED NEW-EXPRESSIONS

When you’re creating a new object, the type is often already given from context, so omit the type:

    Point[] ps = { new (1, 4), new (3,-2), new (9, 5) }; // all Points

# ASYNC STREAMS = ASYNC ENUMERABLE

with C# 5.0 async and await were introduced into the language to simplify using the Task Parallel Library.

async and await were added to C# to deal with results that are not necessarily ready when you ask for them. They can be asynchronously awaited, and the thread can go do other stuff until they become available. But that works only for single values, not sequences that are gradually and asynchronously produced over time, such as for instance measurements from an IoT sensor or streaming data from a service.


using System.Threading.Tasks;
await Task.Delay(1000);  // simulate that GetNames does some asynchronous work by adding an asynchronous delay before the name is yield returned:
yield return name;       // Of course we get an error that you can only await in an async method. So let’s make it async:

static async IEnumerable<string> GetNames()
Now we’re told that we’re not returning the right type for an async method, which is fair. But there’s a new candidate on the list of types it can return besides the usual Task stuff: IAsyncEnumerable<T>. This is our async version of IEnumerable<T>! Let’s return that:

static async IAsyncEnumerable<string> GetNames()
Just like that we’ve produced an asynchronous stream of strings! In accordance with naming guidelines, let’s rename GetNames to GetNamesAsync.

static async IAsyncEnumerable<string> GetNamesAsync()
Now we get an error on this line in the Main method:

foreach (var name in GetNamesAsync())
Which doesn’t know how to foreach over an IAsyncEnumerable<T>. That’s because foreach’ing over asynchronous streams requires explicit use of the await keyword:

await foreach (var name in GetNamesAsync())
It’s the version of foreach that takes an async stream and awaits every element! Of course it can only do that in an async method, so we have to make our Main method async. Fortunately C# 7.2 added support for that:

static async Task Main(string[] args)
Now all the squiggles are gone, and the program is correct. But if you try compiling and running it, you get an embarassing number of errors. That’s because we messed up a bit, and didn’t get the previews of .NET Core 3.0 and Visual Studio 2019 perfectly aligned. Specifically, there’s an implementation type that async iterators leverage that’s different from what the compiler expects.    

## PLATFORM DEPENDENCIES

Most of the C# 8.0 language features will run on any version of .NET. However, a few of them have platform dependencies.
indexers and ranges all rely on new framework types that will be part of .NET Standard 2.1. 

.NET Core 3.0 as well as Xamarin, Unity and Mono will all implement .NET Standard 2.1, but .NET Framework 4.8 will not. 
This means that the types required to use these features won’t be available when you target C# 8.0 to .NET Framework 4.8.

As always, the C# compiler is quite lenient about the types it depends on. If it can find types with the right names and shapes, it is happy to target them.

Default interface member implementations rely on new runtime enhancements, and we will not make those in the .NET Runtime 4.8 either. So this feature simply will not work on .NET Framework 4.8 and on older versions of .NET.

The need to keep the runtime stable has prevented us from implementing new language features in it for more than a decade. With the side-by-side and open-source nature of the modern runtimes, we feel that we can responsibly evolve them again, and do language design with that in mind. Scott explained in his Update on .NET Core 3.0 and .NET Framework 4.8 that .NET Framework is going to see less innovation in the future, instead focusing on stability and reliability. Given that, we think it is better for it to miss out on some language features than for nobody to get them.




https://www.codeproject.com/Articles/1265802/New-Features-of-Csharp-8