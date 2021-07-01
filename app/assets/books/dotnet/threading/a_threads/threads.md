# Threads

Smallest code execution unit 
* Having its own memory stack (local variables are kept separate)
C# client program (Console, WPF, Windows Forms) starts in a single thread (the "main" thread) created automatically by the CLR, and is made multithreaded by creating additional threads ("workers" thread)

Share data between threads with
* a common reference to the same object instance
Threads share (heap) memory with other threads running in the same application
* static fields 
but it's not thread safe: one thread can be reading one as the other thread is writing... remedy is to obtain an exclusive lock while reading and writing to the common data... see 'locking/data races'
Processes are fully isolated from each other; threads have just a limited degree of isolation (stack).
  
***Context switching***
Process of unloading a thread state from the memory, remembering it, and reloading another thread. The more threads, the more switching, the more taxation on the work that should be done.
  
## Threads vs Processes

Each process provides the resources needed to execute a program. A process has a virtual address space, executable code, open handles to system objects, a security context, a unique process identifier, environment variables, a priority class, minimum and maximum working set sizes, and at least one thread of execution. Each process is started with a single thread, often called the primary thread, but can create additional threads from any of its threads.

Processes run in parallel on a computer and are fully isolated from each other
Threads run in parallel within a single process but have a limited degree of isolation
Threads share heap-memory with other threads running in the same application so one thread can fetch data in the background, while another thread can display the data as they arrives.
One or more threads run in the context of the process
  
## worker thread

Any thread other than the Main thread that does some 'work' on behalf of the application that spawned the thread. 'Work' could really mean anything, including waiting for some I/O to complete. The ThreadPool keeps a cache of worker threads because threads are expensive to create.
  
Worker threads are threads that should employ CPU for their work;
I/O threads (also called "completion port threads") should employ device drivers for their work and essentially "do nothing", only monitor the completion of non-CPU operations.
  
## Trading ways
***Thread: Long running tasks***
ThreadStart delegates starts your own threads
***ThreadPool: Briefs jobs***
* Directly
ThreadPool.QueueUserWorkItem
Task Parallel Library
* Indirectly
Asynchronous methods (xxx.BeginYYYY, BeginInvoke on a delegate)
Asynchronous delegates
BackgroundWorker
WCF, Remoting, ASP.NET, and ASMX Web Services application servers
System.Timers.Timer and System.Threading.Timer
PLINQ

## Thread.Sleep

Do Not Put the static Threads.Sleep(number of milliseconds / TimeSpan) in Production Code

Tell the operating system not to schedule any time slices to this thread until the given amount of time has passed. 

Makes the current thread sleep 

Thread.Sleep pauses the current thread for a specified period:
Thread.Sleep (TimeSpan.FromHours(2));  // sleep for 2 hours
Thread.Sleep (500);                     // sleep for 500 milliseconds
A thread waiting on a Sleep or Join is blocked and so does not consume CPU resources

* Thread.Sleep(0) 
- Relinquishes (abandon) the thread’s current time slice immediately, voluntarily handing over the CPU to other threads.
useful in production code for advanced performance tweaks
- Diagnostic tool for thread safety issues: bug if inserting Thread.Yield() anywhere in your code breaks the program
- Thread.Yield() does the same thing but only to threads running on the same processor.

## THREADS

Long running tasks

* start a task on a thread
* configure a thread
* pass data in both directions

local variables are private to a thread
references can be shared among threads, allowing them to communicate via common fields.

.Name       For debugging (Visual Studio display thread name in the Threads Window and Debug Location)

.IsAlive    Returns true until the point where the thread ends
            Once ended, a thread cannot restart
.Join()     Wait for another thread to end by calling its Join method
            Blocking methods: Sleep, Join, EndInvoke, Task.Wait
            
.IsBackground    query or change a thread’s background status 


.Priority       Set how much execution time it gets relative to other active threads in the OS
                enum ThreadPriority { Lowest, BelowNormal, Normal, AboveNormal, Highest }
                Elevating a thread’s priority doesn’t make it capable of performing real-time work, because it’s still throttled by the application’s process priority. To perform real-time work, you must also elevate the process priority using the Process class in System.Diagnostics (we didn’t tell you how to do this):

                using (Process p = Process.GetCurrentProcess())
                    p.PriorityClass = ProcessPriorityClass.High; // High = best for real-time applications
                
Thread.CurrentThread.IsThreadPoolThread     query if you’re currently executing on a pooled thread
Thread.CurrentThread    static property that gives currently executing thread

Thread constructor accept a ThreadStart delegate (indicates where execution should begin)
>public delegate void ThreadStart();
>public delegate void ParameterizedThreadStart (object obj); // To pass parameters
Start() runs the thread. It continues until its method returns, at which point the thread ends.

.ThreadState
![thread states](assets/books/dotnet/threading/a_threads/thread_state.png)

```c#
public static ThreadState SimpleThreadState (ThreadState ts)
{
  return ts & (ThreadState.Unstarted |
               ThreadState.WaitSleepJoin |
               ThreadState.Stopped);
}
```


