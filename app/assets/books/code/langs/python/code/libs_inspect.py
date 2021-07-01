# instrospection

import inspect

def maximum(arg1, arg2): 
""" Return the maximum value. """ 
	return arg2 if arg2 > arg1 else arg1

# On récupère la signature
inspect.signature(maximum) #  <Signature (arg1, arg2)

# docstring
inspect.getdoc(maximum) # (out) Return the maximum value.

# et même les sources !
inspect.getsource(maximum) # def maximum(arg1, arg2):\n """\n Return the maximum value.\n """\n return arg2 if arg2 > arg1 else arg1\n

