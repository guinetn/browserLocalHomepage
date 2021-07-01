## Tasks

System.Threading.Tasks

Before tasks → new Thread() or BackgroundWorker wrapper. 
Issues was using a CPU with 4 cores and you just started 5th thread, at least 2 of them were being executed on the same core (not efficient + led to a context switching)

With Task, instead of creating a thread for each of the tasks you want to run, you’d define a method that should be run. You pass a delegate that should be run and voila, it will just work.

C#5 async-await: To simplify using the TPL

### TPL - Task Parallel Library

### Task

Task
Task<TResult>
[System.Threading.Tasks.Task] | Get-Member
[System.Threading.Tasks.Task] | Get-Member -static

```cs
public class Task : IAsyncResult, IDisposable
```

```cs
public static void TaskWait_MaxInt32()
{
    Task t = Task.Delay(1);
    Debug.WriteLine("Wait with int.Maxvalue");
    Task.WaitAll(new Task[] { t }, int.MaxValue);
}
```


“promise”: object that represents the eventual completion of some operation
You initiate an operation and get back a Task for it, and that Task will complete when the operation completes, which may happen synchronously as part of initiating the operation (e.g. accessing some data that was already buffered), asynchronously but complete by the time you get back the Task (e.g. accessing some data that wasn’t yet buffered but that was very fast to access), or asynchronously and complete after you’re already holding the Task (e.g. accessing some data from across a network). Since operations might complete asynchronously, you either need to block waiting for the results (which often defeats the purpose of the operation having been asynchronous to begin with) or you need to supply a callback that’ll be invoked when the operation completes. In .NET 4, providing such a callback was achieved via ContinueWith methods on the Task, which explicitly exposed the callback model by accepting a delegate to invoke when the Task completed:

## More
- https://devblogs.microsoft.com/dotnet/understanding-the-whys-whats-and-whens-of-valuetask/
- https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task?view=net-5.0
- [Samples](https://github.com/dotnet/corefx/blob/master/src/System.Threading.Tasks/tests/MethodCoverage.cs)