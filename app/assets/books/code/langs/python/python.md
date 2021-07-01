# PYTHON

[PEP 8 for style guide](https://www.python.org/dev/peps/pep-0008/)
[PEP257 for docstring conventions](https://www.python.org/dev/peps/pep-0257/)
[PEP484 for type hints](https://www.python.org/dev/peps/pep-0484/)
[Example Numpy Style Python Docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
[Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)


- https://www.python.org/
- https://docs.python.org/

- https://github.com/python
- https://github.com/python/cpython/tree/3.9
- https://www.python.org/downloads/
- https://jupyter.org	


📌 https://www.bogotobogo.com/python/pytut.php

* Interpreted  
Unlike native languages like C/C++, Python code gets interpreted at runtime instead of being compiled to native code at compile time.
* Just In Time (JIT) Compiler
Other interpreted languages like Java/.NET bytecode run faster that Python because their standard distribution includes a JIT compiler that compiles bytecode into native code at runtime.
* Global Interpreter Lock (GIL)
It prevents multi-threading by mandating the interpreter to execute only a single thread within a single process (i.e. an instance of Python interpreter) at a time.

* Major Competitors

Julia- It is an open source language and community is also growing very fast. It can replace Python in data science, deep earning and machine learning world because Julia is an amazing programming language in terms of speed. Julia programs compile to efficient native code for multiple platforms via LLVM. Only issue with Julia right now is that it has less number of packages/libraries w.r.t Python so many people are still working with Python. But since Julia’s packages/libraries are also increasing, so probably in coming few years Julia will be a very big competitor of Python.

Golang: This language is by Google and its code is extremely easy to write and maintain. Go programmers are among the highest paid programmers in the marker as per stackoverflow. The development of web, desktop and mobile apps all are supported in Go.

Rust: It is a safe, concurrent, practical language. It is a systems programming language that combines strong compile-time correctness guarantees with fast performance. It is most loved programming language as per stackoverflow. The development of web, desktop and mobile apps all are supported in Rust too.

C:\Users\nguin\anaconda3\python.exe

Start Menu open the Anaconda Prompt.
	location of a Python interpreter for a conda environment other than the root conda environment
	>conda activate environment-name
	>which python

	'my-env' environment
	win    C:\Users\jsmith\Anaconda3\envs\my-env\python.exe
	macOS  ~/anaconda/bin/python or /Users/jsmith/anaconda/bin/python
	Linux  ~/anaconda/bin/python or /home/jsmith/anaconda/bin/python

# TUTOS

https://www.programiz.com/python-programming ***
https://github.com/demotu/BMC
https://github.com/demotu/detecta    detect in signals
https://www.statsmodels.org/stable/index.html
http://www.courspython.com/
https://wwww.3schools.com/python
https://www.dataquest.io/dashboard

https://www.pythonanywhere.com/
Host, run, and code Python in the cloud!
develop and host your website or any other code directly from your browser


# SAMPLES

Azure & interesting things
	https://www.youtube.com/c/ProgrammingHero/videos ***

diagrams
	https://towardsdatascience.com/create-beautiful-architecture-diagrams-with-python-7792a1485f97
	https://diagrams.mingrammer.com/



It's easy to learn, easy to read and fast to develop
It's free and opensource
It's multiplatform
	It's slow



# Python Syntax

**Python Syntax compared to other programming languages**

- Python was designed to for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.


## Python Indentations

Where in other programming languages the indentation in code is for readability only, in Python the indentation is very important.
Python uses indentation to indicate a block of code.

```python
if 5 > 2:
  print("Five is greater than two!")
```
Python will give you an error if you skip the indentation.

# Zen of Python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense
Readability counts
Special cases aren't special enough to break the rules
Although practicality beats purity
Errors should never pass silently
Unless explicitly silenced
In the face of ambiguity, refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it
Although that way may not be obvious at first unless you're Dutch
Now is better than never
Although never is often better than *right* now
If the implementation is hard to explain, it's a bad idea
If the implementation is easy to explain, it may be a good idea
Namespaces are one honking great idea -- let's do more of those!


# INSTALLING PYTHON

You can download Python from python.org. But if you don’t already have Python, I
recommend instead installing the Anaconda distribution, which already includes
most of the libraries that you need to do data science.

http://python.org
choco install python
pip: The standard Python package manager


# EDITORS
	With SublimeText
	 	Create xxxx.py
	 	CTRL+B runs it and display the result

	Visual Studio
		PTVS is a free, open source plugin that turns Visual Studio into a Python IDE

	With cmd.exe
		python
		>>> 2+3
		>>> print(2*9)
		 
		>>> import math
		>>> math.sqrt(2)
		1.4142135623730951
		
		md myp1.py
				print("Bonjour tout le monde!")
				print(7 * 3.)  # int x float → float
		cd \...\python myp1.py
		python myp1.py


# EXECUTABLES
	mon_programme.py
		 
	# 	comments
	$ cat > myprog.py << EOF
	
	Comments in Python start with the hash character, # , and extend to the end of the physical line. A comment may appear at the start of a line or following whitespace or code, but not within a string literal.

	EXECUTE PROGRAM

		 $ python mon_programme.py
	 $./mon_programme.py  				# no "python" prefix
	 
	 Linux / Mac OS
	 	#!/usr/bin/env python 			←   interpreter path on 1st line: allow to run with $ mon_programme.py
	 	print("hello")

	SublimeText
	 	Create xxxx.py
	 	CTRL+B runs it and display the result
	 		 

# PYTHON INTERACTIVE SHELL

Interactive mode. Play commands, use it as a Simple Calculator

$ python
Once the Python interpreter is started, issue any command at the command prompt ">>>"
>> exit() ou Ctrl+D to quit
>> print("Hello World")
>> _ 									contains the most recent output value 	 
_ is only available in the Python shell. It's NOT available in Python scripts or programs

2+1  3*4  2**3   
3/2 				1.5
3 // 2  			1 (integer division)
print(7 * 3) 		21		int	
print(7 * 3.)  		21.0 	int x float → float
_ * 4 				4

# Execute

python -c "import struct; print(struct.calcsize('P') * 8)"

RUN A PYTHON SCRIPT FROM WINDOWS
cmd
python C:\Users\Username\Desktop\my_python_script.py
python N:\projects\helloworld.py aaa


python.exe 		terminal to pop-up
pythonw.exe  	no terminal pop-up, for GUI programs, just display your program

>>> execfile('filename.py')
For Python 3:
>>> exec(open("filename.py").read())

RUN A PYTHON SCRIPT UNDER MAC, LINUX, BSD, UNIX
Put a "shebang" line as first line to indicates Python interpreter location
#!/path/to/interpreter
A common shebang line used for the Python interpreter is as follows:
#!/usr/bin/env python
You must then make the script executable, using the following command:
chmod +x my_python_script.py

PYTHON EXECUTION WITH THE SHELL (LIVE INTERPRETER)

everything is read and interpreted in real-time
to execute code interactively. If you want to run a Python script from the interpreter, you must either import it or call the Python executable.

user@hostname:~ python
Python 3.3.0 (default, Nov 23 2012, 10:26:01) 
[GCC 4.2.1 Compatible Apple Clang 4.1 ((tags/Apple/clang-421.11.66))] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>


IDLE > File > Path Browser
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


Built-in function: execfile

Built-in function: execfile
execfile('helloworld.py')
It normally cannot be called with arguments. But here's a workaround:
import sys
sys.argv = ['helloworld.py', 'arg']  # argv[0] should still be the script name
execfile('helloworld.py')

Advance usage: subprocess
import subprocess
subprocess.call(['python', 'helloworld.py']) # Just run the program
subprocess.check_output(['python', 'helloworld.py']) # Also gets you the stdout

With arguments:
subprocess.call(['python', 'helloworld.py', 'arg'])

call with arguments
	import sys
	sys.argv = ['helloworld.py', 'arg']  # argv[0] should still be the script name
	execfile('helloworld.py')



# DEBUG


http://sametmax.com/debugger-en-python-les-bases-de-pdb/
import pdb; pdb.set_trace()
relancez votre programme depuis une console.
L’exécution du programme va alors se figer, et dans la console vous aurez accès à un shell special: Pdb

COMMENT TRANSFÉRER DES FICHIERS TRÈS RAPIDEMENT ENTRE DEUX PCS DISTANTS ?
.Sans forcément partager le répertoire
. Lancez un serveur local Python qui servira les fichiers de manière statique :
Python 2 : python -m SimpleHTTPServer
Python 3 : python3 -m http.server
Et à distance, tapez l’URL du PC sur lequel tourne le serveur, et hop, vous pouvez récupérer ce que vous voulez !




# What is Python

Python is a popular programming language. It was created in 1991 by Guido van Rossum.

Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

It is used for:

- web development (server-side),
- software development,
- mathematics,
- system scripting.

## What can Python do?

- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.

## Why Python?

- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-orientated way or a functional way.

## Good to know

- The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
- In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

## References

- [w3schools.com](https://www.w3schools.com/python/python_intro.asp)