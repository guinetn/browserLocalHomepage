# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# by convention, we give classes PascalCase names
# class: common properties to a group of object (moule) attributs method Fonction in the class First arg MUST BE 'self' (reference to the instance)

# Create class
class User:
  pass        # pass in python means "do nothing"

# creating an instance of User
egclass = FirstClass()
print( type(egclass))     # instance
print( type(User))        # classobj

# Create class
class User:

  kind = 'zzz'  # Class variable shared by all instances.
  # Constructor (magic methods)
  def __init__(self, name, email, age):   # method called when the object is created (constructor)
  # def __init__(self, name=None, email=None, age=None):
    self.name = name     # Instance variable unique to each instance.
    self.email = email
    self.age = age

  # A function inside a class is called as a "Method" of that class
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1

  def __str__(self):   #  method called when a string representation is asked (print)
    return "User [%s, %i]" % (self.name, self.age)


joe = User('joe', 'joe@mail.com', 26)  # __init__ called
print("%s" % joe)  # __str__ called



# STATICS
# https://radek.io/2011/07/21/static-variables-and-methods-in-python/

''' STATIC VARIABLES
  Static: the member is on a class level rather on the instance level. 
  Static variables exist only on class level and aren't instantiated. 
  If you change a static variable in one instance of the class, the change will affect its value in all other instances.
'''

class Example:
    staticVariable = 5 # Access through class

print Example.staticVariable # prints 5

# Access through an instance
instance = Example()
print instance.staticVariable # still 5

# Change within an instance
instance.staticVariable = 6
print instance.staticVariable # 6
print Example.staticVariable # 5

# Change through the class
class Example.staticVariable = 7
print instance.staticVariable # still 6
print Example.staticVariable # now 7



'''
Static Method: 
called by an instance of a class or by the class itself
Static methods don't refer to any instance of the class and can be called outside of it. 
They also cannot access any non-static data members of the class

with @staticmethod or @classmethod (class method recieves one mandatory argument - a class it was called from)
'''

class person:
  @staticmethod
  def greet():
      print("Hello!")
person.greet()        
p1=person()
p1.greet()


# Examine a class
# dir( ) function comes very handy in looking into what the class contains and what all method it offers
dir(User)  #  ['__doc__', '__init__', '__module__']
dir(joe)  #  ['__doc__', '__init__', '__module__', 'name', 'email', 'age']


# Extend class
# class parent:
#    statements                  
# class child(parent):
#    statements

class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())



