# MEMORY ALLOCATION

Writing allocation free code in C#
Performance is a feature 

More allocations = garbage collections = more pauses disrupting the throughput
Better throughput = smoother code (not faster), good for low latency

Trend: improving performance by reducing the amount of memory that you allocate 

Reference and value types in relation to memory allocation to explain the performance issues 

***REFERENCE TYPES***
class keyword 
Allocated on heap 
A variable for a reference type is a reference to the thing on the heap 
Passed around by reference 
Assignment is a copy of the reference, not the object 

***VALUE TYPES***
struct keyword 
Allocated on stack (or embedded into a object)
A variable for a value type is the value itself, e.g. integer, 3D point. etc. 
Passed around by value (i.e. copied) 
Assignment is a copy of the whole value 


***Object reuse***
Reuse of same object instead of new initialization allocation
Pass in existing array rather than allocate new one, polling...
***StringBuiler***
Pre-allocate length if possible

***params args***: introduce overloads with common number of args
f("a","b") is compiled to f(new[]{"a","b"}) event if empty
Newer compilers do a f(Array.Empty<T>())

***Boxing***: introduce generic overloads

Boxing: When the data moves from value types to reference types
UnBoxing: When the data moves from reference types to value types

- Passing value types to method expecting a reference type
- Creates a new object on the heap (box) that contains a copy of the value type
- Any changes to the boxed value doesn't affect the original

Compiler rewrite things:
static void f(int age) { 
    Console.WriteLine("I'm {0}", age);  // Boxing allocation conversion by compiler!
}

***Closures***: avoid in critical paths. Pass state as arg to lambda, investigate local function
Compiler rewrite things:
Capture local variables in a new class (and lambda rewritten as method on this class)

***Linq***: avoid in critical paths. Use good old foreach/if
- use a lot of closures
- is based on lot of static method allocating Enumerator class
Heap allocation viewer can show this

***Iterators***: return a collection has a cost.
Code is rewritten into a state machine that is allocated
foreach(var m in GetMsg()) {... object allocation iterator method call ...}
static IEnumerator<string> GetMsg(){
    yield return "hi";
    yield return "world";
}

***async/await***: investigate ValueTask
Code is rewritten into a state machine that is allocated
More allocations for Task & Task<T>, cannot be reused

Can use TaskValue for common uses cases
ValueTask: a value type which represents the task and it's it's great then for some of these use cases where you want to be able to reuse items where you also want to be able to return synchronously without having to allocate something 


### Reference semantics with value types (C# 7.2)

Allocating a reference type has a cost (GC), but passing it around is cheap 
Allocating a value type is cheap, but passing it around has a cost (gets copied)
***Why can't it be cheap to allocate ANP cheap to pass around? 
That's reference semantics does***

* Allows value types to be used like reference types 
Pass by reference everywhere 
* Use value types to reduce allocations, reduce memory trafic, etc. 
Throughput 
* Pass by reference to avoid copies, enable modifying, etc. 
* Very low level micro-optimisations... 
But they'll be used in the platform...
(And game and parsing, and serialisation, and...) 

C#7.0 ref return
`ref` locals and `ref` returns (C# 7.0) 
ref var location = ref enemy.GetLocationByRef();

* Return a reference to value type, not a copy of the value 
Return type of method becomes e.g. integer reference inte in IL 
* Lifetime of returned value must exceed the lifetime of the called method 
E.g. a reference to a field or method argument. NOT a variable in the callod method. 
Not allow•ed on async methods 
* Modifying this reference is the same as modifying the original value 
E.g_ return reference to array clernent. and update it in place 
* Add ref modifier to method declaration return type, and to return statement 

C# 7.2:
* `in` parameters 
Pass value type by reference. Called method cannot modify original value
static void f(in int age) { ... }

* `ref readonly` returns 
Return a read only value type by reference (caller cannot modify it)
* `readonly struct `
Immutable value types 

* `ref struct` 
Stack only value types (can never be part of a reference type)
Declare a value type that can only be stack allocated 
This constrains lifetime to calling method 
Also, cannot be boxed, cannot use inside a non-ref struct 
Cannot use With async methods or iterators 
Cannet be a generic parameter 
Limited use cases 
Working With stackalloc memory 
Primarily for Span<T> 

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

New API and overloads in the BCL
String.AsSpan(), Stream.ReadAsync(), UTF8Parser.TryParse()
Significant usage of ref semantics - allocation free

Span<T>, ReadOnlySpan<T>, Memory<T>

using structs without creating lots of copies

class vs struct

System.ValueTuple (struct on the stack) not System.Tuple (ref)
IAsyncEnumerator (await foreach) + 





Micro-optimizations 
The managed memory is cheap (easy to allocate memory) but garbage collection is expensive (it stops the world it pauses everything has to do a lot of work then to clear everything up compact your memory down)






## MORE 

- https://www.youtube.com/watch?v=nK54s84xRRs&t=796s