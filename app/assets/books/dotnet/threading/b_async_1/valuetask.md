## ValueTask

System.Threading.Tasks

ValueTask 
ValueTask<TResult> 

To improve asynchronous performance in common use cases where decreased allocation overhead is important.

A struct (stack) that wrap a TResult or a Task<TResult>
This means it can be returned from an async method
- If that method completes synchronously and successfully, nothing need be allocated: we can simply initialize this ValueTask<TResult> struct with the TResult and return that. 
- Only if the method completes asynchronously does a Task<TResult> need to be allocated, with the ValueTask<TResult> created to wrap that instance (to minimize the size of ValueTask<TResult> and to optimize for the success path, an async method that faults with an unhandled exception will also allocate a Task<TResult>, so that the ValueTask<TResult> can simply wrap that Task<TResult> rather than always having to carry around an additional field to store an Exception).

```cs
public readonly struct ValueTask<TResult>
{
    public ValueTask(Task task)
    public ValueTask(TResult result)
    
    public ValueTask(IValueTaskSource<TResult> source, short token)    // .Net Core 2.1
}
```

When we don't want an async method using the C# compiler trickery (await = continuation on another thread using a struct state machine boxed so it can to be inter-threads passed). 
Ex: want just return a value from a method having an asynchronous signature (returning Task) 
Then use `Task.FromResult()` to create the task artificially

ValueTask could be either created from 
- the value (the synchronous path: no await = another thread) 
- the task (unfortunately allocates memory as it’s a class)

```cs
public Task<int> GetIdAsync()
{
    return Task.FromResult(2);
}
```
Simple, does not create the whole async state machine magic but it allocates (Task is class). 
For fast code use `ValueTask` alternative signature:

```cs
public ValueTask<int> GetIdAsync()
{
    return new ValueTask(5);
}
```

This is the synchronous path. No IO, no network is called. What about these cases? What about the cases where you’d like to cover both: a fast non-allocating synchronous path and an asynchronous path but without allocating the Task. Is it possible? Not before .net core 2.1 and IValueTaskSource

```cs
public override ValueTask<int> ReadAsync(byte[] buffer, int offset, int count)
{
    try
    {
        int bytesRead = Read(buffer, offset, count);
        return new ValueTask<int>(bytesRead);
    }
    catch (Exception e)
    {
        return new ValueTask<int>(Task.FromException<int>(e));
    }
}
```

download.page(dotnet/threading/b_async_1/ivaluetasksource.md)

- https://github.com/dotnet/coreclr/blob/85374ceaed177f71472cc4c23c69daf7402e5048/src/System.Private.CoreLib/shared/System/Threading/Tasks/ValueTask.cs#L438
- https://devblogs.microsoft.com/dotnet/understanding-the-whys-whats-and-whens-of-valuetask/
- https://stackoverflow.com/questions/43000520/why-would-one-use-taskt-over-valuetaskt-in-c
- https://blog.scooletz.com/2018/05/14/task-async-await-valuetask-ivaluetasksource-and-how-to-keep-your-sanity-in-modern-net-world/