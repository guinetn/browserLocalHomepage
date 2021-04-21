# fastcore
# Python goodies to make your coding faster, easier, and more maintainable
# https://fastcore.fast.ai/


# Type Dispatch

'''
Change the way a function behaves based upon the input types it receives. 
This is a prominent feature in some programming languages like Julia & Swift. 
'''

from fastcore.all import *
from typing import List

# Function to multiply two ndarrays
@typedispatch
def multiple(x:np.ndarray, y:np.ndarray ): 
    return x * y

# Function to multiply a List by an integer
@typedispatch
def multiple(lst:List, x:int): 
    return [ x*val for val in lst]

# Calling 1st function
x = np.arange(1,3)   # x is [1 2]
y = np.array(10)     # y is [10]
print(f'Result of multiplying two numpy arrays: { multiple(x, y)}')  # [10,20]

# Calling 2nd function:

x = [1, 2]
y = 10
print(f'Result of multiplying a List of integers by an integer: {multiple(x, y)}') # [10, 20]