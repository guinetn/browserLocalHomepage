# StringCollection

strongly typed to store only strings. It is dynamically resizable list and offer similar functionality as ArrayList class.

```cs
using System.Collection;

StringCollection sc = new StringCollection(); 
sc.Add("Oracle"); 
sc.Add("Microsoft"); 
sc.Add("IBM"); 
sc.Add("Intel"); 
 
// sc.Add(50);   Error: only strings can be added

string firstElement = sc[0];

foreach (string item in sc) 
   Console.WriteLine(item); 
```