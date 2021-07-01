## WaitHandle

The handle can be in an
* signaled/set state (free): handle.set() 
* non-signaled/reset state (not free): handle.reset()
handle ~ doors opened (signaled/set state) or closed (non-signaled/reset state)

|Wait...||
|---|---|
|Handle.WaitOne() | waits for the door to be opened so the thread can "go through it"|
|WaitHandle.WaitAny([handle]) | waits for any of the handles in a set to be free/signaled|
|WaitHandle.WaitAll([handle]) | waits for all of the handles in a set to be free/signaled|

WaitXXX() methods have overloads to specify 
* a timeout 
* whether or not to exit the "synchronization domain" (automatic thread handling)

Derived classes from WaitHandle: 
- AutoResetEvent
- ManualResetEvent
- Mutex

AutoResetEvent will reset (close) itself to the non-signalled state immediately after a call to WaitOne() - it's as if anyone going through the door closes it behind them. 

ManualResetEvent: the thread had to reset it (close the door) when you want to make calls to WaitOne() block again. 

Both classes can manually be set or reset at any time, by any thread, using the Set() and Reset() methods, and can be created in the signalled/set or non-signalled/reset state. (These methods return a boolean value saying whether or not they were successful)

## ManualResetEvent

```C#
using System;
using System.Threading;

class Test
{
    static void Main()
    {
        ManualResetEvent[] events = new ManualResetEvent[10]; 
        // 10 runners non-signalled will be started and sleep randomly
        // When a runner completes the race, it signals the event
        for (int i=0; i < events.Length; i++)
        {
            events[i] = new ManualResetEvent(false); // not signaled = free
            Runner r = new Runner(events[i], i);
            new Thread(new ThreadStart(r.Run)).Start();
        }
        
        // Wait for the winner
        int index = WaitHandle.WaitAny(events);        
        Console.WriteLine ("***** The winner is {0} *****", index);        
        // Wait for everyone to finish. 
        WaitHandle.WaitAll(events);
        Console.WriteLine ("All finished!");
    }
}

class Runner
{
    static readonly object rngLock = new object();
    static Random rng = new Random();
    
    ManualResetEvent ev;
    int id;
    
    internal Runner (ManualResetEvent ev, int id)
    {
        this.ev = ev;
        this.id = id;
    }
    
    internal void Run()
    {
        for (int i=0; i < 10; i++)
        {
            int sleepTime;
            // Not sure about the thread safety of Random...
            lock (rngLock)
            {
                sleepTime = rng.Next(2000);
            }
            Thread.Sleep(sleepTime);
            Console.WriteLine ("Runner {0} at stage {1}", id, i);
        }
        ev.Set();
    }
}
```

## AutoResetEvent 

if we'd used AutoResetEvent instead: call Set() on the winner event, as it would have been reset when we detected it being set with the call to WaitAny.
