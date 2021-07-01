# MAP
# apply a function on every item and generate new values. 

# two parameters
# - an array
# - a transform function
# It will return a new transformed array in which each item in an array is the result of transform function called over each element of the original array.

from functools import partial

memes = ["It's over 9000 !", "All your base are belong to us."]
print(s.upper() for s in memes)


def squareIt(n):
  return n*n

values=[0, 1, 2, 3, 4, 5, 6, 7,8,9,10]

squared=list(map(squareIt, values))
print(values)
print(squared)


def double(x):
  return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]  # [2, 4, 6, 8]ù
twice_xs = map(double, xs)          # same as above
print(twice_xs)

list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs)         # again [2, 4, 6, 8]
print('with partial ', twice_xs)



def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
print(products)





def mapping(arr, transform):
    mapped = []
    for element in arr:
        mapped.append(transform(element))
    return mapped

def addTwo(num):
    return num+2

mapping([1, 2, 3], addTwo)  # [3,4,5]