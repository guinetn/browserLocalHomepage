# List []

"""
Array-like structures that let you save a set of mutable objects of the same type to a variable.
"""
# A List is a collection which is ordered and changeable. Allows duplicate members.
# Comma separated values between square brackets
# Mix of types:  might contain items of different types, but usually the items all have the same type
# 0 based

"""

Ordered, Mutable collections of Data, enclosed by square brackets [ ]
Use commas to separate their values
They can contain different data types, repeated values and are iterable.

Advantages:
Simple to create and use data sequences
Automatically scale to meet changing size requirements
Used to create more complex data structures

Disadvantages:
Not optimized for scientific data (unlike NumPy’s array)
Can only manipulate the rightmost end of the list

Applications:
Shared storage of related values or objects, i.e. myDogs
Data collections you’ll loop through
Collections of data structures, such as a list of tuples

Common arrays interview questions in Python
Remove even integers from a list
Merge two sorted lists
Find the minimum value in a list
Maximum sum sublist
Print products of all elements
"""
# TAKE AWAY
nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5] + [6]
for x in nums:
  print(x)
print(nums[-1])
print(nums[1:])
print(nums[2:3])
print(nums[2:-1])
len(nums)
sum(nums)
nums.append(7)
nums.pop(1)
nums.insert(3, 100)      # .insert(index,value) 
nums.extend([200,201])   # .extend() adds multiple items to the list
nums2 = [i * 10 for i in nums]
nums=[-1 if i==4 else i for i in nums]  # You can also use List Comprehension to replace values
s= [1,2,3,4,5]
(s * 5).tolist()  # [5, 10, 15, 20, 25]
nums_x_10 = list(map(lambda x: x * 10, nums))
nums_x_5 = list(map(lambda x: x*5,[5, 10, 15, 20, 25]))
nums.remove(3)
del nums[1]            # del function deletes items based on Index
nums.pop(0)            # .pop() too deletes items based on Index
del nums[1::2]         # Deleting Multiple Elements from a List



# Create list
numbers = [1, 2, 3, 4, 5]
integer_list = [1, 2, 3] + [4, 5, 6]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

lst = [i for i in range(0,10)]
print(lst)  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = list(range(0,10))
print(lst)

lst = [("Hello "+i) for i in ['Karl','Abhay','Zen']]
print(lst) # ['Hello Karl', 'Hello Abhay', 'Hello Zen']

[i for i, j in enumerate(['foo', 'bar', 'baz']) if j == 'bar']

# List Operations

list_length = len(integer_list) # equals 3
list_sum = sum(integer_list) # equals 6

item_list = [1, 2, 3, 1, 2, 3]
item_set = set(item_list) # {1, 2, 3}
distinct_item_list = list(item_set) # [1, 2, 3]

# Finding the index of an item in a list
["foo", "bar", "baz"].index("bar")    # 1
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

# To get all indexes:
indexes = [i for i,x in enumerate(xs) if x == 'foo']

a = ["foo","bar","baz",'bar','any','much']
indexes = [index for index in range(len(a)) if a[index] == 'bar']


cars = ["Toyota", "Tesla", "Ford"]
print(len(cars))
cars.append("Honda")
cars.pop(1)
for x in cars:
  print(x)

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Accessing Items in a List
# Get a value (base is 0)
nums = [0,1,2,3,4,5,6,7,8,9,10]
print(nums[0])
print(nums[1])
print(nums[-1])
print(nums[1:])
print(nums[2:3])
print(nums[2:-1])

# Get length
nums_size = len(nums)
print(nums_size)

# check existence
num = 5
if num in [1,2,3,4,5]:
     print('present')
     
# Append to list
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
fruits.append('Mangos')
fruits.append('Lotus')           # .append() adds an item to the end of the list
fruits.insert(3,'Magnolia')      # .insert(index,value) adds an item to the index of your choice
fruits.extend(['Jasmine','Carnation'])   # .extend() adds multiple items to the list

# Replace
fruits[3]='Orchid' 
fruits=['Daffodil' if i=='Lily' else i for i in flowers]  # You can also use List Comprehension to replace values

# Transform list
my_list = [1, 2, 3, 4, 5]
my_new_list = [i * 5 for i in my_list]

def scale(lst, x): return [i*x for i in lst] 
scale([2,3,4], 2) 

(s * 5).tolist()
[5, 10, 15, 20, 25]

# Mapping Lists 

k = 5
my_list = [1,2,3,4]
result = list(map(lambda x: x * k, my_list))

list(map(lambda x: x*5,[5, 10, 15, 20, 25]))

# TypeCasting Whole List
list(map(int,['1','2','3']))  # [1, 2, 3]
list(map(float,[1,2,3]))      # [1.0, 2.0, 3.0]
[float(i) for i in [1,2,3]]   # [1.0, 2.0, 3.0]

import numpy as np
list(np.array(x) * 5)

