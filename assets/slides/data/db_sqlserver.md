## SQL Server

INSERT INTO students VALUES ('Nick', 'Economy', 12321, NULL);
DELETE FROM students WHERE department = 'Economy' AND gid = 101;

Get Running Time
>EXPLAIN ANALYZE VERBOSE

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