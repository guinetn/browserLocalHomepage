# DECORATORS 

powerful tool to augment the behavior of functions
add functionality to an existing code
metaprogramming because a part of the program tries to modify another part of the program at compile time.
Decorator function added some new functionality to the original function.
The decorator acts as a wrapper. The nature of the object that got decorated (actual gift inside) does not alter.

Decoration is a design pattern in Python that allows you to modify the behavior of a function. A decorator is a function that takes in a function and returns a modified function.

decorators can be easily applied with the @ symbol

everything in Python (Yes! Even classes), are objects 
def first(msg):
    print(msg)
first("Hello")
second = first
second("Hello")  # first and second refer to the same function object

Functions can be passed as arguments to another function: map, filter, reduce
Such functions that take other functions as arguments are also called higher order functions. 

def inc(x): return x + 1
def dec(x): return x - 1

def operate(func, x):
    result = func(x)
    return result
>>> operate(inc,3)   4
>>> operate(dec,3)   2


Function can return another function

def is_called():
    def is_returned():    # is_returned() is a nested function
        print("Hello")
    return is_returned

new = is_called()
new()


Functions and methods are called callable as they can be called.
In fact, any object which implements the special __call__() method is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.

def make_pretty(func):             # make_pretty() is a decorator
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")



>>> ordinary()
I am ordinary

Decorate this ordinary function
>>> pretty = make_pretty(ordinary)   # ordinary() got decorated
>>> pretty()
I got decorated
I am ordinary


Generally, we decorate a function and reassign it as,
ordinary = make_pretty(ordinary).

syntactic sugar to simplify this

@make_pretty
def ordinary():
    print("I am ordinary")

is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)




Decorating Functions with Parameters

nested inner() function inside the decorator is the same as the parameters of functions it decorates. Taking this into account, now we can make general decorators that work with any number of parameters.

# decorator to fix "division by zero"
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

>>> divide(2,5)
I am going to divide 2 and 5
0.4

>>> divide(2,0)
I am going to divide 2 and 0
Whoops! cannot divide



Chaining Decorators

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
Output

******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************






"""Function Decorators.

@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

Function decorators are simply wrappers to existing functions. In the context of design patterns,
decorators dynamically alter the functionality of a function, method or class without having to
directly use subclasses. This is ideal when you need to extend the functionality of functions that
you don't want to modify. We can implement the decorator pattern anywhere, but Python facilitates
the implementation by providing much more expressive features and syntax for that.
"""


def test_function_decorators():
    """Function Decorators."""

    # Function decorators are simply wrappers to existing functions. Putting the ideas mentioned
    # above together, we can build a decorator. In this example let's consider a function that
    # wraps the string output of another function by p tags.

    # This is the function that we want to decorate.
    def greeting(name):
        return "Hello, {0}!".format(name)

    # This function decorates another functions output with <p> tag.
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return function_wrapper

    # Now, let's call our decorator and pass the function we want decorate to it.
    my_get_text = decorate_with_p(greeting)

    # Here we go, we've just decorated the function output without changing the function itself.
    assert my_get_text('John') == '<p>Hello, John!</p>'  # With decorator.
    assert greeting('John') == 'Hello, John!'  # Without decorator.

    # Now, Python makes creating and using decorators a bit cleaner and nicer for the programmer
    # through some syntactic sugar  There is a neat shortcut for that, which is to mention the
    # name of the decorating function before the function to be decorated. The name of the
    # decorator should be prepended with an @ symbol.

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, John!</p>'

    # Now let's consider we wanted to decorate our greeting function by one more functions to wrap a
    # div the string output.

    # This will be our second decorator.
    def decorate_with_div(func):
        def function_wrapper(text):
            return "<div>{0}</div>".format(func(text))
        return function_wrapper

    # With the basic approach, decorating get_text would be along the lines of
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))

    # With Python's decorator syntax, same thing can be achieved with much more expressive power.
    @decorate_with_div
    @decorate_with_p
    def greeting_with_div_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_div_p('John') == '<div><p>Hello, John!</p></div>'

    # One important thing to notice here is that the order of setting our decorators matters.
    # If the order was different in the example above, the output would have been different.

    # Passing arguments to decorators.

    # Looking back at the example before, you can notice how redundant the decorators in the
    # example are. 2 decorators(decorate_with_div, decorate_with_p) each with the same
    # functionality but wrapping the string with different tags. We can definitely do much better
    # than that. Why not have a more general implementation for one that takes the tag to wrap
    # with as a string? Yes please!

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags('div')
    @tags('p')
    def greeting_with_tags(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tags('John') == '<div><p>Hello, John!</p></div>'


## TRACK A FUNCTION’S RUNTIME

"""Build the timefunc decorator."""

import time
import functools


def timefunc(func):
    """timefunc's doc"""

    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        """time_wrapper's doc string"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {time_elapsed}")
        return result

    return time_closure

functool.wraps is a decorator for our closure allowing to preserve func’s metadata as it is passed to the closure.


# Test: see func.__name__ and runtime

@timefunc
def single_thread(inputs):
    """
    Compute single threaded.
    """
    return [f(x) for x in inputs]


if __name__ == "__main__":

    demo_inputs = [randint(1, 100) for _ in range(10_000)]

    single_thread(demo_inputs)    