# HybridDictionary

Use ListDictionary for small collection of items
Use Hashtable when you have large number of items to store

What iff you do not know how many items your program has to store in collection?
HybridDictionary implements ListDictionary and Hashtable both internally and automatically switches between those two based on the number of items you store. 
Using HybridDictionary is similar as other Dictionary based classes in .NET Framework.

```cs
using System.Collection;

HybridDictionary hd = new HybridDictionary(); 
 
hd.Add("1", "Italy"); 
hd.Add("2", "Spain"); 
hd.Add("3", "France"); 
hd.Add("4", "Brazil"); 
 
foreach (DictionaryEntry item in hd) 
   Console.WriteLine(item.Key + " : " + item.Value); 

```