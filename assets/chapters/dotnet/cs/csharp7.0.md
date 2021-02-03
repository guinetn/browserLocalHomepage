# C# 7 (.Net 4.7)  #

## 7.0
Out variables
Tuples and deconstruction
Pattern matching
Local functions
Expanded expression bodied members
Ref locals and returns
Other features included:

Discards
Binary Literals and Digit Separators
Throw expressions


## 7.1
async Main method. The entry point for an application can have the async modifier.
default literal expressions. You can use default literal expressions in default value expressions when the target type can be inferred.
Inferred tuple element names. The names of tuple elements can be inferred from tuple initialization in many cases.
Pattern matching on generic type parameters. You can use pattern match expressions on variables whose type is a generic type parameter.

## 7.2

Techniques for writing safe efficient code
A combination of syntax improvements that enable working with value types using reference semantics.
Non-trailing named arguments
Named arguments can be followed by positional arguments.
Leading underscores in numeric literals
Numeric literals can now have leading underscores before any printed digits.
private protected access modifier
The private protected access modifier enables access for derived classes in the same assembly.
Conditional ref expressions
The result of a conditional expression (?:) can now be a reference.


## 7.3

Tools such as Visual Studio upgrade on a frequent cadence, and there’s no longer a technical reason why C# couldn’t also be updated more frequently. Choose your cadence (major (".0") C# versions or latest)

You can access fixed fields without pinning.
You can reassign ref local variables.
You can use initializers on stackalloc arrays.
You can use fixed statements with any type that supports a pattern.
You can use additional generic constraints.




* Tuples 
* Local Functions
* Pattern Matching feature (is / case extension)

Program complex types with enhanced pattern matching syntax

To match patterns on any data type, even on custom data types
Built-in pattern matching
Pattern matching can extract values from your expression

Allow to
    write additional conditions in case statements
    switch on any type
    use patterns in case statement

class Customer
    {
    public int CustomerId { get; set; }
    public string Name { get; set; }
    public string City { get; set; }
    }

class Agent : Customer {}
class DirectConsumer : Customer {}


So we can write switch case statements as below:    
. Now the sequence of the case statement matters as the first which satisfies the condition will be processed just like catch clauses
. Even though you put default first before null case, it will first check whether it fits with null and if it does not then only it goes for default case so default will be executed at the last
. If customer object is null, processing will fall into the Null case, even if it is an Agent or DirectConsumer null instance

    switch(customer)
    {
    case Agent a when (a.CustomerId == 11):
    Console.WriteLine($"Customer is an agent and Name: {a.Name}");
    break;

    case DirectConsumer b when ((b.CustomerId == 21) & (b.City == "Pune"):
    Console.WriteLine($"Customer is a consumer(Pune location) and Name: {b.Name}");
    break;

    default:
    Console.WriteLine("Customer Not found");
    break;

    case Null:
    throw new ArgumentNullException(nameof(shape));
    }


## Another sample

class Point
{
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) => (X, Y) = (x, y);
    public void Deconstruct(out int x, out int y) => (x, y) = (X, Y);
}

static string Display(object o)
{
    switch (o)
    {
        case Point p when p.X == 0 && p.Y == 0:
            return "origin";
        case Point p:
            return $"({p.X}, {p.Y})";
        default:
            return "unknown";
    }
}



    From C# 7.0 onwards, we can use is with:

Type pattern:
    With type pattern, we can check whether the object is compatible or not:
    if (a is Agent p) Console.WriteLine($"it's an agent: {p.Name}");
    if (d is DirectConsumer b && (b.City == "Pune")) Console.WriteLine($"it's a direct cosumer lives in {b.City}");

Const pattern:
    It can be used to verify any constant numbers or Null:
    if (a is null) throw new ArgumentNullException(nameof(a));
    if (a is 10) Console.WriteLine("it is 10");

Let us take some example to check whether the object is a string:
object obj = "Hello, World!";
if (obj is string str)
{
    Console.WriteLine(str);
}
One more example where we want to check whether an object is equal to some constants:
object obj = 1; 

if (obj is 1)
{
    Console.WriteLine(true);
}


## C# 7.1 

Visual Studio 2017 > 15.3 or .NET Core SDK 2.0
7.1 features are turned off by default
    right-click on the project node in Solution Explorer and select Properties. Select the Build tab and select the Advanced button. In the dropdown, select C# latest minor version (latest), or the specific version C# 7.1 
    (uses the language version selection configuration element to select the compiler language version)
    or in .csproj:
    <PropertyGroup>
        <LangVersion>latest</LangVersion>
    </PropertyGroup>

# ASYNC MAIN

The entry point for an application can have the async modifier.
Main entry point method can now return a Task or a Task<int>: execution  wait for the returned task to complete before shutting down the program.

static async Task Main() // make the Main method async
{}
static async Task Main(string[] args) // make the Main method async
{ }
This lets you await directly in the Main method

