import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot

from collections import defaultdict, Counter
from functools import partial, reduce
from __future__ import division # Get 5/2=2.5 and not 2.0 by default



import math # to import standard module math
print("The value of pi is", math.pi)

print(dir(math))  # view module content
help(math.log)
help(math)   

from math import cos, pi
x = math.cos(2* math.pi)
print(x)

import math as m  # import module by renaming it
print("The value of pi is", m.pi)
print(m.factorial(N))

from math import pi, e # import only pi from math module
print("The value of pi is", pi)
print("The value of e is", e)

from math import *   # import all names from the standard module math
print("The value of pi is", pi)
Not a good programming practice: duplicate definitions, bad readability 


Python Module Search Path
	While importing a module, Python looks at several places.
	1. look for a built-in module
	2. look into a list of directories defined in sys.path
		. current directory
		. PYTHONPATH (an environment variable with a list of directories)
		. The installation-dependent default directory
	import sys
	sys.path
	['',
	'C:\\Python33\\Lib\\idlelib',
	'C:\\Windows\\system32\\python33.zip',
	'C:\\Python33\\DLLs',
	'C:\\Python33\\lib',
	'C:\\Python33',
	'C:\\Python33\\lib\\site-packages']

dir() 
	list the names that are defined inside a module

import re
my_regex = re.compile("[0-9]+", re.I)

# alias if you already had a different re in your code
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

import matplotlib.pyplot as plt

If you need a few specific values from a module, you can import them explicitly and use them without qualification:
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

If you were a bad person, you could import the entire contents of a module into your namespace, which might inadvertently overwrite variables you’ve already defined


Basic unit of code reusability in Python, existing in one of two types: 
    
    Pure Module
    	https://packaging.python.org/glossary/#term-pure-module
        contained in a single .py file
    
    Extension Module     
    	https://packaging.python.org/glossary/#term-extension-module    
        A module written in the low-level language of the Python implementation: C/C++ for Python, Java for Jython. Typically contained in a single dynamically loadable pre-compiled file, e.g. a shared object (.so) file for Python extensions on Unix, a DLL (given the .pyd extension) for Python extensions on Windows, or a Java class file for Jython extensions.


# Module

- [Python Standard Modules Index](https://docs.python.org/3/py-modindex.html)
- a file containing a set of functions to include in your application
- Core python modules: modules installed using pip package manager (including Django) 
- Custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')


# Reload a (changed) module
	import imp
	import my_module
	This code got executed
	import my_module
	imp.reload(my_module)
	This code got executed





# PACKAGES

Divide your code base into clean, efficient modules 
Place similar modules in one package and different modules in different packages
Python has 
	- packages for directories 
	- modules for files

Python looks in the list of directories defined in sys.path
a Python package can have sub-packages and modules.

A directory containing a __init__.py is considered as a package
This file can be left empty but we generally place the initialization code for that package

				     PACKAGE
					   Game
					    +
					    +
		+---------------+--------------------+
	__init.py__		SUB-PACKAGES 		SUB-PACKAGES
					  Sound              Level
					__init.py__ 		__init.py__
					  load.py             open.py
					  play.py             start.py 

import Game.Level.start   # import the start module 
Game.Level.start.select_difficulty(2)

from Game.Level import start
start.select_difficulty(2)

from Game.Level.start import select_difficulty
select_difficulty(2)
not recommended. Using the full namespace avoids confusion and prevents two same identifier names from colliding.



'''
@see: https://docs.python.org/3/tutorial/modules.html

As your program gets longer, you may want to split it into several files for easier maintenance.
You may also want to use a handy function that you’ve written in several programs without copying
its definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an
interactive instance of the interpreter. Such a file is called a module; definitions from a module
can be imported into other modules or into the main module (the collection of variables that you
have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

'''