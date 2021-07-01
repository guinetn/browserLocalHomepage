### Quick Sort

Quicksort is generally considered the “fastest” sorting algorithm

Divide & Conquer

From a ***pivot*** element, recursively:
- Bring pivot to ist right position (left is smaller, right is greater)
- Quick sort on the left
- Quick sort on the right

1 8 3 9 4 5 7
            ↑Pivot
1 8 3 9 4 5 7
1 3 8 9 4 5 7
1 3 8 9 4 5 7

i: index of smaller element
j: loop