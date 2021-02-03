# PLinq

```c#

```


https://github.com/dotnet/samples/blob/master/csharp/parallel/PLINQ/Program.cs
using System;
using System.Diagnostics;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static async Task Main()   <--- Task to retrieve the state of the Task when interrupted
    {
        // Uncomment each of the below four lines one-by-one
        // to test the relevant PLINQ operation

        await AsOrdered();
        // await WithMergeOptions();
        // await WithCancellation();
        // WithDegreeOfParallelism();

        await Task.CompletedTask; <-- how we wait for the async task launched
    }
