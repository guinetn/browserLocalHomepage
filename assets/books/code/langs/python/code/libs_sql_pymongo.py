# PyMongo

import pymongo

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB
db.classroom.insert_many(
    [
      {
        'name': 'Jerry',
        'hobbies': 'gardening',
        'classroom_teacher': "Jerry's Dad",
        'exam_scores': [1, 0, -25]
      },
      {
        'name': 'Muhammed',
        'hobbies': {'exercise': ['swimming', 'running'],
                    'games': 'chess'},
        'classroom_teacher': 'Jerry',
        'exam_scores': [100, 100, 100]
      }
    ])
    
    
    
import pprint  # pprint to make it easier to read the output.

classroom = db.classroom.find()

for student in classroom:
    pprint.pprint(student)
    print()

# {'_id': ObjectId('606b608f07fe3f5be3d00efd'),
#  'name': 'Jerry',
#  'hobbies': 'gardening',
#  'classroom_teacher': "Jerry's Dad",
#  'exam_scores': [1, 0, -25]}

# {'_id': ObjectId('606b608f07fe3f5be3d00efe'),
#  'name': 'Muhammed',
#  'hobbies': {'exercise': ['swimming', 'running'], 'games': 'chess'},
#  'classroom_teacher': 'Jerry',
#  'exam_scores': [100, 100, 100]}    

# add a document with new fields.
import datetime as dt

db.classroom.insert_one(
    {
        'name': 'Samantha',
        'birthday': dt.datetime(2012, 2, 29),
        'favorite_color': None
    }
)


# queries

for student in db.classroom.find({'birthday': {'$exists': True}}):
    pprint.pprint(student)

# {'_id': ObjectId('606b893307fe3f5be3d00f04'),
#  'birthday': datetime.datetime(2012, 2, 29, 0, 0),
#  'favorite_color': None,
#  'name': 'Samantha'}

for student in db.classroom.find({'hobbies.exercise': 'running'}):
    pprint.pprint(student)

# {'_id': ObjectId('606b891107fe3f5be3d00f03'),
#  'classroom_teacher': 'Jerry',
#  'exam_scores': [100, 100, 100],
#  'hobbies': {'exercise': ['swimming', 'running'], 'games': 'chess'},
#  'name': 'Muhammed'}


https://towardsdatascience.com/a-hands-on-demo-of-sql-vs-nosql-databases-in-python-eeb955bba4aa
