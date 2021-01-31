# STACK

LIFO (Last In First Out)
System.Collection.Generic. Doesn't perform boxing-unboxing because it is generic.
Stack<T> and non-generic Stack collection classes
To store temporary data in LIFO style

Add Elements: Push(). Cannot use collection-initializer syntax.
Get Elements: Pop() / Peek() methods. It does not support an indexer.

Count	Returns the total count of elements in the Stack.
Push(T)	Inserts an item at the top of the stack.
Peek()	Returns the top item from the stack.
Pop()	Removes and returns items from the top of the stack.
Contains(T)	Checks whether an item exists in the stack or not.
Clear()	Removes all items from the stack.

```cs
Stack<int> myStack = new Stack<int>();
myStack.Push(1);
myStack.Push(2);
myStack.Push(3);
myStack.Push(4);

Console.Write("Number of elements in Stack: {0}", myStack.Count);
     
foreach (var item in myStack)
     Console.Write(item + ","); //prints 4,3,2,1, 

if(myStack.Count > 0){
     Console.WriteLine(myStack.Peek()); // prints 4
     Console.WriteLine(myStack.Peek()); // prints 4

myStack.Contains(2); // returns true
          
while (myStack.Count > 0)
     Console.Write(myStack.Pop() + ",");

Console.Write("Number of elements in Stack: {0}", myStack.Count); 
     
int[] arr = new int[]{ 1, 2, 3, 4};
Stack<int> myStack = new Stack<int>(arr);
foreach (var item in myStack)
     Console.Write(item + ","); //prints 4,3,2,1,      
```