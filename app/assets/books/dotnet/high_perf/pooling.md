# Pooling

Pool is a set of initialized objects that are ready to use. Instead of allocating a new object, we rent it from the pool.

**Problem:** There is a non-trivial cost of creating objects very often. This cost may be direct (allocation/initialization overhead), indirect (added GC overhead, fragmentation, ...) or both.
**Solution:** Instead of creating an object each time, reuse some objects from a pre-allocated pool.
**Benefits:** Smaller GC overhead, no allocation/initialization cost, better data locality.
**Consequences:** Trimming policy may be not trivial.

Array pooling:
ArrayPool<T> is a high performance pool of managed arrays. You can find it in [System.Buffers](https://www.nuget.org/packages/System.Buffers) package
"Use ArrayPool<T> for large arrays to avoid Full GC"
- https://adamsitnik.com/Array-Pool/  
- https://github.com/dotnet/corefx/blob/master/src/System.Buffers/src/System/Buffers/ArrayPool.cs

* instead of creating an array each time, reuse pooled array:
 ```cs
var pool = ArrayPool<int>.Shared;
int[] buffer = pool.Rent(minLength);
try
{
    Consume(buffer);
}
finally
{
    pool.Return(buffer);
}
```

* `Rent` returns an array with **at least** the specified length
* `Shared` instance has:
    * 17 buckets, with arrays of lengths: 16, 32, 64, 128, 256, 512, 1,024, 2,048, 4,096, 8,192, 16,384, 3,2768, 65,536, 131,072, 262,144, 524,288 and 1,048,576, each bucket contains maximum of 50 arrays
* they are created on demand
* **not cleared** when rented or returned (but `Return(T[] array, bool clearArray = false)`)
* **trimming mechanism** - explicit `Trim()` method

???

`ArrayPool<T>.Shared` uses `TlsOverPerCoreLockedStacksArrayPool<T>` class - there is a small per-thread cache of each array size and a cache shared by all threads split into per-core stacks (hence its name).

```cs
[Benchmark]
public double VersionObjectArray()
{
	DataClass[] data = new DataClass[_itemsCount];
	for (int i = 0; i < _itemsCount; ++i)
	{
		data[i] = new DataClass();
		data[i].Age = _items[i].Age;
		data[i].Gender = Helper(_items[i].Description) ? Gender.Female : Gender.Male;
	}
	return ProcessBatch(data);
}
```


```cs
[Benchmark]
public double VersionClassArrayPool()
{
	DataClass[] data = ArrayPool<DataClass>.Shared.Rent(_itemsCount);
	for (int i = 0; i < _itemsCount; ++i)
	{
		data[i] ??= new DataClass();
		data[i].Age = _items[i].Age;
		data[i].Gender = Helper(_items[i].Description) ? Gender.Female : Gender.Male;
	}
	double result = ProcessBatch(data, _itemsCount);
	ArrayPool<DataClass>.Shared.Return(data);
	return result;
}
```

```bash
|                Method |       Mean |  Gen 0 | Gen 1 | Gen 2 | Allocated |
|---------------------- |-----------:|-------:|------:|------:|----------:|
|    VersionObjectArray | 1,384.1 ns | 0.9689 |     - |     - |    4056 B |
| VersionClassArrayPool |   848.8 ns | 0.0076 |     - |     - |      32 B |
```

* abstract `MemoryPool<T>` - represents a pool of memory blocks
	* `MemoryPool<T>.Shared` - based on `ArrayPool`
	* `SlabMemoryPool : MemoryPool<byte>` - the memory pool behind Kestrel.
* Object pooling:
	* quite often not necessary - cost of handling outweighs benefits
		* maybe for heavy, costly in creation objects 
		* or tremendously often created
	* no standard implementation yet
		* internal [`ObjectPool<T>`](https://github.com/dotnet/roslyn/blob/master/src/Dependencies/PooledObjects/ObjectPool%601.cs) from Roslyn
		* ...
		* [Core support for object pooling](https://github.com/dotnet/coreclr/issues/23342) CoreCLR issue... is closed
