# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

- The value is NOT copied → reference transfer
- All functions are first-class citizens: they are objects just like any other object you might encounter.


# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')

#Assign function to variables
g = sayHello
g()


#Use functions as arguments to other functions
def func_name(function):
    return function.__name__
func_name(g)

# Throw functions into data structures
function_collection = [f, g]
for function in function_collection:
    function()


# Return a value
def getSum(num1, num2):
    total = num1 + num2
    return total

# Returning Multiple Values 
def sum_sub(a,b) :
  Sum = a+b
  Sub = a-b
  return sum, sub

x, y = sum_sub(20, 10)

# Sum of Even Numbers In a List
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2 == 0])  # use the list indexing and sum function
print(s)


Keywords Arguments
Def sub (a,b) :
print(a-b)
sub(200,100)
sub(a=200 , b=100)


Default Arguments
Def identity(name=”Guest”) :
Print(“Hello your name is”, name)
identity()


# Arbitrary Argument Lists: *args
def add_numbers(*args):
  total = 0
  for a in args:
    total += a
  print(total)

add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 43, 5453, 354234, 463463)

def concat(*args, sep='/'):
  return sep.join(args)
assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'



# kwargs

- args    a tuple of its unnamed arguments. Tuple of positional arguments 
- kwargs  a dict of its named arguments. Dictionary of keyword arguments.

def magic(*args, **kwargs):
  print "unnamed args:", args
  print "keyword args:", kwargs

magic(1, 2, key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: {'key2': 'word2', 'key': 'word'}




# Chained function call

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

a,b = 9,6
print((sub if a > b else add)(a, b))





Functions can be passed as arguments to another function: map, filter, reduce
Such functions that take other functions as arguments are also called higher order functions. 

def inc(x): return x + 1
def dec(x): return x - 1

def operate(func, x):
    result = func(x)
    return result
>>> operate(inc,3)   4
>>> operate(dec,3)   2

# Calculator Without if-else
import operator
action = {
  "+" : operator.add,
  "-" : operator.sub,
  "/" : operator.truediv,
  "*" : operator.mul,
  "**" : pow
}

print(action['*'](5, 5))    # 25





Function can return another function

def is_called():
    def is_returned():    # is_returned() is a nested function
        print("Hello")
    return is_returned

new = is_called()
new()



# higher-order function 
# in: some function f
# out: a new function 
def doubler(f):
  def g(x):
    return 2 * f(x)
  return g

def f1(x):
  return x + 1

g = doubler(f1)
print g(3)    # 8 (== ( 3 + 1) * 2)
print g(-1)   # 0 (== (-1 + 1) * 2)

g(1,2)  # TypeError: g() takes exactly 1 argument (2 given)
        # breaks down with functions that take more than a single argument

# Fix:
def doubler_correct(f):
  """works no matter what kind of inputs f expects"""
  def g(*args, **kwargs):
    """whatever arguments g is supplied, pass them through to f"""
    return 2 * f(*args, **kwargs)
   return g
g = doubler_correct(f2)
print g(1, 2) # 6


def doOperation(operation, number1, number2):
    return operation(number1, number2)

def sumBothNumbers(number1, number2):
    return number1 + number2

doOperation(sumBothNumbers, 4, 5)


## Returning a function
def multiplyBy(multiplier):
    def result(num):
        return num * multiplier
    return result

multiplyByThree = multiplyBy(3)
multiplyByThree(4)




# dictionary nlname:(color, marker, nlfun)
nlfuns = {
    'Rectifier (Relu)': ('b', '', lambda x: np.maximum(0, x)),
    'Softplus': ('g', '', lambda x: np.log(1 + np.exp( 1 * x))/ 1),
    'Sigmoid':  ('r', '', lambda x: 1/(1.0+np.exp(-1 * x)))
#   'Exponential':   ('c', '', lambda x: np.exp(x))
}
for nlname, (color, marker, nlfun) in nlfuns.items():
    plt.plot(evalpoints, list(map(nlfun, evalpoints)), hold=True, label=nlname, color=color, marker=marker)




def factorial(n) :
	If n==0:
		result=1
	Else:
		Result =n* factorial(n-1)
	Return result





# Curry

When passing functions around, sometimes we’ll want to partially apply (or curry)
functions to create new functions
def exp(base, power):
  return base ** power

def two_to_the(power):
  return exp(2, power)

# With partial:

from functools import partial
two_to_the = partial(exp, 2)    # Power is set. exp() is now a function of one variable
print two_to_the(3)             # 8

square_of = partial(exp, power=2)
print square_of(3) # 9


# Function Pointer

def f(a,b):
    return a+b
xx = 'f'
print eval('%s(%s,%s)'%(xx,2,3))


funcdict = {
  'mypackage.mymodule.myfunction': mypackage.mymodule.myfunction,
    ....
}
funcdict[myvar](parameter1, parameter2)



# SLOW FUNCTION

def slow_function(i):
    print(int(i),list(x for x in range(int(i)) if 
                str(x)==str(x)[::-1] and 
                str(x**2)==str(x**2)[::-1]))
    return
%%time
slow_function(1e6)