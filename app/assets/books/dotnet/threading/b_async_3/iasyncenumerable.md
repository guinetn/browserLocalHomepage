## IAsyncEnumerable<T>

Asynchronous version of IEnumerable<T>
The language lets you await foreach over these to consume their elements, and yield return to them to produce elements.

```cs
async IAsyncEnumerable<int> GetBigResultsAsync()
{
    await foreach (var result in GetResultsAsync())
    {
        if (result > 20) yield return result; 
    }
}
```
    