# Strings 

Delimited by single or double quotation marks (but the quotes have to match):
single_quoted_string = 'data science'
double_quoted_string = "data science"

# Strings enclosed in tripe quotes (''') can span over multiple lines
multiline_string = """ this is a very
        long string which will not include 
        blanks or newlines..."""

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# 'this is a verylong string toowhich will NOT INCLUDE ANY EXTRA BLANKS OR NEWLINES...'
multiline_string = ("this is a very"
      "long string too"
      "which will NOT INCLUDE ANY EXTRA BLANKS OR NEWLINES..."
     ) 

# SUBSTRINGS
s = "hello joe"
s[6:]   # joe
s[:-3]  # joe

# Contains
if 'r' not in s: 
    passed
	
#Repeat String 
print( '- ' * 10 )

# Remove trailing 's'
term='cars'
if term[-1].lower() == 's':
    term = term[0:-1]
	
	
# Reverse a String
mystring = "Python is awesome"
mystring_reversed = mystring[::-1]
mystring_reversed # emosewa si nohtyP'

sentence = "This is just a test"
reversed = sentence[::-1]
print(reversed)


name = 'Brad'
tab_string = "\t"  		# \ Backslash: to encode special characters
tab_string      # '	'
not_tab_string = r"\t"  #  Raw string: to represents all characters '\' 
not_tab_string  # 't'


# Format number to strings
x=123.456789
xs = "{:3.2}".format(x)   # → 123.46




# STRING INTERPOLATION

 ## Old way
	
	%-format (old method)
		
		print("%s %s" %('Hello','World',))

		name = 'world'
		program ='python'
		print('Hello %s! This is %s.'%(name,program))

	Escaping percent sign with %%
	test = "have it break"
	selectiveEscape = "Print percent %% in sentence and not %s" % test
	print selectiveEscape
	Print percent % in sentence and not have it break.

## Python 3.6

	f-strings 
		user = 'Joe'
		print(f"I am {user}")   

		a = 12
		b = 3
		print(f'12 multiply 3 is {a * b}.')


		some_variable = "HELLO!"
		print(f"some_variable={some_variable}")
		# some_variable=HELLO!

		print(f"{some_variable=}")
		# some_variable=HELLO!


	Template
	
		Template Strings is simpler and less powerful mechanism of string interpolation
		from string import Template
		name = 'world'
		program ='python'
		new = Template('Hello $name! This is $program.')
		print(new.substitute(name= name,program=program))



name = "Abhay"
age = 21

## METHOD A: Concatenation
print("My name is "+name+", and I am "+str(age)+ " years old.")

## METHOD B: F-strings (Python 3+)
print(f"My name is {name}, and I am {age} years old")

## METHOD C: Join
print(''.join(["My name is ", name, ", and I am ", str(age), " years old"]))

#a List of Strings Into One String
words = ["This", "is", "a", "Test"]
combined = " ".join(words)
print(combined)

## METHOD 4: modulus operator
print("My name is %s, and I am %d years old." % (name, age))

## METHOD 5: format(Python 2 and 3)
print("My name is {}, and I am {} years old".format(name, age))




# immutable: can't change a part of it. s[1]='i' → Error xxxxxx

age = 37
print(str(age) + " years old")

i = 10
hello = "Hello world " + str(i)

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# Methods: lower() upper() strip() isdigit() isspace() find() replace() split() join()

s = 'my string'
s = "my string"
print(s)
print("a"+"b")
print("a"*3)   		aaa

#Duplicate Strings 
name = "Banana"
print(name * 4)

print("val = %e" % a) 		exponential     1.000000e+00
print("val = %f" % a) 		float 			1.000000
print("val = %s" % a) 		string 			1.0

print(s[0])
print(s[-1])  	last element
s[0-7]  		entre 0 et 7 (exclus)
s[:7] 			7 first
s[8:] 			from 8 to end
s[-10:] 		last 10 		
print(len(s)

s="ababababab"
s[0::2] "aaaaa"      slicing, step 2
s[1::2] "bbbbb"

s="12345678"
s[:0]   		''			
s[:-1]   		'1234567'
s[:-2]   		'123456'
s[1:-1:2] 		'246'





# String Methods
s = 'helloworld'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))
"python is a programming language.python is python".replace("python",'Java')

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Split a string into a list:
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)		

# Find position
myString = 'position of a char'
print(s.find('o'))    # -1 if not found
print(s.index('o'))   # valueError if not found

