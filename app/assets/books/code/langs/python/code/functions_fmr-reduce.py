# REDUCE

# import functools and then use fully-qualified names like functools.reduce()
# from functools import reduce and then call reduce() directly
'''

three parameters
- a reducer function
- an initial value for accumulator
- an array

This will reduce the iterable down into its simplist form.
For each item in the array, the reducer function is called and passing it to the accumulator, current array element.
Then the return value is assigned to the accumulator. When reducing all the elements in the list gets finished, the accumulator value is returned.


reduce() is roughly equivalent to the following Python function:

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
'''

from functools import reduce 
from functools import partial 


def reducing(reducer, initial, arr):
    acc = initial
    for element in arr:
        acc = reducer(acc, element)
    return acc

def accum(acc, curr):
    return acc + curr

reducing(accum, 0, [1, 2, 3])   # 6



def afficher(a, b):
    print("Entrée :", a, b)
    print("Sortie :", a + b)
    return a + b
 
res = reduce(afficher, range(10))
print("Résultat final", res)

print(sum(range(10)))
print(reduce(lambda a, b: a * b, range(1, 11)))

l=[10, 20 , 30 , 40 , 50]
reduce(lambda x,y:x+y, l)
print(reduce)



def double(x):
  return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]  # [2, 4, 6, 8]
twice_xs = map(double, xs)      # same as above
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs)     # again [2, 4, 6, 8]

def multiply(x, y): return x * y

products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]

def is_even(x):
  """True if x is even, False if x is odd"""
  return x % 2 == 0

x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]

x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24