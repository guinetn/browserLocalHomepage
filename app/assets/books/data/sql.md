# SQL - Sequential Query Language

Most widely used programming language for managing data in a relational database management system. 

Relational database is a set of relations and tables, which are connected with each other through some defined relationships. The main purpose of relational database design is to preserve the information and MINIMIZE DATA REDUNDANCY. 

### RDBMS - Relational Database Management Systems

Oracle
Very stable and mature but can be costly
https://www.oracle.com/uk/database/index.html

MySQL
Lightweight and fast to set up but not as mature as Oracle
https://www.mysql.com/

PostgreSQL
Good for certain use cases but not super fast
https://www.postgresql.org/

Microsoft SQL Server

MariaDB

SQLite

### SQL COMMANDS

DML - Data Manipulation Language: 
    Select
        SELECT expressions
        FROM table_name
        WHERE condition1, condition2,…., conditionN;
            
        SELECT student_name FROM student WHERE age < 18;
        SELECT DISTINCT column_name1, column_name2,…., column_nameN FROM table_name;    
        SELECT DISTINCT Name, Age FROM Student;
        SELECT Name, Age FROM Student ORDER BY Name;
        SELECT Name, Age FROM Student ORDER BY Name DESC;
        SELECT CURDATE();
        SELECT * FROM Students where ROLL_NO BETWEEN 10 AND 50;
        SELECT * FROM students where ROLL_NO IN (8,15,25);
        Alias: SELECT S.StudentID, E.Result from student S, Exam as E where S.StudentID = E.StudentID
        
    Modifying a relational database
    These commands are not auto-committed (changes made aren’t automatically saved)
    
    Insert
        INSERT INTO table_name (column_name1, column_name2,….,column_nameN) VALUES (value1, value2,….,valueN);
        INSERT INTO table_name VALUES (value1, value2,….,valueN);
        INSERT INTO Student (Name, Age) VALUES (“Vijay”, “25”);
        INSERT INTO table_name1 SELECT column_name1, column_name2,….,column_nameN FROM table_name2;
        INSERT INTO Student SELECT Id, Stream FROM Student_Subject_Details
    Update
        UPDATE table_name SET column_name1 = value1, column_name2 = value2,….,column_nameN = valueN (for updating all rows)
        UPDATE table_name SET column_name1 = value1, column_name2 = value2,….,column_nameN = valueN [WHERE CONDITION] (for updating particular rows)
        UPDATE Student SET Name = “Akhil” WHERE Id = 22;
    Delete
        DELETE FROM Student;
        DELETE FROM Student WHERE Name = “Akhil”;
    Merge        
        Conditional updates or inserts into the table. 
        It updates the row if it exists or inserts the row if it does not exist.
    
