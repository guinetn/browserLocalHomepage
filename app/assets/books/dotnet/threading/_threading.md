
# MULTITHREADING

Parallel execution of code 
issues: DataRace & Deadlocks 

Improve multithreading with the task-based async pattern and C# 8.0 asynchronous streams
Enhance performance through the parallel processing of data and multithreading tasks
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

### Multithreading patterns
address the multithreading complexities of monitoring an asynchronous operation, thread pooling, avoiding deadlocks, and implementing atomicity and synchronization across operations and data access.

### Event-Based Asynchronous Pattern

### Dispatching to the Windows UI
One other important threading concept relates to user interface development using the System.Windows.Forms and System.Windows namespaces. The Microsoft Windows suite of operating systems uses a single-threaded, message-processing–based user interface. As a consequence, only one thread at a time should access the user interface, and code should marshal any alternative thread interaction via the Windows message pump. Fortunately, thanks to the fact that TAP uses the synchronization context when executing the continuation task, calls following an await expression call can freely invoke the UI API without concern for dispatching invocations to the UI thread. Unfortunately, in prior versions of C#, this was not the case. Instead, invoking a UI method on the UI thread required special invocation logic both for Windows Forms and for the Windows Presentation Framework API, as we discuss in the following sections.

- https://intellitect.com/interfacing-multithreading-patterns/ ***


### System.Threading Namespace

Provides classes and interfaces that enable multithreaded programming. 
In addition to classes for synchronizing thread activities and access to data (Mutex, Monitor, Interlocked, AutoResetEvent…)
ThreadPool class that allows you to use a pool of system-supplied threads

https://asyncexpert.com/
::::
download.page(dotnet/threading/backgroundworker.md)
::::
download.page(dotnet/threading/a_threads/_threads.md)
::::
download.page(dotnet/threading/b_async_1/_async_1.md)
::::
download.page(dotnet/threading/b_async_2/_async_2.md)
::::
download.page(dotnet/threading/b_async_3/_async_3.md)
::::
download.page(dotnet/threading/c_low-level-concurrency/_low-level-concurrency.md)
::::
download.page(dotnet/threading/d_synchronization/_synchronization.md)
::::
download.page(dotnet/threading/e_concurrent_structures/_concurrent_structures.md)
::::
download.page(dotnet/threading/f_misc/_misc.md)
::::

download.page(dotnet/threading/g_actor_model/orleans.md)
::::
download.page(dotnet/threading/g_actor_model/akka.net.md)
::::

![](assets/books/dotnet/threading/a_threads/threading.png)




## More
- https://docs.microsoft.com/en-us/dotnet/api/system.threading?view=dotnet-plat-ext-5.0
- http://www.albahari.com/threading/part3.aspx#_Apartments_and_Windows
- https://intellitect.com/legacy-system-threading/ ***
- https://intellitect.com/interfacing-multithreading-patterns/ ***
- https://www.codeproject.com/Articles/5278932/Synchronization-with-Visual-Cplusplus-and-the-Wind
