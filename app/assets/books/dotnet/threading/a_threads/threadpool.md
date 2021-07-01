# ThreadPool

Briefs jobs. Few threads do many tasks

Thread start = ~ μs init (private local variable stack..)
Each thread consumes (by default) ~ 1 MB of memory

Thread pool 
    cuts overheads by sharing and recycling threads faster
    Count number of worker threads that will run simultaneously
    Too many active threads throttle OS so after a limit jobs queue up and start only when another finishes. 

There are a number of ways to enter the thread pool:
Via the Task Parallel Library (from Framework 4.0)
By calling ThreadPool.QueueUserWorkItem (Task class a is replacement for)
Via asynchronous delegates
Via BackgroundWorker

* Cannot set the Name of a pooled thread, making debugging more difficult
* Pooled threads are always background threads 
* Blocking a pooled thread may trigger additional latency in the early life of an application unless you call ThreadPool.SetMinThreads 

### Thread Pool via TPL
Task class a replacement for ThreadPool.QueueUserWorkItem
Task<TResult> a replacement for asynchronous delegates

```c#
using System.Threading.Tasks;

static void Main()    
{
  Task.Factory.StartNew(Go); //returns a Task object used to monitor the task
  // wait for it to complete by calling its Wait()   
}
 
static void Go(string s="")
{
  Console.WriteLine ("Hello from the thread pool! " + s);
}
```

```c#
// Start the task executing. <string> would be inferred if we omitted it
  Task<string> task = Task.Factory.StartNew<string>( () => DownloadString ("http://www.linqpad.net") );
 
  // We can do other work here and it will execute in parallel:
  RunSomeOtherMethod();
 
  // When we need the task's return value, we query its Result property:
  // If it's still executing, THE CURRENT THREAD WILL NOW BLOCK (wait) until the task finishes:
  string result = task.Result;
}
 
static string DownloadString (string uri)
{
  using (var wc = new System.Net.WebClient())
    return wc.DownloadString (uri);
}
```

### Thread Pool without TPL

```c#
using System.Threading.Tasks;

static void Main()    
{  
  // Old way < .NET Framework 4.0
  ThreadPool.QueueUserWorkItem (Go);  // no easy mechanism for getting return values back
  ThreadPool.QueueUserWorkItem (Go, 123);
  WaitCallback callback = delegate (object state) { Fetch ((string)state); };
  ThreadPool.QueueUserWorkItem(callback, myUrl);
}
 
static void Go(string s="")
{
  Console.WriteLine ("Hello from the thread pool! " + s);
}
```

## Thread Pool Optimization

It starts out with one thread in its pool
Pool manager “injects” new threads according workload up to a maximum limit
After a sufficient period of inactivity, the pool manager may “retire” threads if it suspects that doing so will lead to better throughput.

ThreadPool.SetMaxThreads() set the upper limit of threads that the pool will create
32 768 in Framework 4.0 in a 64-bit environment
1023 in Framework 4.0 in a 32-bit environment
250 per core in Framework 3.5
25 per core in Framework 2.0

ThreadPool.SetMinThreads()
Pool manager will not delay allocation of threads until reaching the lower limit. Raising the minimum thread count improves concurrency when there are blocked threads 

## ThreadPool.BindHandle

Binds an operating system handle to the ThreadPool.
>public static bool BindHandle (IntPtr osHandle);

https://docs.microsoft.com/en-us/dotnet/api/system.threading.threadpool.bindhandle?view=net-5.0
https://www.codeproject.com/Articles/523355/Asynchronous-I-O-with-Thread-BindHandle