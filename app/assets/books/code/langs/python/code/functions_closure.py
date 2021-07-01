https://www.programiz.com/python-programming/closure
https://www.bogotobogo.com/python/python_closure.php

- nested function 
- nonlocal variable
- value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

Use:
	Avoid the use of global values and provides some form of data hiding. 
	When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more 
	elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # Nested functions. Can access variables of the enclosing scope
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")     # returned function was bound to the name another.  
another()                        # On calling another(), the message was still remembered although we had already finished executing the print_msg() function. This technique is called "closure"


non-local variables are read-only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.



def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

closure1 = startAt(10)
closure2 = startAt(100)
print('closure1(3) = %s' %(closure1(3)))
print('closure2(3) = %s' %(closure2(3)))

Output:
closure1(3) = 13
closure2(3) = 103


# Using lambda

def startAt(start):
	return lambda inc: start+inc

f = startAt(10)
g = startAt(100)

print f(1), g(2)



# __closure__ attribute and cell objects
# We can get more info using __closure__ attribute and cell objects:

def startAt(start):
	def incrementBy(inc):
		return start + inc
	return incrementBy

f = startAt(10)
g = startAt(100)

print 'type(f)=%s' %(type(f))
print 'f.__closure__=%s' %(f.__closure__)
print 'type(f.__closure__[0])=%s' %(type(f.__closure__[0]))
print 'f.__closure__[0].cell_contents=%s' %(f.__closure__[0].cell_contents)

print 'type(g)=%s' %(type(g))
print 'g.__closure__=%s' %(g.__closure__)
print 'type(g.__closure__[0])=%s' %(type(g.__closure__[0]))
print 'g.__closure__[0].cell_contents=%s' %(g.__closure__[0].cell_contents)