# JSON is commonly used with data APIS
# see: https://www.learnpython.org/en/Serialization


import json


userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse json to dict
user = json.loads(userJSON)
print(type(user))
print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)


import os
print(os.getcwd())
    
    
    
# There are two basic formats for JSON data. Either in a string or the object data-structure.
# The object data-structure, in Python, consists of lists and dictionaries nested inside each
# other. The object data-structure allows one to use python methods (for lists and dictionaries)
# to add, list, search and remove elements from the data-structure. The String format is mainly
# used to pass the data into another program or load into a data-structure.

person_dictionary = {'first_name': 'John', 'last_name': 'Smith', 'age': 42}
assert person_dictionary['first_name'] == 'John'
assert person_dictionary['age'] == 42

json_string = '{"first_name": "John", "last_name": "Smith", "age": 42}'

# To load JSON back to a data structure, use the "loads" method. This method takes a string
# and turns it back into the json object data-structure:
person_parsed_dictionary = json.loads(json_string)

assert person_parsed_dictionary == person_dictionary
assert person_parsed_dictionary['first_name'] == 'John'
assert person_parsed_dictionary['age'] == 42

# To encode a data structure to JSON, use the "dumps" method. This method takes an object and
# returns a String:
encoded_person_string = json.dumps(person_dictionary)

assert encoded_person_string == json_string






import urllib.request

url_mag="https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json"
url_plasma="https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"

mag = urllib.request.urlopen(url_mag)
mag_json = json.loads(mag.read())
plasma = urllib.request.urlopen(url_plasma)
plasma_json = json.loads(plasma.read())

import sqlite3
conn = sqlite3.connect("space.db", isolation_level=None)
cur = conn.cursor()
cur.execute('''
    CREATE TABLE mag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time DATETIME,
    bx REAL,
    by REAL,
    bz REAL,
    bt REAL
    );
    ''')
cur.execute('''
    CREATE TABLE plasma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time DATETIME,
    density REAL,
    speed REAL,
    temp REAL
    );
    ''')

for line in mag_json[1:]:    
    query = 'INSERT INTO mag (date_time, bx, by, bz, bt) VALUES ("%s", "%s", "%s", "%s", "%s")' % (line[0][:19], line[1], line[2], line[3], line[6])    
    cur.execute(query)

conn.commit()



data = {'name': 'erik', 'age': 38, 'married': True} 
json.dumps(data) 
'{"name": "erik", "age": 38, "married": true}'

print(json.dumps(data, indent=2))
{
  "name": "erik",
  "age": 38,
  "married": true
}

## Write JSON to a file

data = {'name': 'Eric', 'age': 38 }
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)


## Read a JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
    ...

## Pretty printing JSON
# Python’s JSON module can also be used from the command-line. 
# It will both validate and pretty-print your JSON:
'''
> echo "{ \"name\": \"Joe\", \"age\": 20 }" | \ python3 -m json.tool
{ 
    "name": "Joe",
    "age": 20
}    
'''
#  See also https://python.land/the-unix-shell/process-json-with-jq

"""
PARSE JSON IN PYTHON
Parsing a string of JSON data, also called decoding JSON, is as simple as using json.loads(...) (loads is short for load string).
It converts:
- objects to dictionaries
- arrays to lists,
- booleans, integers, floats, and strings are recognized for what they are and will be converted into the correct types in Python
- Any null will be converted into Python's None type

json.loads in action:
"""
jsonstring = '{"name": "erik", "age": 38, "married": true}'
data = json.loads(jsonstring)
print(data)
# >> {'name': 'erik', 'age': 38, 'married': True}
# The output might look like a string, but it’s actually a dictionary 
type(data)
#>><class 'dict'>
print('Hello', data['name'], "you're", data['age'], 'years old')
#>>Hello erik you're 38 years old
