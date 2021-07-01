# if

if 1 > 2:
	message = "if only 1 were greater than two..."
elif 1 > 3:
	message = "elif stands for 'else if'"
else:
	message = "when all else fails use else (if you want to)"


# Ternary

parity = "even" if x % 2 == 0 else "odd"


# Loops

for x in [1,2,3]:
  print(x)

for x in range(4): 
  print(x)      0 1 2 3

for x in ["big","foot","feet"]:
  print(x)

cities = ["Austin", "Dallas", "Houston"]
for city in cities:
    print(city)
    
for c in "MyName"
  print(c)

s = "hello"
for idx, c in enumerate(s):
  print(idx, c)         0  h    1  e  ....

for key,value in params.items():
  print("%s = %s" % (key,value))

for key in params
  print(key)

# LIST COMPREHENSION: see list
  # Adding 2 to every number in an existing list:
  numbers = [1,2,3]
  new_list = [ x+2 for x in numbers ]

  l= [x**2 for x in range(0,5)]
  print(l)    0 1 4 9 16

 while i<5:
  print(i)
  i+=1




# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
  print(f'Current Person: {person}')

# Break
for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue
for x in range(10):
	if x == 3:
		continue # go immediately to the next iteration
	if x == 5:
		break # quit the loop entirely
	print x

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

for i in range(0, 11):
  print(f'Number: {i}')




# enumerate: produces tuples (index, element)

# not Pythonic
for i in range(len(documents)):
  document = documents[i]
  do_something(i, document)

i = 0
for document in documents:
  do_something(i, document)
  i += 1

# Pythonic: enumerate produces tuples (index, element):
for i, document in enumerate(documents):
  do_something(i, document)

# want just the indexes:
for i in range(len(documents)): do_something(i) # not Pythonic
for i, _ in enumerate(documents): do_something(i) # Pythonic




# While loops execute a set of statements as long as a condition is true.

# Infinite loop
while True:
   print("I will never stop!")
   
count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1

while True:
    try:
        number = int(input("What's your fav number hoss?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("loop complete")




#from 0 to 10
for x in range(10):
    print(x)

#from 5 to 12
for x in range(5, 12):
    print(x)

#from 10 to 40 increment value 5
for x in range(10, 40, 5):
    print(x)

# "is"
magicNumber = 15
for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number ! ")
        break
    else:
        print(n)

name = "joe"
if name is "joe":
    print("Hey there Bucky")





# List Comprehensions: transform a list into another (filter, transorm..)


squares = [x * x for x in range(5)] 			# [0, 1, 4, 9, 16]

even_squares = [x * x for x in even_numbers] 		# [0, 4, 16]

even_numbers = [x for x in range(5) if x % 2 == 0] 	# [0, 2, 4]

num_friends_good = [x for i, x in enumerate(num_friends) if i != outlier]


# lists → dictionaries
# lists → sets

square_dict = { x : x * x for x in range(5) } # { 0:0, 1:1, 2:4, 3:9, 4:16 }

square_set = { x * x for x in [1, -1] } # { 1 }

# Use _ if you don’t need the value from the list
zeroes = [0 for _ in even_numbers] # has the same length as even_numbers

A list comprehension can include multiple fors:
pairs = [(x, y)
	for x in range(10)
	for y in range(10)] 	# 100 pairs (0,0) (0,1) ... (9,8), (9,9)

increasing_pairs = [(x, y) 		# only pairs with x < y,
	for x in range(10) 		# range(lo, hi) equals
	for y in range(x + 1, 10)] 	# [lo, lo + 1, ..., hi - 1]


def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"] 	# for each of user's friends
            for foaf in friend["friends"]] 	# get each of _their_ friends

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# https://www.analyticsvidhya.com/blog/2016/02/bigmart-sales-solution-top-20
#Filter categorical variables
categorical_columns = [x for x in data.dtypes.index if data.dtypes[x]=='object']



###################
# Not-So-Basics
###################

foods = ['bacon', 'tuna', 'ham', 'snausages', 'beef']
for f in foods[:2]:
    print(f)
    print(len(f))


classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' asks too many questions'}
for k, v in classmates.items():
    print(k + v)


total_connections = sum(number_of_friends(user) for user in users) 	# 24

from collections import Counter # not loaded by default
def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]  # for each of my friends
                   for foaf in friend["friends"]  # count *their* friends
                   if not_the_same(user, foaf)    # who aren't me
                   and not_friends(user, foaf))   # and aren't my friends



# dictionary nlname:(color, marker, nlfun)
nlfuns = {
    'Rectifier (Relu)': ('b', '', lambda x: np.maximum(0, x)),
    'Softplus': ('g', '', lambda x: np.log(1 + np.exp( 1 * x))/ 1),
    'Sigmoid':  ('r', '', lambda x: 1/(1.0+np.exp(-1 * x)))
#   'Exponential':   ('c', '', lambda x: np.exp(x))
}
for nlname, (color, marker, nlfun) in nlfuns.items():
    plt.plot(evalpoints, list(map(nlfun, evalpoints)), hold=True, label=nlname, color=color, marker=marker)




#Exclude ID cols and source:
categorical_columns = [x for x in categorical_columns if x not in ['Item_Identifier','Outlet_Identifier','source']]
#Print frequency of categories
for col in categorical_columns:
    print '\nFrequency of Categories for varible %s'%col
    print data[col].value_counts()
    
    
    
# create a random DataFrame

{ '': , '':, '': } 
{ 'Country': , 'Price':, 'Year': } 
{ 'Country': ['US','GB']*3, 'Price':, 'Year': } 
{ 'Country': ['US','GB']*3, 'Price': np.random.randint(50, size=6), 'Year': } 
{ 'Country': ['US','GB']*3, 'Price': np.random.randint(50, size=6), 'Year': [i for i in range(1990,1993,1) for j in range(3) ] } 