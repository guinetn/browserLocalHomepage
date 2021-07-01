# diagnostics

System.Runtime.InteropServices.RuntimeInformation.OSDescription
System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription
System.DateTime.Now.ToLongTimeString()

### stopwatch
using System.Diagnostics;

Stopwatch stopwatch = new Stopwatch();
var list = new List<string>();
for (int i = 0; i < 5000000; ++i)
    list.Add(i.ToString());
stopwatch.Start();
Console.WriteLine("Creation: " + stopwatch.Elapsed);


many to add:
- https://speakerdeck.com/davidfowl/application-diagnostics-in-net-core-3-dot-1
+ code https://github.com/davidfowl/NdcLondon2020