class MyCustomError(Exception):
    """Example of MyCustomError exception."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        


# Multiple Inheritance
'''
https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

Some classes may derive from multiple classes. This means that the derived class would have
its attributes, along with the attributes of all the classes that it was derived from.
'''
class CalendarClock(Clock, Calendar):
  pass

  

import threading
class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name='Receive messages')
x.start()
y.start()



PROPERTIES:  (@property) are much cleaner than getters and setter
GET/SET: property decorator

- code that retrieves the value of temperature will automatically call get_temperature() 
instead of a dictionary (__dict__) look-up. 
- code that assigns a value to temperature will automatically call set_temperature()
- actual temperature value is stored in the private _temperature variable. 
- The temperature attribute is a property object which provides an interface to this private variable.


class A:

  def __init__(self, some)!
    self._b = some

  def get_b(self):
    return self._b

  def set_b(self, val):
    self._b = val

a = A(‘123’)
print(a.get_b())
a.set_b(“444”)

Now compare this with a code written using Python-style properties:

class A:

  def __init__(self, some)
    self._b = some

  @property
  def b(self):
    return self._b

  @b.setter
  def b_setter(self, val):
    self._b = val

A = A(‘123’)
print(a.b)
a.b = ‘123’



# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300





# @[decorator_function_name] syntax to specify a decorator (a function that receives another function as argument)
# A decorator is a function that receives another function as argument. The behaviour of the argument function is extended by the decorator without actually modifying it.
def mydecoratorfunction(some_function): # function to be decorated passed as argument
    def wrapper_function(): # wrap the some_function and extends its behaviour
        # write code to extend the behaviour of some_function()
        some_function() # call some_function. some_function is a function whose behaviour we want to extend.
        return wrapper_function # return wrapper function

def display(str):
    print(str)
def displaydecorator(fn):
    def display_wrapper(str):
        print('Output:', end=" ")  # Output: Hello World
        fn(str)
    return display_wrapper
out = displaydecorator(display)
out('Hello World')

@displaydecorator  # Apply @displaydecorator decorator: call display() function to get the extended behaviour
def display(str):
    print(str)
display('Hello World') 
#Output: Hello World
#   \___ extended behaviour applied ("Output:")


# @property built-in decorator for the property() function
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
coldest_thing = Celsius(-300)


'''
@classmethod decorator
Call method using class name instead of the object
The class method can be called both by the class and its object.
@classmethod
def func(cls, args...)

method bounded to a class rather than its object (don't require creation of a class instance, much like staticmethod)
* Static method knows nothing about the class and just deals with the parameters
* Class method works with the class since its parameter is always the class itself.

'''

class Person:
  age = 0
  def __init__(self):
      Person.age = Person.age + 1

  @classmethod
  def show_age(cls):  # cls parameter refers to the Person class
      print("Age: ", cls.age, cls.__name__)    # cls.__name__ is the class name
  @classmethod
  def show_age_x(cls, x):  # cls parameter refers to the Person class
      print("Age: ", cls.age*x) 
      
p1=Person()
p2=Person()
Person.show_age() # age: 2
p1.show_age()     # age: 2
p1.show_age(10)     # age: 2


'''
CLASS METHOD USAGE:

return a modified initialitialized class

1. Factory methods: return a class object (like constructor) for different use cases. ~ function overloading in C++
'''

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()

'''
2. Correct instance creation in inheritance
'''
from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))



# get the class name from within a class method 
# A classmethod receives the class as its argument. 
# Calling it cls: cls.__name__

__name__ :  gives the program name
__class__.__name__ gives the class name
inspect.stack()[0][3] gives the module name. (you have to import inspect).

class Set:
  # these are the member functions
  # every one takes a first parameter "self" (another convention)
  # that refers to the particular Set object being used

  def __init__(self, values=None):
    """the constructor, called when you create a new Set.  
    s1 = Set() # empty set
    s2 = Set([1,2,2,3]) # initialize with values"""
    self.dict = {} # each instance of Set has its own dict property
    
    # which is what we'll use to track memberships
    if values is not None:
      for value in values:
        self.add(value)

  def __repr__(self):
    """this is the string representation of a Set object
    if you type it at the Python prompt or pass it to str()"""
    return "Set: " + str(self.dict.keys())

  # we'll represent membership by being a key in self.dict with value True
  def add(self, value):
    self.dict[value] = True

  # value is in the Set if it's a key in the dictionary
  def contains(self, value):
    return value in self.dict

  def remove(self, value):
  del self.dict[value]


s = Set([1,2,3])
s.add(4)
print s.contains(4) # True
s.remove(3)
print s.contains(3) # False







# COMPARE OBJECTS

compare two objects using ‘==’ operator

If a class doesn’t provide __eq__ method, Python will compare two objects and return True value only if both two objects are actually the same object:

class A:

  def __init__(self, i):
  self.i = i

a = A(1)
b = a
c = A(1)

a == b # True
a == c # False
In this example, objects a and c are False, even though they store the same value inside.

If you want to enable your own comparison logic for two objects and use a == operator, you can implement __eq__ method:

class Car(object):

  def __init__(self, horse_power, color):
    self.horse_power = power
    self.color = color

  def __eq__(self, other):
    if self.horse_power == other.horse_power and self.color == other.color:
      return True
    else:


## Type Annotations (PEP 526)
https://www.python.org/dev/peps/pep-0526

Python has dynamic types: don’t have to specify the type of a variable, you just use 
variables as labels for containers of data. But in bigger projects, having types is helpful.

def some_function(param_name : typename) -> return_type_name:
    ...  # whatever the function does

Type Checking:
Install mypy via pip install mypy and run it:
> mypy . --ignore-missing-imports
Success: no issues found in 1 source file

setup.cfg
  [mypy]
  ignore_missing_imports=true

The typing module adds support for type
https://docs.python.org/3/library/typing.html



from typing import TypedDict
class Movie(TypedDict):
    name: str
    year: int
movie: Movie = {'name': 'Blade Runner', 'year': 1982}




