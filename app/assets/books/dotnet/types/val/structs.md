## Structs

Value type
Encapsulate data and related functionality, to design small data-centric types that provide little or no behavior

A variable of a structure type contains an instance of the type. 
By default, ***variable values are copied on assignment***, passing an argument to a method, and returning a method result. In the case of a structure-type variable, an instance of the type is copied. If you're focused on the behavior of a type, consider defining a class. Class types have reference semantics. That is, a variable of a class type contains a reference to an instance of the type, not the instance itself.

You can avoid value copying by passing a structure-type variable by reference. Use the ref, out, or in method parameter modifiers to indicate that an argument must be passed by reference. Use ref returns to return a method result by reference

```cs
public struct Coords
{
    public Coords(double x, double y)
    {
        X = x;
        Y = y;
    }

    public double X { get; }
    public double Y { get; }

    public override string ToString() => $"({X}, {Y})";
}

public static class StructWithoutNew
{
    public struct Coords
    {
        public double x;
        public double y;
    }

    public static void Main()
    {
        Coords p;
        p.x = 3;
        p.y = 4;
        Console.WriteLine($"({p.x}, {p.y})");  // output: (3, 4)
    }
}
```

### ref struct (C# 7.2)

Instances of a ref struct type (Ex: span<T>) are allocated on the stack and can't escape to the managed heap. To ensure that, the compiler limits the usage of ref struct types as follows:

A ref struct can't be the element type of an array.
A ref struct can't be a declared type of a field of a class or a non-ref struct.
A ref struct can't implement interfaces.
A ref struct can't be boxed to System.ValueType or System.Object.
A ref struct can't be a type argument.
A ref struct variable can't be captured by a lambda expression or a local function.
A ref struct variable can't be used in an async method. However, you can use ref struct variables in synchronous methods, for example, in those that return Task or Task<TResult>.
A ref struct variable can't be used in iterators.

Typically, you define a ref struct type when you need a type that also includes data members of ref struct types:
public ref struct CustomRef
{
    public bool IsValid;
    public Span<int> Inputs;
    public Span<int> Outputs;
}

https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/struct#ref-struct