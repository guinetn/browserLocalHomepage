## Benchmarking

***Benchmark***
Measurement or set of measurements relating to the execution of some code.Benchmarks have a mechanism to compare proposed changes against the original code which then guide your optimisation work.

### Stopwatch

```cs
using System;
using System.Diagnostics;

class Program
{
    const int _max = 1000000;
    static void Main()
    {
        var s1 = Stopwatch.StartNew();        
        for (int i = 0; i < _max; i++)
        {
        }
        s1.Stop();

        var s2 = Stopwatch.StartNew();
        for (int i = 0; i < _max; i++)
        {
        }
        s2.Stop();
        
        Console.WriteLine(((double)(s1.Elapsed.TotalMilliseconds * 1000000) /
            _max).ToString("0.00 ns"));
        Console.WriteLine(((double)(s2.Elapsed.TotalMilliseconds * 1000000) /
            _max).ToString("0.00 ns"));
    }
}
```

### BenchmarkDotNet

- https://benchmarkdotnet.org/
- https://github.com/dotnet/BenchmarkDotNet

Tons of features in comprehensive performance investigations
Transform methods into benchmarks, track their performance, and share reproducible measurement experiments. 

Use 'jobs' to compare performance in different environments
Use '[Params(1, 2, 3)]' to run benchmarks for each case on the field

* Attributes
[Benchmark]  
to compare benchmarks with each other, reference beeing [Benchmark(baseline: true)] 
* Console
>dotnet benchmark MyAssembly.dll --runtimes net472 netcoreapp2.1 Mono
* Fluent
ManualConfig.CreateEmpty() // A configuration for our benchmarks
    .With(Job.Default // Adding first job
            .With(ClrRuntime.Net472) // .NET Framework 4.7.2
            .With(Platform.X64) // Run as x64 application
            .With(Jit.LegacyJit) // Use LegacyJIT instead of the default RyuJIT
            .WithGcServer(true) // Use Server GC
    ).With(Job.Default // Adding second job
            .AsBaseline() // It will be marked as baseline
            .WithEnvironmentVariable("Key", "Value") // Setting an environment variable
            .WithWarmupCount(0) // Disable warm-up stage
    );

mkdir Benchmarks
cd Benchmarks
dotnet new console
references the Benchmark.NET NuGet package 

```cs
[SimpleJob(RuntimeMoniker.Net472, baseline: true)]
[SimpleJob(RuntimeMoniker.NetCoreApp30)]
[SimpleJob(RuntimeMoniker.CoreRt30)]
[SimpleJob(RuntimeMoniker.Mono)]
[RPlotExporter]
public class Md5VsSha256
{
    private SHA256 sha256 = SHA256.Create();
    private MD5 md5 = MD5.Create();
    private byte[] data;

    [Params(1000, 10000)]
    public int N;

    [GlobalSetup]
    public void Setup()
    {
        data = new byte[N];
        new Random(42).NextBytes(data);
    }

    [Benchmark]
    public byte[] Sha256() => sha256.ComputeHash(data);

    [Benchmark]
    public byte[] Md5() => md5.ComputeHash(data);
}
```

```cs
private byte[] data;

public static int ArraySum(byte[] data)
{
    int sum = 0;
    for (int i = 0; i &lt; data.Length; i++)
    {
        sum += data[i];
    }
    return sum;
}

public static int SpanSum(Span<byte> data)
{
    int sum = 0;
    for (int i = 0; i &lt; data.Length; i++)
    {
        sum += data[i];
    }
    return sum;
}

[GlobalSetup]
public void Setup()
{
    data = new byte[10_000];
    new Random(42).NextBytes(data);
}
[Benchmark(Baseline = true)] // <----- Benchmark reference
public int ArraySum() => ArraySum(data);
[Benchmark]                 // <----- Benchmark challenger 
public int SpanSum() => SpanSum(data);
```

## More

- https://www.codemag.com/article/1807051/Introducing-.NET-Core-2.1-Flagship-Types-Span-T-and-Memory-T
- https://michaelscodingspot.com/category/performance/
- https://michaelscodingspot.com/ways-to-cause-memory-leaks-in-dotnet/