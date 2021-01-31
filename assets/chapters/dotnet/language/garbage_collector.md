# GARBAGE COLLECTOR

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