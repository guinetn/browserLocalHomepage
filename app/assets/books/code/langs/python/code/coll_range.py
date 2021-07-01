# iterables: range

# range(from, to, step)

# range(max_not_included)
# 0 to max_not_included-1

# range(from, to)
#         ↑    ↑
#    include  not include

x = range(10) # is the list [0, 1, ..., 9]
zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nine = x[-1] # equals 9, 'Pythonic' for last element
eight = x[-2] # equals 8, 'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 9]


for i in range(5, 10):
   print(i)
# 5 6 7 8 9

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)

for i in range(len(people)):
  print(people[i])    

list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l= [x**2 for x in range(0,5)]
  print(l)    0 1 4 9 16


list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(0,10,3))
[0, 3, 6, 9]


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
