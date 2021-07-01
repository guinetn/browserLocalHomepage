## HEAP VS STACK

### THE HEAP
- the managed memory where all objects are allocated (whenever you call new…)
- is general purpose memory (Lasts for the life of the application) 
- it not related or connected to any thread so it can be used to transfer some data between threads: One thread can allocate an object and pass it to another thread
- an object will be on the heap as long as it’s not collected by Garbage Collector

### THE STACK 
- is a block of memory for data required by methods 
- the stack has frames
- assigned to a specific thread (every thread has a limited size of its stack)
Each method pushes space onto the stack for local variables 
Pops the stack on method exit: stack allocation is for the lifetime of the method
Value types are the whole data, so live directly on the stack 
Stackalloc keyword allows creating blocks of memory on the stack
Allocation and cleanup is cheap. but limited space 
`var id = Guid.NewGuid();`  the value stored "in" the id is on the stack