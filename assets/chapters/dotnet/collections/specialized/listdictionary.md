# ListDictionary

.NET developers normally use Hashtable to store key/value pairs, the most common type of dictionary 
One issue is it requires a bit of overhead and if you want to store only few elements this overhead can cause performance issues. This is where another specialized .NET Framework class ListDictionary comes in. 
ListDictionary is very efficient for small collections of items (less than ten elements) because it is implemented as a simple array of items underneath. It has similar interface as Hashtable and can be used as replacement.

```cs
using System.Collection;

ListDictionary ld = new ListDictionary(); 
 
ld.Add("1", "Italy"); 
ld.Add("2", "Spain"); 
ld.Add("3", "France"); 
ld.Add("4", "Brazil"); 
 
foreach (DictionaryEntry item in ld) 
{ 
   Console.WriteLine(item.Key + " : " + item.Value); 
}

```