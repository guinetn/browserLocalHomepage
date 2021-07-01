## Memory<T>

Represents a contiguous region of memory (like Span<T>)
Unlike Span<T>, however, Memory<T> is not a ref struct. This means that Memory<T> can be placed on the managed heap, whereas Span<T> cannot. As a result, the Memory<T> structure does not have the same restrictions as a Span<T> instance. In particular:
* It can be used as a field in a class
* It can be used across await and yield boundaries.

In addition to Memory<T>, you can use System.ReadOnlyMemory<T> to represent immutable or read-only memory.