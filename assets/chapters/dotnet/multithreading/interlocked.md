## memory models

Platform hardware optimize variable r/w by caching, regiters...
When you have access to shared data, make sure you read fresh data and write any changes back in a timely manner by using
- lock 
- volatile variables


## Volatility

Uses volatile reads and writes for all its accesses. 

Can be a reference type, byte, sbyte, short,ushort, int, uint, char, float, or bool, or an enumeration with a base type of byte, sbyte, short, ushort, int, or uint
For a reference type, only the access to the variable itself is volatile - if you write to something within the instance the reference refers to, that write won't be volatile.

```c#
using System;
using System.Threading;

public class Test
{
    static bool stop;
    
    static void Main()
    { 
        ThreadStart job = new ThreadStart(ThreadJob);
        Thread thread = new Thread(job);
        thread.Start();

        // Let the thread start running
        Thread.Sleep(2000);
        
        // Now tell it to stop counting
        stop = true;
    }
    
    static void ThreadJob()
    {
        int count = 0;
        while (!stop) // stop is not guaranteed
        {
            Console.WriteLine ("Extra thread: count {0}", count);
            Thread.Sleep(100);
            count++;
        }
    }
}
```

A fix:
```c#
static bool Stop
{
    get { lock (stopLock) { return stop; } }
    set { lock (stopLock) { stop = value; } }
}
Unfortunately there is no way of getting the compiler to complain if you access stop directly, so you do need to be careful to always use the property.
```

## Atomicity 

atomic operation is indivisible: nothing else can happen in the middle. With an atomic write, you can't have another thread reading the value half way through the write, and ending up "seeing" half of the old value and half of the new value. Similarly, with an atomic read, you can't have another thread changing the value half way through the read, ending up (again) with a value which is neither the old value nor the new value.

CLR guarantees that for types which are no bigger than the size of a native integer, 
reads and writes are atomic: if one thread is changing a properly aligned int variable's value from 0 to 5 and another thread is reading the variable's value, it will only ever see 0 or 5 - never 1 or 4, for instance. For a long, however, on a 32-bit machine, if one thread is changing the value from 0 to 0x0123456789abcdef, there's no guarantee that another thread won't see the value as 0x0123456700000000 or 0x0000000089abcdef.

if you use locking, you don't need to worry as you're already making sure that a read and a write can't overlap. If you use volatile variables there may be a slight chance of problems, as although every type which can be volatile can be atomically written and read, if the alignment of the variable is wrong, you could still get non-atomic reads and writes - the volatility doesn't provide any extra guarantees. Just another reason to use locking :)

## Interlocked

Writing code which needs to perform at its absolute fastest
Locking is a bit too much effort (and possibly too much of a performance hit) for doing very simple operations such as counting. 

Interlocked class performs atomic changes
- exchanges (optionally performing a comparison first)
Exchange and CompareExchange methods act on variables of type int, object or float
- increments and decrements
Increment and Decrement methods act on variables of type int or long.


```c#
using System;
using System.Threading;

public class Test
{
    static int count=0;
    
    static void Main()
    {
        ThreadStart job = new ThreadStart(ThreadJob);
        Thread thread = new Thread(job);
        thread.Start();
        
        for (int i=0; i < 5; i++)
        {
            Interlocked.Increment(ref count);
        }
        
        thread.Join();
        Console.WriteLine ("Final count: {0}", count);
    }
    
    static void ThreadJob()
    {
        for (int i=0; i < 5; i++)
        {
            Interlocked.Increment(ref count);
        }
    }
}
```
