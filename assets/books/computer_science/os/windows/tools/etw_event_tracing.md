# ETW - Event Tracing for Windows 

Event Tracing for Windows (ETW) is a powerful logging mechanism built into the Windows OS and is used extensively in Windows.
You can also log ETW events yourself code using the System.Diagnostics.Tracing.EventSource class.
TraceEvent library contains the classes needed to control ETW providers (including .NET EventSources) and parse the events they emit.
- TraceEventSession: enable ETW providers
- EtwTraceEventSource: to read the stream of ETW events
- TraceLog: digested form of ETW events (decoded stack traces of events)
          
     
Using the ETW to collect the PMC counters is easy

Counters are :
```cs
public class ProfileSourceInfo
{
    public string Name;     /// Human readable name of the CPU performance counter (eg BranchInstructions, TotalIssues ...)
    public int ID;          /// The ID that can be passed to SetProfileSources
    public int Interval;    /// This many events are skipped for each sample that is actually recorded
    public int MinInterval; /// The smallest Interval can be (typically 4K)
    public int MaxInterval; /// The largest Interval can be (typically maxInt).
}
// Choose the counters available you can collect for your machine:
var infos = TraceEventProfileSources.GetInfo()

// Collect counters:
TraceEventProfileSources.Set(
    selectedCounters.Select(counter => counter.ID).ToArray(),
    selectedCounters.Select(counter => counter.MinInterval).ToArray());

// Create a Kernel ETW Session:
var session = new TraceEventSession(KernelTraceEventParser.KernelSessionName);

// As admin, enable the right Kernel Provider:
session.EnableKernelProvider(KernelTraceEventParser.Keywords.PMCProfile | KernelTraceEventParser.Keywords.Profile)

// before you start processing events you should sign up for following two events:
session.Source.Kernel.PerfInfoCollectionStart += _ => { }; // we must subscribe to this event, otherwise the PerfInfoPMCSample is not raised ;)
session.Source.Kernel.PerfInfoPMCSample += OnPerfInfoPmcSample;

// PerfInfoCollectionStart contains info about the interval 
PerfInfoPMCSample is raised when a new sample is collected. It contains the id of the process and id of the counter, which should allow you to do the math (counters[processId][counterId].SamplesCollected += Interval). It also contains InstructionPointer which could be used to connect the sample with source code line. If I ever found few weeks of free time I would implement such feature for BenchmarkDotNet.
    
```
or
>tracelog.exe -profilesources Help
Id  Name                        Interval  Min      Max
--------------------------------------------------------------
  0 Timer                          10000  1221    1000000
  2 TotalIssues                    65536  4096 2147483647
  6 BranchInstructions             65536  4096 2147483647
 10 CacheMisses                    65536  4096 2147483647
 11 BranchMispredictions           65536  4096 2147483647
 19 TotalCycles                    65536  4096 2147483647
 25 UnhaltedCoreCycles             65536  4096 2147483647
 26 InstructionRetired             65536  4096 2147483647
 27 UnhaltedReferenceCycles        65536  4096 2147483647
 28 LLCReference                   65536  4096 2147483647
 29 LLCMisses                      65536  4096 2147483647
 30 BranchInstructionRetired       65536  4096 2147483647
 31 BranchMispredictsRetired       65536  4096 2147483647
 32 LbrInserts                     65536  4096 2147483647
 33 InstructionsRetiredFixed       65536  4096 2147483647
 34 UnhaltedCoreCyclesFixed        65536  4096 2147483647
 35 UnhaltedReferenceCyclesFixed      65536  4096 2147483647
 36 TimerFixed                     10000  1221    1000000
    
- Create project
- Add  
    Nuget package: https://www.nuget.org/packages/Microsoft.Diagnostics.Tracing.TraceEvent/
    Reference to Microsoft.Diagnostics.Tracing.TraceEvent 

Logs all the kernel (clr and dynamic events) in an ETL (ETW Trace File) that perview.exe can read.

```cs
using Microsoft.Diagnostics.Tracing;
using System;

class Program
{
    static void Main()
    {
        using (var source = new ETWTraceEventSource("ETWData.etl"))
        {
            // setup the callbacks
            source.Clr.All += Print;
            source.Kernel.All += Print;
            source.Dynamic.All += Print;

            // iterate over the file, calling the callbacks.  
            source.Process();
        }
    }

    static void Print(TraceEvent data)
    {
        Console.WriteLine(data.ToString());
    }
}
```

## more

- https://adamsitnik.com/Hardware-Counters-ETW/
- https://www.infoworld.com/article/2980677/implement-a-simple-logger-in-csharp.html