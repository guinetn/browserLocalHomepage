# generator is a special type of function which does not return a single value, instead it returns an iterator object with a sequence of values

def myGenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = myGenerator()
next(gen)
next(gen)
next(gen)
next(gen)


def getSequenceUpTo(x):
    for i in range(x):
        yield i

seq = getSequenceUpTo(5)
next(seq)        
next(seq)        
next(seq)        
next(seq)        
next(seq)        
next(seq)        


def squareOfSequence(x):
    for i in range(x):
        yield i*i

gen = squareOfSequence(5)
while True:
    try:
        print ("Received on next(): ",next(gen))
    except StopIteration:
        break


def count(a,b):
    x = a
    while x < b:
        yield x
        x += 1
count(10,20)
# <generator object count at 0x000001...>
[x for x in count(10,20)]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


def squares():
    for x in range(0,10):
        yield x*x
list(squares())
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        

# GENERATORS - yield

Something that you can iterate over (for us, usually using for) but whose values are produced only as needed (lazily).
Ex: A list of 1 million elements...you only need to deal with them one at a time = inefficiency 

The flip side of laziness is that you can only iterate through a generator once. 
If you need to iterate through something multiple times, you’ll need to either recreate the generator each time or use a list.

- Unlike normal functions, the local variables are not destroyed when the function yields
- The generator object can be iterated only once
- Memory Efficient
- Can represent finite or infinite Stream

def all_even():
    n = 0
    while True:
        yield n
        n += 2


        

def lazy_range(n):
  """a lazy version of range"""
  i = 0
  while i < n:
   yield i
   i += 1

for i in lazy_range(10):
  do_something_with(i)

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)


infinite sequence:
def natural_numbers():
  """returns 1, 2, 3, ..."""
  n = 1
  while True:
    yield n
    n += 1

Python lazy_range function range()



Generator Expression: building generators easy (similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses)

- lazy execution ( producing items only when asked for ). For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.

my_list = [1, 3, 6, 10]           # Initialize the list
list_ = [x**2 for x in my_list]   # square each term using list comprehension
print(list_)

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
my_list = [1, 3, 6, 10]
a = (x**2 for x in my_list)
print(next(a))   1
print(next(a))   9
print(next(a))   36 
print(next(a))   100
next(a)          Traceback (most recent call last): StopIteration
 



Generator expressions can be used as function arguments. 
When used in such a way, the round parentheses can be dropped.
>>> sum(x**2 for x in my_list)
146
>>> max(x**2 for x in my_list)
100



def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1




# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)



'''
Generators are used to create iterators, but with a different approach. Generators are simple
functions which return an iterable set of items, one at a time, in a special way.

When an iteration over a set of item starts using the for statement, the generator is run. 
Once the generator's function code reaches a "yield" statement, the generator yields its execution 
back to the for loop, returning a new value from the set. 
The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.
'''

import random


def lottery():
    """Generator function example.

    Here is a simple example of a generator function which returns random integers.
    This function decides how to generate the random numbers on its own, and executes the yield
    statements one at a time, pausing in between to yield execution back to the main for loop.
    """
    # returns first 3 random numbers between 1 and 10
    # pylint: disable=unused-variable
    for i in range(3):
        yield random.randint(1, 10)

    # returns a 4th number between 10 and 20
    yield random.randint(10, 20)


def test_generators():
    """Yield statement"""
    for number_index, random_number in enumerate(lottery()):
        if number_index < 3:
            assert 0 <= random_number <= 10
        else:
            assert 10 <= random_number <= 20



