## SIGNALING

### Monitor.Wait - Monitor.Pulse - Monitor.PulseAll

Signaling between threads: a thread tells to another that something happens

The lock is a monitor (a reference object)

One thread calls ***Monitor.Wait(lock_ref_object)*** which 
- Block it
- Released (unlocks) the monitor you're waiting on but it needs to be reacquired before the thread will actually run (means blocking again until the thread which calls Pulse or PulseAll releases the monitor)
***ONLY REACQUIRING IT AFTER BEING WOKEN UP BY A CALL TO Pulse()***

...so the thread is blocked until another thread calls... 
* Monitor.Pulse(lock_ref_object) only wakes up a single waiting thread
* Monitor.PulseAll(lock_ref_object) wakes up all threads waiting on that monitor
That doesn't mean they'll all instantly start running, if multiple threads are woken up, they'll all try to acquire the monitor, which only one can have at a time

In order to call any of these three methods the thread has to own the monitor of the object reference it passes in as a parameter. 

Use Case: producer/consumer relationships
* producer pulses the lock when it adds an item to the list
* consumer thread takes items off the list until it's empty, then waits on a lock

```c#
using System;
using System.Collections;
using System.Threading;

public class Test
{
    static ProducerConsumer queue;
    
    static void Main()
    {
        queue = new ProducerConsumer();
        new Thread(new ThreadStart(ConsumerJob)).Start();
        
        Random rng = new Random(0);
        for (int i=0; i < 10; i++)
        {
            Console.WriteLine ("Producing {0}", i);
            queue.Produce(i);
            Thread.Sleep(rng.Next(1000));
        }
    }
    
    static void ConsumerJob()
    {
        // Make sure we get a different random seed from the first thread
        Random rng = new Random(1);
        // We happen to know we've only got 10 items to receive
        for (int i=0; i < 10; i++)
        {
            object o = queue.Consume();
            Console.WriteLine ("\t\t\t\tConsuming {0}", o);
            Thread.Sleep(rng.Next(1000));
        }
    }
}

public class ProducerConsumer
{
    readonly object listLock = new object();
    Queue queue = new Queue();

    public void Produce(object o)
    {
        lock (listLock)
        {
            queue.Enqueue(o);
            // We always need to pulse, even if the queue wasn't
            // empty before. Otherwise, if we add several items
            // in quick succession, we may only pulse once, waking
            // a single thread up, even if there are multiple threads
            // waiting for items.            
            Monitor.Pulse(listLock);
        }
    }
    
    public object Consume()
    {
        lock (listLock)
        {
            // If the queue is empty, wait for an item to be added
            // Note that this is a while loop, as we may be pulsed
            // but not wake up before another thread has come in and
            // consumed the newly added object. In that case, we'll
            // have to wait for another pulse.
            while (queue.Count==0)
            {
                // This releases listLock, only reacquiring it
                // after being woken up by a call to Pulse
                Monitor.Wait(listLock);
            }
            return queue.Dequeue();
        }
    }
}
```

You can have more than one consumer or producer in the above. 
Each produced object will only be consumed once, and will be consumed (almost) immediately if there are any consumers waiting for work.