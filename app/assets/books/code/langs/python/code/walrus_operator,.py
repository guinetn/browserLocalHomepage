 # Python 3.8
 # accomplish two tasks at once

 num = 15
 print(num)

# Walsrus operator - assignment expression operator
# name := expr
# allows us to both assign a value to a variable, and to return that value, all in the same expression
# The name is due to its similarity to the eyes and tusks of a Walrus on its side.

print(num := 15)
# The value of 15 is assigned to num. 
# Then this same value is returned, which will become the argument for the print function. 
# Thus, 15 is printed.

# print(num = 15) → TypeError

value = input('enter:')
while (value != ''):
	print('nice')
	value = input('enter:')

while (value := input('enter:') !=''):		
	print('nice')
