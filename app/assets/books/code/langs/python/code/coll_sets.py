# Sets
Collection of distinct elements:

"""
Sets are unordered collections, meaning that elements are unindexed and have no set sequence. They’re declared with curly braces.
Unordered, mutable collections of data, which CAN’T CONTAIN REPEATED VALUES. They can take different data types, and are enclosed by curly braces {}.
Use Case: Sets are helpful for performing mathematical operations on the data, and when you need to store distinct values.
"""

s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2 }
s.add(2) # s is still { 1, 2 }
x = len(s) # equals 2
y = 2 in s # equals True
z = 3 in s # equals False

# Square of all even numbers in an range
{x**2 for x in range(10) if x%2==0} # {0, 4, 16, 36, 64}

# 1. Fast check existing item
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]
"joe" in stopwords_list # False, but have to check every element

stopwords_set = set(stopwords_list)
"joe" in stopwords_set # very fast to check

# 2. Find the distinct items in a collection:
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6

item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]


Removing Items from a Set
Genres.remove("Poetry")       # .remove() deletes an item, and raises an Error 
                                 if it doesn't already exist in the set
Genres.discard("Thriller")    # .discard() deletes an item in a set, 
                                 but in case the item doesn't exist, it doesn't return an error
                                 
                                 
# Mathematical Operations on Sets

Set1={1,2,3,4,5}
Set2={4,5,6,7,8}

#Intersection
Set1 & Set2              #Use '&' for intersection
#output: {4, 5}
Set1.intersection(Set2)  # or use .intersection() to find common elements

#Union
Set1.union(Set2)  
#output: {1, 2, 3, 4, 5, 6, 7, 8}


#Subset
Set3={1,2,3}
Set3.issubset(Set1)              #check if subset
#output: True         

#Superset
Set1.issuperset(Set3)    #check if superset
#output: True

#Difference
Set1.difference(Set2)     # finds how different Set1 is from Set2 
#output: {1, 2, 3}