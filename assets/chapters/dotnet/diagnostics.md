# diagnostics

### stopwatch
using System.Diagnostics;

Stopwatch stopwatch = new Stopwatch();
var list = new List<string>();
for (int i = 0; i < 5000000; ++i)
    list.Add(i.ToString());
stopwatch.Start();
Console.WriteLine("Creation: " + stopwatch.Elapsed);