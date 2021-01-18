# BIG O NOTATION: Algorithmic Complexity

The amount of time it takes to run an algorithm = its computational complexity
Big O is used to analyze algorithms computational complexity (time or space used) to determine how fast an algorithm is
Knowing whether our algorithm is fast or slow lets us design better algorithms.
Invented by Paul Bachmann, Edmund Landau [1894 and 1820]
Popularised in the 1970s by Donald Knuth
    
## Big O Notation's Order Of Growth
Big O is easy to read once we learn this table

|   |Constant|Logarithm|Linear|Polynomial|Cubic…|Exponential|Exponential|Factorial|
|---|---|---|---|---|---|---|---|---|
|   |  O(1)  |O(log(n))| O(n) |	O(n²) | O(n^3)…O(n^x)|O(2^n)|O(e^n)|O(n !)|
|n=10 |  1   |  3 |   10   |100    |    1000         | 1024  |22026 | 3 628  800|
|n=100|  1   |  7 |   100  |10 000 |    1 000 000    | 2^100 | e^100 | 100! = 9e+157|
 
* n is the size of the input
* Big O notation uses these functions to describe algorithm efficiency

![big_o](assets/slides/computer_science/assets/big_o.png)     
  

## Best, Worst and Average Case

## Roughly Estimated Complexity
Hard to evaluate the exact complexity of an algorithm
 
## CONSTANT TIME: O(1)
No matter how many elements the sequence is processing time is fixed
Having a larger sequence does not increase the time required to extract the first element.
Ex: Extract a random sample from a list
```python
def OddOrEven(n):
    return "Even" if n % 2 else "Odd"
```

## LOGARITHMIC TIME: O(log n) - DIVIDE AND CONQUER SEARCHES
A logarithmic algorithm `halves` the list every iteratation
Typical of algorithms that divide the input, then look at one of the sections
- Searching sorted data
- Fibonacci number calculations
- Searching a Binary Search Tree
Increase in complexity as the number of elements in the data set increases but by a relatively smaller amount as the size grows

```python
# Find the number "2" in 
a = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
binarySearch(a, 2);

def binarySearch(alist, item):
    # Algorithm halves the input every single time it iterates. Therefore it is logarithmic
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
            last = midpoint-1
            else:
                first = midpoint+1

    return found    
```

## LINEAR TIME: O(n) - LINEAR GROWTH
ex: a search through an unsorted set of data by reading one item after another until a specific item is found.
Every element from the input is visited exactly once. As the size of the input grows our algorithm’s run time scales the same size of the input.

- Sum an array
- Find the max of an unsorted array (when sorted, use divide and conquer)
- Traversal of a list (a linked list or an array) with n elements

```python
users = ['Joe','Paul','Tim']
for user in users:
    print(user)
    
# Find max value:
a = [12, 4, 16, 22, 33, 8, 15, 3]
max_item = a[0]
for item in a:
    if item > max_item:
        max_item = item
```

## O(n log n) - DIVIDE AND PICK A SECTION FOR EVERY PIECE OF INPUT

Sorting with quicksort, merge sort, or another reasonably fast sort.
loglinear. Often they are algorithms that may perform an O(log n) operation for every item in the input data. Several sorting algorithms, such as quick sort and heap sort are O(n log n).

## Polynomial Time: O(n^x) - EXAMPLES:

Polynomial time is a polynomial function of the input. 
A polynomial function looks like n² n³
Quadratic, algorithms increase in complexity proportionally to the square of the number of items in the input data
Two nested loops for the input data in your algorithm, such as with bubble sort, it is likely to be O(n^2). Other variations of this are O(n^x) or polynomial algorithms. For example, three nested loops would be O(n^3), four nested loops are O(n^4) and so on.

- Two nested loops
- Finding duplicates in an unsorted list of n elements (implemented with two nested loops)
- Insertion Sort
- Selection Sort
- Bubble Sort

>ANY ALGORITHM WITH A POLYNOMIAL TIME OR ABOVE IS:
>A complete disaster! A catastrophe!
>Than means whe have to improve it! We can speed it up.

```python
def bubbleSort(arr):
    # O(n^2)
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
    
        # Last i elements are already in place
        for j in range(0, n-i-1):
    
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
data = [12, 4, 16, 22, 33, 8, 15, 3]
bubbleSort(data)
```

```python
# Count sentence's words that are in a dictionary
dictionary = ["a", "in"] # this is our words dictionary
sentence = "Count sentence's words that are in a dictionary".split(" ")
   
counter = 0
for word in sentence:
    for dicword in dictionary:
        if word == dicword:
            counter = counter + 1
```

Improve it with dictionaries (are sorted by default)
1. Sort the list of words in the sentence
Check each sentence's word = only once loop through the dictionary
2. For each word in dictionary: if the dictionary word is less than the word we’re on in the sentence, we switch to the next dictionary's word. 
Algorithm is now O(n log n). Acceptable.

## Exponential Time: O(x^n) - Exponential growth and very poor scalability
>Explosive algorithm! Each additional item in the input data has the potential to double the amount of time/resources used by the algorithm
>ONE NEW PIECE OF DATA DOUBLES THE WORK IS 2^N
- Naive Fibonacci (compute many time same values)
- Password of length n → Cracking it = 10^n combinations 
- Subsets of a set, 2^n: subsets(['a', 'b']) → ['a', 'b', 'ab', 'ba']

```python
#Naive Fibonacci sequence
def F(n):
	if n == 0 or n == 1:
		return n
	else:
		return F(n-1)+F(n-2)
```
<pre>
    F(4) calculation is
          4     
      ┌───┴───┐
      3       2      F(2) is computed twice!
    ┌─┴─┐   ┌─┴─┐
    1   2   0   1  
      ┌─┴─┐
      1   0   
</pre>

To improve the algorithm, instead of calculating F(2) twice, we store the solution somewhere to only calculate it once:

```python
# Fibonacci sequence with memoization (synamic programming)
def fibonacciVal(n):
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]
```

```python
from itertools import chain, combinations

def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
```

## O(n!)
List all combinations of the subset of a set. 
Impossibly slow and hardly ever needed.
Naive traveling salesman
Factorial growth in complexity.

::::

![big_o_data_structure_operations](assets/slides/computer_science/assets/big_o_data_structure_operations.png)
![big_o_data_heap_structure_operations](assets/slides/computer_science/assets/big_o_data_heap_structure_operations.png)
![big_o_graph_datastructure_operations](assets/slides/computer_science/assets/big_o_graph_datastructure_operations.png)

::::
![big_o_sorting_algo](assets/slides/computer_science/assets/big_o_sorting_algo.png)
![big_o_data_graph_algorithms](assets/slides/computer_science/assets/big_o_data_graph_algorithms.png)