# string.index(s, sub[, start[, end]])
s = 'shak#spea#e'
c = '#'
print([pos for pos, char in enumerate(s) if char == c])
# which will print: [4, 9]

# Contains
if 'r' not in s: 
    pass

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())






#%%
# python.exe xxxx.py

# MANIPULATING STRINGS
# strings are immutable (cant changed). Any change to a string’s contents requires making a new copy.

# STRING CONCATENATION
s = "welcome " + "to Python"
print(s)


# STRING MULTIPLICATION
s = "LikeGeeks" * 2
print(s)

# CONCATENATE WITH NON-STRING
# You can concatenate with non-string by just converting the value to a string using the str() function like this:
s = "This is test number " + str(15)


# SEARCH FOR A SUBSTRING
s = "welcome to likegeeks website"
print(s.find("likegeeks"))   # find() prints the position of the first occurrence found. (else return -1)
# The find function starts from the first character, however, you can start from the nth character like this:
s = "welcome to likegeeks website"
print(s.find("likegeeks",12))
# Since we start from the 12th character, there is no word called likegeeks from that position so it will return -1.


# GET SUBSTRINGS
# So we got the index of the string we’re searching for, now we want to print that matched.
s = "first second third"
print(s[:2])
print(s[2:])
print(s[3:5])
print(s[-1])
# The first print line prints from the first character till the second character, while the second print line prints from the second character till the end. Notice the position of the colon. The count starts from zero.
# If you use a negative number, the counting will start backward instead, like the fourth print line which prints the last character in the string.


# REPLACE STRINGS
# You can replace a string using the replace method like this:
s = "This website is about programming"
s2 = s.replace("This", "That")
print(s2)
# If you have many occurrences and you want to replace the first occurrence only, you can specify that:
s = "This website is about programming I like this website"
s2 = s.replace("website", "page",1)
print(s2)
# The first word only got replaced.


# STRIP STRINGS
# You can trim white spaces from a string using the strip method like this:
# strip: remove all the unnecessary space
s = "   This website is about programming    "
print(s.strip())
# You can strip from the right only or left only using rstrip() or lstrip() methods respectively.

# CHANGE CASE
# You can change the case of the characters if you want to compare them or something.
s = "Welcome to likegeeks"
print(s.upper())
print(s.lower())


# CONVERT STRINGS TO NUMBERS
# str() function which casts the value to a string, but this is not the only cast function in Python programming.
# int() function cast the input to integer
# float() function cast the input to float.
# long()
s="10"
s2="20"
print(s+s2)
print(int(s)+int(s2))
# The first print line just concatenates the two numbers without summation, while the second print line adds the two values and print the total.


# COUNT STRINGS
# You can use the min(), max() and len() functions to calculate the minimum character or maximum character value or the total length of characters.
s = "welcome to likegeeks website"
print(min(s))
print(max(s))
print(len(s))


# ITERATE OVER STRINGS
# You can iterate over the string and manipulate every character individually like this:
s = "welcome to likegeeks website"
for i in range(len(s)):	# The len() function counts the length of objects.
	print(s[i])


# ENCODE STRINGS
# If you are using Python 3, all strings are stored as Unicode strings by default, but if you are using Python 2 you may need to encode your strings like this:
str="welcome to likegeeks website"
str.encode('utf-8')
print(s)

# Printing Patterns
n = 5
print('\n'.join('😀' * i for i in range(1, n + 1)))
😀
😀😀
😀😀😀
😀😀😀😀
😀😀😀😀😀


#Most Frequent Element in a List
test = [6, 2, 2, 3, 4, 2, 2, 90, 2, 41]
most_frequent = max(set(test), key = test.count)
print(most_frequent)


# Rich: Beautiful Text Formatting

open-source python library that is used for beautiful text-formatting. It contains a large variety of text-formatting options whether it is a font, color of text, or style of the text Rich got it all covered. 

pip install rich

from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
import os
import sys
from rich.columns import Columns
from rich.markdown import Markdown
from rich.syntax import Syntax

print("Hello, [bold red]World[/bold red]!")
print("Hello, [italic red]World[/italic red]!")

console = Console()
console.print("Hello", "World!")
console.print("Hello", "World!", style="italic magenta")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# Emoji’s
console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon: :cry: :thumbs_down: :kiss: :cool:")

Formatting Tables
# Table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
console.print(table)

Markdown function
for i in 'i am best programmer'.split():
    markdown = Markdown(i)
    console.print(markdown)