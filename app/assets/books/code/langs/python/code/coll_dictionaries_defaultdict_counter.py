# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Associates values with keys
# Dictionary keys must be immutable
# fast value retrieve (hash is used, O(1) retrieve)

"""
Similar to hashmap or hash tables in other languages, a dictionary is a collection of key/value pairs. You initialize an empty dictionary with empty curly braces and fill it with colon-separated keys and values. All keys are unique, immutable objects.
Unordered, Mutable collections of data, where the data is stored in the form of key:value pairs. The values can be accessed directly if their keys are known, without having to iterate over. The data is enclosed in curly brackets. The values can be mutable and repetitive, but keys have to be unique and immutable.
Use Case: Dictionaries are useful when you need instant access to data, without having to iterate over all the values. For example, employee data can be stored in dictionaries.
"""

# Create dict

empty_dict = {} # Pythonic
empty_dict2 = dict() # less Pythonic
grades = { "Joel" : 80, "Tim" : 95 } # dictionary literal

# Add values
grades["Paul"] = 88

# Get values
joels_grade = grades["Joel"] # equals 80

joels_grade.keys()  
joels_grade.values()  

# Stop Using Square Brackets To Get Dictionary Items — Use .get()
joels_grade = grades["Joe"]  # KeyError: 'location', to avoid this:
print(grades.get('Joe'))     # → None 


# default value
joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals 0
no_ones_grade = grades.get("No One") # default default is None

# Assign key-value pairs
grades["Tim"] = 99 # replaces the old value
grades["Kate"] = 100 # adds a third entry
num_students = len(grades) # equals 3


# KeyError if you ask for a key that’s not in the dictionary
try:
  kates_grade = grades["Kate"]
except KeyError:
  print("no grade for Kate!")

# check for the existence of a key using in:
joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False

# use dictionaries as a simple way to represent structured data
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

print(person.keys()) 	# Get dict keys
print(person.valuess())	# Get dict values

# Get dict items
print(person.items())    # returns a list of its key-value pairs
# .iteritems() lazily yields the key-value pairs one at a time as we iterate over it: a generator

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
del person['age']
person.pop('phone')
person.popitem() 

# Clear
person.clear()
del Employee        # deletes the dictionary

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])


classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' asks too many questions'}
for k, v in classmates.items():
    print(k + v)

# Merging Two Dictionaries
basic_information = {"name":['karl','Lary'],"mobile":["0134567894","0123456789"]}
academic_information = {"grade":["A","B"]}
details = dict() ## Combines Dict

## Dictionary Comprehension Method
details = {key: value for data in (basic_information, academic_information) for key,value in data.items()}
print(details)

## Dictionary unpacking
details = {**basic_information ,**academic_information}
print(details)

## Copy and Update Method
details = basic_information.copy()
details.update(academic_information)
print(details)


# in
groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duck tape', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
  print("You already have milk hoss!")
else:
  print("Oh yea, you need milk!")




# dictionary nlname:(color, marker, nlfun)
nlfuns = {
    'Rectifier (Relu)': ('b', '', lambda x: np.maximum(0, x)),
    'Softplus': ('g', '', lambda x: np.log(1 + np.exp( 1 * x))/ 1),
    'Sigmoid':  ('r', '', lambda x: 1/(1.0+np.exp(-1 * x)))
#   'Exponential':   ('c', '', lambda x: np.exp(x))
}
for nlname, (color, marker, nlfun) in nlfuns.items():
    plt.plot(evalpoints, list(map(nlfun, evalpoints)), hold=True, label=nlname, color=color, marker=marker)


# defaultdict
Ex: Count words in a document

#1. 
word_counts = {}
for word in document:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1

#2. “forgiveness is better than permission” 
word_counts = {}
for word in document:
  try:
    word_counts[word] += 1
  except KeyError:
    word_counts[word] = 1

#3.
word_counts = {}
for word in document:
  previous_count = word_counts.get(word, 0)
  word_counts[word] = previous_count + 1

# 4. defaultdict

from collections import defaultdict
word_counts = defaultdict(int) # int() produces 0
for word in document:
  word_counts[word] += 1

Useful with list or dict or even your own functions:
dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1) # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict) # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle" # { "Joel" : { "City" : Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1 # now dd_pair contains {2: [0,1]}

# 5. Counter & most_common
# Turns a sequence of values into a defaultdict(int)-like object mapping keys to counts. 

from collections import Counter
word_counts = Counter(document)

c = Counter([0, 1, 2, 0]) # c = { 0 : 2, 1 : 1, 2 : 1 }

# 10 most common words and their counts
for word, count in word_counts.most_common(10):
  print word, count


# sorting

# Declaring the hash function      
 key_value ={}    
   
# Initialize value 
 key_value[2] = 56       
 key_value[1] = 2 
 key_value[5] = 12 
 key_value[4] = 24
 key_value[6] = 18      
 key_value[3] = 323 
   
 print ("Task 2:-\nKeys and Values sorted in", 
            "alphabetical order by the key  ")  
  
 # sorted(key_value) returns an iterator over the 
 # Dictionary’s value sorted in keys.  
 for i in sorted (key_value) :
    print ((i, key_value[i]), end =" ")


# sorted by value

sorted(d.items(), key=lambda x: x[1])
sorted(d.items(), key=lambda x: x[1], reverse=True)
d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = sorted(d.items(), key=lambda x: x[1])    
print(a)

>>> from collections import OrderedDict
>>> d_sorted_by_value = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
The OrderedDict behaves like a normal dict:

>>> for k, v in d_sorted_by_value.items():
...     print "%s: %s" % (k, v)
...
first: 1
second: 2
third: 3
fourth: 4

>>> d_sorted_by_value
OrderedDict([('first': 1), ('second': 2), ('third': 3), ('fourth': 4)])

>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
or

>>> dict(sorted(x.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
