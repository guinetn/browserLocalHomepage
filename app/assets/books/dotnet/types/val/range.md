## RANGE [x..y] AND INDICES ^

Written with a x..y range expression
Two int indexes (one for the start, one for the end) that can
- counts from the beginning
- counts from the the end when prefixed with ^

Range(inclusive_Start_Index, exclusive_End_Index)	new Range instance with the specified starting and ending indexes

Index. Used for indexing
```cs
int[] someArray = new int[5] { 1, 2, 3, 4, 5 };
int[] subArray1 = someArray[0..2];               // { 1, 2 }
int[] subArray2 = someArray[1..^0];              // { 2, 3, 4, 5 }

public string OperationId { get; } = NewGuid().ToString()[^4..];

Index i1 = 3;  // number 3 from beginning
Index i2 = ^4; // number 4 from end
int[] a = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
Console.WriteLine($"{a[i1]}, {a[i2]}); // "3, 6"
```cs

Index with a Range in order to produce a slice:
```cs
var slice = a[i1..i2]; // { 3, 4, 5 }
MyName.Substring(0, MyName.Length-2)  →  MyName[0..^2]
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
```

System.Linq.IEnumerable<int> squares = Enumerable.Range(1, 10).Select(x => x * x);        
        
https://docs.microsoft.com/en-us/dotnet/api/system.range?view=net-5.0        