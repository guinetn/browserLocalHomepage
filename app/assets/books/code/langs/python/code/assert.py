# Assert

# assert statement to check if a given logical expression is true or false. 
# Program execution 
# - proceeds only if the expression is true 
# - raises the AssertionError when it is false. 

num=int(input('Enter a number: '))
assert num>=0, "Only positive numbers accepted."
print('You entered: ', num)


try:
    num=int(input('Enter a number: '))
    assert(num >=0), "Only positive numbers accepted."
    print(num)
except AssertionError as msg:
    print(msg)
