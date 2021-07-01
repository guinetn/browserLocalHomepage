# CSHARP: MIN

Say hi.cs
```c#
using System;
namespace SayingHi {    
    public class Program {
        public static void Main() {
            Console.WriteLine("hi");   
        }
    }        
}
```
To compile:
>cmd.exe
>csc hi.cs
>hi.exe

Console.ReadLine()
```cs
using system;
class abc
{
    public static Void Main()
    {
        int ndistance, nresult;
        Console.WriteLine("Enter the distance in kilometers");
        ndistance = convert.ToInt32(Console.ReadLine());
        nresult = ndistance * 1000;
        Console.WriteLine("Distance in meters: " + nresult);
        Console.ReadLine();
    }
}
```

# CSHARP: ALL

```cs
[Debugger, Display("{descrition} prix :{m_price}  #")]
[DebuggerVisualizerAttribute]	//	visualization par gdi  ??
class Article
{ 
    private int price ;   
    string description ;
    public Guid articleID { get; set; } = Guid.NewGuid();    // Auto-Property Initializers
}


public class Purchase
{
    public Guid FictionalArticleNumber { get; set; }
    public string ArticleName { get; set; }
    public Guid CustomerId { get; set; }
    public DateTimeOffset TransactionDate { get; set; }

    [JsonProperty("id")]
    public Guid PurchaseId { get; set; }
    
    public void test() {
        public Dictionary<string, string> customerNames = new Dictionary<string, string>()
        {
        ["Michael Jordan"] = "Basketball", // old way: { "Michael Jordan", "Basketball" },
        ["Peyton Manning"] = "Football",
        ["Babe Ruth"] = "Baseball"
        };
    }
}
    
   
   
https://github.com/dotnet/corefx/blob/master/src/System.Threading.Tasks/tests/Helpers.cs    
namespace System.Threading.Tasks.Tests
{
    internal class InvokeActionOnFinalization
    {
        public Action Action;
        ~InvokeActionOnFinalization() => Action?.Invoke();
    }
}
```