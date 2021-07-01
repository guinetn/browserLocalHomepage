# REGEX - REGULAR EXPRESSIONS
# a way of searching text. useful but complicated

- https://www.tutorialspoint.com/python/python_reg_expressions.htm
- https://docs.python.org/3/howto/regex.html


import re
re.split("[ab]", "carbs"), 	    # split on a or b to ['c','r','s']
re.sub("[0-9]", "-", "R2D2") 	# Replace digits with dashes. R-D-


# Matching Versus Searching: all checks for a match…
#   match    …only at the beginning of the string
#   search   … anywhere in the string 

#!/usr/bin/python
import re
re.search("c", "dog") 		    # contains
re.match("a*", "cat") 		    # starts with

# EXTRACT SOME PARTS OF A STRING 
line = "Cats are smarter than dogs";
found = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if found:
   print "found.group() : ", found.group()      # Cats are smarter than dogs
   print "found.group(1) : ", found.group(1)    # Cats
   print "found.group(2) : ", found.group(2)    # smarter
else:
   print "Nothing found!!"



import re
my_regex = re.compile("[0-9]+", re.I)
# 'regex' alias if you already had a different 're' in your code
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)



import re
print(all([ 					            # ALL OF THESE ARE TRUE, BECAUSE
	not re.match("a", "cat"), 		        # * 'cat' doesn't start with 'a'
	re.search("a", "cat"), 			        # * 'cat' has an 'a' in it
	not re.search("c", "dog"), 		        # * 'dog' doesn't have a 'c' in it
	3 == len(re.split("[ab]", "carbs")), 	# * split on a or b to ['c','r','s']
	"R-D-" == re.sub("[0-9]", "-", "R2D2") 	# * replace digits with dashes
	])) # True


# Remove trailing 's'
term='cars'
if term[-1].lower() == 's':
    term = term[0:-1]


para='''Game of Thrones is an fantasy drama television series
created by David Benioff and D. B. Weiss. It is an adaptation
of A Song of Ice and Fire, George R. R. Martin series of fantasy
novels, the first of which is A Game of Thrones. It is filmed in
Belfast and elsewhere in the United Kingdom, Canada, Croatia,
Iceland, Malta, Morocco, Spain, and the United States. The series
premiered on HBO in the United States on April 17, 2011, and its
seventh season ended on August 27, 2017. The series will conclude
with its eighth season premiering in 2019.'''

# Extract all characters from the paragraph
import re
pattern = r'.'
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)

# Extracts only word character
import re
pattern = r'\w'
patter_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)

# Extract only numeric digits from it
import re
pattern = r'\d'
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)


# Extract all of the words and numbers
import re
pattern = r'\w+'
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)

# Extract only numbers
import re
pattern = r'\d+'
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)

# Extract the beginning word
import re
pattern = r'^\w+'
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)

# Extract first two characters from each word (not the numbers)
import re
pattern = r'\b[a-zA-Z].'     # \b, which define the word boundary
pattern_regex = re.compile(pattern)
result = pattern_regex.findall(para)
print(result)

# Find out all of the words, which start with a vowel
import re
pattern = r'\b[aeiou]\w+'
pattern_regex = re.compile(pattern, re.IGNORECASE)
result = pattern_regex.findall(para)
print(result)

# Find out all of the words, which start with a consonant
import re
pattern = r'\b[^aeiou0-9 ]\w+'
pattern_regex = re.compile(pattern, re.IGNORECASE)
result = pattern_regex.findall(para)
print(result)

# Count total numbers of a, an and the
import re
pattern = r'the|a|an'
pattern_regex = re.compile(pattern, re.IGNORECASE)
result = pattern_regex.findall(para)
len(result)

# Substitutions
# re.sub(pattern, repl, string, count=0, flags=0)
# Find 'pattern' in 'string' and replace it with replacement string 'repl'

print(re.sub(r'\d', '*', 'User\'s mobile number is 1234567890'))
def hide_reserve_3(s):
    return '*' * (len(s[0])-3) + s[0][-3:]
print(re.sub(r'\d+', hide_reserve_3, "User\'s #1 mobile number is 1234567890"))
print(re.sub(r'\d+', lambda s: '*' * (len(s[0])-3) + s[0][-3:], 'User\'s #2 mobile number is 1234567890'))

# Generate a Dictionary
print('Generate a Dictionary')
res = re.match(
    r"My name is (?P<first_name>\w+) (?P<last_name>\w+) and I like (?P<preference>\w+).", 
    "My name is Christopher Tao and I like Python."
).groupdict()
print(res)

# Catch Repeat Patterns
pair = re.compile(r'''
    .*    # Match any number of any charaters
    (.)   # Match 1 character, whatever it is (except new-line), this will be the "group 1"
    .*    # Match any number of any charaters
    \1    # Match the group 1
''', re.VERBOSE)
print("repeated chars: "+  pair.match('abcdefgc').groups()[0])


def test_re():
    """String Pattern Matching"""

    assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
        'foot',
        'fell',
        'fastest'
    ]

    assert re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') == 'cat in the hat'

    # When only simple capabilities are needed, string methods are preferred because they are
    # easier to read and debug:
    assert 'tea for too'.replace('too', 'two') == 'tea for two'


# Counting occurrence of a pattern
import re; 
len(re.findall('python','python is a programming language. python is python.'))  # 3

