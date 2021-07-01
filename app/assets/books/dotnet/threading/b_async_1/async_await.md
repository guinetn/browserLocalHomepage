## ASYNC AWAIT

C# 5.0
To simplify using the TPL (Task Parallel Library)
To deal with results that are not necessarily ready when you ask for them. They can be asynchronously awaited, and the thread can go do other stuff until they become available. 

Lets you consume (and produce) asynchronous results in straightforward code, without callbacks:

We need to `Task-ify` our methods: put a keyword 'await' before every method call

```cs
using System.Threading.Tasks;
await Task.Delay(1000);  // asynchronous delay = simulate some asynchronous work
```

```cs
async Task<int> GetBigResultAsync()
{
    var result = await GetResultAsync();
    // we don’t know which thread will continue to run the rest of the code after the await statement
    // we might be running the rest of this code on different thread ~ optimization
    if (result > 20) return result; 
    else return -1;
}
```

***The continuation*** 
Is the code that follows an await statement. Pass data to it with the heap. C# compiler transforms it into a special structure that captures the data and methods being called. Asynchronous code consists of continuations.

If this is another thread, we can pass data only via objects allocated on the managed heap. For an await it will generate a state machine, a simple struct that will capture all the data needed to run the continuation (the code after await). 

An async state machine:
```cs
[CompilerGenerated]
[StructLayout(LayoutKind.Auto)]
private struct \u003CAsyncModeCopyToAsync\u003Ed__135 : IAsyncStateMachine
{
    // fields with state omitted
}

public interface IAsyncStateMachine { 
    MoveNext()	                            Moves the state machine to its next state.
    SetStateMachine(IAsyncStateMachine)	    Configures the state machine with a heap-allocated replica.
}
```

It's a struct (stack instantiated: cheap+fast). If the continuation is run on another thread, we cannot use the struct as we cannot pass the stack from one thread to another. ***THE ONLY WAY TO DO IT, IT’S TO PUT IN ON THE HEAP***
As the state structure implements the IAsyncStateMachine interface, we can cast the struct to the interface (boxing = go on the heap). With this boxed value, it can be passed to another thread.
 
await = continuation on another thread using a struct state machine boxed so it can to be inter-threads passed 

Async/Await is not so helpful if you want to consume (or produce) continuous streams of results, such as you might get from an IoT device or a cloud service. Async/await works only for single values, not sequences that are gradually and asynchronously produced over time, such as for instance measurements from an IoT sensor or streaming data from a service. ***Async streams are there for that***

- https://blog.scooletz.com/2018/05/14/task-async-await-valuetask-ivaluetasksource-and-how-to-keep-your-sanity-in-modern-net-world/