DDL - Data Definition Language: creating, deleting, and modifying data
    Create
        CREATE TABLE table_name (column_name1 data_type(size), column_name2 data_type(size),…., column_nameN data_type(size));
        CREATE TABLE Employee(Name varchar2(20), D.O.B. date, Salary number(6);
        CREATE TABLE NEW_TABLE_NAME AS SELECT [column1, column2 ……column] FROM EXISTING_TABLE_NAME [WHERE ]

    Alter
        ALTER TABLE table_name ADD (column_name1 data_type (size), column_name2 data_type (size),….., column_nameN data_type (size));
        ALTER TABLE Student ADD (Address varchar2(20));
        ALTER TABLE Student ADD (Age number(2), Marks number(3));
        ALTER TABLE table_name MODIFY (column_name new_data_type(new_size));
        ALTER TABLE Student MODIFY (Name varchar2(20));
        ALTER TABLE table_name DROP COLUMN column_name;
        ALTER TABLE Student DROP COLUMN Age;
    Drop
        DROP TABLE table_name;
    Truncate
        TRUNCATE TABLE table_name;
    Describe
    Rename
        RENAME old_table_name TO new_table_name

DCL - Data Query Language: Manage authorizations. Enable or disable a user from accessing information from a database
    Grant:  granting user access privileges to a database.
        GRANT object_privileges ON table_name TO user_name1, user_name2,….,user_nameN;
        GRANT object_privileges ON table_name TO user_name1, user_name2,….,user_nameN WITH GRANT OPTION; (allows the grantee to grant user access privileges to others)
        GRANT SELECT, UPDATE ON Student TO Akhil Bhadwal
        GRANT ALL ON Student TO Akhil Bhadwal WITH GRANT OPTION

    Revoke: for taking back permission given to a user.
        REVOKE object_privileges ON table_name FROM user1, user2,… userN;
        REVOKE UPDATE ON Student FROM Akhil;

    User access privileges:
        ALTER
        DELETE
        INDEX
        INSERT
        SELECT
        UPDATE
        
TCL - Transaction Control Language
    SavePoint: for rolling back to a certain state known as the savepoint. Savepoints need to be created first so that they can be used for rollbacking transactions partially.
        SAVEPOINT savepoint_name;
        
        SQL> SAVEPOINT A
        SQL> INSERT INTO TEST VALUES (1,'Savepoint A');
        1 row inserted.
        SQL> SAVEPOINT B
        SQL> INSERT INTO TEST VALUES (2,'Savepoint B');
        1 row inserted.
        SQL> ROLLBACK TO B;
        Rollback complete.
        SQL> SELECT * FROM TEST;
        ID MSG
        -------- -----------
        1  Savepoint A

    RollBack: to undo transactions that aren’t yet saved in the database.
        DELETE FROM Student WHERE Age = 25;
        ROLLBACK;
    Commit: for saving all transactions made to a database.        
        DELETE FROM Student WHERE Age = 25;
        COMMIT;
        
        BEGIN TRANSACTION;   
        DELETE FROM HumanResources.JobCandidate  
            WHERE JobCandidateID = 13;   
        COMMIT TRANSACTION;  

    TSQL - Transact SQL         
        Extension of SQL developed by Sybase and used by Microsoft

### SQL QUERY EXECUTION ORDER
- FROM, JOIN
- WHERE
- GROUP BY
- HAVING
- SELECT
- DISTINCT
- ORDER BY
- LIMIT, OFFSET

### JOINS
CROSS JOIN                    # cartesian product
JOIN ... ON ...               # no NULL values
LEFT JOIN ... ON ...          # values in the left table else NULL
RIGHT JOIN ... ON ...         # values in the right table else NULL
FULL JOIN ... ON ...          # values in both tables else NULL

There are four different types of JOIN, but in most cases, we only use INNER, LEFT, and FULL JOIN.  
RIGHT JOIN is not very intuitive and can be easily rewritten using LEFT JOIN.

![](assets/books/data/assets/join_01.jpg)
![](assets/books/data/assets/join_02.jpg)

## duplicates

    UNION operator combines the results of two or more Select statements by removing duplicate rows. The columns and the data types must be the same in the SELECT statements.

    SELECT City FROM Customers
    UNION
    SELECT City FROM Suppliers
    ORDER BY City;

## GROUP
Group functions work on a set of rows and return a single result per group.
AVG, MAX, MIN, SUM, VARIANCE, COUNT
 
### GROUP BY
SQL's most essential function used for data aggregation (sum, average, minimum, maximum)
A common pitfall is mixing WHERE and HAVING when filtering data along with GROUP BY 

SELECT student_id, school_year, AVG(gpa) AS avg_gpa
FROM gpa_history
WHERE is_required = TRUE
GROUP BY student_id, school_year
HAVING AVG(gpa) >= 3.5

### NULL
unknown or missing data values.
IS (NOT) NULL, IFNULL, and COALESCE

### Window functions

Select “TOP N”: use either ORDER BY or ranking functions

RANK/DENSE_RANK /ROW_NUMBER: these assign a rank to each row by ordering specific columns. If any partition columns are given, rows are ranked within a partition group that it belongs to.
LAG/LEAD: it retrieves column values from a preceding or following row based on a specified order and partition group.

WITH T AS (
SELECT *, ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY employee_salary DESC) AS rank_in_dep
FROM employee_salary)
SELECT * FROM T
WHERE rank_in_dep <= 3

* ROW_NUMBER()

numbers the rows (1 based) according to the ORDER BY part of the window statement.

SELECT start_terminal, start_time, duration_seconds,
       ROW_NUMBER() OVER (ORDER BY start_time) AS row_number
FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08'

PARTITION clause: to begin counting 1 again in each partition

SELECT start_terminal, start_time, duration_seconds,
       ROW_NUMBER() OVER (PARTITION BY start_terminal ORDER BY start_time) AS row_number
FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08'

* RANK() 
If you order by start_time and some terminals have two identical start times: they are given the same rank (whereas ROW_NUMBER() gives them different numbers).

SELECT start_terminal, duration_seconds, 
       RANK() OVER (PARTITION BY start_terminal ORDER BY start_time) AS rank
FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'

DENSE_RANK()
    RANK() would give the identical rows a rank of 2, then skip ranks 3 and 4, so the next result would be 5
DENSE_RANK() 
    would still give all the identical rows a rank of 2, but the following row would be 3—no ranks would be skipped.
    
    
## SQL constraints
To specify the rules of data type in a table.    

- NOT NULL - Restricts NULL value from being inserted into a column.
- DEFAULT - Automatically assigns a default value if no value has been specified for the field.
- UNIQUE - Ensures unique values to be inserted into the field.
- INDEX - Indexes a field providing faster retrieval of records.
- PRIMARY KEY - Uniquely identifies each record in a table.
- FOREIGN KEY - Ensures referential integrity for a record in another table.
- CHECK - Verifies that all values in a field satisfy an integrity constraint 

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        CHECK (Age>=18)
    );

