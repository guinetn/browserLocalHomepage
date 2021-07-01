# DATA STRUTURES

![](assets/books/data/data_structures/types_of_data_structures.png)

download.page(data/data_structures/intervals.md)
download.page(data/data_structures/types/array.md)
download.page(data/data_structures/types/graphs.md)
download.page(data/data_structures/types/hash_table.md)
download.page(data/data_structures/types/heap.md)
download.page(data/data_structures/types/linked_list.md)
download.page(data/data_structures/types/queue.md)
download.page(data/data_structures/types/stack.md)
download.page(data/data_structures/types/tree.md)
download.page(data/data_structures/types/trie.md)


## primitive data structure
integer
float
double
character
string
boolean
pointer

## Non primitive data structures

record: group of primitive data

Linear
	list
	sets
	tuples
	queues
	stacks
	heaps
Non-Linear
	tree
	binarytree
	tables
	containers
Homogeneus
	2D arrays
	MultiDArrays
Heterogeneus
	LinkedList
	OrderedList
	UnOrderedList
Dynamic
	Dictionaries (hash) O(1) = linkedlist
	TreeSets
	Sequences

http://www.cs.otago.ac.nz/cosc242/lectures.php
https://medium.com/@binyamin/data-structures-and-big-o-notation-ec7ac060f186

# FUNDAMENTALS

most are position-oriented: i
But many simple tasks involve values, not positions; e.g. find Joe's phone number. Search trees are value-oriented, and so are hash tables.

### Arrays/Lists	Indexed elements
A group of related and equal sized variables can be stored one after another in a contiguous portion of the computer’s memory is known as an array.
Reading/Writing data in array takes constant time O(1)	
In most cases, the memory required to append a new value has already been allocated, which is strictly O(1)		
Expansion rate is cleverly chosen to be three times the previous size of the array; when we spread the expansion cost over each additional append afforded by this extra space
Inserting at an index is O(n): shift every subsequent element one position closer to the end. Deletion does the same.
Iteration: O(n)
slice [a:b] is O(k): iterate between indices a and b. k is the size of the slice
Deleting a slice is O(n) for the same reason that deleting a single element is O(n)
Sorting O(nlogn) 
	
|Operation|Big O Efficiency|
|---|---|
| index []			| O(1) |
| index assignment	| O(1) |
| append			| O(1) |
| pop()				| O(1) |
| pop(i)			| O(n) |
| insert(i, item)	| O(n) |
| del operator		| O(n) |
| iteration			| O(n) |
| contains (in)		| O(n) |
| get slice [x:y]	| O(k) |
| del slice			| O(n) |
| reverse			| O(n) |
| concatenate		| O(k) |
| sort				| O(nlogn) |
| multiply			| O(nk) |

Ordered List
add  require the traversal process
Unordered List
Adding an item to an unordered list will be O(1)

The members of a list are commonly refered to as nodes. 
singly linked list: each node holds a reference to the next node in the list
doubly linked list: each node holds a reference to both the next and previous nodes in the list

### Queues			FIFO	people waiting in line at the bank. 

Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
is_empty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the queue. It needs no parameters and returns an integer.

#### Priority queue

Logical order of items inside a queue is determined by their “priority”. Specifically, the highest priority items are retrieved from the queue ahead of lower priority items.
A data structure for specific algorithms such as Dijkstra’s shortest path algorithm
binary heap data structure implements a priority queue and allow to enqueue/dequeue items in O(logn)
 
### Deques/Linked List
double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. Likewise, existing items can be removed from either end. In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.
Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
add_front(item) adds a new item to the front of the deque. It needs the item and returns nothing.
add_rear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
remove_front() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
remove_rear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
is_empty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the deque. It needs no parameters and returns an integer.

Ex: Palindrome Checker
radar, toot, madam
remove both of them directly, we can compare them and continue only if they match. If we can keep matching first and the last items, we will eventually either run out of characters or be left with a deque of size 1 depending on whether the length of the original string was even or odd. In either case, the string must be a palindrome.

### Stacks 			LIFO 	pile of plates (Pringles tube of chips potatoes)
An ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the “top”, and the opposite end is known as the “base”.
Insertion order is the reverse of the removal order.

