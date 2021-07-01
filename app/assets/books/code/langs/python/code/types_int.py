Check if a String is Integer

Input String is Integer or Not Using isnumeric
isnumeric() is a builtin function. It returns True if all the characters are numeric, otherwise False.

string.isdigit()
str = input("Enter any value: ")
 
if str.isdigit():
    print("User input is an Integer ")
else:
    print("User input is string ")


Check If The String is Integer Using Regular Expression
import re
value = input("Enter any value: ")
 
result = re.match("[-+]?\d+$", value)
 
if result is not None:
    print("User input is an Integer")
else:
    print("User Input is not an integer")


Check If The String is Integer Using any() and map() 
input = "sdsd"
 contains_digit = any(map(str.isdigit, input))
print(contains_digit)
isdigit:
Returns True – If all characters in the string are digits.
Returns False – If the string contains one or more non-digits


Check If The String is Integer Using Exception Handling
s = '951sd'
isInt = True
try:
   # converting to integer
   int(s)
except ValueError:
   isInt = False
if isInt:
   print('Input value is an integer')
else:
   print('Not an integer')