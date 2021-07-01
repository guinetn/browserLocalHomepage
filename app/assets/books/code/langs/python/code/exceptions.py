
try:
    #statements in try block
except:
    #executed when error in try block
else:
    #executed if try block is error-free
finally:
    #executed irrespective of exception occured or not




try:
  print 0 / 0
except ZeroDivisionError:
  print "cannot divide by zero"



# Example 1
try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
    print(c)
except:  
    print("Can't divide with zero") 
    
# Example 2
try:    
    #this will throw an exception if the file doesn't exist.     
    fileptr = open("file.txt","r")    
except IOError:    
    print("File not found")    
else:    
    print("The file opened successfully")    
    fileptr.close()  

# Example 3
try:
  fptr = open("data.txt",'r')
  try:
    fptr.write("Hello World!")
  finally:
    fptr.close()
    print("File Closed")
except:
  print("Error")
  
  
  

class MyCustomError(Exception):
    """Example of MyCustomError exception."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

custom_exception_is_caught = False

try:
    raise MyCustomError('My custom message')
except MyCustomError:
    custom_exception_is_caught = True

assert custom_exception_is_caught



try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")  

# mention a specific type of exception in front of the except keyword. 
# The subsequent block will be executed only if the specified exception occurs.
try:
    a=5
    b='0'
    print (a+b)
except TypeError:
    print('Unsupported operation')
print ("Out of try except blocks")

try:
    a=5
    b=0
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')


try:
    print("try block")
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )


# Raise an Exception
try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")





"""Errors and Exceptions.

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt
is made to execute it. Errors detected during execution are called exceptions and are not
unconditionally fatal.

It is possible to write programs that handle selected exceptions.
"""


def test_handle_exceptions():
    """Handling of exceptions

    The try statement works as follows.

    - First, the try clause (the statement(s) between the try and except keywords) is executed.

    - If no exception occurs, the except clause is skipped and execution of the try statement
    is finished.

    - If an exception occurs during execution of the try clause, the rest of the clause is skipped.
    Then if its type matches the exception named after the except keyword, the except clause is
    executed, and then execution continues after the try statement.

    - If an exception occurs which does not match the exception named in the except clause, it is
    passed on to outer try statements; if no handler is found, it is an unhandled exception and
    execution stops with a message.
    """

    # Let's simulate division by zero exception.
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except ZeroDivisionError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Let's simulate undefined variable access exception.
    exception_has_been_handled = False
    try:
        # pylint: disable=undefined-variable
        result = 4 + spam * 3  # name 'spam' is not defined
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # A try statement may have more than one except clause, to specify handlers for different
    # exceptions. At most one handler will be executed. Handlers only handle exceptions that occur
    # in the corresponding try clause, not in other handlers of the same try statement. An except
    # clause may name multiple exceptions as a parenthesized tuple, for example:

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except (ZeroDivisionError, NameError):
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Exception handlers may be chained.
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True
    except ZeroDivisionError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # The try … except statement has an optional else clause, which, when present, must follow all
    # except clauses. It is useful for code that must be executed if the try clause does not raise
    # an exception. For example:

    exception_has_been_handled = False
    no_exceptions_has_been_fired = False

    try:
        result = 10
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True
    else:
        no_exceptions_has_been_fired = True

    assert not exception_has_been_handled
    assert no_exceptions_has_been_fired






"""Raising Exceptions.

@see: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

The raise statement allows the programmer to force a specified exception to occur.
"""


def test_raise_exception():
    """Raising Exceptions.

    The raise statement allows the programmer to force a specified exception to occur.
    """
    exception_is_caught = False

    try:
        # The sole argument to raise indicates the exception to be raised. This must be either an
        # exception instance or an exception class (a class that derives from Exception). If an
        # exception class is passed, it will be implicitly instantiated by calling its constructor
        # with no arguments
        raise NameError('HiThere')  # shorthand for 'raise ValueError()'
    except NameError:
        exception_is_caught = True

    assert exception_is_caught


def test_user_defined_exception():
    """User-defined Exceptions"""

    # Programs may name their own exceptions by creating a new exception class. Exceptions should
    # typically be derived from the Exception class, either directly or indirectly.
    # Most exceptions are defined with names that end in “Error,” similar to the naming of the
    # standard exceptions. Many standard modules define their own exceptions to report errors
    # that may occur in functions they define.
    class MyCustomError(Exception):
        """Example of MyCustomError exception."""
        def __init__(self, message):
            super().__init__(message)
            self.message = message

    custom_exception_is_caught = False

    try:
        raise MyCustomError('My custom message')
    except MyCustomError:
        custom_exception_is_caught = True

    assert custom_exception_is_caught
