# SQL


## sqlalchemy
https://www.sqlalchemy.org/

To create, modify, and interact with relational databases in Python via an object relational mapper. The main idea to wrap your head around is that SQLAlchemy uses Python classes to represent database tables. Instances of a Python class can be considered rows of a table.
SQLAlchemy is an open-source SQL toolkit and object-relational mapper for the Python programming language


https://www.fullstackpython.com/object-relational-mappers-orms.html



from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session

# Use the default method for abstracting classes to tables
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Classroom(Base):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(255))

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    hobby = Column(String(255))
    classroom_id = Column(Integer, ForeignKey(Classroom.id))

class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    exam_id = Column(Integer)
    student_id = Column(Integer, ForeignKey(Student.id))
    exam_score = Column(Integer)
    
    
## create our database and tables
 
# Create DB connection
engine = create_engine("sqlite:///students.sqlite")
conn = engine.connect()
session = Session(bind=engine)

# Create metadata layer that abstracts our SQL DB
Base.metadata.create_all(engine)

classroom1 = Classroom(teacher_name="Jerry's Dad")
classroom2 = Classroom(teacher_name="Jerry")

jerry = Student(name='Jerry', hobby='gardening', classroom_id=1)
muhammed = Student(name='Muhammed', hobby='swimming', classroom_id=2)

exam_j1 = Grade(exam_id=1, student_id=1, exam_score=1)
exam_j2 = Grade(exam_id=2, student_id=1, exam_score=0)
exam_j3 = Grade(exam_id=3, student_id=1, exam_score=-25)

exam_m1 = Grade(exam_id=1, student_id=2, exam_score=100)
exam_m2 = Grade(exam_id=2, student_id=2, exam_score=100)
exam_m3 = Grade(exam_id=3, student_id=2, exam_score=100)


## write our data to the database
objects = [classroom1, classroom2, jerry, muhammed,
           exam_j1, exam_j2, exam_j3, exam_m1, exam_m2, exam_m3]:

for obj in objects:
    session.add(obj)

# Commit changes to database
session.commit()




import pandas as pd

query = """
    SELECT s.id AS student_id,
           s.name AS student_name,
           s.hobby AS student_hobby,
           c.id AS classroom_id,
           c.teacher_name,
           g.exam_id,
           g.exam_score
      FROM student AS s
INNER JOIN grade as g
        ON s.id = g.student_id
INNER JOIN classroom as c
        ON c.id = s.classroom_id;"""

pd.read_sql_query(query, session.bind)