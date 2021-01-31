## Expression Trees
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/expression-trees/
code in a tree-like data structure, each node is an expression (method call, binary operation: x<y ...>)
Compile and run code represented by expression trees. This enables dynamic modification of executable code (linq queries)

Used in the dynamic language runtime (DLR) to provide interoperability between dynamic languages and .NET and to enable compiler writers to emit expression trees instead of Microsoft intermediate language (MSIL).

```cs
// Creating a lambda expression tree.  
Expression<Func<int, bool>> expr = num => num < 5;  
  
// Compiling the expression tree into a delegate.  
Func<int, bool> result = expr.Compile();  
  
// Invoking the delegate and writing the result to the console.  
Console.WriteLine(result(4));  // Prints True
  
// Simplified syntax to compile and run an expression tree.  
Console.WriteLine(expr.Compile()(4));  
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
