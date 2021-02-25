## Span<T>

System.Memory NuGet package
using Systems
A new memory efficient value type 
Philosophy of no allocations and no data copies

Span<T> runtime type to work with slices of existing memory
- New type to unify working With any kind of contiguous memory 
Arrays, array segments, strings and substrinqs, native mernoty, stackalloc.. 
- Provides array-like API - indexer 
ReadOnlySpan<T> provides getter indexer only 
- Type safe - each element is of type T 
- Array-like performance 
Not quite, but newer runtimes have special suppo«t 
- Slicing 
Cteate a new Span<T> With a sub-section of existing Span - without allocations! 

It contains a length and a *managed pointer*, it cannot appear on the Managed Heap

```cs
public ref struct Span<T>
{
   * internal ref T _pointer;
   private int _length;
   ...
}
```
New API and overloads in the BCL
String.AsSpan(), Stream.ReadAsync(), UTF8Parser.TryParse()
Significant usage of ref semantics - allocation free

![](assets/books/dotnet/types/val/span01.png)]
![](assets/books/dotnet/types/val/span02.png)]
![](assets/books/dotnet/types/val/span03.png)]
Slicing is quite efficient because you don't need to allocate anything on the heap or copy any data when you're creating the new span.


C# 7.2 Ref struct: cannot be placed on the managed heap

There are some trade-offs to consider when determining where using span is beneficial. You should be using spans predominantly in synchronous, performance-sensitive code paths where you want to avoid excessive data copies and allocations. This includes any scenario that involves substantial string manipulation or buffer management, or where you previously had to rely on writing unsafe code to get pointer-like performance in your libraries and server applications. Due to its design as a ref-like type, span comes with the following set of restrictions that are enforced by the C# compiler and the core runtime:

Span can only live on the execution stack.
It cannot be used as a field in a class
Span cannot be used within asynchronous methods (await and yield boundaries)
Span cannot be boxed or put on the heap.
Span cannot be used as a generic type argument.
Span cannot be an instance field of a type that itself is not stack-only.


Span<T> represents a contiguous region of arbitrary memory
A ref struct that is allocated on the stack rather than on the managed heap. 
Isolated view of a part of a larger array without any memory operations
It is very useful for efficient parsing and other processing of large inputs.
Used to implement a new HttpClient class for better networking performance.

use Span<T> as an abstraction to uniformly represent arrays, strings, memory allocated on the stack, and unmanaged memory.
~ C# arrays with ability to create a view of a portion of the array without allocating a new object on the heap or copying the data. This feature is called 'slicing' and types with this feature are known as 'sliceable types'
Span promises type and memory safety with checks to avoid out-of-bounds access, but that type of safety comes with certain usage restrictions enforced by the C# compiler and runtime.
ReadOnlySpan<T> is the read-only flavor of Span<T> 

Spans are only a view into the underlying memory and aren't a way to instantiate a block of memory. Span<T> provides read-write access to the memory and ReadOnlySpan<T> provides read-only access. Therefore, creating multiple spans on the same array creates multiple views of the same memory.

Span<T> gains certain benefits because of these restrictions. These limitations enable efficient buffer access, safe and concrete lifetime semantics that are tied to stack unwinding, and they circumvent concurrency issues like struct tearing. To support the developer scenarios that cannot be addressed by span due to its usage constraints, .NET Core 2.1 also provides another type called Memory<T>.


Span has a constructor that accepts an array and there's an extension method on the array itself to support fluent interface (method chaining)

```cs
var array = new int[64];
Span<int> span1 = new Span<int>(array);
Span<int> span2 = new Span<int>(array, start: 8, length: 4);

Span<int> span3 = stackalloc[] { 1, 2, 3, 4, 5 };

IntPtr memory = Marshal.AllocHGlobal(64);
void* ptr = memory.ToPointer();
Span<byte> span4 = new Span<byte>(ptr, 64);

string str = "Hello world";
ReadOnlySpan<char> span5 = str.AsSpan();

var span6 = span.Slice(0, 4); // Zero-copy slicing:

int value = int.Parse("123");
int value = int.Parse("content-length:123".Substring(15)); // this allocates a string
  
public struct Int32 {
    static bool TryParse(this ReadOnlySpan<char> text, out int value);
}
Int32.TryParse("content-length:123".AsReadOnlySpan().Slice(15), out int value);
```

### Async-await problem
Span<char> cannot be declared in async methods or lambda expressions
Main concern - `async` methods with their *boxing* state machines

```cs
// Compile error: 
// "Parameters or locals of type 'Span<char>' cannot be declared in async methods or lambda expressions"
public async Task DoAsync(Span<char> data)
{
    Do(data.Slice(0, 10));
    await DoOtherAsync();
}
```

Use `Memory<T>` instead - general-purpose slicing of arrays, strings and ...

```cs
// Does compile - Span is not a local variable here!
public async Task DoAsync(Memory<char> data)
{
	DoSync(data.Span.Slice(0, 10));
	await DoOtherAsync();
}

private void DoSync(Span<char> data) => Console.WriteLine(data.Length);
```


```cs
public unsafe Span<byte> rocksdb_get_span(
	IntPtr db,
	IntPtr read_options,
	byte[] key,
	long keyLength,
	out IntPtr errptr,
	ColumnFamilyHandle cf = null)
{
	...
	var resultPtr = rocksdb_get(db, read_options, key, skLength, out UIntPtr valueLength, out errptr)
	...
	return new Span<byte>((void*)resultPtr, (int)valueLength);
}

public unsafe void dangerous_rocksdb_release_span(in Span<byte> span)
{
	ref byte ptr = ref MemoryMarshal.GetReference(span);
	IntPtr intPtr = new IntPtr(Unsafe.AsPointer(ref ptr));
	rocksdb_free(intPtr);
}
```

## SPAN and linguistic behavior 

.NET has adopted Span<T> as a first-class citizen (and ReadOnlySpan<char> as the convention for a cheap string slice), there are also consistency issues to deal with. All Span<T>-based extension methods (including extension methods that operate on ReadOnlySpan<char>) are ordinal by default, unless an explicit StringComparison has been provided. As developers begin using span-based code more frequently, the risk of mixing and matching linguistic and non-linguistic operations on the same text increases.

string str = GetString();
bool b1 = str.StartsWith("Hello"); // uses 'CurrentCulture' by default (search a string in a string)

ReadOnlySpan<char> span = str.AsSpan();
bool b2 = span.StartsWith("Hello"); // uses 'Ordinal' by default
This mismatch of expectations could cause developers to introduce latent bugs into their code bases.

string str = GetString();
if (str.StartsWith("Hello")) // This line produces warning CA1307.
...    

if (str.StartsWith("Hello", StringComparison.CurrentCulture)) // Explicit comparison specified, no warning produced.
...

Search a string in a string and search a char in a string are different: https://github.com/dotnet/runtime/issues/43956
## More 

- https://docs.microsoft.com/en-us/dotnet/api/system.span-1?view=net-5.0
- https://github.com/dotnet/corefxlab/blob/master/docs/specs/span.md
- https://www.codemag.com/article/1807051/Introducing-.NET-Core-2.1-Flagship-Types-Span-T-and-Memory-T
 