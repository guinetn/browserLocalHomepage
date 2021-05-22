#  three numeric types in Python:
'''
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
'''


#%%
# python.exe xxxx.py

import matplotlib.pyplot as plt
from decimal import * 	#  decimal module that handles numbers of user-defined precision

# Define integers, floats the same way.
a=12
a=15.5
print(a)


# ROUND NUMBERS
a=15.5652645
print(int(a))
print(round(a,2)) #	Specify how many numbers need to be rounded
print(round(a,5))

# FLOATING NUMBERS 
# Arbitrary precision (user-defined Precision Numbers)
a=Decimal(5.5)
print(a)
print(int(a))

# INT

"""Type casting to integer"""

    assert int(1) == 1
    assert int(2.8) == 2
    assert int('3') == 3


def test_type_casting_to_float():
    """Type casting to float"""

    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2


def test_type_casting_to_string():
    """Type casting to string"""

    assert str("s1") == 's1'
    assert str(2) == '2'
    assert str(3.0) == '3.0'



# FLOAT
float_number = 7.0
# Another way of declaring float is using float() function.
float_number_via_function = float(7)
float_negative = -35.59

assert float_number == float_number_via_function
assert isinstance(float_number, float)
assert isinstance(float_number_via_function, float)
assert isinstance(float_negative, float)

# Float can also be scientific numbers with an "e" to indicate
# the power of 10.
float_with_small_e = 35e3
float_with_big_e = 12E4

assert float_with_small_e == 35000
assert float_with_big_e == 120000
assert isinstance(12E4, float)
assert isinstance(-87.7e100, float)



# COMPLEX

c = complex('5+2j')
print( abs(c) )       # 5.38516480713

complex_number_1 = 5 + 6j
complex_number_2 = 3 - 2j

assert isinstance(complex_number_1, complex)
assert isinstance(complex_number_2, complex)
assert complex_number_1 * complex_number_2 == 27 + 8j

