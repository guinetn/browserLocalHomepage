## IValueTaskSource

.NET Core 2.1
System.Threading.Tasks

mind blowing IValueTaskSource enables allocate even less for the asynchronous path…
To execute async-await code synchronous/asynchronous path without additional allocations
If you stick to regular async-await, soon, you’ll see some methods will change their signature from Task to ValueTask. 
 
.NET Core < 2.1: ValueTask could be either created from the value (the synchronous path) or the task, that unfortunately allocates memory as it’s a class

Socket class in .NET Core 2.1 has been ported to the IValueTaskSource approach bringing massive performance gains: a single socket can issue only a single send and a single receive at the same time (a call to the socket object). With this, only two objects implementing IValueTaskSource will be needed per socket, to provide same functionality, without any allocations. [socket implementation](https://github.com/dotnet/corefx/blob/master/src/System.Net.Sockets/src/System/Net/Sockets/Socket.Tasks.cs#L808-L1097)

```cs
public interface IValueTaskSource<TResult>
{
    ValueTaskSourceStatus GetStatus(short token);
    void OnCompleted(Action continuation, object state, short token, ValueTaskSourceOnCompletedFlags flags);
    TResult GetResult(short token);
}
```

```cs
public readonly struct ValueTask<TResult>
{
    public ValueTask(Task task)
    public ValueTask(TResult result)
    
    public ValueTask(IValueTaskSource<TResult> source, short token)    // .Net Core 2.1
    /* This constructor
     - requires no Task
     - depends on an interface to implement
    
    Objects implementing this interface can be pooled and returned to the pool as soon as the ValueTask is awaited. 
    
    token: ensures that the ValueTask won’t be used after your IValueTaskSource is returned to the pool. 
    value passed to every method of your implementation of IValueTaskSource which enables you to check, if the caller does not abuse your ValueTask    
    */
}
```

