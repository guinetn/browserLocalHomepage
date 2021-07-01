# Recursion algorithms

method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. In computer science, recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.

### The Three Laws of Recursion

A recursive algorithm must
1. Have a base case
2. Change its state and move toward the base case
3. Call itself, recursively


```python

def iterative_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

iterative_sum([1, 3, 5, 7, 9])  # => 25
```

Recursion
```python
def sum_of(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_of(numbers[1:])

sum_of([1, 3, 5, 7, 9])  # => 25
```

Converting a number to any base <=16
```python
CHAR_FOR_INT = '0123456789abcdef'


def to_string(n, base):
    if n < base:
        return CHAR_FOR_INT[n]

    return to_string(n // base, base) + CHAR_FOR_INT[n % base]

to_string(1453, 16)  # => 5Ad
```

- https://bradfieldcs.com/algos/searching/hashing/




