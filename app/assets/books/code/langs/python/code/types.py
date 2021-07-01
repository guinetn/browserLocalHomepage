## Types

Python is a dynamically typed language: type of a variable is determined only during runtime


my_number = 4
type(my_number)  # int
We can change the value of “my_number” and it does not have to be an integer.
my_number = '4'
type(my_number) " str

Dynamic typing is a cool feature but it may cause issues if not used carefully
4 + 4      # 8
'4' + '4'  # '44'