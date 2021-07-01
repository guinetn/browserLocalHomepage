## Frugal Object

Application must have some collection optimized to store 0,1 or a little number of elements (JetBrainRider, VisualStudio have them): this save memory footprint from list with single elements: don't allocate real list until number of elements is more that 1.
 
**Problem:** We need to store efficiently set of data that can take various forms.
**Solution:** Instead of creating an object for each form separately, create kind of *discriminated union*.
**Benefits:** (Sometimes) smaller memory usage and better data locality. Better JIT optimizations - bound checks etc.
**Consequences:** Sometimes more complex API comparing to the plain approach. Some performance overhead due to type checks and/or additional wrappers.

Ex: jetbrain CompactList<T>
- https://twitter.com/korifey_ad/status/1168843280982917120

```cs
public struct CompactList<T>:IEnumerab1e<T>
{
   internal static readonly List<T> SingleMarker = new List<T>(); 
   private T mySing1eValue; 
   // or or 
   private List<T> myMu1tip1eVa1ues; 
}
```

ASP.NET Core example

```cs
/// Represents zero/null, one, or many strings in an efficient way.
public readonly struct StringValues : IList<string>, ...
{
	private readonly object _values;	
	...
	public string this[int index]
	{
		[MethodImpl(MethodImplOptions.AggressiveInlining)]
		get
		{
			var value = _values;
			if (index == 0 && value is string str)
			{
				return str;
			}
			else if (value != null)
			{
				// Not string, not null, can only be string[]
				return Unsafe.As<string[]>(value)[index]; // may throw
			}
			else
			{
				return OutOfBounds(); // throws
			}
		}
	}
}
```


Frugal objects - WPF example

```cs
// These classes implement a frugal storage model for lists of type <T>.
// Performance measurements show that Avalon has many lists that contain
// a limited number of entries, and frequently zero or a single entry.
...
// The code is also structured to perform well from a CPU standpoint. Perf
// analysis shows that the reduced number of processor cache misses makes
// FrugalList faster than ArrayList or List<T>, especially for lists of 6
// or fewer items. Timing differ with the size of <T>.
```

```cs
internal sealed class SingleItemList<T> : FrugalListBase<T>
{
  public override T EntryAt(int index)
  {
    return _loneEntry;
  }
  ...
  private T _loneEntry;
}
	

internal sealed class ThreeItemList<T> : FrugalListBase<T>
{
  public override T EntryAt(int index)
  {
    switch (index)
    {
		case 0:
			return _entry0;

		case 1:
			return _entry1;

		case 2:
			return _entry2;

		default:
			throw new ArgumentOutOfRangeException(nameof(index));
	}
  }
  ...
  private T _entry0;
  private T _entry1;
  private T _entry2;
}
```
Frugal objects - WPF example

```cs
internal class FrugalObjectList<T>
{
  public T this[int index]
  {
    get
    {
      // If no entry, default(T) is returned
      if ((null != _listStore) && ((index < _listStore.Count) && (index >= 0)))
      {
        return _listStore.EntryAt(index);
      }
      throw new ArgumentOutOfRangeException(nameof(index));
    }
    set
    {
	  ...
    }
  }
  internal FrugalListBase<T> _listStore;
}
```