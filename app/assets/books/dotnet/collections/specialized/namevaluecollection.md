# NameValueCollection 

Specialized dictionary where keys and values are strings just as StringDictionary class. 
Difference: it allows you to add multiple values with the single key and those values can be retrieved by index as well as key. 
To retrieve all values associated with any particular key you can use GetValues()

```cs
using System.Collection;

NameValueCollection nvc = new NameValueCollection(); 
 
nvc.Add("System", "Systen.String"); 
nvc.Add("System", "Systen.Int32"); 
nvc.Add("System", "Systen.Decimal"); 
nvc.Add("System", "Systen.Boolean"); 
 
nvc.Add("System.IO", "Systen.IO.File"); 
nvc.Add("System.IO", "Systen.IO.FileInfo"); 
nvc.Add("System.IO", "Systen.IO.DirectoryInfo"); 
nvc.Add("System.IO", "Systen.IO.DriveInfo"); 
 
nvc.Add("System.Data", "Systen.Data.DataTable"); 
nvc.Add("System.Data", "Systen.Data.DataSet"); 
nvc.Add("System.Data", "Systen.Data.DataRow"); 
 
if (nvc.HasKeys()) 
{ 
   foreach (string key in nvc.Keys) 
   { 
      Console.WriteLine("-----------------------"); 
      Console.WriteLine(key); 
      Console.WriteLine("-----------------------"); 
 
      foreach (string value in nvc.GetValues(key)) 
            Console.WriteLine(value); 
   } 
}

```