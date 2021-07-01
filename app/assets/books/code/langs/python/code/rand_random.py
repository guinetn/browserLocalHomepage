import random 			# The random module gives functions to generate random numbers


# GENERATE RANDOM NUMBERS
print(random.random())   # 0.0 - 1.0
numbers=[1,2,3,4,5,6,7]
print(random.choices(numbers))  # generate a random number from your choices 

import random; 
random.choice(['Head',"Tail"])

list = ["Item 1", "Item 2", "Item 3"]			# List
item = random.choice(list)						# Chooses from list
print(item)					# Prints choice


import secrets 
secrets.token_hex(nbytes=16) # Ex: aa82d48e5bff564f3221d02194611c13

import string
import random

length=5
randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=length))
