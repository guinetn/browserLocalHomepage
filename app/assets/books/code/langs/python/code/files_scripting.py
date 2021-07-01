
for filename in '.*':
    print(filename)
        
    
# python script that loops through a directory and use files one at a time

import os
import sys
args = sys.argv
directory = args[1]
protoc_path = args[2]
for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system( my_action_path+" "+directory+"/"+file+" --python_out=.")
        
        
        


import os
from os.path import join
import datetime
def modification_date(filename):
    t = os.path.getmtime(filename)
    return t
def creation_date(filename):
    t = os.path.getctime(filename)
    return t
for root, dirs, files in os.walk("."):
    for name in files:
        print join(root, name), 
                   modification_date(join(root, name)), 
                   creation_date(join(root, name))        