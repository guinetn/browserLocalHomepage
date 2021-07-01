# LIST COMPREHENSION
'''
A short hand way of creating a new list
More efficient than loops where the list in the loop is created with no elements initialised. 
In the list comprehension, we know what the size of the result is going to be: Python can allocate the memory upfront, which is much more efficient than dynamically adding to a list.

Not a good idea: Defining lambda expressions directly in a list comprehension
'''
  # Adding 2 to every number in an existing list:
  numbers = [1,2,3]
  [ x for x in numbers ]

  new_list = [ x+2 for x in numbers ]
  
  # Filtering elements in list comprehension
  new_list = [ x+2 for x in numbers if x in%2==0 ]

  MONTHS = ['January','February','March']
  YEARS = [2018,2019,2020]
  [m + " " + str(y) for y in YEARS for m in MONTHS]
  # ['January 2018',
  # 'February 2018',
  # ... 
  [[m + " " + str(y) for y in years] for m in months]
  # [['January 2018', 'January 2019', 'January 2020'],
  # ['February 2018', 'February 2019', 'February 2020'],
  # ...


  (x*x for x in range(0,10))

  l= [x**2 for x in range(0,5)]
  print(l)    0 1 4 9 16

 while i<5:
  print(i)
  i+=1


keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
>>> dictionary
{'a': 1, 'b': 2, 'c': 3}


# DOUBLE ITERATION IN LIST COMPREHENSION

romaia = [[1, 2], [3, 4]]
[x for b in a for x in b]
[1, 2, 3, 4]
[x for x in b for b in a]
[3, 3, 4, 4]


# Iterating over one column - `f` is some function that processes your data
result = [f(x) for x in df['col']]

# Iterating over two columns, use `zip`
result = [f(x, y) for x, y in zip(df['col1'], df['col2'])]

# Iterating over multiple columns - same data type
result = [f(row[0], ..., row[n]) for row in df[['col1', ...,'coln']].to_numpy()]

# Iterating over multiple columns - differing data type
result = [f(row[0], ..., row[n]) for row in zip(df['col1'], ..., df['coln'])]



# Without list comprehension
list_of_words = []
for sentence in text:
    for word in sentence:
       list_of_words.append(word)
return list_of_words
I like to think of list comprehension as stretching code horizontally.

Try breaking it up into:

# List Comprehension 
[word for sentence in text for word in sentence]
Example:

>>> text = (("Hi", "Steve!"), ("What's", "up?"))
>>> [word for sentence in text for word in sentence]
['Hi', 'Steve!', "What's", 'up?']


