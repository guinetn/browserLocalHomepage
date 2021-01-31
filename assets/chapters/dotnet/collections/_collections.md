# COLLECTIONS

https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-5.0

Enumerable.Range(1, 5).Select(i => {})


## Non-generic Collections
***System.Collections***
|||
|---|---|
|ArrayList |	ArrayList stores objects of any type like an array. However, there is no need to specify the size of the ArrayList like with an array as it grows automatically|
|SortedList |	SortedList stores key and value pairs. It automatically arranges elements in ascending order of key by default. C# includes both, generic and non-generic SortedList collection|
|Stack |	Stack stores the values in LIFO style (Last In First Out). It provides a Push() method to add a value and Pop() & Peek() methods to retrieve values. C# includes both, generic and non-generic Stack|
|Queue |	Queue stores the values in FIFO style (First In First Out). It keeps the order in which the values were added. It provides an Enqueue() method to add values and a Dequeue() method to retrieve values from the collection. C# includes generic and non-generic Queue|
|Hashtable |	Hashtable stores key and value pairs. It retrieves the values by comparing the hash value of the keys|
|BitArray |	BitArray manages a compact array of bit values, which are represented as Booleans, where true indicates that the bit is on (1) and false indicates the bit is off (0)|

## Generic Collections
***System.Collections.Generic***
|||
|---|---|
| List<T> | Contains elements of specified type. It grows automatically as you add elements in it|
| Dictionary<TKey,TValue> | Contains key-value pairs|
| SortedList<TKey,TValue> | Stores key and value pairs. It automatically adds the elements in ascending order of key by default|
| Queue<T> | Stores the values in FIFO style (First In First Out). It keeps the order in which the values were added. It provides an Enqueue() method to add values and a Dequeue() method to retrieve values from the collection|
| Stack<T> | Stores the values as LIFO (Last In First Out). It provides a Push() method to add a value and Pop() & Peek() methods to retrieve values|
| Hashset<T> | Contains non-duplicate elements. It eliminates duplicate elements|

download.chapter(dotnet/collections/tuple.md)

download.chapter(dotnet/collections/ienumerable.md)

download.chapter(dotnet/collections/generics.md)

download.chapter(dotnet/collections/bitarray.md)

download.chapter(dotnet/collections/hashset.md)

download.chapter(dotnet/collections/arrays.md)

download.chapter(dotnet/collections/arrayslist.md)

download.chapter(dotnet/collections/list.md)

download.chapter(dotnet/collections/queue.md)

download.chapter(dotnet/collections/stack.md)

download.chapter(dotnet/collections/hashtable.md)

download.chapter(dotnet/collections/dictionary.md)

download.chapter(dotnet/collections/sortedlist.md)

download.chapter(dotnet/collections/lookup.md)

