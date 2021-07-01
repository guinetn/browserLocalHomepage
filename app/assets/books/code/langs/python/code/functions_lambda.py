"""Lambda Expressions

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
wherever function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested function
definitions, lambda functions can reference variables from the containing scope.


To define a function without defining it using def. Helps define anonymous functions mainly one-line functions. 
To define a complicated function, it is better to define a function using def.

"""




# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

sqr = lambda x: x * x  ##Function that returns square of any number
sqr(10)

getSum = lambda num1, num2: num1 + num2
print(getSum(10, 3))

s=lambda a,b:a+b
print(s(2,4))

beta = lambda x: x>0
print(beta(10))
print(beta(-10))

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b 
print(x(5, 6))

# lambda power is when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)))


student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('joe', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
# [('joe', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# Prime Number
# A prime number is a number that is divisible only by itself and 1. eg: 2,3,5,7 etc. To generate prime numbers in a range we can use the list function with filter and lambda to generate prime numbers.
list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13)))
# [2, 3, 5, 7, 11]

# Finding Max Number
findmax = lambda x,y: x if x > y else y 
findmax(5,14) # or max(5,14)



def test_lambda_expressions():
    """Lambda Expressions"""

    # This function returns the sum of its two arguments: lambda a, b: a+b
    # Like nested function definitions, lambda functions can reference variables from the
    # containing scope.

    def make_increment_function(delta):
        """This example uses a lambda expression to return a function"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44

    # Another use of lambda is to pass a small function as an argument.
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # Sort pairs by text key.
    pairs.sort(key=lambda pair: pair[1])

    assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
