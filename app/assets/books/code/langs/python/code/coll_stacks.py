# STACKS


dinner plates; you can add or remove plates to the top of the stack but must move the whole stack to place one at the bottom.

Stacks are a sequential data structure that acts as the Last-in, First-out (LIFO) version of queues. The last element inserted in a stack is considered at the top of the stack and is the only accessible element. To access a middle element, you must first remove enough elements to make the desired element at the top of the stack.


stack = []
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')
print(stack)
# pop() function to pop
# element from stack in 
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)
# uncommenting print(stack.pop())  
# will cause an IndexError 
# as the stack is now empty


Advantages:
Offers LIFO data management that’s impossible with *Applications:*s or arrays
Automatic scaling and object cleanup
Simple and reliable data storage system
Disadvantages:
Stack memory is limited
Too many objects on the stack leads to a stack overflow error
Applications:
Used for making highly reactive systems
Memory management systems use stacks to handle the most recent requests first
Helpful for questions like parenthesis matching
Common stacks interview questions in Python
Implement a queue using stacks
Evaluate a Postfix expression with a stack
Next greatest element using a stack
Create a min() function using a stack