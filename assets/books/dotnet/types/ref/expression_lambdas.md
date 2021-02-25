## Expression Lambda

ideal for passing functions into methods
can be converted to an expression tree

(parameters)=>expression   parentheses are optional if only one parameter
x => x*x;           an expression lambda that takes x and squares it
x => x <= 10;       confusing with comparison operators

```cs

public int total => t1 + t2;   // define a getter only property

public int square(int x) => x * x;

int i=Array.Find<int>(MyIntArray, x => x>0);

List<int> elements = new List<int>() { 10, 20, 31, 40 };
int firstOddIndex = elements.FindIndex(x => x % 2 != 0);
Console.WriteLine(firstOddIndex);
elements.Where(v => (int)v > 11).ToArray()

class myArray
{
 private string[] myarray= { "test0", "test1" };
 public string this[int i] => myarray[i];
}
myArray myArrayObject = new myArray();
MessageBox.Show(myArrayObject[0]);
```

download.page(dotnet/types/ref/expression_tree.md)

- https://www.i-programmer.info/programming/c/10097-deep-c-anonymous-methods-lambdas-and-closures.html