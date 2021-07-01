Magic Methods

https://www.tutorialsteacher.com/python/magic-methods-in-python

Special methods which add "magic" to your class. 
- not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the __add__() method will be called.
- used to define overloaded behaviours of predefined operators in Python

>dir() 		to see the number of magic methods inherited by a class
__abs__, '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'

Initialization & Construction
__new__(cls, other) 		To get called in an object's instantiation
__init__(self, other)		To get called by the __new__ method
__del__(self)			Destructor method

__new__
Java and C# use the 'new' operator to create a new instance of a class. 
In Python the __new__() magic method is implicitly called before the __init__() method. 
The __new__() method returns a new object, which is then initialized by __init__()

class employee:
  def __new__(cls):
    print ("__new__ magic method is called")
    inst = object.__new__(cls)
    return inst
  def __init__(self):
    print ("__init__ magic method is called")
    self.name='Satya'

>e1 = employee()
__new__ magic method is called
__init__ magic method is called



__str__()
It is overridden to return a printable string representation of any user defined class. We have seen str() built-in function which returns a string from the object parameter. For example, str(12) returns '12'. When invoked, it calls the __str__() method in the int class.

class employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)

__add__()
performs the addition of two objects

__ge__()
overload the >= operator