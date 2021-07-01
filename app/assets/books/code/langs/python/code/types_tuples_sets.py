# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Can be a return type !  (total, max) = f(...)
# A number of values separated by commas
# Immutable (but can hold mutable data)
# Output is surrounded by parentheses so that nested tuples are processed correctly
# Not mutables n-uplets defined by ( and )
# Faster in processing as compared to lists
# 0 based

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

tup = 1, 5, 7
(a,b,c) = tup
print(a)
print(c)
print(b)

# Can't change value
fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)



tup = 1, 5, 7, 20
tup[2] 					7
tup[2]=3 				Error

point = (10,20)
point[0]				10
x, y = point 			depile   print("x=%s" % x)  print("y=%s" % y)
point[0] = 20   		ERROR !! (immutable)

rectangle = (30.0, 70.0)
longueur = rectangle[-1]  		70



# Jupyter: ipywidgets HBox, VBox... are tuples
# How to add new items to a HBox after being created ?
- https://github.com/jupyter-widgets/ipywidgets/issues/1764

NewLabelWidget = widgets.Label('New Column')
HorizBox.children += (NewLabelWidget,)

# Python 3 'splatting syntax' to create the new tuple: 
HorizBox.children = (*HorizBox.children, NewLabelWidget)


Convert tuple into list with list()
Convert list into tuple with tuple()

# Change items in tuples
L = list(t)
L[1] = 100
t_change = tuple(L)
print(t_change)       # (0, 100, 2)

# Remove items in tuples
L = list(t)
L.remove(1)
t_remove = tuple(L)
print(t_remove)   # (0, 2)