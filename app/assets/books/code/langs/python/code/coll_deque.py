# DEQUES

Queues are a linear data structure that store data in a “first-in, first-out” (FIFO) order. Unlike arrays, you cannot access elements by index and instead can only pull the next oldest element. This makes it great for order-sensitive tasks like online order processing or voicemail storage.

from collections import deque
# Initializing a queue
q = deque()
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty
Advantages:
Automatically orders data chronologically
Scales to meet size requirements
Time-efficient with deque class
Disadvantages:
Can only access data on the ends
Applications:
Operations on a shared resource like a printer or CPU core
Serve as temporary storage for batch systems
Provides an easy default order for tasks of equal importance
Common queue interview questions in Python
Reverse first k elements of a queue
Implement a queue using a linked list
Implement a stack using a queue




Circular linked lists in Python

Advantages:
Can traverse the whole list starting from any node
Makes linked lists more suited to looping structures
Disadvantages:
More difficult to find the Head and Tail nodes of the list without a null marker
Applications:
Regularly looping solutions like CPU scheduling

Common circular linked list interview questions in Python
Detect loop in a linked lists
Reverse a circular linked list
Reverse circular linked list in groups of a given size