# Asterisk prefix operator: * and **

# Asterisks for unpacking into function call

	* to unpack the remaining items in an iterable:
	first, second, *rest = [1, 2, 3, 4, 5, 6]
	>>> first
	1
	>>> second
	2
	>>> *rest
	[3, 4, 5, 6]

	** operator does something similar with keyword arguments
	to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call.
	persons = [
	  {'first_name': 'Louis', 'last_name': 'de Bruijn', 'age': 26, 'profession': 'Data Scientist'},
	  {'first_name': 'Pietje', 'last_name': 'Puk', 'age': 18, 'profession': 'student'},
	]
	for cnt, person in enumerate(persons):
	  print("Person {0}'s occupation is {profession}.".format(cnt, **person))
	>>> Person 0's occupation is Data Scientist.
	>>> Person 1's occupation is student.



	print() and zip() accept any number of positional arguments 

	Unpack an iterable into the arguments in the function call

	def add(a, b): return a + b
	add(1, 2) 		# returns 3
	add([1, 2]) 	# TypeError !
	add(*[1, 2]) 	# returns 3

	fruits = ['lemon', 'pear', 'watermelon', 'tomato']
	print(fruits) 										# ['lemon', 'pear', 'watermelon', 'tomato']
	print(fruits[0], fruits[1], fruits[2], fruits[3]) 	# lemon pear watermelon tomato
	print(*fruits) 										# lemon pear watermelon tomato

	# unzip: * (asterisk) performs argument unpacking
	pairs = [('a', 1), ('b', 2), ('c', 3)]
	letters, numbers = zip(*pairs)


	# Rranspose of a Matrix
	matrix = [[1, 2, 3], [1, 2, 3]]
	matrix_T = [list(i) for i in zip(*matrix)]
	print(matrix_T)
	# [[1, 1], [2, 2], [3, 3]]    
	
	** operator 
		to take a dictionary (key-value pairs) and unpack it into keyword arguments in a function call.
		date_info = {'year': "2020", 'month': "01", 'day': "01"}
		filename = "{year}-{month}-{day}.txt".format(**date_info)
		filename 	# '2020-01-01.txt'

# Asterisks for packing arguments given to function

	from random import randint

	def roll(*dice): return sum(randint(1, die) for die in dice)
	roll(20) 	   18
	roll(6, 6)		9
	roll(6, 6, 6)	8

	
	def tag(tag_name, **attributes):
	    attribute_list = [f'{name}="{value}"' for name, value in attributes.items() ]
	    return f"<{tag_name} {' '.join(attribute_list)}>"
		
	That ** will capture any keyword arguments we give to this function into a dictionary which will that attributes arguments will reference.
	tag('a', href="http://treyhunner.com")				'&lt; a href="http://treyhunner.com" &gt;'
	tag('img', height=20, width=40, src="face.jpg")		'&lt; img height="20" width="40" src="face.jpg" &gt;'

# Positional arguments with keyword-only arguments

	def get_multiple(*keys, dictionary, default=None):
	    return [ dictionary.get(key, default) for key in keys ]
	
	fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
	get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown')  
	#	['yellow', 'red', 'unknown']

# Keyword-only arguments without positional arguments


# Asterisks in tuple unpacking

	fruits = ['lemon', 'pear', 'watermelon', 'tomato']
	first, second, *remaining = fruits
	remaining #	['watermelon', 'tomato']
	first, *remaining = fruits
	remaining  # 	['pear', 'watermelon', 'tomato']
	first, *middle, last = fruits
	middle #	['pear', 'watermelon']

# Asterisks in list literals


# Double asterisks in dictionary literals


# Python’s asterisks are powerful


# Practice makes perfect


Using * and ** to pass arguments to a function
Using * and ** to capture arguments passed into a function
Using * to accept keyword-only arguments
Using * to capture items during tuple unpacking
Using * to unpack iterables into a list/tuple
Using ** to unpack dictionaries into other dictionaries




"""Unpacking Argument Lists

@see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

Unpacking arguments may be executed via * and ** operators. See below for further details.
"""


def test_function_unpacking_arguments():
    """Unpacking Argument Lists"""

    # The situation may occur when the arguments are already in a list or tuple but need to be
    # unpacked for a function call requiring separate positional arguments. For instance, the
    # built-in range() function expects separate start and stop arguments. If they are not
    # available separately, write the function call with the *-operator to unpack the arguments out
    # of a list or tuple:

    # Normal call with separate arguments:
    assert list(range(3, 6)) == [3, 4, 5]

    # Call with arguments unpacked from a list.
    arguments_list = [3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]

    # In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
    def function_that_receives_names_arguments(first_word, second_word):
        return first_word + ', ' + second_word + '!'

    arguments_dictionary = {'first_word': 'Hello', 'second_word': 'World'}
    assert function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'



# Example 1: shuffle data to ensure random class distribution in train/test split
import random
documents = ["positive tweet message", "negative tweet message"]
labels = ["pos", "neg"]

tuples = [(doc, label) for doc, label in zip(documents, labels)]
random.shuffle(tuples)
X, Y = zip(*tuples)


# Example 2: merging two dictionaries
first_dictionary = {"A": 1, "B": 2}
second_dictionary = {"C": 3, "D": 4}
merged_dictionary = {**first_dictionary, **second_dictionary}
>>> merged_dictionary
{"A": 1, "B": 2, "C": 3, "D": 4}


# Example 3: dropping unneccesary function variables
def return_stuff():
  """Example function that returns data."""
  return "This", "is", "interesting", "This", "is", "not"

a, b, c, *_ = return_stuff()