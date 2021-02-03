## Span<T>

A new memory efficient type 
Isolated view of a part of a larger array without any memory operations
It is very useful for efficient parsing and other processing of large inputs.
Used to implement a new HttpClient class for better networking performance.

```cs
public struct Span<T> {
    internal ref T _pointer;
    internal int _length;
}
```

https://github.com/dotnet/corefxlab/blob/master/docs/specs/span.md


```cs
int value = int.Parse("123");
int value = int.Parse("content-length:123".Substring(15)); // this allocates a string
    
public struct Int32 {
    static bool TryParse(this ReadOnlySpan<char> text, out int value);
}
Int32.TryParse("content-length:123".AsReadOnlySpan().Slice(15), out int value);
```