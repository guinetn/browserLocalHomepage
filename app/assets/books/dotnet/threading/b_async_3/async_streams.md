## ASYNC STREAMS = ASYNC ENUMERABLE

For continuous streams

The async/await is not so helpful if you want to consume (or produce) continuous streams of results, such as you might get from an IoT device or a cloud service. 
Async streams are there for that.

async and await were added to C# to deal with results that are not necessarily ready when you ask for them. They can be asynchronously awaited, and the thread can go do other stuff until they become available. But that works only for single values, not sequences that are gradually and asynchronously produced over time, such as for instance measurements from an IoT sensor or streaming data from a service.


using System.Threading.Tasks;
await Task.Delay(1000);  // simulate that GetNames does some asynchronous work by adding an asynchronous delay before the name is yield returned:

→ yield return name;    
→→ static async IEnumerable<string> GetNames()            // make it async
→→→ static async IAsyncEnumerable<string> GetNamesAsync()  // an asynchronous stream of strings

Foreach’ing over asynchronous streams requires explicit use of the await keyword:
❌ foreach (var name in GetNamesAsync()) {...}
✔️ await foreach (var name in GetNamesAsync()) {
    // Foreach's version taking an async stream and awaits every element
    // it can only do that in an async method
    // Note: C# 7.2 makes our Main method async: static async Task Main(string[] args)
}

