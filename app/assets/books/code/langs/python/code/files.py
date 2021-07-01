# Python has functions for creating, reading, updating, and deleting files.
# https://www.tutorialsteacher.com/python/python-read-write-file

import os
print(os.getcwd())   # current working directory 

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)   # Full path to the directory a Python file is contained in

img_path = os.path.join(dir_path, "park.jpg") 

path = "/home"
print(os.path.join(path, "User/Desktop", "file.txt"))  # Join various path components
print(os.path.join(path, "Downloads", "file.txt", "/home")) # Join various path components
# In above example '/User' and '/home' both represents an absolute path but '/home' is the last value 
# # so all previous components before '/home' will be discarded and joining will continue from '/home'

print(os.getcwd().split('\\')[-1])   

'''
The os and os.path modules.
The __file__ constant
os.path.realpath(path) (returns "the canonical path of the specified filename, eliminating any symbolic links encountered in the path")
os.path.dirname(path) (returns "the directory name of pathname path")
os.getcwd() (returns "a string representing the current working directory")
os.chdir(path) ("change the current working directory to path")
'''

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))




# Open a file
myFile = open('file_sample.txt', 'w')

# open(file name[, access mode][, buffersize])
#                      \                \___ desired buffer size: 0 unbuffered, 1  line buffered, other positive values indicate the buffer size. A negative buffersize uses the default value.
# 					    \___ purpose of opening: read (r), write (w), append (a)
# 								r     reading only
# 								rb	  reading only in binary format
# 								r+	  both reading and writing
# 								rb+	  both reading and writing in binary format
# 								w	  writing only
# 								wb	  writing only in binary format
# 								w+	  both writing and reading
# 								wb+	  both writing and reading in binary format
# 								a	  appending
# 								ab	  appending in binary format
# 								a+	  both appending and reading
# 								ab+	  both appending and reading in binary format

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file

with open("data.txt",'a',newline='\n') as f: f.write("Python is awsome")

myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('file_sample.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Write Lines to File
lines=["Hello world.\n", "Welcome to TutorialsTeacher.\n"]
f=open("D:\file_sample.txt","w")
f.writelines(lines)
f.close()

# Write to a Binary File
f=open("binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()


# check File exists
# Brute force Method
import os.path
from os import path

def check_for_file():
	print("File exists: ",path.exists("data.txt"))

if __name__=="__main__":
   check_for_file()
    

# Read from file
# 	readline()    reads the characters starting from the current reading position up to a newline character.
#	read(chars)   reads the specified number of characters starting from the current position.
#	readlines()   reads all lines until the end of file and returns a list object.

f=open("file_sample.txt","r")
line=f.readline()
print(line)
f.close()

# Reading a Binary File
f=open("binfile.bin","rb")
num=list(f.read())
print (num)
f.close()

f=open("D:\file_sample.txt","r")
line=f.readline()
while line!='':
    print(line)
    line=f.readline()

f=open("file_sample.txt","r")
for line in f:
    print(line)
f.close()

myFile = open('file_sample.txt', 'r+')
text = myFile.read(100)
print(text)

# seek: r/wat a specific position, use the seek() function to set the current read/write position.
f=open("D:\file_sample.txt","r+")
f.seek(6,0)
lines=f.readlines()
for line in lines:
    print(line)
f.close()



fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# using list comprehension
lst = [line.strip() for line in open('data.txt')]
print(lst)
lst(open('data.txt'))
##Using with will also close the file after use
with open("data.txt") as f: lst=[line.strip() for line in f]
print(lst)


# file.close()		Closes the file.
# file.flush()		Flushes the internal buffer.
# next(file)		Returns the next line from the file each time it is called.
# file.read([size])	Reads at a specified number of bytes from the file.
# file.readline()	Reads one entire line from the file.
# file.readlines()	Reads until EOF and returns a list containing the lines.
# file.seek(offset, from)	Sets the file's current position.
# file.tell()		Returns the file's current position
# file.write(str)	Writes a string to the file. There is no return value.




# Dealing with File System

# Copy Files
# The shutil module contains a function for copying files.
import shutil
copied_path = shutil.copy('my_file.txt', 'copied_file.txt')
# If my_file.txt is a symlink, the above code will create copied_file.txt as a separate file.
# You can create a copy of a symlink instead like this:
copied_path = shutil.copy('my_file.txt', 'copied_file.txt', follow_symlinks=False)

# Move Files
# You can move files from one location to another like this:
import shutil
shutil.move('file1.txt', 'file3.txt')

# You can rename a file using the rename function from os module like this:
import os
os.rename('file1.txt', 'file3.txt')

# Read and Write Text Files
# You can use the open function to open files, and then use the read or write methods to read from them and write to them.
fd = open('file1.txt')
content = fd.read()
print(content)

# First, we open the file for reading using the open function, then we start reading the file content using read function, finally, we put the grabbed content into the variable content.
# You can specify how many bytes you want to read for the read() function:
fd.read(20)
# If the file is not too big, you can read the entire contents into a list, then iterate over that list to print the output.
content = fd.readlines()
print(content[0])

# You can write to a file by specifying the mode to open function like this. You have two modes of writing, the write mode and append mode.
# This is the write mode where you will overwrite the old file content.
fd = open('file1.txt','w')
content = fd.write('YOUR CONTENT GOES HERE')

# And this is the append mode:
fd = open('file1.txt','a')
content = fd.write('YOUR CONTENT GOES HERE')


# Creating Directories
# You can create a new directory using mkdir function from os module like this:
import os
os.mkdir('./NewFolder')
# This code will throw an error if the directory exists. Don’t worry, we will talk about exception handling in future posts so you can avoid such errors.


# Get Access & Modification & Creation Time
# You can use getmtime(), getatime() and getctime() to get modification time, access time and creation time respectively.
# The returned time is formatted as a Unix timestamp, we can convert it to human readable format like this:
import os 
import datetime 
tim=os.path.getctime('./file1.txt') 
print(datetime.datetime.fromtimestamp(tim))


# Iterating Over Files
# You can use listdir() function from os module to get the files:
import os
files= os.listdir('.')
print(files)

# Also, you can use the glob module to do the same thing:
import glob 
files=glob.glob('*') 
print(files)
# You can write any extension for file globbing, like *.doc to get all word documents only.





import os 
import time 
st=os.stat(Filename) 
Age=(time.time()-st.st_mtime) 
print(Age)

import time, os, stat
def file_age_in_seconds(pathname):
    return time.time() - os.stat(pathname)[stat.ST_MTIME]


from datetime import *
import time, os, stat
from os.path import join
from tkinter import *


def modification_date(filename):
    t = os.path.getmtime(filename)
    return t

def creation_date(filename):
    t = os.path.getctime(filename)
    return t

def file_age_in_seconds(pathname):
    age = time.time() - os.stat(pathname)[stat.ST_MTIME]
    print(pathname + " age=" + str(age/60))
    return age

# -ctime n File's status was last changed n*24 hours ago.
# -mtime n File's data was last modified n*24 hours ago.    
# /path/to/device/ + /dcim/camera
src = r'Ce PC\Galaxy S5\Phone\DCIM\Camera'
src = r'C:\Users\guine\Pictures'


def files_before(root, files, min):        
    return filter(lambda f: file_age_in_seconds(join(root, f)) < min*60, files)

#def files_after(files, min):
#    lower_time_bound = datetime.datetime.now() - timedelta(minutes=min)
#    return filter(lambda f: datetime.datetime.fromtimestamp(os.path.getmtime(f)) > lower_time_bound, files)

for root, dirs, files in os.walk(src):
    for name in files_before(root, files, 60):
        print(join(root, name), modification_date(join(root, name)), creation_date(join(root, name)))
#for root, dirs, files in os.walk(src):
#    for name in files:


window = Tk()
window.title("Welcome to LikeGeeks app")
window.mainloop() # calls the endless loop of the window, so the window will wait for any user interaction till we close it.
            # If you forget to call the mainloop function, nothing will appear to the user.

# https://stackoverflow.com/questions/11868148/getting-files-in-a-directory-modified-within-a-date-range-in-linux-using-python          

https://stackoverflow.com/questions/11868148/getting-files-in-a-directory-modified-within-a-date-range-in-linux-using-python

One option would be to use something in lines of os.walk and filter out files based on ctime/mtime, which you can get like this:
import os.path, time
print "last modified: %s" % time.ctime(os.path.getmtime(file))
print "created: %s" % time.ctime(os.path.getctime(file))
If you prefer to do it with shell, then find is your friend, with the following flags:

-ctime n File's status was last changed n*24 hours ago.
-mtime n File's data was last modified n*24 hours ago.


# Parsing some files

import glob 
files=glob.glob('*') 
print("%s files"%(len(files)) )

out=open(r"D:\me\data\out.txt', 'w')
for filename in files:
    extract_info(filename)

def extract_info(filename):
    f=open(r"D:\me\data\%s"(%filename), 'r')
    line_1 = f.readline()
    line_2 = f.readline().replace(',','|')
    out.write("- " + filename + "\n")
    out.write(line1.replace(',','|') + "\n")
    out.write("---|"*line_1.count(',') + "---\n")
    out.write(line2.replace(',','|') + "\n")

import glob  
print('Named explicitly:')
for name in glob.glob('/home/geeks/Desktop/gfg/data.txt'):
    print(name)
  
# Using '*' pattern 
print('\nNamed with wildcard *:')
for name in glob.glob('/home/geeks/Desktop/gfg/*'):
    print(name)
  
# Using '?' pattern
print('\nNamed with wildcard ?:')
for name in glob.glob('/home/geeks/Desktop/gfg/data?.txt'):
    print(name)
  
# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for name in glob.glob('/home/geeks/Desktop/gfg/*[0-9].*'):
    print(name)    