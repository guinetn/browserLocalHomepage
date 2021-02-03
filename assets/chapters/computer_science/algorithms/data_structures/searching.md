# Searching algorithms

## Sequential Search
With an ordered container it is possible to visit them in sequence O(n)

|Case	             |Best Case	| Worst Case | Average Case ||
|---|---|---|---|
|item is present	 | 1        |	n	     | n/2 |​ sequential_search/ ordered_sequential_search|
|item is not present | n        |	n	     | n  sequential_search||
|item is not present | n        |	n	     | n/2 | ordered_sequential_search|

```python
def sequential_search(alist, item):
    position = 0

    while position < len(alist):
        if alist[position] == item:
            return True
        position = position + 1

    return False

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

sequential_search(testlist, 3)  # => False
sequential_search(testlist, 13)  # => True 
``` 

if items were in ascending order the algorithm does not have to continue looking through all of the items to report that the item was not found. It can stop immediately. 
```python
def ordered_sequential_search(alist, item):
    position = 0

    while position < len(alist):
        if alist[position] == item:
            return True

        # exit if ordered
        if alist[position] > item:
            return False

        position = position + 1

    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
ordered_sequential_search(testlist, 3)  # => False
ordered_sequential_search(testlist, 13)  # => True
``` 

## Binary Search

Divide and conquer strategy in O(log n)

Instead of searching the list in sequence, a binary search will use the ORDERED nature of the list to eliminate half of the left/right.
* start by examining the middle item
* If is the correct item, we are done
* If it is not and the item searching for is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration. The item, if it is in the list, must be in the upper half. Repeat the process with the upper half. Start at the middle item and compare it against what we are looking for. Again, we either find it or split the list in half, therefore eliminating another large part of our possible search space. 

Each comparison eliminates around half of the remaining items from consideration. 
|Comparisons | ~ Number of Items Left |
|---|---|
|1|n/2|
|2|n/4|
|…||
|i|n/2^i|

| | |
|----------------------------|----------|
|Worst-case performance      | O(log n) |
|Best-case performance       | O(1) |
|Average performance         | O(log n) |
|Worst-case space complexity |  O(1) |

The number of comparisons necessary to get to this point is i where n/2^i=1 ==> comparisons number is i=log n
 

```python
def binary_search(alist, item):
    if not alist:  # list is empty -- our base case
        return False

    midpoint = len(alist) // 2
    if alist[midpoint] == item:  # found it!
        return True

    if item < alist[midpoint]:  # item is in the first half, if at all
        return binary_search(alist[:midpoint], item)

    # otherwise item is in the second half, if at all
    return binary_search(alist[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
binary_search(testlist, 3)  # => False
binary_search(testlist, 13)  # => True
```

```cs
public static object BinarySearchDisplay(int[] arr, int key) {
   int minNum = 0;
   int maxNum = arr.Length - 1;

   while (minNum <=maxNum) {
      int mid = (minNum + maxNum) / 2;
      if (key == arr[mid]) {
         return ++mid;
      } else if (key < arr[mid]) {
         max = mid - 1;
      }else {
         min = mid + 1;
      }
   }
   return "None";
}
```

Binary search in...
https://www.tutorialspoint.com/Binary-search-in-Chash

## Hashing

Previously we make improvements in our search algorithms by taking advantage of information about where items are stored in the collection with respect to one another. Knowing a list was ordered, we could search in logarithmic time using a binary search. 
Hash is a data structure that can be searched in O(1) time

A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0.

#### Hash function
Maps an item and the slot that item belongs to
Take any item in the collection and return an integer in the range of slot names [0 ; n-1]
remainder method: 
(item/table size)
will typically be present in some form in all hash functions, since the result must be in the range of slot names.
Perfect hash function: maps each item into A UNIQUE slot
 
* load factor: number of slots occupied
λ = ​numberofitems / ​tablesize
​​
#### collision

item        | 77 |   |   |   | 26 | 93 | 17 |   |    | 31 | 54 |
slots       | 0  | 1 | 2 | 3 | 4  | 5  | 6  | 7 | 8  | 9  | 10 |      λ = 6/11
item hash     ↑
              44%11=0. Since 77 also had a hash value of 0, we would have a problem.
              collision: same hash for two different item

given an arbitrary collection of items, there is no systematic way to construct a perfect hash function. Luckily, we do not need the hash function to be perfect to still gain performance efficiency.

One way to always have a perfect hash function is to increase the size of the hash table so that each possible value in the item range can be accommodated. This guarantees that each item will have a unique slot. Although this is practical for small numbers of items, it is not feasible when the number of possible items is large. For example, if the items were nine-digit Social Security numbers, this method would require almost one billion slots. If we only want to store data for a class of 25 students, we will be wasting an enormous amount of memory.

Collision Resolution
When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table. This process is called collision resolution.
open addressing 
linear probing