import pandas as pd
s = pd.Series(my_list)
s5 = s * 5

from functools import partial as p
from operator import mul
map(p(mul,5),my_list)


# List Methods: append() extend() insert() remove() pop() count() sort() reverse()

# concat lists
x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1,2,3,4,5,6]

x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6]; # ! x is unchanged !

# Remove from list
fruits.remove('Grapes')
del fruits[1]            # del function deletes items based on Index
fruits.pop(0)            # .pop() too deletes items based on Index

# Deleting Multiple Elements from a List
a = [1,2,3,4,5]
del a[1::2]
print(a) # [1, 3, 5]

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)


# Get values
# nth element = square brackets:

# _ underscore for a value you’re going to throw away:
_, y = [1, 2] # now y == 2, didn't care about the first element


# SLICE A LIST

x = range(10) # is the list [0, 1, ..., 9]
first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [-1, 1, 2, ..., 9]


mylist = [1,2,3,4]
print(mylist)
mylist[0]
# return a new list containing just the values you're interested in. 
# The value at the starting index and all of the values in between will be returned. The value at the ending index will not.
# To slice a list, pass the starting and ending index positions into the brackets as integer values, separated by a colon :

mylist[-1]     # 4
mylist[-2]     # 3
mylist[1:3]    # Range [2,3]
mylist[-2:]    # [3, 4]  last 2 elements
mylist[::3]    # [1, 4]
mylist[::-3]   # [4, 1]



list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Iterator
people = ['John', 'Paul', 'Sara', 'Susan']
for person in people:
  print(f'Current Person: {person}')

for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# in operator

1 in [1, 2, 3] # True
0 in [1, 2, 3] # False

numbersTaken = [2, 5, 12, 13, 17]
for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)


values = [65, 76, 98, 54, 21]
avg = sum(values) / len(values)



def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)
drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])

# Continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# List of tuples
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
for i, j in friendships:
	print(i,j)

# range
for i in range(len(people)):
  print(people[i])

          1 
01234567890
Tuna McFish
>>> user = "Tuna McFish"
>>> user[0]
'T'
>>> user[5]
'M'
>>> user[-1]
'h'
>>> user[-3]
'i'
>>> user[2:7]
'na Mc'
>>> user[:7]
'Tuna Mc'
>>> user[2:]
'na McFish'
>>> user[:]
'Tuna McFish'
>>> len(user)
11


# Better: change range(len()) to enumerate()
# Define a collection, such as list:
names = ['Nik', 'Jane', 'Katie', 'Jim', 'Luke']

# Using the range(len(collection)) method, you'd write:
for i in range(len(names)):
    print(i, names[i])

# Using enumerate, you can define this by writing:
for idx, name in enumerate(names):
    print(idx, name)
    
# Both ways of doing this return:
# 0 Nik
# 1 Jane
# 2 Katie
# 3 Jim
# 4 Luke

for idx, name in enumerate(names, start=1):  # START AT 1
    print(idx, name)
    
# This returns:
# 1 Nik
# 2 Jane
# 3 Katie
# 4 Jim
# 5 Luke

# List of lists 
  
has some unique interaction mechanisms. 
Using bracket notation to retrieve an element at a certain index returns a list object. 
However, using bracket notation on the resulting list will actually return a data point 

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
list_of_lists[2][1]

data = [['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', '828'], ['Arlington', '503'], ['Atlanta', '1379']]
first_list = data[0]        # Returns the first list: ['Albuquerque', '749'].
first_list_first_value = first_list[0]  # Returns the first list's first element: 'Albuquerque'.

# Transpose of a matrix
a=[[1,2,3],
   [4,5,6],
   [7,8,9]] 
transpose = [list(i) for i in zip(*a)] 
transpose
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Generating Groups
groups = [(a, b) for a in ['a', 'b'] for b in [1, 2, 3]] 
groups  # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]


# Converting two lists into a dictionary
list1 = ['karl','lary','keera']
list2 = [28934,28935,28936]

# Method 1: zip()
dictt0 = dict(zip(list1,list2))

# Method 2: dictionary comprehension
dictt1 = {key:value for key,value in zip(list1,list2)}

# Method 3: Using a For Loop (Not Recommended)
tuples = zip(column_names, column_values) 
dictt2 = {} 
for key, value in tuples: 
  if key in dictt2: 
    pass
  else: 
    dictt2[key] = value
    
    
    

# Sorting a List of Strings
list1 = ["Karl","Larry","Ana","Zack"]

# Method 1: sort()
list1.sort()

# Method 2: sorted()
sorted_list = sorted(list1)

# Method 3: Brute Force Method 
size = len(list1)
for i in range(size): 
  for j in range(size): 
    if list1[i] < list1[j]: 
       temp = list1[i] 
       list1[i] = list1[j] 
       list1[j] = temp
print(list1)    