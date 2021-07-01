# MUTEX

Machine wide lock ~ Monitor.Enter/Exit (ex: different windows console exe use the same lock). A thread in one process can wait for a thread in another process to release the mutex. 
Cross-process object - the same mutex can be used in many processes

|counter|number of times it's been acquired||
|---|---|---|
|0| no owner|it can be acquired by anyone|
|non-zero| owned by a thread||
||current owner can acquire it many times they like without blocking|
||other thread has to wait until the count becomes zero before they can acquire it|
|WaitXXX() | to acquire the mutex||
|ReleaseMutex()| thread's owner use it to decrease the count by one. Only the owner can decrease the count||


Mutex names should start with either 
- "Local\"  created in the local namespace: specific to the current user
- "Global\" created in the global namespace: shared with other users logged into the same machine
Should be unique name so you don't clash with other programs.


bool firstInstance;
Mutex(true, @"Global\John.Doe.MutexTestApp", out firstInstance);

When you construct a named mutex, you should be careful about making assumptions as to whether or not you will be able to acquire initial ownership of it. Fortunately, there is a constructor which allows the code to detect whether the system has created a whole new mutex or whether it's used an existing one. If the constructor requested initial ownership, it will only have been granted it if it created a new mutex - even if the existing mutex can immediately be acquired.

Principle use is detecting that another instance of an application is already running. Most don't need inter-process communication on this kind of level. The other use is to enable you to block until either one or all of a set of WaitHandles is released. For other purposes, where Monitor is good enough, I suggest using that - especially as C# has the lock statement specifically to support it. 
 
```c#
using System;
using System.Threading;

// Detecting a running application
class Test
{
    static void Main()
    {
        bool firstInstance;
        
        using (Mutex mutex = new Mutex(true, 
                                       @"Global\john.doe.MutexTestApp",
                                       out firstInstance))
        {
            if (!firstInstance)
            {
                Console.WriteLine ("Other instance detected; aborting.");
                return;
            }
            
            Console.WriteLine ("We're the only instance running - yay!");
            for (int i=0; i < 10; i++)
            {
                Console.WriteLine (i);
                Thread.Sleep(1000);
            }
        }
    }
}
```

Run the example in two different console windows - one will count to ten slowly; the other will abort after it detects that the other application instance is running.

using statement around the mutex: this should extend across the whole of the application's execution, otherwise another instance would be able to create a new mutex with the same name, after the old one had been destroyed. For instance, suppose you use a local variable without a using statement, like this:

Witout 'using' everything would probably work fine under debug, where the GC is very conservative about what it collects. When not running under the debugger, however, the GC can tell that the mutex variable isn't used after its initial assignment, so for the main duration of the app, it can be garbage collected at any time - and that destroys the mutex! The using statement shown earlier is only one way round this. You could make it a static variable instead, or use GC.KeepAlive(mutex); at the end of the method to make sure that the GC doesn't ignore the variable.