from typing import Optional
class Position:
    MIN_LATITUDE = -90
    MAX_LATITUDE = 90
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180

    def __init__(
        self, longitude: float, latitude: float, address: Optional[str] = None
    ):
        self.longitude = longitude
        self.latitude = latitude
        self.address = address

    @property
    def latitude(self) -> float:
        """Getter for latitude."""
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        """Setter for latitude."""
        if not (Position.MIN_LATITUDE <= latitude <= Position.MAX_LATITUDE):
            raise ValueError(f"latitude was {latitude}, but has to be in [-90, 90]")
        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Getter for longitude."""
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        """Setter for longitude."""
        if not (Position.MIN_LONGITUDE <= longitude <= Position.MAX_LONGITUDE):
            raise ValueError(f"longitude was {longitude}, but has to be in [-180, 180]")
        self._longitude = longitude


pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
pos2 = Position(42.1238762, 9.1649964)


def get_distance(p1: Position, p2: Position) -> float:
    pass      
  
  
## dataclasses 
https://www.youtube.com/watch?v=vBH6GRJ1REM&t=328s
  
import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint

import attr


## 1. MANUAL

class ManualComment:
    def __init__(self, id: int, text: str):
        self.id: int = id
        self.text: str = text

    def __repr__(self):
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented

## 2. WITH DATACLASS: create le, ge,gt...
@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


@attr.s(frozen=True, order=True, slots=True)
class AttrComment:
    id: int = 0
    text: str = ""


def main():
    comment = Comment(1, "I just subscribed!")
    # comment.id = 3  # can't immutable
    print(comment)
    print(dataclasses.astuple(comment))
    print(dataclasses.asdict(comment))
    copy = dataclasses.replace(comment, id=3)
    print(copy)

    pprint(inspect.getmembers(Comment, inspect.isfunction))














# Define Static Method: 
class Person: 
  
  @staticmethod 
  def greet(): 
  print("Hello static Person.greet()") 
  
class Master(Person): 
  
  def __init__(self, cry=None):
  # called by an instance of a class or by the class itself 
    self.cry = cry

  def run(self): 
    if self. cry is not None: 
      self.cry() 

  Person. greet( ) 
  pl = Person ( ) 
  pl.greet ( ) 
  m=Master(pl.greet) 
  m.run() 
  # Error  self.cellCIicked():  TypeError: 'tuple' object is not callable 
  

  #Hint: check functions addresses 
  class A: 
    def hello(self): 
      print("Hello")
  class B:
    def __init(self, target):
      self.target = target
    def run(self):
      print(self.target)
a = A()      
print(a.hello)
b = B(a.hello)
print(b.target)
b.run()

  # STEP 2 
  # Define Static Method: 
  class Person: 
  @staticmethod 
  def greet(): 
  print ( "Hello I 
  class Master(Person) : 
  def init (self, 
  cal led by an instance of a class o 
  cel-LCLicked = None) : 
  b 
  the class itself 
  = cellC1icked, 
  self. cellC1icked 
  def run(seLf) : 
  is not None: 
  if seLf.ce11C1icked 
  self. 
  Person. greet() 
  pl=Person() 
  pl. greet() 
  print (pl. greet) 
  m = Master(pl.greet) 
  print (m. cellC1icked) 
  m. run() 
  print ( ) 
  print ( 
  print() 
  # <function Person.greet at exeaee01F777EF75E8> 
  (<function Person.greet at 
  # self. 
  1 
  The same but is in A TUPLE, 
  so call with 


  class Person: 
    @staticmethod 
    def greet(): 
      print("Hello from Person static!") 
    def greet2(seLf, caLLer_msg): 
      print("He1101 %s"%(caller_msg)) 
class Master(Person) : 
    def init (self, ceLLCLicked = None): 
      seLf.ce11C1icked = cellC1icked 
      self.rowClicked = rowClicked 
    def run(seLf): 
    if self.cellC1icked is not None: 
      self.cellC1icked()
    if seLf.rowClicked is not None: 
      self.rowC1icked( 'from Master') 
      
Person. greet( ) 
pl-Person() 
pl. greet() 
pl. greet2( • from Person') 
print (pl. greet) 
# <function 
m = Master(pl.greet, pl.greet2) 
# (<function 
print (m. cellClicked) 
# (<function 
print (m. rowClicked) 
m.run() 
rowCLicked None) : 
at axaeeea1F777EF75E8> 
at axaeeea1F777EF75E8>,) 
at exaaeea1F777EF75E8>,) 
1 
The same but in a tuple 

