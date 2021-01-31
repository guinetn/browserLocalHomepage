# Lookup

Lookup: Represents a collection of keys each mapped to one or more values.

System.Linq;
public class Lookup<TKey,TElement> : 
       System.Collections.Generic.IEnumerable<System.Linq.IGrouping<TKey,TElement>>, System.Linq.ILookup<TKey,TElement>

return an immutable: cannot add/remove elements or keys from a Lookup<TKey,TElement> object after it has been created.

- https://docs.microsoft.com/en-us/dotnet/api/system.linq.lookup-2?view=net-5.0
      
## Samples


```c#
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

Stopwatch stopwatch = new Stopwatch();
var list = new List<string>();
for (int i = 0; i < 5000000; ++i)
{
    list.Add(i.ToString());
}
stopwatch.Start();
var lookup = list.ToLookup(x => x);         // 00:00:03.8478120
stopwatch.Stop();
Console.WriteLine("Creation: " + stopwatch.Elapsed);

stopwatch.Start();
var lookup2 = list.ToDictionary(x => x);   // 00:00:04.6473218
stopwatch.Stop();
Console.WriteLine("Creation: " + stopwatch.Elapsed);
```

```c#
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

/*
csc ToLookup.cs
ToLookup.exe
*/
namespace ToLookup_Test {
    
    public class Program {

        public static void Main() {
            Console.WriteLine("hi");   
        
          ToLookupEx1();
        }

         public static void ToLookupEx1()
        {
            // Create a list of Packages.
            List<Package> packages =
                new List<Package>
                    { new Package { Company = "Coho Vineyard", Weight = 25.2, TrackingNumber = 89453312L }, 
                      new Package { Company = "Lucerne Publishing", Weight = 18.7, TrackingNumber = 89112755L },
                      new Package { Company = "Wingtip Toys", Weight = 6.0, TrackingNumber = 299456122L },
                      new Package { Company = "Contoso Pharmaceuticals", Weight = 9.3, TrackingNumber = 670053128L },
                      new Package { Company = "Wide World Importers", Weight = 33.8, TrackingNumber = 4665518773L } };

            // Create a Lookup to organize the packages.
            // Use the first character of Company as the key value.
            // Select Company appended to TrackingNumber
            // as the element values of the Lookup.
            ILookup<char, string> lookup = packages
                .ToLookup(p => Convert.ToChar(p.Company.Substring(0, 1)), 
                          p => p.Company + " " + p.TrackingNumber);

            // Iterate through each IGrouping in the Lookup.
            foreach (IGrouping<char, string> packageGroup in lookup)
            {
                // Print the key value of the IGrouping.
                Console.WriteLine(packageGroup.Key);
                // Iterate through each value in the
                // IGrouping and print its value.
                foreach (string str in packageGroup)
                    Console.WriteLine("    {0}", str);
            }
        }
    }      

  class Package
  {
      public string Company { get; set; }
      public double Weight { get; set; }
      public long TrackingNumber { get; set; }
  }

 

/*
 This code produces the following output:

 C
     Coho Vineyard 89453312
     Contoso Pharmaceuticals 670053128
 L
     Lucerne Publishing 89112755
 W
     Wingtip Toys 299456122
     Wide World Importers 4665518773
*/
  
}
```