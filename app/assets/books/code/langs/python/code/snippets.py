  
# swapping two numbers
a,b = 2,3
print(a,b) #prints 2 3
a,b = b,a
print(a,b) # 3 2

#reversing strings

string = "Python is awesome"
rev_string = string[::-1]
print(rev_string)

# create a single string from list of string

statement= ['I','love', 'Python']
inonestring = ' '.join(statement)
print(inonestring)


#chaining of comparision operator

x = 20
result = 1<x<22
result = 1<x<18
print(result)


# print the file path of imported modules

import os
import socket
print(os)
print(socket)

# return multiple values from function

def addition():
    return 2,3

l,b = addition()
print(l,b)


# most frequent value in list
lst = [1,2,2,3,3,34,4,4,3,3,3,333,5,5,5,5]

print(max(set(lst),key=lst.count))


# memory usage of object
import sys
x = 23
y = 33.3
print(sys.getsizeof(y))

# print string n times

print("hello world " * 100)

# anagrams checking
from collections import Counter
def is_anagrams(str1,str2):
    return Counter(str1) == Counter(str2)

print(is_anagrams('cat','tac'))
