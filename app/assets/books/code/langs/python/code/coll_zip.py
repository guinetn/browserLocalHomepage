# zip Argument Packing/Unpacking
# transforms multiple lists into a single list OF TUPLES of corresponding elements
# If the lists are different lengths, zip stops as soon as the first list ends

# zip: write less code and do more operations.

zip(('a', 1), ('b', 2), ('c', 3))   #  [('a','b','c'), ('1','2','3')].

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2) 		# [('a', 1), ('b', 2), ('c', 3)]


# unzip: * (asterisk) performs argument unpacking
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

def add(a, b): return a + b
add(1, 2) 		# returns 3
add([1, 2]) 	# TypeError!
add(*[1, 2]) 	# returns 3



# Get dictionaries instead of tuples
names = ['Nik', 'Jane', 'Melissa', 'Doug']
ages = [32, 28, 37, 53]
gender = ['Male', 'Female', 'Female', 'Male']
ages = dict(zip(names,ages))
print(ages)
# {'Nik': 32, 'Jane': 28, 'Melissa': 37, 'Doug': 53}



coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)

result_list = list(result)
print(result_list)



c, v =  zip(*result_list)
print('c =', c)
print('v =', v)


number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()
# Converting itertor to list
result_list = list(result)
print(result_list)



#  Zip Less or More Iterables at Once
id = [1, 2, 3, 4]
record = zip(id)
print(list(record))
# [(1,), (2,), (3,), (4,)]

id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
sex = ['male', 'male', 'male', 'male']
record = zip(id, leaders, sex)
print(list(record))
# [(1, 'Elon Mask', 'male'), (2, 'Tim Cook', 'male'), (3, 'Bill Gates', 'male'), (4, 'Yang Zhou', 'male')]




first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']
names = zip(first, last)
for a, b in names:
    print(a, b)

# Rranspose of a Matrix
matrix = [[1, 2, 3], [1, 2, 3]]
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)
# [[1, 1], [2, 2], [3, 3]]    

#  Zip Function in For-Loops
products = ["cherry", "strawberry", "banana"]
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is £{p-c}!')
# The profit of a box of cherry is £1.5!
# The profit of a box of strawberry is £1.5!
# The profit of a box of banana is £3!


# Create and Update Dictionaries by the Zip Function
id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']

# create dict by dict comprehension
leader_dict = {i: name for i, name in zip(id, leaders)}
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# create dict by dict function
leader_dict_2 = dict(zip(id, leaders))
print(leader_dict_2)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# update
other_id = [5, 6]
other_leaders = ['Larry Page', 'Sergey Brin']
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou', 5: 'Larry Page', 6: 'Sergey Brin'}



# Deal With Unequal Length Arguments
# By default, the result of the zip function is based on the shortest iterable.

id = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(id, leaders)
print(list(record))
# [(1, 'Elon Mask'), (2, 'Tim Cook')]


from itertools import zip_longest
id = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
long_record = zip_longest(id, leaders)  # itertools.zip_longest: its result is based on the longest argument
print(list(long_record))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), (None, 'Bill Gates'), (None, 'Yang Zhou')]
long_record_2 = zip_longest(id, leaders, fillvalue='Top')
print(list(long_record_2))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), ('Top', 'Bill Gates'), ('Top', 'Yang Zhou')]




# unzip
# Python doesn’t have an unzip function. However, if we are familiar with the tricks of asterisks, unzipping is a very simple task.

record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
id, leaders = zip(*record)
#  the asterisk did the unpacking operation, which is unpacking all the four tuples from the record list.
print(id)
# (1, 2, 3, 4)
print(leaders)
# ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')


record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
print(*record)  # unpack the list by one asterisk
# (1, 'Elon Mask') (2, 'Tim Cook') (3, 'Bill Gates') (4, 'Yang Zhou')
id, leaders = zip((1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou'))
print(id)
# (1, 2, 3, 4)
print(leaders)
# ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')