Stacks, queues, deques, and lists are data collections with items ordered according to how they are added or removed. Once an item is added, it stays in the same position relative to its neighbors. Because of this characteristic, we call these collections linear data structures.

Fundamental operations
	push(element)	Adding new elements at the top of the stack
	pop()			Removing/Returning element from the top of the stack
	peek()/top()	Returns a reference to the top element of the stack
	is_empty()		Returns Boolean true is the stack has no elements
	len() 			Returns the number of elements in the stack
	size()
						
Ex: Infix/Prefix/Postfix/ expression
Parentheses gone
Ooperators are no longer ambiguous with respect to the operands that they work on. Only infix notation requires the additional symbols. The order of operations within prefix and postfix expressions is completely determined by the position of the operator and nothing else. In many ways, this makes infix the least desirable notation to use.
https://bradfieldcs.com/algos/stacks/infix-prefix-and-postfix-expressions/
						
| Infix expression | Prefix expression | Postfix expression|
|---|---|
| A + B	    |+ A B	     | A B +
| A + B * C	| + A * B C	 | A B C * +

Ex: Balanced Parentheses
(5+6)×(7+8)/(4+3)
```python
PAIRINGS = { '(': ')', '{': '}', '[': ']' }

def is_balanced(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  # too many closing symbols
            return False
        if s != PAIRINGS[expected_opening_symbol]:  # mismatch
            return False
    return len(stack) == 0  # false if too many opening symbols

is_balanced('{{([][])}()}')  # => True
is_balanced('{[])')  # => False
is_balanced('((()))')  # => True
is_balanced('(()')  # => False
is_balanced('())')  # => False					
```					
					
### Hash Tables/Dictionary
Collection of unique. typically used to implement a "dictionary" interface
Differs from a list in its ability ***to access items by key rather than position***
Get/Set are O(1)
***Dictionaries were created specifically to get and set values by key as fast as possible***

Unfortunately, not every type of data is quite as easy to sort as a simple dictionary word, and this is where the "hash" comes into play. 
Hashing is the process of generating a key value (in this case, typically a 32 or 64 bit integer) from a piece of data. This hash value then becomes a basis for organizing and sorting the data.
The simplest hash function, called direct addressing, is h(k) = k. If you have the keys 5, 3, 8, 9, 6 then you could insert key i into position A[i] of an array A of length 10.
We want a hash function that generates few collisions and a strategy for resolving those collisions that can’t be avoided.
Division Hashing
	h(k) = k % m where m is the size of the array, k the key, and k % m is the remainder after dividing k by m.
	Is this a perfect hash function (no collisions)?
	Rule of thumb: Choose the table size m to be a prime not too close to a power of 2 (e.g. 37 rather than 31).
	We will still need a collision resolution strategy, because perfect hash functions are rare.

|Operation |	Big O Efficiency|
|---|---|
| copy			| O(n) |
| get item		| O(1) |
| set item		| O(1) |
| delete item	| O(1) |
| contains (in)	| O(1) |
| iteration		| O(n) |

	
### Tree
Represent hierarchical relationships: directory/subdirectories, xml
Trees are a data structure consisting of one or more data nodes. The first node is called the "root", and each node has zero or more "child nodes"
	 				ex: an XML document
A tree is a data structure where each node has 0 or more children
					 
* Root (top)
Only node in the tree that has no incoming edges
* Branches
* Leaves
* Node
have a unique name (key)
* Edge 
Connects two nodes 
Every node other than the root is connected by exactly one incoming edge from another node. 
Each node may have several outgoing edges.
* Path
Ordered list of nodes connected by edges. 
Ex: Mammal → Carnivora → Felidae → Felis → Domestica
* Children
Set of nodes that have incoming edges from the same node 
* Parent
A node is the parent of all the nodes to which it connects with outgoing edges
* Sibling
Nodes that are children of the same parent 
* Subtree
Set of nodes and edges comprised of a parent and all the descendants of that parent.
* Leaf Node
Node without children
* Node Level
Number of edges on the path from the root node
* Tree Height
Maximum level of any node in the tree