WriteLine($"Fib {tuple.input} = {await tuple.task}");
What you had to do previously was quite unappetizing: first you’d create an async helper method, MainAsync, say, with all the logic in. Then you’d write this cryptic Main method:
static void Main(string[] args) => MainAsync().GetAwaiter().GetResult();
Now you can just make your Main method async, and the compiler will rewrite it for you.



    static string Main()
    {
        await AsyncMethod1();   // Before, to put await for your async method, you need to use GetAwaiter() method
    }

    static async Task Main()    If your main method returns Task, then it can include async modifiers
    {
        await AsyncMethod1();  
    }

## Inferred tuple element names

The names of tuple elements can be inferred from tuple initialization in many cases.

    int count = 5;
    string label = "Colors used in the map";
    var pair = (count: count, label: label);        
    var pair = (count, label); // # 7.1: element names are "count" and "label"

In this lambda expression inside the query:
input => (input, task: FibonacciAsync(input))
You notice that we create a tuple, but only give a name, task, for the second element. Yet a few lines later we are able to say
WriteLine($"Fib {tuple.input} = {await tuple.task}");
Accessing the first element by the name tuple.input. That’s because when you create a tuple with an expression that "has" a name, like input in the lambda expression above, we’ll now automatically give the corresponding tuple element that name.

## Default literals expressions

You can use default literal expressions in default value expressions when the target type can be inferred.
This avoids tedious repetition of type names, or typing out long ones when they are already given by context.

If there’s an expected type for a default expression, you can now omit the mention of the type, as we do for the CancellationToken in in the signature of the FibonacciAsync method:

    private static Task<int> FibonacciAsync(int n, CancellationToken token = default)


    Func<string, bool> whereClause = default(Func<string, bool>);
                                                ↑ 
                                #7.1: omit the type on the right-hand side of the initialization
                                                ↓
    Func<string, bool> whereClause = default;

## Reference semantics with value types 

work with value types while using reference semantics (best perf)

A combination of syntax improvements that enable working with value types using reference semantics.
- in modifier on parameters
    specify that an argument is passed by reference but not modified by the called method.
- ref readonly modifier on method returns
    indicate that a method returns its value by reference but doesn't allow writes to that object.
- readonly struct declaration
    indicate that a struct is immutable and should be passed as an in parameter to its member methods.
-ref struct declaration
    indicate that a struct type accesses managed memory directly and must always be stack allocated.

Non-trailing named arguments
Named arguments can be followed by positional arguments.
To supply arguments for only a few parameters from a list of optional parameters. This capability greatly facilitates calls to COM interfaces such as the Microsoft Office Automation APIs.

C# 4: named and optional arguments
PrintOrderDetails(orderNum: 31, productName: "Red Mug", sellerName: "Gift Shop");
PrintOrderDetails(orderNum: 31, productName: "Red Mug", sellerName: "Gift Shop");
PrintOrderDetails(productName: "Red Mug", sellerName: "Gift Shop", orderNum: 31);

Leading underscores in numeric literals
Numeric literals can now have leading underscores before any printed digits.
Hex and binary numeric literals for may now begin with an _
int binaryValue = 0b_0101_0101;

private protected access modifier
A member may be accessed by derived classes that are declared in the same assembly. 

private protected       enables access for derived classes in the same assembly
protected internal      allows access by derived classes or classes that are in the same assembly
private protected       limits access to derived types declared in the same assembly


## Tuples 

## Tuples were available before C# 7 as an API, but had many limitations. Most importantly, the members of these tuples were named Item1, Item2 and so on. The language support enables semantic names for the fields of a Tuple.

Tuples are lightweight data structures that contain multiple fields to represent the data members. To return more than one variable, the traditional way is using out parameter but there are some limitations for out parameter, like we can’t use it with async method.
Tuples are value types not reference type.
Tuple elements are public and mutable fields.
You can convert tuples to other tuples.
Tuple is not built in visual studio but you should install it as nuGet package
Tuple can be return type and also can be literal type.
Tuple can have two values or more.

"Manage NuGet Packages" → "System.ValueTuple"

* First way to use tuple is to just write types of the variables returned

    static (string, string, int) MyData()  
    {  
        return ("Omar", "maher", 123456);  
    }   

    static void Main(string[] args)  
    {  
        var userData = MyData();  
        Console.WriteLine($"My name is { userData.Item1} " +  
            $"{ userData.Item2} and my password is " +  
            $"{ userData.Item3}");  
              }  
        userData.Item1 refers to first variable and userData.Item2 refers to the second variable...



* Second way to use tuple is to give variables a name

    static (string firstName, string lastName, int password) MyData2()  
    {  
        return ("Omar", "maher", 123456);  
    }   

    static void Main(string[] args)  
    {  
        var userData2 = MyData2();  
        Console.WriteLine($"My name is { userData2.firstName} " +  
            $"{ userData2.lastName} and my password is " +  
            $"{ userData2.password}");  

        Console.WriteLine($"My name is { userData2.Item1} " +  
            $"{ userData2.Item2} and my password is " +  
            $"{ userData2.Item3}");  
      }   



