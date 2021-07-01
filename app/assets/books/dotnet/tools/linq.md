# Linq

All LINQ methods, accept delegate as a parameter.
LINQ is much easier to read and maintain 

Simple LINQ queries have performance similar to 'For' loops but require much more allocations to operate and on a large scale, allocations will lead to more frequent GC calls and performance decrease across all application layers.
LINQ is the best option for most cases. However, for performance-critical path usage of loops might be a better decision.

Find Ids of all customers having at least two orders of more than 100€ in total.
```c#
var customersIds<IEnumerable> = customers.where(customer=>customer.Orders.Count(order=>order.TotalPrice >= 100m) > 2).Select(customer=>customer.Id);
```


Enumerable.Range(1, 5).Select(i => {})

* Sort a string
var s = "zacb";
var s2 = String.Concat(s.OrderBy(c => c)); // abcz
var s2 = String.Concat(s.OrderBy(c => c).Distinct()); // remove duplicates


var elements = new List<string>() {"water air earth fire", "grass sky thunder air"}; 
var query = elements.SelectMany(f => f.Split(' ')).OrderBy(x => x)
.GroupBy(x =>x).Select((x, i) => new { Element = x, Count = x.Count() }); 
var first = query.First(); 
Console.WriteLine(first.Count); 

var list = new List<string>() {"water", "air"};
var r = list.Contains("air");
System.Console.WriteLine("air" + r); // true
var r2 = list.Find(x=> x=="air");
System.Console.WriteLine("air2: " + r2); // true
System.Console.WriteLine(list[1]); // true

string s= "zacbc";
var s2 = String.Concat(s.OrderBy(c => c));
System.Console.WriteLine(s2); // abccz
s2 = String.Concat(s.OrderBy(c => c).Distinct());
System.Console.WriteLine(s2); // abcz			

## [Linq Methods](https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.aggregate?view=net-5.0)

- Aggregate
- All
- Any
- Append
- AsEnumerable
- Average
- Cast
- Concat
- Contains
- Count
- DefaultIfEmpty
- Distinct
- ElementAt
- ElementAtOrDefault
- Empty
- Except
- First
- FirstOrDefault
- GroupBy
- GroupJoin
- Intersect
- Join
- Last
- LastOrDefault
- LongCount
- Max
- Min
- OfType
- OrderBy
- OrderByDescending
- Prepend
- Range
- Repeat
- Reverse
- Select
- SelectMany
- SequenceEqual
- Single
- SingleOrDefault
- Skip
- SkipLast
- SkipWhile
- Sum
- Take
- TakeLast
- TakeWhile
- ThenBy
- ThenByDescending
- ToArray
- ToDictionary
- ToHashSet
- ToList
- ToLookup
- Union
- Where
- Zip

## LINQPad

- https://www.linqpad.net

To query databases using LINQ modern programming language. LINQPad provides an opportunity to try out code lines and test snippets or programs. You can also take advantage of output formatting, optional autocompletion, and integrated debugging.
LINQPad is a completely free tool. 

## More

- https://www.ezzylearning.net/tutorial/introduction-to-language-integrated-query-linq
- https://intellitect.com/notes-on-some-c-3-0-features-that-make-linq-possible/