# OrderedDictionary

Hashtable do not have index access and if you try to iterate items using enumerator, the items are ordered based on their hash value and not in the order you need. When you need both the power of a collection, and the simple access of a numeric index, the OrderedDictionary is the collection of choice. It not only gives you 
- a very fast dictionary 
- keep your items in order
Using this class, you can perform specific actions at a numeric index in the collection, or you can use the Dictionary Entry style of looping over the collection.

```cs
using System.Collection;

OrderedDictionary od = new OrderedDictionary(); 
 
od.Add("1", "Italy"); 
od.Add("2", "Spain"); 
od.Add("3", "France"); 
od.Add("4", "Brazil"); 
 
// Iterate items using index no (array style) 
for (int i = 0; i < od.Count; i++) 
   Console.WriteLine(od[i]); 
 
// Iterate items using DictionaryEntry (dictionary style) 
foreach (DictionaryEntry item in od) 
   Console.WriteLine(item.Key + " : " + item.Value); 

```