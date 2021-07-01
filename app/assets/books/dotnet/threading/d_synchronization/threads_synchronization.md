# THREADS SYNCHRONIZATION

Coordinating the actions of threads for a predictable outcome
When threads access the same data

4 Synchronization categories

* Blocking methods
Wait for another thread to finish or for a period of time to elapse
Sleep, Join, EndInvoke, Task.Wait

Blocked thread
- execution is paused (Sleep, Join...)
- immediately yields its processor time slice
- consumes no processor time

    bool blocked = (someThread.ThreadState & ThreadState.WaitSleepJoin) != 0;

Thread blocks/unblocks = operating system performs a context switch = overhead ~ μs

Unblocking happens
- by the blocking condition being satisfied
- by the operation timing out (if a timeout is specified)
- by being interrupted via Thread.Interrupt
- by being aborted via Thread.Abort

Blocking vs spinning
Spinning is awaiting a condition by spinning in a polling loop that is a wasteful on processor time  and so gets allocated resources:
while (!proceed);
while (DateTime.Now < nextStartTime);
while (!proceed) Thread.Sleep (10);    // a hybrid blocking/spinning 

* Locking constructs
Limit the number of threads that can access a resouce/execute a section of code at a time.
Exclusive locking: allow one thread at a time, allow competing threads to access common data without interfering with each other
lock (Monitor.Enter/Monitor.Exit), Mutex, SpinLock
Nonexclusive locks: Semaphore, SemaphoreSlim, reader/writer locks

* Signaling constructs
A thread can pause until receiving a notification from another (avoid polling)
Event wait handles
Monitor’s Wait/Pulse 
Framework 4.0 introduces the CountdownEvent and Barrier classes.

* Nonblocking synchronization constructs
Protect access to a common field by calling upon processor primitives
Thread.MemoryBarrier
Thread.VolatileRead
Thread.VolatileWrite
volatile keyword
Interlocked class

download.page(dotnet/threading/g_actor_model/akka.net.md)
