# buil-in-functions

Python has many built-in functions improving code clarity and decomposing complex problem into simpler pieces of code


## hash()
Return the hash value of an object if it has one. Hash values are integer numbers that are used to compare dictionary keys during a dictionary lookup.
input: immutable object
returns the hash value of that object

str1 = "Hello World"
a = 12.5
tup = ('a', 'b', 'c')

print('hash value for a string: ', hash(str1))
print('hash value for a decimal: ', hash(a))
print('hash value for a tuple: ', hash(tup))

hash value for a string:  5497742200142074869
hash value for a decimal:  1152921504606846988
hash value for a tuple:  -5693404743884429734

##  map()
Execute a specified function for each item in an iterable that it takes as input

def square(n):
    return n * n

num_list = [1,2,3,4]
result = map(square, num_list)
print('Mapped result is: ', list(result))

## zip()
map a similar index of passed iterators so that they can be used using a single entity

numbers = [1, 2, 3]
letters = ['One', 'Two', 'Three']

result = zip(numbers, letters)

# converting values to print as set
result = set(result)
print('The zipped result is: ', result)


## eval()
evaluate Python expressions from a string-based or compiled-code-based input.
In simple words, the eval function evaluates a string input as a python expression and returns the output as an integer.
result1 = eval('10 + 15')

result2 = eval('3 * 8')

print(result1)
print(result2)

## split() 
returns a list of the string after splitting the given string by the specified separator.

txt1 = "apple#banana#cherry#orange"
txt2 = "Hello how are you"

result1= txt1.split("#")
result2 = txt2.split(" ")

print(result1)
print(result2)

## ord

ord()
This function is used to return the Unicode code point of a given character. The ord() function takes a character as input and then returns an integer number representing the given input character’s Unicode code point.
Syntax: ord(character)

x = ord('a')
y = ord('$')
z = ord(' ')   #space character

print(x) # 97
print(y) # 36
print(z) # 32


##  dir()
list of all the attributes of the specified object. It returns all the properties, even built-in properties that are the default for all objects.

class Student:
  name = "Joy",
  age = 16,
  rollNo = 25
  
print(dir(Student))

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'age', 'name', 'rollNo']

## pow()
x = pow(2, 3)
y = pow(3, 3)