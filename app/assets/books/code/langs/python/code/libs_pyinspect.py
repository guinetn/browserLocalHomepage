# Pyinspect 
''' 
ttps://github.com/FedeClaudi/pyinspect
https://id1000000.medium.com/pyinspect-the-python-package-for-lazy-programmers-fa77d336c6df

Don’t remember a function’s name? Use pyinspect to look for it.
Don't remember what a function does? Use pyinspect to print its source code directly to your terminal.
Can't figure out why you keep getting an error? Use pyinspect's fancy tracebacks to figure it out
Still can't figure it out, but too lazy to google it? Use pyinspect to print Stack Overflow's top answer for your error message dir

 '''
# import pyinspect
import pyinspect as pi

# Find the functions you're looking for
pi.search(pi, name='what')
# This results in a table with all the function’s matching your search name

# import pyinspect
import pyinspect as pi
pi.ask("python Concatenate two lists?")