1. A tree is a set of nodes + edges that connect pairs of nodes having some properties:
- One node of the tree is designated as the root node.
- Every node n, except the root node, is connected by an edge from exactly one other node p where p is the parent of n
- A unique path traverses from the root to each node
- If each node in the tree has a maximum of two children, we say that the tree is a ***binary tree***

2. A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree. The root of each subtree is connected to the root of the parent tree by an edge.

```python
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

https://bradfieldcs.com/algos/trees/introduction

#### Binary tree

a type of tree with the addition of a few rules
Each node has, at most, two children
One of the most efficient ways to store and read a set of records that can be indexed by a key value in some way. 

https://www.i-programmer.info/programming/javascript/1899.html


* Balanced binary tree
Has roughly the same number of nodes in the left and right subtrees of the root
* Complete binary tree 
Each level has all of its nodes

Degrade to O(n) for get/set when the tree becomes unbalanced

#### Binary heap 

* min heap
smallest key is always at the front
* max heap
largest key value is always at the front

#### Binary Search Trees

BST property:
* Keys less than the parent are found in the left subtree
* keys that are greater than the parent are found in the right subtree
 
#### AVL tree 

A self-balancing binary search tree
Automatically makes sure that the tree remains balanced at all times (so not degrade in O(n) for get/set when the tree becomes unbalanced)
 
By G.M. Adelson-Velskii, E.M. Landi
Like a regular binary search tree, the only difference is in how the tree perform


balanceFactor = height(leftSubTree) − height(rightSubTree)  Each node has one
|right heavy||perfectly in balance||left-heavy|
|---|---|---|---|---|
|procedure to bring the tree back into balance|-1|0|1|procedure to bring the tree back into balance|

Unbalanced right-heavy tree with balance factors 
![unbalanced tree](assets/books/data/assets/unbalanced_tree.png)
 
https://bradfieldcs.com/algos/trees/avl-trees/
 
#### Red-black tree

Self-balancing binary search trees,

## Graphs 			
We are connected on Twitter. Thank you, Graphs.
https://bradfieldcs.com/algos/graphs/introduction/



# Core elements of scripting languages
	HASH TABLES 
		Powerful fundamental data structure to produce efficient joins.
		are lists of name-value pairs (~arrays indexed by strings) where insertion or deletion of an element is very fast.
		Hash tables store data using a syntax such as $myhash{"Vincent Granville|Data Scientist"} = "yes"; In this case the index is bi-dimensional and is made up of the name and job title; the value is "yes" or "no". If the name or job title is not in your data, no entry is created (that's why this data structure produces efficient joins)
	ASSOCIATIVE ARRAYS 
		are just hash tables: arrays indexed by strings rather than integers		
	STRING PROCESSING AND REGULAR EXPRESSIONS


https://www.topcoder.com/community/data-science/data-science-tutorials/data-structures/
https://speakerdeck.com/atomicobject/data-structures-the-code-that-isnt-there
http://www.infoq.com/presentations/Data-Structures
# Most programmers rely on a few core data structures, but they’re missing out on useful properties that more specialized data structures provide.
# The wrong data structures can bog implementation down in irrelevant detail or create behaviors which waste time and effort, but the right ones can give powerful guarantees for free. My talk will present lesser-known data structures and their unique advantages:

- Skiplists are simple data structures whose design leads to balanced binary tree-like performance, without any need for non-localized operations such as rebalancing. (Example use case: Demonstrating how simple invariants can lead to powerful emergent properties.)

- Difference lists provide a way to explicitly model temporary uncertainty. They are immutable, yet can still be refined as more information becomes available. They have much in common with lazy evaluation, but for data rather than control flow. (Example use case: Adding more flexibility to immutable languages by relaxing the flow of time.)

- Rolling hashes can find deterministic breaking points in buffers of binary data, enabling consistent chunking and re-use as data changes. (Example use case: rsync.)

- Jumpropes (a data structure of my own invention) automatically de-duplicate content stored in them, including data shared between multiple files. Modified content can be stored with very little additional overhead, allowing for cheap versioning. Finally, the next several fragments can always be retrieved in parallel, enabling simple buffering for streaming media. (Example use case: scatterbrain, a distributed filesystem to be released soon.)


# DATA STRUCTURES AND ALGORITHMS

- https://github.com/wdi-sf-jan/notes/tree/master/ds_algorithms
- http://www.csharpstar.com/csharp-algorithms/
- https://www.toptal.com/algorithms/interview-questions
- https://betterprogramming.pub/top-30-apple-coding-interview-questions-with-solutions-19990071ebfc
# See also <Coding_functional_programming.md>



	HASH TABLES 
		Powerful fundamental data structure to produce efficient joins.
		are lists of name-value pairs (~arrays indexed by strings) where insertion or deletion of an element is very fast.
		Hash tables store data using a syntax such as $myhash{"Vincent Granville|Data Scientist"} = "yes"; In this case the index is bi-dimensional and is made up of the name and job title; the value is "yes" or "no". If the name or job title is not in your data, no entry is created (that's why this data structure produces efficient joins). See also this article on 
	ASSOCIATIVE ARRAYS 
		are just hash tables: arrays indexed by strings rather than integers		
	STRING PROCESSING AND REGULAR EXPRESSIONS



# DATA-STRUCTURES
http://xbox.create.msdn.com/downloads/?id=123&filename=DataStructures_CheatSheet.doc
# DataStructures_CheatSheet.pdf

	Indexed collections
	
		Arrays and lists, the index is a key from [0, N-1]
	  	To get your data in a certain order every time, or their order in relation to each other is important	  						

		* Array
							

	  	* List              STRONGLY TYPED list of objects that can be accessed by index.
	  						Lists use arrays internally
	  						To map (=associates) positions (=indices) to values.
	  						A List deals with order, where a Dictionary deals with association

  	Dictionary=Map      Collection of key/value pairs. A hashtable
  						To map (=associate) meaningful (significative) keys to values
  						Dictionaries tend to be unordered, and deal with mapping key -> value relationships
  						A map (also called 'hash map' or 'associative array') provides a mapping from keys to their associated values. The keys of a JS map are string literals that may include blank spaces like in:
						var myTranslation = { 
						    "my house": "mein Haus", 
						    "my boat": "mein Boot", 
						    "my horse": "mein Pferd"
						}
						
						A map is processed by looping over all keys of the map with the help of the pre-defined function Object.keys(m), which returns an array of all keys of a map m. 
						var i=0, key="", keys=[];
						keys = Object.keys( myTranslation);
						for (i=0; i < keys.length; i++) {
						  key = keys[i];
						  alert('The translation of '+ key +' is '+ 
						      myTranslation[key]);
						}

  	Collection          strongly typed dictionary
  	
  	ReadOnlyCollection  read-only wrapper collection.
  	
  	Hash/Associative arrays
  		A Hash is a dictionary-like collection of unique keys and their values.
		Similar to Arrays, but where an Array uses integers as its index, a Hash allows you to use any object type.
	
	HashSet             high-performance set of values that contains no duplicate elements.
	
	Hashtable
	
	SortedList          a collection of key/value pairs that are sorted by a key.
	
	LinkedList          doubly linked list.
	
	Queue               first-in, first-out (FIFO) collection of objects.
	
	Stack               last-in-first-out (LIFO) collection of objects.
	
	Lookup              collection of keys each mapped to one or more values.



# CHOOSING A DATA-STRUCTURES
 [Selecting a Collection Class][https://msdn.microsoft.com/en-us/library/6tc79sx1.aspx]

### Selecting a Collection Class in .Net 
[When to Use a Thread-Safe Collection][https://msdn.microsoft.com/en-us/library/dd997373.aspx]
[Selecting a Collection Class for concurrent][https://msdn.microsoft.com/en-us/library/6tc79sx1.aspx]

 	you would need a justifiable reason to use any data structure

## Looking for, the hash table is around O(1) time, while the array is O(logN) in the best case (sorted and w/o duplicates) and O(N) in the worst case.

	Dictionary is sparse and permits random insertions but makes in-order traversal a problem
	List is not sparse and an out of order insertion is expensive, it inherently provides in-order traversal.

	dictionary is faster than list (for less than 10 items)
		The reason is because a dictionary is a lookup, while a list is an iteration
		Dictionary is based on a hash table which is a rather efficient algorithm to look up things. In a list you have to go element by element in order to find something.

		To access 105th element of an array (lists use arrays internally) CPU simply has to add (105 - 1) * element size to an address of the first element to get it's location in memory. With dictionaries it has to calculate hash code of the key, make "bucket" index from it (hash code % bucket count) and check elements in the bucket one by one to find the one with the given key. How dictionary distributes elements to buckets affects performance but in average case it's good enough to minimize having too many items it the same one
		

### When using Dictionary you are using a key to retrieve your information, which enables it to find it more efficiently, with List you are using Single Linq expression, which since it is a list, has no other option other than to look in entire list for wanted the item.

		The Dictionary uses hashing to search for the data. A Dictionary first calculated a hash value for the key and this hash value leads to the target data bucket. After that, each element in the bucket needs to be checked for equality. But actually the list will be faster than the dictionary on the first item search because nothing to search in the first step. But in the second step, the list has to look through the first item, and then the second item. So each step the lookup takes more and more time. The larger the list, the longer it takes.
		f you want to find a certain element by key in a dictionary, it can instantly jump to where it is in the dictionary - this is O(1). O(n) for doing it for every student. (If you want to know how this is done - Dictionary runs a mathematical operation on the key, which turns it into a value that is a place inside the dictionary, which is the same place it put it when it was inserted)
		So, dictionary is faster than list because you used a better algorithm.

### Dictionary uses a hash lookup, while your list requires walking through the list until it finds the result from beginning to the result each time.

		to put it another way. The list will be faster than the dictionary on the first item, because there's nothing to look up. it's the first item, boom.. it's done. but the second time the list has to look through the first item, then the second item. The third time through it has to look through the first item, then the second item, then the third item.. etc..

### So each iteration the lookup takes more and more time. The larger the list, the longer it takes. While the dictionary is always a more or less fixed lookup time (it also increases as the dictionary gets larger, but at a much slower pace, so by comparison it's almost fixed).


		A dictionary uses a hash table, it is a great data structure as it maps an input to a corresponding output almost instantaneously, it has a complexity of O(1) as already pointed out which means more or less immediate retrieval.

### The cons of it is that for the sake of performance you need lots of space in advance (depending on the implementation be it separate chaining or linear/quadratic probing you may need at least as much as you're planning to store, probably double in the latter case) and you need a good hashing algorithm that maps uniquely your input ("John Smith") to a corresponding output such as a position in an array (hash_array[34521]).

		Also listing the entries in a sorted order is a problem. If I may quote Wikipedia:

		Listing all n entries in some specific order generally requires a separate sorting step, whose cost is proportional to log(n) per entry.
		Have a read on linear probing and separate chaining for some gorier details :)
		http://en.wikipedia.org/wiki/Linear_probing

# LISTS 
  order is important
  zero based indexing
  index based collections are very efficient than other collections
  T[], List<T> , Collection<T>, ReadonlyCollection<T>, ObservableCollection<T>, IList<T>

# LINKED LISTS, STACKS, QUEUES

# DICTIONARIES
  key indexed: key is nothing but the unique item in the dictionary
  IDictionary<TKey, TValue>
  Pretty fast but Lists are having edge over dictionaries.

# DATA DICTIONARY	(Data science)
	When processing data, the first step is to produce a data dictionary. It is easily done using a scripting language
	http://www.analyticbridge.com/profiles/blogs/why-and-how-you-should-build-a-data-dictionary-for-big-data-sets :

	Identify areas of sparsity (clairsemé) and areas of concentration in high-dimensional data sets
	Identify outliers (contours) and data glitches (a sudden, usually temporary malfunction or irregularity of equipment)
	Get a good sense of what the data contains, and where to spend time (or not) in further data mining
	
	DATA DICTIONARY COLUMNS
		A data dictionary is a table with 3 or 4 columns. 
		1. LABEL: the name of a variable, or a combination of multiple (up to 3) variables
		2. VALUE(s) attached to the label (first and second columns actually constitute a name-value pair)
		3. FREQUENCY count: it measures how many times the value (attached to the label in question) is found in the data set. 
		4. DIMENSION OF THE LABEL (1 if it represents one variable, 2 if it represents a pair of two variables etc.)

	Ex: category~keyword travel~Tokyo 756 2
	In this example, the entry corresponds to a label of dimension 2 (as indicated in column 4), and the simultaneous combination of the two values (travel, Tokyo) is found 756 times in the data set.
	THE FIRST THING YOU WANT TO DO WITH A DICTIONARY is to SORT it using the following 3-dim index: column 4, then column 1, then column 3. Then look at the data and find patterns.

## BUILD A DICTIONARY

### Browse your data set sequentially. For each observation, store all label/value of dim 1 and dim 2 as hash table keys, and increment count by 1 for each of these label/value. In Perl, it can be performed with code such as $hash{"$label\t$value"}++. 

		If the hash table grows very large, stop, save the hash table on file then delete it in memory, and resume where you paused, with a new hash table. At the end, merge hash tables after ignoring hash entries where count is too small.

# SETS
  Treating the whole collection as a single group to get intersection, union..
  In .Net most common set collection is called HashSet<T>
  ISet<T> defines standard contract for set collection  
  Similarity between Dictionaries and Sets as the underlying technology powering both is hashtable
  but sets don´t have a key

# TREE 

  A tree is a data structure where each node has 0 or more children

  . binary tree: a type of tree with the addition of a few rules
    1. Each node can have 0, 1, or 2 children.
    2. Any value less than the node’s value goes to the left child (or a child of the left child).
    3. Any value greater than, or equal to, the node’s value goes to the right child (or a child thereof).

# ACTIONS

 lookup a single element: provide index or key
 enumerate in the collection:  foreach() loop
 modify: add/remove an item





# DATA STRUCTURE
	
	a way to store and organize data in a computer, so that it can be used efficiently
	Data structures → Treatments → Algorithms (sort, insert…) → Big O
									appliquer sur ces données des algorithmes de segmentation, ou de prédiction pour anticiper les comportements des consommateurs
	which data structure to use?

# COMMON DATA STRUCTURES


# Data Formats
	Flat Text
	HDFS
	SQL
	NoSQL (mongoDb, CouchDb)
	JSON
	XML
	HBase

## INTERFACES

	Interfaces
	They behave like a black box. They provide details about how they can be used without exposing their implementation. 
	
	Set
	A data structure having 4 basic operations: Items can be added, items can be removed, a “contains" method can verify an item’s existence, and the set can return a list of it’s items.
	
	Maps or dictionaries
	key-value sets. Maps are also very similar to an associative array. Since the keys in a map are a set, there cannot be any duplicates. When a value of a key is updated, the previous value is lost.
	
	Stack
	an interface that adheres to the “last-in first-out” LIFO principle. You can only push (add) or pop(remove) from the stack. Stacks may also contain a “peek” method to view the current top value without modifying the stack.
	
	Queue
	a “first-in first-out” FIFO data structure similar to a waiting line. Like a stack, queues have push/pop methods called enqueue and dequeue. They are useful for items that need to be handled in order or prioritize based on their need.


## LINEAR AND/OR SEQUENTIAL DATA STRUCTURES

		Array List
		created from directly interacting with the allocated memory. They are simple in the way they are constructed. However, inserting and removing values can be costly since the entire list must be collapsed or expended to accommodate the updated value.

		Linked Lists
		composed of nodes which point to the next node in the list. While item retrieval is slower with a linked list, adding and removing is much faster.

### Doubly Linked List

		Stacks - LIFO (last-in-first-out)
		 	extremely useful and efficient data structure for solving algorithms
			Typical application areas include compilers, operating systems, handling of program memory (nested function calls)

		Queues - FIFO (first-in-first-out)
			All operations  O(1)
			Batch processing (buffer: stored and held to be processed later)


		Hash tables
		key-value stores used to implement maps or sets. With hash tables, the key is used as the index for where to find the value in memory. 
		This is done by passing the key through a hashing function which converts it to an addressable space. 

## HIERARCHICAL DATA		

		Trees
			Trees are useful middle ground between array lists and linked lists.

			a collection of entities called 'nodes' are linked together to simulate a hierarchy. 
			a non linear data structure 
			top most node in the tree is called the root
			 can contain any type of data and may contain a link or reference to other nodes which can be called its children

			Use:
				The file system on your disk is hierarchical data
				Organizing data for quick search insertion deletion, (BST is O(log n))
				Storing dictionary for spellchecking

			TREE VOCABULARY

				Root 					node at the top of the tree                      
				Parent 					node above a node                    
				Child 					nodes below a node                  
				Grandparent 			parent of parent                      
				Grandchild 				child of child                          
				Sibling 				children of same parent        
				Leaf 					node that does not have a child
				Internal 				node that has a child            
				Cousin/Uncle 			you get the hint…..                
				Ancestor/Descendent 	same kind of idea….
				Height 					Number of edges in longest path from X to a leaf
				Depth 					length of the path from root to node X or number of edges in path from root to node X
			
			Some tree facts:

				Height of a tree = longest path of root to leaf
				Link - connection from a node to another node
				In a tree with N nodes, there will always be N-1 edges.

			Binary Tree
				each node can have at most 2 children
				For fast search

			BST - Binary Search Tree 
				composed of nodes with 0, 1, or 2 subtrees. Elements in the left subtree are lesser than the node value. Elements in the right subtree are greater than the node value.
				
				A left child node must be less than its parent and a right child node must be more than its parent. This rule follows all the way down.
				left child < parent
				right child > parent
				As we insert new nodes with values, the tree must always stay sorted.
				A BST is often used to store key-value pairs, so in this case, what we’d be storing is the key to an object.
					   50
						| 
				______________
				|            |
				25           75
				________     _________
				|      |     |       |
				10     40   60       90

				Search
				Each time we head down a path, we discard entire sections of the tree, so it is very quick to find a specific element.
				To keep this optimized, the tree MUST
				
				More nodes on one side of the tree than the other: unbalanced BST

				Big-O for BSTs
					Balanced BST: Logarithmic time — O(log n)
					Unbalanced BST: Linear time — O(n)
					
				Although dictionaries are often implemented with hash tables, if you want to keep your keys in a sorted order, hash tables aren’t really good at that while binary search trees do a great job.

			Trie (digital tree, radix tree or prefix tree)
				no node in the tree stores the key associated with that node
				its position in the tree defines the key with which it is associated
				
				All the descendants of a node have a common prefix of the string associated with that node
				the root is associated with the empty string

			B-Trees
				keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time
				generalization of a binary search tree
				In DB & File Systems

			Decision Tree
				http://dms.irb.hr/tutorial/tut_dtrees.php
				 for classification and prediction
				decision trees represent rules. Rules can readily be expressed so that humans can understand them

			Red-Black Trees and B-Trees
				Both Red-Black Trees and B-Trees are balanced search trees that can be used on items that can have a comparison operator defined on them. They allow operations like minimum, maximum, predecessor, successor, insert, and delete, in O(log N) time (with N being the number of elements). Thus, they can be used for implementing a map, priority queue, or index of a database, to name a few examples.

				Red-Black Trees are an improvement upon Binary Search Trees. Binary Search Trees use binary trees to perform the named operations, but the depth of the tree is not controlled - so operations can end up taking a lot more time than expected. Red-Black Trees solve this issue by marking all nodes in the tree as red or black, and setting rules of how certain positions between nodes should be processed. Without going into too much detail, this method guarantees that the longest branch isn’t more than twice as long as the shortest branch, so each branch is shorter than 2*log_base2(N).

				This is the ideal structure for implementing ordered maps and priority queues. B-Trees branch into K-2K branches (for a given number K) rather than into 2, as is typical for binary trees. Other than that, they behave pretty similarly to a binary search tree. This has the advantage of reducing access operations, which is particularly useful when data is stored on secondary storage or in a remote location. This way, we can request data in larger chunks, and by the time we finish processing a previous request, our new request is ready to be handled. This structure is often used in implementing databases, since they have a lot of secondary storage access.

		Graphs
 			a non-linear data structure, a hierarchical structure
			a collection of objects we call nodes or vertices connect to each other through a set of edges. 
			In a tree there are rules dictating edges, in a graph we have none! 
			In a tree, all nodes must be accessible from the root. 
			So in short, a tree is just a type of graph.

In a graph there are no rules. It has a set of nodes and edges. So if you think about it some more, a tree is a special kind of graph!




- https://www.bogotobogo.com/Algorithms/algorithms.php