```c#
using System;
using System.Threading;

class ThreadTest
{
  static void Main()
  {
    Thread t = new Thread(WriteY);  // Kick off a new thread, No need to explicitly use ThreadStart
    t.Start();                      // running WriteY()
    
    Thread tAnonym = new Thread (delegate() { Console.WriteLine ("Hello!") }).Start(); // anonymous method
    
    Thread tLambda = new Thread ( () => Console.WriteLine ("Hello!") ); // a lambda expression 
    tLambda.Start();
    
    // Multi-statement lambda
    Thread tMLambda =new Thread (() => { 
        Console.WriteLine ("I'm running on another thread!");
        Console.WriteLine ("This is so easy!");
        }).Start();
      
    // Simultaneously, do something on the main thread.
    for (int i = 0; i < 1000; i++) Console.Write ("x");
  }
 
  static void WriteY()
  {
    for (int i = 0; i < 1000; i++) Console.Write ("y");
  }
}
```

Foreground and Background Threads
By default, threads you create explicitly are foreground threads. Foreground threads keep the application alive for as long as any one of them is running, whereas background threads do not. Once all foreground threads finish, the application ends, and any background threads still running abruptly terminate.
A thread’s foreground/background status has no relation to its priority or allocation of execution time.

```c#
class ThreadNaming
{
  static void Main()
  {
    Thread.CurrentThread.Name = "main";
    Thread worker = new Thread (Go);
    worker.Name = "worker";
    worker.Start();
    Go();
  }
 
  static void Go()
  {
    Console.WriteLine ("Hello from " + Thread.CurrentThread.Name);
  }
}
```



```C#
static void Main() 
{
  new Thread(Go).Start();      // Call Go() on a new thread
  Go();                         // Call Go() on the main thread
}
 
static void Go()
{
  // Declare and use a local variable - 'cycles'
  for (int cycles = 0; cycles < 5; cycles++) Console.Write ('?');
}
```

Passing parameters to the thread
```c#
static void Main()
{
  Thread t = new Thread( () => Print ("Hello from t!") );
  t.Start();
  
  Thread t2 = new Thread (Print);
  t2.Start("Hello from t!");
  
  // Lambda expression is the most powerful way to pass data to a thread
  // But variables are shared: i variable refers to the same memory location throughout the loop’s lifetime
  for (int i = 0; i < 10; i++)
    new Thread (() => Console.Write (i)).Start();  // nondeterministic: 0223557799
    
  // Fix:
  for (int i = 0; i < 10; i++)
  {
    int temp = i; // temp is now local to each loop iteration. Therefore, each thread captures a different memory location
    new Thread (() => Console.Write (temp)).Start();
  }
}
 
static void Print (string message) 
{
  Console.WriteLine (message);
}
```

```c#
using System;
using System.Threading;

public class Test
{
    static void Main()
    {
        ThreadStart job = new ThreadStart(ThreadJob);
        Thread thread = new Thread(job);
        thread.Start();
        // new Thread(new ThreadStart(ThreadJob)).Start();   // shortcut
                
        Thread paramThread = new Thread(new ParameterizedThreadStart(makeDouble));
        paramThread.Start(100);
 
        for (int i=0; i < 5; i++)
        {
            Console.WriteLine ("Main thread: {0}", i);
            Thread.Sleep(1000);
        }
    }
    
    static void ThreadJob()
    {
        for (int i=0; i < 10; i++)
        {
            Console.WriteLine ("Other thread: {0}", i);
            Thread.Sleep(500);
        }
    }
    static int makeDouble(int value) {         
        Console.WriteLine ("makeDouble: {0}", value *2);            
    }
}
```

```c#

```


```C#
using System;
using System.Threading;

public class Test
{
    static void Main()
    {
        Counter classInstance = new Counter();
        ThreadStart job = new ThreadStart(classInstance.Count);
        Thread thread = new Thread(job);
        thread.Start();
        
        for (int i=0; i < 5; i++)
        {
            Console.WriteLine ("Main thread: {0}", i);
            Thread.Sleep(1000);
        }
    }
}

public class Counter
{
    public void Count()
    {
        for (int i=0; i < 10; i++)
        {
            Console.WriteLine ("Other thread: {0}", i);
            Thread.Sleep(500);
        }
    }
}

```

## Exception Handling

You need an exception handler on all thread entry methods
try/catch/finally blocks in scope when a thread is created are of no relevance to the thread when it starts executing

```c#
public static void Main()
{
  try
  {
    new Thread (Go).Start();
  }
  catch (Exception ex)
  {
    // We'll never get here!
    Console.WriteLine ("Exception!");
  }
}
 
static void Go() { throw null; }   // Throws a NullReferenceException
```

Fix is to move the exception handler into the Go method:
```c#
public static void Main()
{
   new Thread (Go).Start();
}
 
static void Go()
{
  try
  {
    // ...
    throw null;    // NullReferenceException will get caught below
    // ...
  }
  catch (Exception ex)
  {
    // Log exception, and/or signal another thread
  }
}
```