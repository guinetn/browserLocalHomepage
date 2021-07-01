## Stack Based Data

**Problem:** We allocate a lot of small, temporary objects, which puts a high pressure on the GC.
**Solution:** We avoid using Manged Heap by utilizing various possibilities like: `structs`, `ref structs`, `stackalloc`.
**Benefits:** No GC overhead makes data processing much faster.
**Consequences:** Operating on the stack may be dangerous due to "uncatchable" `StackOverflowException`. Moreover, using the stack has its own cost of memory zeroing. 

* structs
	* good data locality
	* can be *enregistered* .green[:-)]
	* can be *boxed* .red[:-(]
	* we love `ValueTuple` or `ValueTask`
* stackalloc 
* ref structs
* fixed sized buffers


`stackalloc` operator allocates a block of memory on the stack:
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/stackalloc

```cs
stackalloc T[E]
```
where `T` must be an *unmanaged type* and `E` must be an expression of type `int`
PS. Doesn't have to be pinned.

```cs
unsafe 
{
	byte* ptr = stackalloc byte[128];
}
```

Or C# 7.0+:

```cs
Span<byte> span = stackalloc byte[128];
```
What about `StackOverflowException`?
```
RuntimeHelpers.EnsureSufficientExecutionStack()
```

*"ensures that the remaining stack space is large enough to execute **the average .NET Framework function**"*

```cs
[Benchmark]
public double VersionStructStackalloc()
{
	Span<DataStruct> data = stackalloc DataStruct[_itemsCount];
	for (int i = 0; i < _items.Count; ++i)
	{
		data[i].Age = _items[i].Age;
		data[i].Gender = Helper(_items[i].Description) 
		                 ? Gender.Female : Gender.Male;
	}
	return ProcessBatch(data);
}
```
```bash
|                  Method |       Mean |  Gen 0 | Gen 1 | Gen 2 | Allocated |
|------------------------ |-----------:|-------:|------:|------:|----------:|
|      VersionObjectArray | 1,384.1 ns | 0.9689 |     - |     - |    4056 B |
|   VersionClassArrayPool |   848.8 ns | 0.0076 |     - |     - |      32 B |
| VersionStructStackalloc |   538.9 ns |      - |     - |     - |         - |
```
* ~33% faster!
* Mostly, the cost of stack memory zeroing...

```cs
[Benchmark]
[LocalsInit(false)]
public double VersionStructStackallocEx()
{
	Span<DataStruct> data = stackalloc DataStruct[_itemsCount];
	for (int i = 0; i < _items.Count; ++i)
	{
		data[i].Age = _items[i].Age;
		data[i].Gender = Helper(_items[i].Description) 
		                 ? Gender.Female : Gender.Male;
	}
	return ProcessBatch(data);
}
```

```cs
[Benchmark]
*[LocalsInit(false)]
public double VersionStructStackallocEx()
{
	Span<DataStruct> data = stackalloc DataStruct[_itemsCount];
	for (int i = 0; i < _items.Count; ++i)
	{
		data[i].Age = _items[i].Age;
		data[i].Gender = Helper(_items[i].Description) 
		                 ? Gender.Female : Gender.Male;
	}
	return ProcessBatch(data);
}
```
```bash
|                    Method |       Mean |  Gen 0 | Gen 1 | Gen 2 | Allocated |
|-------------------------- |-----------:|-------:|------:|------:|----------:|
|        VersionObjectArray | 1,384.1 ns | 0.9689 |     - |     - |    4056 B |
|     VersionClassArrayPool |   848.8 ns | 0.0076 |     - |     - |      32 B |
|   VersionStructStackalloc |   538.9 ns |      - |     - |     - |         - |
| VersionStructStackallocEx |   475.2 ns |      - |     - |     - |         - |
```
* Again, ~10% faster.
* Using [LocalsInit.Fody](https://github.com/ltrzesniewski/LocalsInit.Fody) plugin for Fody code weaver: *"lets you control the value of the `localsinit` flag on methods. This is most useful to eliminate the zero-initialization of memory returned by `stackalloc`"*


Ref struct (aka *byref-like type*)

```cs
public ref struct RefBook
{
  public string Title;
  public string Author;
}
```
* a bunch of limitations:
* it cannot be a field of a class or struct (boxing!)
* it cannot be a static field
* it cannot be an array type element (boxing!)
* it cannot be *boxed* explicitly
* it cannot implement an interface 
* it cannot be a generic type argument
* it cannot be a local variable in `async` method
* it cannot be a part of *closure*
* everything **to not occur on the Managed Heap** so it **can contain *managed pointer***

So what does it give us?
* they are never *heap-allocated*
* fast allocation/deallocation guaranteed (stack/CPU)
* guaranteed no GC overhead - never leaks through boxing
* can contain *managed pointer*
* guaranteed safe thread access 
* only single thread can use it
* no need for any synchronization
* guaranteed lifetime
    * as long as you have it as local variable - for every subsequent call

It **can contain *managed pointer***, thus also `Span<T>`:

```cs
public ref struct RefData
{
  public int Id;
  public Span<byte> Data;
}
```

It can be a field of other *ref struct*:

```cs
public ref struct RefBook
{
   public string Title;
   public RefData Publisher;
}
```

It can be a local variable and method's argument (including *byref*):

```cs
public void Test(ref RefBook refBook)
{
	ref RefData refPublisher = ref refBook.Publisher;
}
```


Fixed size buffers

```cs
struct StructWithArray
{
  public char[] Text;
  public int F2;
  // other fields...
}
```
]

```cs
unsafe struct StructWithFixedBuffer
{
  public fixed char Text[128];
  public int F2;
  // other fields...
}
```
.center[![:scale 60%](assets/books/dotnet/cs/assets/hperf_stack_based_01.png)]
.center[![:scale 60%](assets/books/dotnet/cs/assets/hperf_stack_based_02.png)]

And we can `stackalloc` them! Or box in an array!


```cs
unsafe ref struct FileSystemEntry
{
  private fixed char _fileNameBuffer[NameBufferSize];
  private ReadOnlySpan<char> _fileName;
  ...

  public ReadOnlySpan<char> FileName
  {
    get
    {
      fixed (char* c = _fileNameBuffer)
      {
        Span<char> buffer = new Span<char>(c, NameBufferSize);
        _fileName = _directoryEntry.GetName(buffer);
      }
      return _fileName;
    }
  }
}
```