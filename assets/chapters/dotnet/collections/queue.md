# QUEUE

Enqueue items --> First In First Out --> Dequeue items

System.Collection.Generic (Doesn't perform boxing-unboxing because it is generic)
Queue<T> is FIFO (First In First Out) collection
Add Elements Enqueue(). Cannot use collection-initializer syntax
Get Elements Dequeue() / Peek() methods
No indexer support 

Enqueue(T)	Adds an item into the queue.
Dequeue	Returns an item from the beginning of the queue and removes it from the queue.
Peek(T)	Returns an first item from the queue without removing it.
Contains(T)	Checks whether an item is in the queue or not
Clear()	Removes all the items from the queue.
Count	Returns the total count of elements in the Queue.

```cs
Queue<int> callerIds = new Queue<int>();
callerIds.Enqueue(1);
callerIds.Enqueue(2);
callerIds.Enqueue(3);
callerIds.Enqueue(4);

foreach(var id in callerIds)
    Console.Write(id); //prints 1234
```

Find element
```cs
Queue<string> strQ = new Queue<string>();
strQ.Enqueue("H");
strQ.Enqueue("e");
strQ.Enqueue("l");
strQ.Enqueue("l");
strQ.Enqueue("o");

Console.WriteLine("Total elements: {0}", strQ.Count); //prints 5

if(strQ.Count > 0){
    Console.WriteLine(strQ.Peek()); //prints H
    Console.WriteLine(strQ.Peek()); //prints H

strQ.Contains('o'); // True
    
while (strQ.Count > 0)
    Console.WriteLine(strQ.Dequeue()); //prints Hello

Console.WriteLine("Total elements: {0}", strQ.Count); //prints 0
```
    