## Data integrity

Defines the accuracy, consistency, reliability of data that is stored in the database.

There are four kinds of data integrity:
- Row integrity
- Column integrity
- Referential integrity
- User-defined integrity

## primary key
a field in the table which uniquely identifies a row. It cannot be NULL

## foreign key
a field in one table, which is a primary key in another table. A relationship is created between the two tables by referencing the foreign key of one table with the primary key of another table.

## composite key

When more than one column is used to define the primary key

Create a composite key in MySQL

    CREATE TABLE SAMPLE_TABLE  
    (COL1 integer,  
    COL2 varchar(30),  
    COL3 varchar(50),  
    PRIMARY KEY (COL1, COL2));  

## entities and relationship

* Entity
A person, place, any real-world thing that `can be represented as a table` is called an entity.
Example: Employee table represents the details of an employee in an organization.

* Relationship
Relationship defines the `dependency that entities share` amongst each other.
Example: Employee name, id, salary might belong to the same or different tables.

* One-Many Relationship
a record in One Table can be associated or related to Many records in another table.

## index

# composite index
An index that is created on more than one column

## clustered indexes 

A table can have only one clustered index. 
This type of index reorders the table based on the key values and physically stores them in that order.

Creates a clustered index on the “gender” and “total_score” columns. 
An index that is created on more than one column is called the “composite index”.
    
CREATE CLUSTERED INDEX IX_tblStudent_Gender_Score
ON student(gender ASC, total_score DESC)
## non-clustered indexes

Doesn't have the physical ordering of the data in the table it has a logical order.
Doesn’t sort the physical data inside the table. 
A non-clustered index is stored in one place, and table data is stored in another place. 
This allows for more than one non-clustered index per table.

Creates a non-clustered index on the “name” column of the student table 
    CREATE NONCLUSTERED INDEX IX_tblStudent_Name
    ON student(name ASC)
The table data and index will be stored in different places. 
The index sorts by name in ascending order. 

## SQL TYPES

CHAR is used to store fixed-length character strings
VARCHAR2 is used to store variable-length character strings.

## Trigger

stored programs that get automatically executed when an event such as INSERT, DELETE, UPDATE(DML) statement occurs. 
Triggers can also be evoked in response to Data definition statements(DDL) and database operations, for example, SERVER ERROR, LOGON.

```sql
create trigger dbtrigger  
on database  
for  
create_table,alter_table,drop_table  
as  
print'you can not create ,drop and alter table in this database'  
rollback; 
create trigger emptrigger  
on emp  
for  
insert,update,delete  
as  
print'you can not insert,update and delete this table i'  
rollback;
```

## NORMALIZATION - DENORMALIZATION

Data Redundancy: When the same set of data is present multiple times in the database (storage waste). Redundant data has an impact on performance

Normalized: Optimizes for minimizing redundancy, not for read time.

Denormalized: Optimizes for read time, not for minimizing redundancy.
Technique sometimes used to improve performance so the table design allows redundant data to avoid complex joins. 
If the application involves heavy read operations, then de-normalization is used at the expense of the write operations performance.

## system functions

perations performed on the database server, and values are returned accordingly. Example @@ERROR - Returns 0 if the previous Transact-SQL statement encountered no errors. Otherwise returns an error number.
@@ERROR - Returns 0 if the previous Transact-SQL statement encountered no errors. 

## transaction log

audit trail file where the history of actions executed by the DBMS is stored.

shared lock
When two transactions are granted read access to the same data, they are given a shared lock. 
This enables reading the same data, and data is not updated until the shared lock is released.

deadlock
Unwanted situation where two or more transactions are waiting indefinitely for one another to 
release the locks.

## Schema

A schema is a collection of types, interfaces, enums, and unions that make up your API’s data model. 
Accessing, inserting, deleting, finding, and sorting the data are some of the well-known operations that one can perform using data structures.

Collection of database objects in a database for a particular user/owner. 
Objects can be tables, views, indices and so on.

## Stored procedures
Function consisting of many SQL statements consolidated into a stored procedure and are executed wherever and whenever required. 

Create PROCEDURE Procedure1
AS BEGIN
Exec Procedure2
END


## character manipulation

CONCAT: joins two or more string values.
SUBSTR: extracts string of a specific length.
LENGTH: returns the length of the string
INSTR: returns the position of the specific character.
LPAD: padding of the left-side character value for right-justified value.
RPAD: padding of right-side character value for left-justified value.
TRIM: removes the defined character from beginning and end or both.
REPLACE: replaces a specific sequence of characters with another sequence of characters.

## Collation
Set of rules that determines how to store and compare data.
Case
Kana
Width
Accent

## More

https://hackr.io/blog/top-sql-interview-questions