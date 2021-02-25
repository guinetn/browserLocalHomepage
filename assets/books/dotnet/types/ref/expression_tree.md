## Expression Trees

Lambdas expression can be converted to an expression tree (an object which contains all of the information contained in the lambda. It is a representation of the function in data)
An expression tree can be stored or transmitted to another system where it can be implemented at a later time or remotely. You can think of an expression trees as a data exchange format for lambdas but they also allow you to create lambdas dynamically.

https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/expression-trees/
code in a tree-like data structure, each node is an expression (method call, binary operation: x<y ...>)
Compile and run code represented by expression trees. This enables dynamic modification of executable code (linq queries)

Used in the dynamic language runtime (DLR) to provide interoperability between dynamic languages and .NET and to enable compiler writers to emit expression trees instead of Microsoft intermediate language (MSIL).

```cs
// Creating a lambda expression tree.  
Expression<Func<int, int>> ExTree = (x) => x * x;
// Explore the expression tree
Console.WriteLine(ExTree.Body);
Console.WriteLine(ExTree.Parameters[0]);
Console.WriteLine(ExTree.ReturnType);

Func<int, int> MyNewDelegate = ExTree.Compile();
int result=MyNewDelegate(3);
int result= ExTree.Compile()(3)


Expression<Func<int, bool>> expr = num => num < 5;  
// Compiling the expression tree into a delegate.  
Func<int, bool> result = expr.Compile();  
  
// Invoking the delegate and writing the result to the console.  
Console.WriteLine(result(4));  // Prints True
  
// Simplified syntax to compile and run an expression tree.  
Console.WriteLine(expr.Compile()(4));  
```

***ParameterExpression***
```cs
ParameterExpression param = Expression.Parameter(typeof(int), "x");
Expression square = Expression.Multiply(param, param);
Expression<Func<int,int>> ExTree = Expression.Lambda<Func<int,int>>(square,param);
Func<int, int> MyNewDelegate = ExTree2.Compile();
Console.WriteLine( MyNewDelegate(3).ToString());
```

```cs
using System.Linq.Expressions;  
  
// Manually build the expression tree for the lambda expression num => num < 5
ParameterExpression numParam = Expression.Parameter(typeof(int), "num");  
ConstantExpression five = Expression.Constant(5, typeof(int));  
BinaryExpression numLessThanFive = Expression.LessThan(numParam, five);  
Expression<Func<int, bool>> lambda1 =  
    Expression.Lambda<Func<int, bool>>(  
        numLessThanFive,  
        new ParameterExpression[] { numParam }); 
```

## More

- https://www.i-programmer.info/programming/c/10097-deep-c-anonymous-methods-lambdas-and-closures.html