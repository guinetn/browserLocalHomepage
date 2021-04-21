
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
#	lower_time_bound = datetime.datetime.now() - timedelta(minutes=min)
#	return filter(lambda f: datetime.datetime.fromtimestamp(os.path.getmtime(f)) > lower_time_bound, files)

for root, dirs, files in os.walk(src):
	for name in files_before(root, files, 60):
		print(join(root, name), modification_date(join(root, name)), creation_date(join(root, name)))
#for root, dirs, files in os.walk(src):
#	for name in files:


window = Tk()
window.title("Welcome to LikeGeeks app")
window.mainloop() # calls the endless loop of the window, so the window will wait for any user interaction till we close it.
		  # If you forget to call the mainloop function, nothing will appear to the user.

# https://stackoverflow.com/questions/11868148/getting-files-in-a-directory-modified-within-a-date-range-in-linux-using-python		  