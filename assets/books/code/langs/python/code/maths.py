# math module
# https://docs.python.org/3/library/math.html
import math
from math import pi
pi


import math
math.pi  # 3.141592653589793
math.e   # 2.718281828459045

math.radians(30)          # 0.5235987755982988
math.degrees(math.pi/6)   # 29.999999999999996

# (sin, cos, tan, etc.) need the angle in radians as an argument
math.sin(pi/3)  
math.sin(0.5235987755982988)  # 0.49999999999999994
math.cos(0.5235987755982988)  # 0.8660254037844387
math.tan(0.5235987755982988) # 0.5773502691896257

math.log(10)    # Natural logarithm. 2.302585092994046
math.log10(10)  # base-10 logarithm of the given number. It is called the standard logarithm.  1.0

math.exp(10)    # 1.0
math.e**10      # 22026.465794806703
math.log(math.exp(2))

math.pow(2,4) # 16.0
2**4          # 16
math.sqrt(100)     # 10.0
math.sqrt(3)       #1.7320508075688772

math.ceil(4.5867)  # 5
math.floor(4.5687) # 4

prices = [1,2,3,4,5]
mean = sum(prices)/len(prices)
print(f"{prices}.   Mean ={mean}")
