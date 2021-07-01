# GARBAGE COLLECTOR

.NET’s Garbage Collector (GC) implements many performance optimizations. One of them, the generational model assumes that young objects die quickly, whereas old live longer. This is why managed heap is divided into three Generations. We call them Gen 0 (youngest), Gen 1 (short living) and Gen 2 (oldest). New objects are allocated in Gen 0. When GC tries to allocate a new object and Gen 0 is full, it performs the Gen 0 cleanup. So it performs a partial cleanup (Gen 0 only)! It is traversing the object’s graph, starting from the roots (local variables, static fields & more) and marks all of the referenced objects as living objects.



GC will handle above situations: 
- If program ends GC automatically reclaims all the memory occupied by the objects in the program.
- GC keeps tracks of all the objects and ensures that each object gets destroyed once.
- GC ensures that objects, which are being referenced, are not destroyed.
- GC destroys the objects only when necessary. Some situations of necessity are memory is exhausted or user explicitly calls System.GC.Collect() method. 

GC is a .net framework thread, which runs when needed or when other threads are in suspended mode. 
1. GC creates the list of all the objects created in the program by traversing the reference fields inside the objects. This list helps the GC to know how many objects it needs to keep track. 
2. GC ensures that there are no circular references inside this list. In this list GC then checks for all the objects, which have destructor, declared and place them in another list called Finalization List. 
3. Now GC creates two threads 
- one is a reachable list
Reachable objects are cleared one by one from the list and memory occupied by these objects are reclaimed back. 
- one is an unreachable (finalization List)
Reads the finalization lists and calls, the each object finalized in separate object. 


// Check the memory before...
long memoryBefore = GC.GetTotalMemory(true);
...
GC.GetTotalMemory(true);
// Check the memory after ...
long memoryAfter = GC.GetTotalMemory(false);
Console.WriteLine("Memory Used With Iterator = \t" + string.Format(((memoryAfter - memoryBefore) / 1000).ToString(), "n") + "kb");

.NET’s Garbage Collector (GC) implements many performance optimizations. One of them, the generational model assumes that young objects die quickly, whereas old live longer. This is why managed heap is divided into three Generations. We call them Gen 0 (youngest), Gen 1 (short living) and Gen 2 (oldest). New objects are allocated in Gen 0. When GC tries to allocate a new object and Gen 0 is full, it performs the Gen 0 cleanup. So it performs a partial cleanup (Gen 0 only)! It is traversing the object’s graph, starting from the roots (local variables, static fields & more) and marks all of the referenced objects as living objects.

This is the first phase, called “mark”. This phase can be nonblocking, everything else that GC does is fully blocking. GC suspends all of the application threads to perform next steps!

Living objects are being promoted (most of the time moved == copied!) to Gen 1, and the memory of Gen 0 is being cleaned up. Gen 0 is usually very small, so this is very fast. In a perfect scenario, which could be a web request, none of the objects survive. All allocated objects should die when the request ends. So GC just sets the next object pointer to the beginning of Gen 0. After some Gen 0 collections, we get to the situation, when Gen 1 is also full, so GC can’t just promote more objects to it. Then it simply collects Gen 1 memory. Gen 1 is also small, so it’s fast. Anyway, the Gen 1 survivors are being promoted to Gen 2. Gen 2 objects are supposed to be long living objects. Gen 2 is very big and it’s very time-consuming to collect its memory. So garbage collection of Gen 2 is something that we want to avoid. Why? let’s take a look at the following video to find out how the Gen 2 collection can affect user experience:

## Large Object Heap (LOH)
When GC is promoting objects to next generation it’s copying the memory. As you can imagine, it would be very time-consuming for large objects like big arrays or strings. This is why GC has another optimization. Any object that is bigger than 85 000 bytes is considered to be large. Large objects are stored in a separate part of the managed heap, called Large Object Heap (LOH). This part is managed with free list algorithm. It means that GC has a list of free segments of memory, and when we want to allocate something big, it’s searching through the list to find a feasible segment of memory for it. So large objects are by default never moved in memory. However, if you run into LOH fragmentation issues you need to compact LOH. Since .NET 4.5.1 you can do this on demand.

## More
- https://adamsitnik.com/Array-Pool/
- https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals
- https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/large-object-heap
