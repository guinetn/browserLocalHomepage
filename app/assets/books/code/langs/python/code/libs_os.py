import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH')) # Added PYTHONPATH in "Env Var system"
print("PATH:", os.environ.get('PATH'))

# Folder path of the current script
print(os.getcwd())

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
# To iterate through all files / folders
os.listdir("path/to/folder") 

# To build paths to a subdirectory
os.path.combine 

# search through all text files in a folder while excluding all other file types
for file in os.listdir(os.getcwd()):
    if '.txt' in file:
        doStuff()

os.chdir(path)
os.getenv(key, default=None)
os.uname()
os.listdir(path='.')
os.mkdir(path, mode=0o777, *, dir_fd=None)
os.makedirs(name, mode=0o777, exist_ok=False)
os.mkfifo(path, mode=0o666, *, dir_fd=None) FIFOs are pipes that can be accessed like regular files. 
os.remove(path, *, dir_fd=None)
os.removedirs(name)
os.rmdir(path, *, dir_fd=None)   If the directory does not exist or is not empty, an FileNotFoundError or an OSError
os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
os.scandir(path='.')  Return an iterator of os.DirEntry objects 

train_csv = os.path.join(os.path.dirname(notebook_path), "Datasets/train.csv")

if os.access("myfile", os.R_OK):
    with open("myfile") as fp:
        return fp.read()
return "some default data"

# is better written as:

try:
    fp = open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()

- https://www.codegrepper.com/code-examples/python/how+to+get+current+path+in+jupyter+notebook        