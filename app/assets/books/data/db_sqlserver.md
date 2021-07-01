## SQL Server

Install sql server express...fast... connect using ".\sqlexpress"

C:\Program Files\Microsoft SQL Server

- https://github.com/Microsoft/sql-server-samples/tree/master/samples
- https://github.com/Azure/azure-sql-database-samples
- https://docs.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?tabs=azure-portal
- https://www.codeproject.com/Tips/5298962/How-to-Create-SQL-Server-Database-Project-With-Vis

Create New SQL Server Database Project
Import database schema from an existing database, a .sql script file or a Data-tier application (.bacpac) the Project
Publish to create new Database in SQL server

Create SQL server database project in Visual Studio 
Import the SQL database: development database and finally publish into UAT, production or another server from Visual Studio itself with this project template. 
Imports/publishing options of the database: compare and identify the differences in two databases (development and production), then we can generate updated script or update directly from the project

![](assets/sqlserver_cheatsheetjpg
INSERT INTO students VALUES ('Nick', 'Economy', 12321, NULL);
DELETE FROM students WHERE department = 'Economy' AND gid = 101;

Get Running Time
>EXPLAIN ANALYZE VERBOSE

SQL SERVER: NULL = CTRL + ZERO


Import Base  Attach - Ecrase DB Files - Detach
How to import a database in Sql Server

In Sql Server Management Studio

1. Create new database 'myDB'
2. Right clic on 'myDB' database. Tasks -> Choose 'Detach'
3. Copy files myDB.mdf & myDB.ldf in
C:\Program Files\Microsoft SQL Server\MSSQL10.MSSQLSERVER\MSSQL\DATA
4. Right clic on 'myDB' database. Tasks -> Choose 'Attach'


### Indexing
Indexing By Hash Table (Equality Searching / Deleting)
CREATE INDEX indexname
ON tablename
USING hash (colname);
Indexing By Binary Tree (Range Searching / Sorting / Deleting)
CREATE INDEX indexname
ON tablename
USING btree (colname);
CLUSTER tablename
USING indexname
No Index (Inserting)
Delete indexing
DROP INDEX IF EXISTS indexname CASCADE;


### Conditional Statement
CASE WHEN ... THEN ...
     WHEN ... THEN ...
     ELSE ...
END AS ...

### Window Function
SUM all column name
SUM(col) OVER () 
            
SUM the col1 values group by cole2  
SUM(col1) OVER (PARTITION BY col2)       
SUM the col1 values group by cole2    
SUM(col1) OVER (  
     PARTITION BY col2  
     ORDER BY col1  
     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)  
# Accumulate col1 values group by cole2
SUM(col1) OVER (
    PARTITION BY col2
    ORDER BY col1)       
# Accumulate col1 values group by cole2   
SUM(col1) OVER (
     PARTITION BY col2
     ORDER BY col1
     ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
# Add the col1 values (current, current + 1) group by col2
SUM(col1) OVER (
     PARTITION BY col2
     ORDER BY col1
     ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)

### CTE - Common Table Expression
make the table a variable for us to use in the new query

WITH tablename1 AS (SELECT * FROM tablename3),
     tablename2 AS (SELECT * FROM tablename4)
SELECT tablename1.colname1, tablename2.colname2
FROM tablename1, tablename2;

### Function

CREATE OR REPLACE FUNCTION sid_by_name(name VARCHAR) 
RETURNS TABLE (sid INTEGER, sname VARCHAR) AS
$$
    SELECT sid, sname
    FROM students
    WHERE sname = name
$$
LANGUAGE SQL;
Delete a function
DROP FUNCTION IF EXISTS functname;

### View
Create a view
CREATE VIEW viewname AS
...
Delete a view
DROP VIEW IF EXISTS viewname CASCADE;

### JSON
Get a JSON value of ‘_id’ in a json datatype
SELECT colname -> '_id'
FROM tablename;
Get a text value of ‘_id’ in a json datatype
SELECT colname ->> '_id'
FROM tablename;
Convert a table to JSON
SELECT TO_JSON(tablename) 
FROM tablename;
 
### PIVOT

input                                  Output 
+---------+----------+---------+       +---------+----------+-----------+-----------+
|   sid   |  subject |  grade  |       |   sid   |   Math   |  Physics  |  English  |
+---------+----------+---------+       +---------+----------+-----------+-----------+
|    1    |   Math   |   94    |       |    1    |    94    |     87    |           |
|    1    |  Physics |   87    |       |    2    |          |           |     82    |
|    2    |  English |   82    |       |    3    |    91    |           |     97    |
|    3    |   Math   |   91    |       +---------+----------+-----------+-----------+
|    3    |  English |   97    |
+---------+----------+---------+

WITH tmp AS (
   SELECT sid,
       CASE WHEN subject = 'Math' THEN grade END AS Math,
       CASE WHEN subject = 'Physics' THEN grade END AS Physics,
       CASE WHEN subject = 'English' THEN grade END AS English
   FROM finalscore
)
SELECT sid, 
       SUM(Math) AS Math, 
       SUM(Physics) AS Physics, 
       SUM(English) AS English
FROM tmp
GROUP BY sid
ORDER BY sid;







IF OBJECT_ID('Dept','U') IS NOT NULL
	DROP TABLE dbo.Dept

CREATE TABLE dbo.Dept
(
	DeptId INT PRIMARY KEY,
	DeptName VARCHAR(10) NOT NULL,
	DeptDesc VARCHAR(100)
)
INSERT INTO dbo.Dept (DeptId,DeptName,DeptDesc)
VALUES 
(201,'NS','Network Security'),
(202,'FS','Financial Services'),
(203,'HR','Human Resources')
SELECT DeptId,DeptName,DeptDesc
FROM dbo.Dept
/*
DeptId	DeptName	DeptDesc
201	NS	Network Security
202	FS	Financial Services
203	HR	Human Resources
*/
IF OBJECT_ID('Emp','U') IS NOT NULL
	DROP TABLE dbo.Emp

CREATE TABLE dbo.Emp
(
	EmpId INT PRIMARY KEY,
	EmpName VARCHAR(100) NOT NULL,
	EmpAddr VARCHAR(100) NOT NULL,
	DeptId INT NOT NULL,
	CONSTRAINT FK_Emp_DeptId FOREIGN KEY (DeptId) REFERENCES dbo.Dept(DeptId) 
)
INSERT INTO dbo.Emp (EmpId,EmpName,EmpAddr,DeptId)
VALUES 
(101,'e1','e1addr1',201),
(102,'e2','e2addr2',201),
(103,'e3','e3addr3',202),
(104,'e4','e4addr4',202),
(105,'e5','e5addr5',203)
SELECT EmpId,EmpName,EmpAddr,DeptId
FROM dbo.Emp
--Retrieve records by joining both the tables
SELECT E.EmpId,E.EmpName,E.EmpAddr,D.DeptName,D.DeptDesc
FROM dbo.Emp E
INNER JOIN dbo.Dept D ON E.DeptId = D.DeptId
/*
EmpId	EmpName	EmpAddr	DeptName	DeptDesc
101	e1	e1addr1	NS	Network Security
102	e2	e2addr2	NS	Network Security
103	e3	e3addr3	FS	Financial Services
104	e4	e4addr4	FS	Financial Services
105	e5	e5addr5	HR	Human Resources
*/


## Json

https://jsonformatter.org/json-pretty-print

- https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server

- https://levelup.gitconnected.com/how-to-easily-parse-and-transform-json-in-sql-server-c0b091a964de

- https://docs.microsoft.com/en-us/sql/relational-databases/json/convert-json-data-to-rows-and-columns-with-openjson-sql-server?view=sql-server-ver15

CREATE TABLE superHero(
 [heroID] [int] PRIMARY KEY CLUSTERED IDENTITY(1,1) NOT NULL,
 [description] nvarchar(MAX) NOT NULL,
) ON [PRIMARY]
insert into superhero([description])
select '{
  "universe": "dc",
  "characters": [
    {
      "hero": "superman",
      "alias": "clark kent",
      "powers": [
        "x-ray vision",
        "super strength",
        "super speed",
        "laser eyes",
        "bullet proof"
      ],
      "friends": [
        {
          "hero": "batman",
          "alias": "bruce wayne"
        },
        {
          "hero": "cyborg",
          "alias": "victor stone"
        }
      ]
    }
  ]
}'

select * from superHero
select * 
from OPENJSON((select description from superHero where heroID = 1))

select * 
from OPENJSON(
    (select description from superHero where heroID = 1),
    '$.characters[0]'
  )
  
  select *
from superHero s
CROSS APPLY OPENJSON(s.description)



## SQL Server User Defined Type (UDT)
https://www.codeproject.com/Articles/28626/Vector-A-Concept-Driven-Approach-to-SQL-UDT

User Defined Type (UDT) is a SQL Server data type created using your favorite .NET language. It is one of the artifacts you can create with SQL Server CLR Integration (SQL-CLR for short). Let’s just say it’s the closest thing SQL Server can get to object-based programming.

