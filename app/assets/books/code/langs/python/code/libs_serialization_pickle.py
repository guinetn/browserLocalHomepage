
# Serialisation
  
Pickle : Python pickle module is used for serializing and de-serializing python object structures. The process to convert any kind of python object (list, dict, etc.) into byte streams (0s and 1s) is called pickling or serialization or flattening or marshalling. We can converts the byte stream (generated through pickling) back into python objects by a process called as unpickling.
- https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask
- https://pythonprogramming.net/python-pickle-module-save-objects-serialization/
- https://www.bogotobogo.com/python/Flask/Python_Flask_Embedding_Machine_Learning_1.php

# Saving model to current directory
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(regressor, open('model.pkl','wb'))
'''
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2.6, 8, 10.1]]))
'''

# Serializing Python Objects

# This process is used to serialize Python object to a byte stream for later reuse.
# You can do that using pickle module:
import pickle 
fd = open('myfile.pk ', 'wb') 
pickle.dump(mydata,fd)
# You can deserialize this data using load() function like this:
import pickle 
fd = open('myfile.pk ', 'rb') 
mydata = pickle.load(fd)


"""

https://docs.python.org/2/library/pickle.html

To save objects as .pkl files. The process of saving the object is referred to as pickling
- to save objects like lists, dictionaries...
- popular use of pickling in Data Science to save trained models or machine learning pipelines into .pkl files

Pickle files are used to store the serialized form of Python objects. This means objects like list, set, tuple, dict, etc. are converted to a character stream before being stored on the disk. This allows you to continue working with the objects later on. These are particularly useful when you have trained your machine learning model and want to save them to make predictions later on.

So, if you serialized the files before saving them, you need to de-serialize them before you use them in your Python programs. This is done using the pickle.load() function in the pickle module. But when you open the pickle file with Python’s open() function, you need to provide the ‘rb’ parameter to read the binary file.

import pickle

with open('./Importing files/sample_pickle.pkl','rb') as file:
    data = pickle.load(file)

# pickle data
print(type(data))

df_pkl = pd.DataFrame(data)
df_pkl


import pickle 

...
# categorical refers to an object in Python (e.g. list).
...
# Write pickle
with open('categorical.pkl', 'wb') as pickle_file:
    pickle.dump(categorical, pickle_file)

# Load pickle    
with open('categorical.pkl', 'rb') as pickle_file:
    categorical = pickle.load(pickle_file)

"""




import pickle

filename = 'libs_serialization__pickle.py.data'
# take user input to take the amount of data
number_of_data = int(input('Enter the number of data (0 to read): '))
print(f"number_of_data: {number_of_data}")

if (number_of_data>0):
	data = []

	# take input of the data
	for i in range(number_of_data):
	    raw = input('Enter data '+str(i)+' : ')
	    data.append(raw)

	# open a file, where you ant to store the data
	file = open(filename, 'wb')

	# dump information to that file
	pickle.dump(data, file)

	# close the file
	file.close()



# open a file, where you stored the pickled data
file = open(filename, 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print(f'Showing the pickled data: {filename}')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1


# ex: read the model of ML
# https://github.com/basil-b2s/Language-Detector/blob/master/app.py