### Cython

Cython creates C modules that speed up Python code execution, important for complex applications where an interpreted language isn't efficient.
- https://opensource.com/article/21/4/cython

Python compiler optimizing performance and form an extended Cython programming language. 
As an extension of Python, Cython is also a superset of the Python language, and it supports calling C functions and declaring C types on variables and class attributes. This makes it easy to wrap external C libraries, embed C into existing applications, or write C extensions for Python in syntax as easy as Python itself.

Cython is commonly used to create C modules that speed up Python code execution. This is important in complex applications where an interpreted language isn't efficient.

> python -m pip install Cython

.pyx extension could technically be anything, but it's Cython's default extension

hello.pyx 
```python
print("hello world")
```

setup.py 
```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("hello.pyx")
)
```

>python setup.py build_ext --inplace

hello.pyx → cythonize module → hello.c → xxx.so library

>>> import hello
hello world

## ntegrate C code into Python