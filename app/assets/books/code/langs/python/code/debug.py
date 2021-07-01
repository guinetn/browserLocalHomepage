# DEBUG

See libs_pyinspect.py

import os
os?
os??
dir(os)

##  dir()
list of all the attributes of the specified object. It returns all the properties, even built-in properties that are the default for all objects.

class Student:
  name = "Joy",
  age = 16,
  rollNo = 25
  
print(dir(Student))

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'age', 'name', 'rollNo']


## python-traceback

https://realpython.com/python-traceback/

Prints a traceback when an exception is raised in your code.  information that help to diagnose and fix the reason for the exception.
Traceback: report of functions calls at a specific point (known by many names "stack trace, stack traceback, backtrace..."

# example.py
def greet(someone):
    print('Hello, ' + someon)
greet('Chad')

'''
python example.py
Traceback (most recent call last):
  File "/path/to/example.py", line 4, in <module>
    greet('Chad')
  File "/path/to/example.py", line 2, in greet
    print('Hello, ' + someon)
NameError: name 'someon' is not defined
'''


# greetings.py
def who_to_greet(person):
    return person if person else input('Greet who? ')

def greet(someone, greeting='Hello'):
    print(greeting + ', ' + who_to_greet(someone))

def greet_many(people):
    for person in people:
        try:
            greet(person)
        except Exception:
            print('hi, ' + person)
$ python example.py
'''
Traceback (most recent call last):
  File "/path/to/greetings.py", line 19, in <module>
    greet('Chad', greting='Yo')
TypeError: greet() got an unexpected keyword argument 'greting'            
'''
            
            

import ipywidgets as widgets
print(widgets.Button.on_click.__doc__)


## Jupyter Visual Debugger
https://blog.jupyter.org/a-visual-debugger-for-jupyter-914e61716559
a visual debugger that can be used within the Jupyter environment 
set breakpoints in notebook cells or source files, inspect variables, and navigate the call stack


https://jupyterlab.readthedocs.io/en/stable/user/debugger.html

Kernels that are known to be supporting the Jupyter Debug Protocol:

- xeus-python: Jupyter kernel for the Python programming language
conda install xeus-python -c conda-forge

- xeus-robot: Jupyter kernel for Robot Framework

Other Jupyter Kernels can also support debugging and be compatible with the JupyterLab debugger by implementing the Jupyter Debugger Protocol:  https://jupyter-client.readthedocs.io/en/latest/messaging.html#debug-request



## Python Standard Debugger (pdb)
https://docs.python.org/3/library/pdb.html#module-pdb
PDB is a default debugger that comes with all versions of Python, which means no installation

A command-line debugger where you can insert breakpoints in your code and then run your code using the debugger mode. 
Using these breakpoints, you can inspect your code and the stack frames

Pdb is a very basic debugger, but various extensions can be added to make it more useful

- rpdb
https://pypi.python.org/pypi/rpdb/

- pdb++
https://github.com/antocuni/pdb

-ipdb
when working with IPython.
https://github.com/gotcha/ipdb



## PyCharm
Python-Specific IDE developed by JetBrains


## Visual Studio Debugger
Visual Studio 2019: Which is a full-featured, multi-language IDE.https://docs.python.org/3/library/timeit.html
Visual Studio Code (vscode): A lightweight alternative to VS2019.


## Komodo
https://www.activestate.com/products/komodo-ide/

# benchmark-functions

* Using the time library
import time
def func():
   lst = [i for i in range(100000)]
   start = time.perf_counter()
func()
print(f"Completed Execution in {time.perf_counter() - start} seconds")

* Using timeit
https://docs.python.org/3/library/timeit.html
timeit.Timer(funcName).repeat(repeat=num_repetions,number=num_runs)
timeit.Timer(funcName).timeit(number=number)

built-in method in Python. It lets us specify the number of times we want to run the function, this helps us to calculate the average time the function takes. This is a better measure than the execution time of a single run. However, for a complex function that takes a long time, this method may not be ideal.

import timeit
num_runs = 10
duration = timeit.Timer(func).timeit(number = num_runs)
avg_duration = duration/num_runs
print(f'On average it took {avg_duration} seconds')



num_runs = 10
num_repetions = 3
ex_time = timeit.Timer(func).repeat(repeat=num_repetions, number=num_runs)
print(f'It took {ex_time}')




* Using line_profiler
conda install -c anaconda line_profiler
add a decorator before our function
@profile
def func():
    lst = []
    for i in range(100000):
       lst.append(i)

kernprof -l main.py
python -m line_profiler main.py.lprof

Hit- The number of times that line was executed.
Time- Total time taken by that line
Per Hit- Average time taken by the line
% Time- Fraction of total execution time. As we can see from the above picture, the append function takes around 57% of the execution time.
If you want to change the number of times the function is executed for line_profiler, use the following code
prof = profile(func)
for i in range(10):
   prof()


* Using memory_profile
conda install -c anaconda memory_profiler
@profile
def func():
    lst = []
    for i in range(100000):
       lst.append(i)
Then type the following command in the Anaconda Prompt
python -m memory_profiler main.py

Mem usage- The total memory usage at the line
Increment- memory usage by each execution of that line
Occurrences- number of times the line was executed



## more

- https://towardsdatascience.com/5-python-debugging-tools-that-are-better-than-print-1aa02eba35
- https://towardsdatascience.com/how-to-benchmark-functions-in-python-ed10522053a2