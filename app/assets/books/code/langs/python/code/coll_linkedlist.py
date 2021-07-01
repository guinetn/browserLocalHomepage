# Linkedlist


Linked lists are a sequential collection of data that uses relational pointers on each data node to link to the next node in the list.
Unlike arrays, linked lists do not have objective positions in the list. Instead, they have relational positions based on their surrounding nodes.
The first node in a linked list is called the head node, and the final is called the tail node, which has a null pointer.

Image Source: Author
Linked lists can be singly or doubly linked depending if each node has just a single pointer to the next node or if it also has a second pointer to the previous node.
You can think of linked lists like a chain; individual links only have a connection to their immediate neighbors but all the links together form a larger structure.
Python does not have a built-in implementation of linked lists and therefore requires that you implement a Node class to hold a data value and one or more pointers.


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3


Linked lists are primarily used to create advanced data structures like graphs and trees or for tasks that require frequent addition/deletion of elements across the structure.

Advantages:
Efficient insertion and deletion of new elements
Simpler to reorganize than arrays
Useful as a starting point for advanced data structures like graphs or trees
Disadvantages:
Storage of pointers with each data point increases memory usage
Must always traverse the linked list from Head node to find a specific element
Applications:
Building block for advanced data structures
Solutions that call for frequent addition and removal of data
Common linked list interview questions in Python
Print the middle element of a given linked list
Remove duplicate elements from a sorted linked list
Check if a singly linked list is a palindrome
Merge K sorted linked lists
Find the intersection point of two linked lists