## functools

## 1. Cache
save processing times:
cache certain calculations inside of memory rather than throwing them away just to recalculate them later. 

For caching factorial function, import lru_cache from functools and call it before our function

from functools import lru_cache

@lru_cache
def factorial(n):
    return n * factorial(n-1) if n else 1
    
%timeit factorial(10)   # 86 ns
%timeit factorial(12)   # 32 ns

 ## 2. Partial Functions
 
from functools import partial
fact = partial(factorial)
fact(10)

def partial(func, /, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
 
 ## 3. Reduce
Apply the function of two arguments with cumulative iteration.
This will reduce the iterable down into its simplist form.
 
from functools import reduce
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])

# Dispatch

@singledispatch
def fun(arg, verbose=False):
        if verbose:
            print("Let me just say,", end=" ")
        print(arg)

Register dispatching for new types:

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)