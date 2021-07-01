# Trees

- https://dev.to/edwardcashmere/binary-search-tree-javascript-and-python-22om
- https://dev.to/edwardcashmere/binary-search-tree-series-part-2-503k

Trees are another relation-based data structure, which specialize in representing hierarchical structures. Like a linked list, they’re populated with Node objects that contain a data value and one or more pointers to define its relation to immediate nodes.
Each tree has a root node that all other nodes branch off from. The root contains pointers to all elements directly below it, which are known as its child nodes. These child nodes can then have child nodes of their own. Binary trees cannot have nodes with more than two child nodes.
Any nodes on the same level are called sibling nodes. Nodes with no connected child nodes are known as leaf nodes.

A binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.

It is called a binary tree because each tree node has a maximum of two children.
It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.

The value of the key of the left sub-tree is less than the value of its parent (root) node's key. The value of the key of the right sub-tree is greater than or equal to the value of its parent (root) node's key.
The logic being lower value as compared to the parent node should always be on the left.


				     			Root node
		            			/ 
						parent node
		    		      /      \
depth of 2 →		   leaf     leaf       		← siblings
					    |
					  child
					  /   \


The most common application of the binary tree is a binary search tree. Binary search trees excel at searching large collections of data, as the time complexity depends on the depth of the tree rather than the number of nodes.

Binary search trees have four strict rules:

- The left subtree contains only nodes with elements lesser than the root.
- The right subtree contains only nodes with elements greater than the root.
- Left and right subtrees must also be a binary search tree. They must follow the above rules with the “root” of their tree.
- There can be no duplicate nodes, i.e. no two nodes can have the same value.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()

Advantages:
Good for representing hierarchical relationships
Dynamic size, great at scale
Quick insert and delete operations
In a binary search tree, inserted nodes are sequenced immediately.
Binary search trees are efficient at searches; length is only O(height).
Disadvantages:
Time expensive, O(logn), to modify or “balance” trees or retrieve elements from a known location
Child nodes hold no information on their parent node and can be hard to traverse backward
Only works for lists that are sorted. Unsorted data degrades into linear search.
Applications:
Great for storing hierarchical data such as a file location
Used to implement top searching and sorting algorithms like binary search trees and binary heaps
Common tree interview questions in Python
Check if two binary trees are identical
Implement level order traversal of a binary tree
Print the perimeter of a binary search tree
Sum all nodes along a path
Connect all siblings of a binary tree