* Third way to consume tuple is by Deconstructions (will create new variables to assign to its values from the return of the method)

    static void Main(string[] args)  
    {  
       (var firstName, var lastName, var password) = MyData2();   // way 1
       var (firstName, lastName, password) = MyData2();           // way 2 

        Console.WriteLine($"My name is {firstName} " +  
             $"{ lastName} and my password is " +  
             $"{ password}");  
     }   


## Local Functions
    you can create a function within anther function and it is fully encapsulates within that function

Parameters and local variable from the enclosing scope are visible within the local function.

    Why
    for readability and if you will use this method just in this place ,so you should think in local functions

Local functions can improve the readability of complex methods. Yes you could use private methods. But then you'd need to pass a ton of arguments to them. Local functions give you the scope of the current method. So, if your algorithm could be broken down into private functions with 8 arguments or local functions with 1 or 2, you might see a good use for locals. 

    Let's think about when you need a helper function, which will be called once.
    In the old days, before C# 7, you could think in 2 ways.
    1. Create a private method inside the class and call it in the function but that will end up having many private methods, which wouldn’t be reused.
    2. Using Func and Actions types with the anonymous methods but this solution has a limitation like you can’t use generics , out , ref and params.
    Now in C# 7 world, you can declare a function inside anther one.

    static void Main(string[] args)  
    {  
        // Method calling  ( after or before the local function declaration)
        GetMyName();  

        //Method Declaration: created a function GetMyName() inside Main Function. 
        void GetMyName()  
        {  
            Console.WriteLine( "My Name Is Omar Maher"  );  
        }          
    }   


## Example 2

    static void Main(string[] args)  
    {  
        // Method calling  
        GetMyName("Omar Maher");  

        //Method Declaration  
        void GetMyName(string name)  
        {  
            Console.WriteLine($"My Name Is {name}");  
        }  
    }   

## Example 3

    static void Main(string[] args)  
    {  
        string name = "Omar Maher";  
        // Method calling  
        GetMyName();  

        //Method Declaration  
        void GetMyName()  
        {  
            Console.WriteLine($"My Name Is {name}");  
        }  
    }   

## Example 4

    class MyData  
    {  
        public MyData()  
        {  
        }  
    }   
    Now, let's create a local function GetMyName() inside the MyData Contractor, as shown. 

    class MyData  
    {  
        public MyData()  
        {  
            // Method calling  
            GetMyName();  

            //Method Declaration  
            void GetMyName()  
            {  
                Console.WriteLine($"My Name Is Omar Maher");  
            }  
        }  
    }   


    static void Main(string[] args)  
    {  
        MyData data = new MyData();  
    }   


## Example 5

    class MyData  
    {  
        public MyData(string name)  
        {  
            // Method calling  
            GetMyName();  

            //Method Declaration  
            void GetMyName()  
            {  
                Console.WriteLine($"My Name Is {name}");  
            }  
        }  
    }   

    static void Main(string[] args)  
    {  
        MyData data1 = new MyData("Omar Maher");  
    }   
    The result will be the same

## Discards _ write only

    a way to ignore local variables if not used instead of creating it.

    Write-only local variable in which you can assign but cannot read. 
    A way to ignore local variables if not used instead of creating it.
    Represented by "_" (underscore, They don't have names)
    Since _ cannot be read, it will not appear on the right side of an assignment. 

    to create dummy variable defined by underscore character _. Discards are equal to unassigned variables. The purpose of this feature is to use this variable when you want to intentionally skip the value by not creating variable explicitly.
    For example, if you are calling the method and it returns the object but caller is only interested in calling the method but not interested in the return object. In such case, we can use discards variable so that it can reduce in terms of memory allocation and make your code clear as well.

    Without Discards Variable
        bool boolParsedValue;
        if (bool.TryParse("False", out boolParsedValue)) { /* Custom Code */ }
    With Discards Variable
        if (bool.TryParse("False", out _)) { /* Custom Code */ }


    // not considered as discard (since you are explicitly declaring _)
    var _ = true;
    if (bool.TryParse("False", out _)) { bool b = _; }

    bool _ = false, v = false;
    if (bool.TryParse("TRUE", out var _))
    {
         v = _;     // false
    }

    _ = DateTime.TryParse("02/29/2019", out result); 

    if (DateTime.TryParse("02/29/2019", out _))  
    {  
        Console.WriteLine("Date is valid");  
    }  
    else  
    {  
        Console.WriteLine("Date is not valid");  
    } 

    * Use discards when not interested in all tuple values: var (a, _, _) = (1, 2, 3)

    * Use discards with Task.Run method where you are not interested in return result: _ = Task.Run(() => { }



## More

- https://intellitect.com/csharp-7-msdn/
- https://intellitect.com/csharp7-tuples-explained/