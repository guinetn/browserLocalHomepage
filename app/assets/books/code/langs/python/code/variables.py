# A variable is a container for a value, which can be of various types

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
  - Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Case-sensitive (age, Age and AGE are three different variables)
"""

# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str
# is_cool = True  # bool

a = 1
b = 3.14
c = "hello" 
d = 'joe'
e = '''multi lines
	string'''
f = True
g = False
h = int("5.6")

#Duplicate Strings 
name = "Banana"
print(name * 4)

# Prints the Unique ID of a Variable
# id() method allows you to find the unique id of a variable. You just need to pass the variable name in the method.
print( id(a) )

# Declared in the global context
API_KEY = "ABCDEF1234"

def demo():
   # This works fine
   print(API_KEY)
   # local context declaration
   SECRET_STRING = "my secret"

# Doesn't work: error undefined variable: 'SECRET_STRING'
print(SECRET_STRING)

# Multiple Variable Assignments
x, y, name, is_cool = (1, 2.5, 'John', True)
a,b,c = 4,5.5,'Hello'
print(a,b,c) 

a,b,*c = [1,2,3,4,5]
print(a,b,c) # 1 2 [3,4,5]

# Swapping Two Variables
a = 4
b = 5
a,b = b,a
print(a,b) >> 5,4

# Basic math
a = x + y
string_result = c + ' ' + d
print(string_result)

# Casting
x_to_string = str(x)
y_to_int    = int(y)
z_to_float  = float(y)

print(type(z), z)

# PrecisionWidth and FieldWidth

''' Fieldwidth is the width of the entire number
''' Precision is the width towards the right
print( "%f" % 3.121312312312)   # '3.121312'

#Notice upto 6 decimal points are returned. To specify the number of decimal points, `%(field-width).(precisionwidth)f' is used.
print( In [15]: "%.5f" % 3.121312312312)   # '3.12131'
If the field width is set more than the necessary than the data right aligns itself to adjust to the specicified
values.
print( In [16]: "%9.5f" % 3.121312312312)   # ' 3.12131'
Zero padding is done by adding a 0 at the start of fieldwidth.
print( In [17]: "%020.5f" % 3.121312312312)   # '00000000000003.12131'
For proper alignment, a space can be left blank in the eld width so that when a negative number is
used, proper alignment is maintained.
print "% 9f" % 3.121312312312
3.121312
print "% 9f" % -3.121312312312
-3.121312
`+' sign can be returned at the beginning of a positive number by adding a + sign at the beginning of the field width.
print "%+9f" % 3.121312312312
+3.121312
print "% 9f" % -3.121312312312
-3.121312



# isinstance( ) returns True, if the 1st argument is an instance of that class. Multiple classes can also be checked at once.
print( isinstance(1, int) )           # True
print( isinstance(1.0,int) )          # False 
print( isinstance(1.0,(int,float)) )  # True

# OPERATORS

'''
+ 	Addition
- 	Substraction
* 	Multiplication
** 	Exponentiation
/   Division
% 	Modulus
//	floor division
'''
print(1/2)
print(1/2.0)
print(15%10)   		# 5
print(2.8//2.0)   	# 1.0

# divmod(x,y) outputs the quotient and the remainder in a tuple in the format (quotient, remainder)
print( divmod(9,2) )  # (4, 1)
print( pow(3,3))      # 27
print( pow(3,3,5) )   # 2


# RELATIONAL OPERATORS

'''
==
!=
<
>
<=
>=
'''

# cmp(x,y)
'''
	x < y -1
	x == y 0
	x > y 1
'''
print( cmp(1,2) )  # -1
print( cmp(2,1) )  #  1
print( cmp(2,2) )  #  0


# BITWISE OPERATORS

'''
& 	Logical and
| 	Logical oe
^   Xor
~   Negate
>>  Right shift
<<  Left shift
'''

print(5>>1)
'''
0000 0101 -> 5
Shifting the digits by 1 to the right and zero padding
0000 0010 -> 2
'''

# BOOL
Booleans in Python are capitalized:

one_is_less_than_two = 1 < 2 # equals True
true_equals_false = True == False # equals False

# 'None' value to indicate a nonexistent value ~ null in others languages
x = None
print x == None # prints True, but is not Pythonic
print x is None # prints True, and is Pythonic
safe_x = x or 0 # definitely a number 

“Falsy”:
• False
• None
• [] (an empty list)
• {} (an empty dict)
• ""
• set()
• 0
• 0.0

Pretty much anything else gets treated as True

all(): returns True when every list element is truthy
is truthy:
all([True, 1, { 3 }]) # True
all([True, 1, {}]) # False, {} is falsy

any(): returns True when at least one element is truthy
any([True, 1, {}]) # True, True is truthy
all([]) # True, no falsy elements in the list
any([]) # False, no truthy elements in the list


# CONVERSION
hex(170)  '0xaa'
oct(8)    '010'

print int('010', 8)     # 8
print int('0xaa', 16)   # 170
print int('1010', 2)    # 10

chr(98)  # b
ord('b') # 98


# range( ) function outputs the integers of the specied range. It can also be used to generate a series by
# specifying the dierence between the two numbers within a particular range. The elements are returned in a list (will be discussing in detail later.)
print( range(3) )      # [0, 1, 2]
print( range(2,9) )    # [2, 3, 4, 5, 6, 7, 8]
print( range(2,27,8) ) # [2, 10, 18, 26]