"""
pip install tqdm
to display smart progress bars in Python.
"""

from tqdm import tqdm
for x in tqdm(range(1000000)):
    pass
    
from tqdm.notebook import tqdmdef 
add(num):
    return reduce(lambda x,y: x+y, tqdm(range(num+1))) if type(num) == int else 0