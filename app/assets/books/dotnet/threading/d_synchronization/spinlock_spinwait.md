## SpinLock and SpinWait

In multithreading, a brief episode of spinning is often preferable to blocking, as it avoids the cost of context switching and kernel transitions.

Structs = extreme optimization to avoid the cost of indirection and garbage collection. It means that you must not unintentionally copy instances 

## SpinLock 

Struct for high-concurrency scenarios when locking will be very brief (a spinlock contended for too long ~ms, it will yield its time slice, causing a context switch just like an ordinary lock)
Using an ordinary lock

```c#
var spinLock = new SpinLock (true);   // Enable owner tracking
bool lockTaken = false;
try
{
  spinLock.Enter(ref lockTaken);
  // Do stuff...
}
finally
{
  if (lockTaken) spinLock.Exit();
}
```

## SpinWait 

Struct for high-concurrency scenarios
Lock-free code that spins rather than blocks.
Implements safeguards to avoid the dangers of resource starvation and priority inversion that might otherwise arise with spinning.

```c#
bool _proceed;
void Test()
{
  SpinWait.SpinUntil (() => { Thread.MemoryBarrier(); return _proceed; });
  ...
}


bool _proceed;
void Test()
{
  // Spin until another thread sets _proceed to true:
  while (!_proceed) Thread.MemoryBarrier();
  ...
}
```