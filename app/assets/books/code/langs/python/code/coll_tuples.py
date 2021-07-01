# Tuples
# lists’ IMMUTABLE cousins

"""
Tuples are immutable lists, meaning the elements cannot be changed. It’s declared with parenthesis instead of square brackets.
Ordered, Immutable collections of Data, and are the default data type in Python. Immutable means that they can’t be modified and items can’t be added or deleted. The data is enclosed in parenthesis ().
Use Case: Tuples are ideal data structures where the data shouldn’t be changed. For example, coordinates i.e. Latitudes and Longitudes of places can be stored in tuples.

Python tuples are;
immutable objects: values inside a tuple object cannot be revised after creation.
sequence type data structures that allow accessing items contained with the 0-based integer positional index.

"""
my_tuple = (1, 2)
other_tuple = 3, 4
try:
  my_tuple[1] = 3
  pincodes = (500010, 500045, 500022, 500068, 500034)
  print(pincodes[0:4])        #output: (500010, 500045, 500022, 500068)
  
  sorted(pincodes) 
  
  a,b,c=(1,2,3)
  
  tuple1=(10,20,30)
  tuple2= tuple1 + (40,50,60) #concatenation
except TypeError:
  print "cannot modify a tuple"

# Tuples are a convenient way to return multiple values from functions:
def sum_and_product(x, y):
  return (x + y),(x * y)
sp = sum_and_product(2, 3) # equals (5, 6)
s, p = sum_and_product(5, 10) # s is 15, p is 50

Tuples (and lists) can also be used for multiple assignment:
x, y = 1, 2 # now x is 1, y is 2

# SWAP
x, y = y, x # Pythonic way to swap variables; now x is 2, y is 1


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
for i, j in friendships:
	print(i,j)



a_tuple = tuple()
a_tuple = (1,2,3,4,5)
print (a_tuple[2]) #accessing the element with only positional index
a_tuple[0] = 10 #tuples are immutable so you can not revise them
Output:
3
TypeError: 'tuple' object does not support item assignment


# Named Tuples

You can access the elements of tuple only with the positional index.
Each element contained in NamedTuples can be accessed through a unique and human-readable identifier. 

from collections import namedtuple
import math
# Access the items with their names, which are r and theta respectively.
Polar_Coordinate = namedtuple('Polar_Coordinate', 'r theta')

def convert_cartesian_to_polar(x, y):
  #Calculate Polar Cooordinates
  r0 = (x**2 + y**2)**0.5
  theta0 = math.atan2(y,x)
  #Convert from radians to degrees
  theta0 = math.degrees(theta0)
  
  return Polar_Coordinate(theta=theta0, r=r0)

box_position = convert_cartesian_to_polar(10, 10)
print(box_position)
print(box_position.r)
print(box_position.theta)
print(type(box_position))
Output:
Polar_Coordinate(r=14.142135623730951, theta=45.0) 
14.142135623730951 
45.0 
<class '__main__.Polar_Coordinate'>