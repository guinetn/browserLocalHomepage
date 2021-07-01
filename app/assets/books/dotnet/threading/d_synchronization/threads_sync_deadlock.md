
## MULTITHREADING ISSUE #2: DEADLOCKS

When two threads each hold a monitor that the other one wants. Each blocks, waiting for the monitor that it's waiting for to be released - and so the monitors are never released, and the application hangs 

Involve a minimum of two threads and a minimum of two resources (I think). The goal being to engineer a scenario in which the first thread has a lock on resource one, and is waiting for the lock on resource two to be released, whilst at the same time thread two holds a lock on resource two, and is waiting for the lock on resource one to be released.
 
```c#
object locker1 = new object();
object locker2 = new object();
 
new Thread (() => {
                    lock (locker1)
                    {
                      Thread.Sleep (1000);
                      lock (locker2);      // Deadlock
                    }
                  }).Start();
lock (locker2)
{
  Thread.Sleep (1000);
  lock (locker1);                          // Deadlock
} 
``` 