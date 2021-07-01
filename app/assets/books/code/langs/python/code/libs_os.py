import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH')) # Added PYTHONPATH in "Env Var system"
print("PATH:", os.environ.get('PATH'))

# Folder path of the current script
print(os.getcwd())

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
# To iterate through all files / folders
os.listdir(“path/to/folder”) 

# To build paths to a subdirectory
os.path.combine 

# search through all text files in a folder while excluding all other file types
For file in os.listdir(os.getcwd()):
    if '.txt' in file:
        doStuff()