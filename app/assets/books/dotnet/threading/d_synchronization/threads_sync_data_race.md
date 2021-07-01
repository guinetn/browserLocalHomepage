## MULTITHREADING ISSUE #1: DATA RACES

Shared data is the primary cause of obscure behaviors in multithreading.

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
            count++;        
            /*
            1. Reads the current value of count
            2. Increments that number
            3. Writes the new value back to the count variable
            If one thread gets as far as reading current value, then other thread takes over
            */
        
        thread.Join(); // pauses main thread until the other thread has completed
        Console.WriteLine ("Final count: {0}", count); // isn't guaranteed to be 10
    }
    
    static void ThreadJob()
    {
        for (int i=0; i < 5; i++)        
            count++;        
    }
}    
```
