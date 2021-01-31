### Lock - Monitor

Exclusive access to a resource to avoid data races issues
To limit access to a single thread at a time

Every object in .NET has a (theoretical) monitor associated with it. A thread can enter (or acquire) a monitor only if no other thread has currently "got" it. Once a thread has acquired a monitor, it can acquire it more times, or exit (or release) it. The monitor is only available to other threads again once it has been exited as many times as it was entered. If a thread tries to acquire a monitor which is owned by another thread, it will block until it is able to acquire it.

#### Lock

Faster than Mutex

```c#
class ThreadSafeClass 
{
  static bool done;
  static readonly object locker = new object();
 
  static void Main()
  {
    new Thread (Go).Start();
    Go();
  }
 
  static void Go()
  {
    lock (locker)
    {
      if (!done) { Console.WriteLine ("Go() is done"); done = true; }
    }
  }
}
```

#### Monitor

```c#
static void ThreadJob()
{
    // Lock
    static readonly object countLock = new object();   
    
    for (int i=0; i < 5; i++)
    {
        Monitor.Enter(countLock);
        count++;        
        Monitor.Exit(countLock);        
    }
 
    lock call automatically Monitor.Enter() and Monitor.Exit() with a try/finally block 
    lock (countLock)
    {          
        count++;                 
    }

```

### Monitor.TryEnter()
attempts to acquire a lock, but doesn't block (or only blocks for a given period of time) if the lock cannot be acquired.

### Wait, Pulse, PulseAll

download.chapter(dotnet/multithreading/spinlock_spinwait.md)