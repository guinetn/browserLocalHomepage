# StringDictionary

strongly typed version of the dictionary

```cs
using System.Collection;

StringDictionary sd = new StringDictionary(); 
 
sd.Add("1", "Italy"); 
sd.Add("2", "Spain"); 
sd.Add("3", "France"); 
sd.Add("4", "Brazil");
 
// Iterate Keys 
foreach (string key in sd.Keys) 
{ 
   Console.WriteLine(key); 
} 
 
// Iterate Values 
foreach (string value in sd.Values) 
{ 
   Console.WriteLine(value); 
} 
 
// Iterate both Keys and Values 
foreach (DictionaryEntry item in sd) 
{ 
   Console.WriteLine(item.Key + " : " + item.Value); 
} 
```