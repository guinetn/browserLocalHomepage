# SQL

### SQL QUERY EXECUTION ORDER
- FROM, JOIN
- WHERE
- GROUP BY
- HAVING
- SELECT
- DISTINCT
- ORDER BY
- LIMIT, OFFSET

### JOIN
CROSS JOIN                    # cartesian product
JOIN ... ON ...               # no NULL values
LEFT JOIN ... ON ...          # values in the left table else NULL
RIGHT JOIN ... ON ...         # values in the right table else NULL
FULL JOIN ... ON ...          # values in both tables else NULL

There are four different types of JOIN, but in most cases, we only use INNER, LEFT, and FULL JOIN.  
RIGHT JOIN is not very intuitive and can be easily rewritten using LEFT JOIN.

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