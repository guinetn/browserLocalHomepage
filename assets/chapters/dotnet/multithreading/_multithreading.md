
# MULTITHREADING

Parallel execution of code 
issues: DataRace & Deadlocks 

## Use cases

* Responsive user interface
By running time-consuming tasks on a parallel “worker” thread, the main UI thread doesn't freeze and continue processing user inputs.
* Making efficient use of an otherwise blocked CPU
* Parallel programming
Intensive calculations are faster when workload is shared among multiple threads in a “divide-and-conquer” strategy
* Speculative execution
Improve performance by predicting something that might need to be done, and then doing it ahead of time (LINQPad speed up the creation of new queries). A variation is to run a number of different algorithms in parallel that all solve the same task. First “wins”
* Allowing requests to be processed simultaneously
Server client requests need to be handled in parallel

### Thread scheduler 
CLR delegates multithreading management to the OS
A thread scheduler ensures all active threads are allocated appropriate execution time, and that threads that are waiting or blocked (lock/user input) do not consume CPU time.

Single-processor: thread scheduler performs time-slicing (switch execution between  active threads: Windows time-slice ~ 10ms much larger than the CPU overhead in actually switching context between one thread and another (few-microseconds).

Multi-processor: mixture of time-slicing and genuine concurrency, where different threads run code simultaneously on different CPUs.

Preempted thread: interrupted execution due to an external factor such as time-slicing. In most situations, a thread has no control over when and where it’s preempted.


### System.Threading Namespace

Provides classes and interfaces that enable multithreaded programming. 
In addition to classes for synchronizing thread activities and access to data (Mutex, Monitor, Interlocked, AutoResetEvent…)
ThreadPool class that allows you to use a pool of system-supplied threads

::::
download.chapter(dotnet/multithreading/backgroundworker.md)
::::
download.chapter(dotnet/multithreading/threads.md)
::::
download.chapter(dotnet/multithreading/threadpool.md)
::::
download.chapter(dotnet/multithreading/threads_synchronization.md)
::::
download.chapter(dotnet/multithreading/plinq.md)
::::
download.chapter(dotnet/multithreading/tasks.md)
::::

![](assets/chapters/dotnet/multithreading/threading.png)

## More
- https://docs.microsoft.com/en-us/dotnet/api/system.threading?view=dotnet-plat-ext-5.0
- http://www.albahari.com/threading/part3.aspx#_Apartments_and_Windows

