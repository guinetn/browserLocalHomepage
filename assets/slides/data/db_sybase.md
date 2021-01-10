# SYBASE

Has a Single-Process, Multi-threaded Database Engine 
Includes a query optimizer 
! case sensitive
Comments: --
sp_help 
sp_helptext objname [,number]
sp_depends objname[, column_name]

Standard SQL: 
* DDL (Data Definition language)
* DML (Data Modification language)
* DCL (Data Control Language) 

TSQL (Transact-SQL) = SQL + flow-control (if and while), local variables, etc..

4 main verbs:  select, insert, update, delete.

LIST TABLES
select * from sysobjects 
select * from sysobjects where type = 'U' order by name

LIST COLS
SELECT c.colid, c.name colname,
       t.name Type,
       Convert(varchar(10), c.prec ) +
           CASE WHEN c.scale > 0 THEN ',' + Convert(varchar(10), c.scale) 
                         ELSE '' 
END Taille
 FROM syscolumns c INNER JOIN systypes t ON t.usertype=c.usertype
WHERE c.id=object_id('nom_table_ici')
ORDER BY c.colname

select * into Test from Test    -- create table
create table #temptable (task char(30)) 
select * from SYS.SYSPROCEDURE where proc_defn like '%whatever%' 
select * from syscomments where texttype = 0 and text like '%whatever%' 
select * from sysobjects where sysobjects.type = 'P' -- STORED PROCEDURES
select * from sysobjects where sysobjects.type = 'U' order by name -- TABLES
select name from sysobjects where type = "U" order by name

select distinct sysobjects.name, case   
    when sysobjects.type = 'TR' then 'TRIGGER'   
    when sysobjects.type = 'P' then 'PROCEDURE'   
    when sysobjects.type = 'V' then 'VIEW'   
    else 'UNKNOWN' 
    end 
type, text from sysobjects 
inner join syscomments 
on sysobjects.id = syscomments.id and  sysobjects.type = 'P'

convert(varchar(255) not null, text)
where syscomments.text like '%tbl_books%' 
select proc_name from sysprocedures where proc_defn like "%tbl_books%" 

SELECT c.name colname FROM syscolumns c INNER JOIN systypes t ON t.usertype=c.usertype WHERE c.id=object_id('nom_table_ici') ORDER BY c.colname

## DDL - Sybase data types

Only numeric data types with a precision of zero can be used for an identity column.

|DATATYPE           | STORAGE     | RANGE/LENGTH           | COMMENTS|
|---|---|---|---|---|
|integer            |  4          |  +/- 2.1 billion||
|smallint           |  2          |  +/- 32768||
|tinyint            |  1          |  0 .. 255||
|float              |  4          |                        |   storage req is machine dependant|
|real               |  4|||
|double precision   |  8|||
|smallmoney         |  4          |  +/- 214,748           |   4 decimal places|
|money              |  8          |  +/- 922 trillion      |   4 decimal places|
|decimal/numeric    |  varies|||
|decimal(9,0)       |  4|||
|decimal(12,0)      |  5|||
|char(n)            |  n          |  length <= 255||
|varchar(n)         |  varies     |  length <= 255         |   over 4000 allowed in ASE 12.5|
|text               |  varies     |  length up to 2 GB     |   16 bytes stored in record (default)|
|image              |  varies     |  length up to 2 GB     |   16 bytes stored in record (default)|
|datetime           |  8          |  1/1/1753 .. 12/31/9999|    precision to 1/300 second|
|smalldatetime      |  4          |  1/1/1900 .. 6/6/2079  |    precision to minutes|
|timestamp          |  8          |                        |    same as varbinary(8)|
|bit                |  1          |  0/1                   |    up to 8 bit fields stored within 1 byte|
|binary(n)          |  length n|||
|varbinary(n)       |  length n|||

Datetime: starts with 1753 because the English-speaking world converted from the Julian to the Gregorian calendar in 1752. To do that, the day after September 2, 1752 was decreed to be September 14, 1752. 

## Listing object names and attributes

Examples below are formatted to run using the isql utility.
/* list all table names for current database */
select name from sysobjects where type = 'U'
go
sp_tables
go
/* list all trigger names for current database */
select name from sysobjects where type = 'T'
go
/* list all procedure names for current database */
select name from sysobjects where type = 'P'
go
/* display column definitions and indexes for employee table */
sp_help employee
go
/* display spaced used for employee table */
sp_spaceused employee
go
/* display source code for proc_rtv_employee */
sp_helptext proc_rtv_employee
go

## Creating a table

Table create examples:
create table employee (
emp_id    numeric(8,0)  identity,
fname     varchar(10)   not null,
lname     varchar(25)   not null,
salary    money         not null,
dept_cd   char(3)       not null,
fax_no    integer       null
)
go
create table invoice (
invoice_id     numeric(8,0)  identity,
sales_rep_id   numeric(8,0)  not null,
date           smalldatetime not null,
comment        varchar(255)  null )
on data_seg2
go

create table  err_cd (
 err_id       integer       not null,
 err_desc     varchar(60)   not null,
   constraint pk_err_cd primary key clustered (err_id)
)
go

## Creating a proxy table

Proxy table create example:
create proxy_table invoice_items at 'SERVERXXX01.dbxxx001.dbo.invoice_items'
go

## Altering a table

Alter table examples:
alter table employee add cell_no numeric(10) null
go
alter table employee drop constraint 'emp_dept_constr'
go

/* add default */
alter table charge_item replace price_overridable_ind default 0
go

/* change column name -- quotes are required */
sp_rename 'employee.dept',dept_name
go


## Creating an index

Sample index creates:
create unique clustered index emp_idx
  on employee (emp_id)
go
create index emp_name_idx
  on employee (lname)
go


-- With sorted data!

create unique clustered index pk_invoice_data on invoice_data  with sorted_data on segment1
go

## Clustered vs non-clustered indexes

Typically, a clustered index will be created on the primary key of a table, and non-clustered indexes are used where needed. 

Non-clustered indexes
Leaves are stored in b-tree
Lower overhead on inserts, vs clustered
Best for single key queries
Last page of index can become a 'hot spot'

Clustered indexes
Records in table are sorted physically by key values
Only one clustered index per table
Higher overhead on inserts, if re-org on table is required
Best for queries requesting a range of records
Index must exist on same segment as table


Note! With "lock datapages" or "lock datarows" ... clustered indexes are sorted physically only upon creation. After that, the indexes behave like non-clustered indexes.

## Creating a constraint

Contraints are used to define primary keys, enforce uniqueness, and to describe foreign key relationships. Note that unique or primary key constraints create indexes upon creation.
/* primary key for the employee table */
alter table employee add constraint
  emp_constr primary key(emp_id)
go
/* add unique requirement for invoice table */
alter table invoice add constraint
  inv_constr unique nonclustered(cust_id,inv_date)
go
/* add foreign key for relationship between invoice and employee */
alter table invoice add constraint inv_fk_emp
  foreign key (sales_rep_id)
  references employee(emp_id)
go

## Creating a stored procedure

Stored procedures a compiled versions SQL statements. Performance benefits are significant as network traffic is reduced, and the optimizer does not need to re-parse the code.
/* stored procedure to retrieve an invoice */
create procedure proc_rtv_invoice (@inv_id numeric(8,0) as

select inv_id, inv_date, salesrep_emp_id
from invoice
where inv_id = @inv_id

return
go

/* now, execute the stored procedure */
exec proc_rtv_invoice 325
go

## Table Partitioning

Insert performance on partitioned tables is improved, as multiple 'entry points' (last page entries) are created. Partitioned tables require slightly more disk space and need a chunk of memory also.
/* create 4 partitions for the invoice table */
alter table invoice
partition 4
go

## Tables which span multiple segments

Tables containg large amounts of data (> 2 GB) need to be spread across several devices, using sp_placeobject. Note that this procedure affects only future operations - if a table load of more the 2 GB is to be performed, it would have to be split into two or more stages.
/* Future inserts will reside on data_seg2 */
sp_placeobject 'data_seg2','invoice'
go

## Object Permissions

Object security is fairly straightforward. Here are some examples:
grant all on invoice to jsmith
go
grant select on invoice to wriker
go
grant update on invoice to wriker
go
revoke select on invoice from wriker
go

Stored procedure security allows you to grant access on a business logic basis. For example, if you had a stored proc that updated the invoice table and selected data from the customer table, you could grant the execute priviledge on the stored proc, and you're done. The user would be able to run the procedure to update/select from the tables, but could not get at the tables directly.
grant execute on proc_upd_invoice to jsmith
go

## Binding Rules to Colunms

Default values for colunms can be specified at the time a table is created, or afterwards via the modify command.

/* Employee will have a default salary of 10000, and a hire date of today */

create table employee (
  emp_id   integer  not null,
  salary   money    default 0,
  hire_dt  datetime default getdate()
)
go

/* alter the table, so salary starts at 49000 */

# ALTER TABLE employee REPLACE salary DEFAULT 49000
go


/* create a new default;  bind the column to your custom default */


create default def_highsal as 55000
go 
sp_bindefault def_highsal,'employee.salary'
go 


-- creating your own custom defaults has a significant advantage:
--  you can actually choose the name of the default.


## Modifying a Colunm

With Sybase 12.1.X and higher, a column type can be altered. You need to be dbo and have select into turned on, in the database defaults.

create table employee (
  emp_id   integer  not null,
  salary   money    default 0,
  hire_dt  datetime default getdate(),
  last_name varchar(5)  null
)
go


/* make the name column longer */

alter table employee modify last_name varchar(80) not null
go


/* rename the column (works with Sybase 11 and 12) */

sp_rename 'employee.last_name',last_nm
go



## Moving an object to another segment

When databases contain more segments than the usual default, it is often necessary to move tables between segments.

/* move a table, in its entirety, to the new segment */

drop index 'employee.idx_employee'
go
create clustered index on employee (emp_id) on new_seg
go


/* leave table where it is, but future allocations go to the new segment */

sp_placeobject new_seg , 'employee'
go


/* leave table where it is, but future allocations for the 
   text column (employee_notes) go to the new segment */

sp_placeobject new_seg , 'employee.temployee_notes'
go





## Transact SQL: numeric functions

 Mathematic Functions

abs            absolute value             abs(-5) = 5
ceiling        next highest int           ceiling(5.3) = 6
floor          next lowest int            floor(5.7) = 5
power          exponential                power(2,8)=256
rand           random number              rand=0.315378 for example
round          round to n places          round(5.6,0)=6   round(5.66,1)=5.7
sign           -1,0,1                     sign(-5)=-1

### Trigonometric and Log Functions

acos
asin
atan
atn2
cqos
cot
degrees
pi
radians
sin
exp            exponential e
log            log function
log10          log function base 10

## Transact SQL: string functions

 plus sign (+)      concatenation             'one'+'two'='onetwo'
ascii              char->ascii value         ascii('A')=65
char               ascii->char               char(65)='A'
charindex          similar to instring       charindex('two','onetwothree')=4
char_length        length of string          charlength('onetwo')=6
lower              lower case                lower('ONE')='one'
ltrim              trim left blanks          ltrim('   one')='one'
replicate          repeat chars              replicate('*',8)='********'
reverse            flip string               reverse('salad')='dalas'
right              right chunk of string     right('Chicago',2)='go'
rtrim              trim right blanks         rtrim('test   ')='test'
space              spaces                    space(5)='     '
str                float->char               str(5.6,12,2)='        5.60'
stuff              insert chars within str   stuff('onetwothree',4,3,'*****')='one*****three'
substring          get piece of string       substring('sybase',1,2)='sy'
upper              upper case                upper('one')='ONE'
 
## Transact SQL: date/time functions

datepart*        get part of a date         datepart(MM,'10/21/98')=10
dateadd*         manipulate a date          dateadd(DD,10,'10/21/98')= 10/31/98
getdate          todays date and time       getdate()=Nov 16 1998-2000  7:27PM

* date parts are MM,DD,YY,HH,MI,SS,MS

## Transact SQL: date/time formats

# Use the convert function to format the date into the style of your choice.

# Examples:
 select convert(char(20),getdate(),101)

 select emp_id,convert(char(20),hire_dt,101)
 from employee

 Sample Date            Format
_________________________________
 04/05/2000                   101
 2000.04.05                   102
 05/04/2000                   103
 05.04.2000                   104
 05-04-2000                   105
 05 Apr 2000                  106
 Apr 05, 2000                 107
 11:33:24                     108
 Apr  5 2000 11:33:24         109
 04-05-2000                   110
 2000/04/05                   111
 20000405                     112

## Transact SQL: misc functions

convert          convert between data types      convert(float,'5.50')=5.50
suser_name()     current login id
getdate()        current date

## Transact SQL: Conditionals

Conditional statements allow branching within stored procedures in a fashion similar to other languages, like Visual Basic. The example below returns the matching invoice if a non-zero value is passed to it, otherwise it raises an error.
create procedure proc_rtv_invoice (@inv_id numeric(8,0) as

if @inv_id > 0
   select inv_id, inv_date, sales_rep_id
   from invoice
   where inv_id = @inv_id
else
   raiserror 99999 'Error: invalid invoice #'

return
go

Another example, which illustrates the begin and end constructs
create procedure proc_rtv_invoice (@inv_id numeric(8,0)) as

declare @date   datetime

if @inv_id > 0
   begin
   select @date = getdate()

   select inv_id, inv_date, sales_rep_id,@date
   from invoice
   where inv_id = @inv_id
   end
else
   raiserror 99999 'Error: invalid invoice #'

return
go

Note how the variable @date was declared, and given a value.

## Transact SQL: looping constructs

The while ().. begin..end is the best way to preform loops within a stored procedure. Note that declared variables in T-SQL need to be initialized.
create proc proc_looper (@loops int) as

declare @count   integer,
        @power2  float

select @count = 0, @power2 = 1

while (@count < @loops)
begin
  select @power2 = @power2 * 2

  select @count = @count + 1
end

select 'Result is: ', @power2

return
go


## Transact SQL: Cursors

Database cursors allow row by row processing to occur within a stored procedure.
create procedure proc_upd_commiss as

declare @inv_id       integer,
        @sales_rep_id integer

declare cursor1 cursor for
   select inv_id,sales_rep_id
   from invoice

open cursor1

fetch cursor1 into @inv_id,@sales_rep_id

while (@@sqlstatus=0)
   begin

   update employee
   set commiss_tot = commiss_tot + 15
   where emp_id = @sales_rep_id

   fetch cursor1 into @inv_id,@sales_rep_id
   end

close cursor1

return
go

## Transact SQL: Complex Updates

This example illustrates how to perform an update while joining to another table.
 update employee
 set t1.dept = t2.dept
 from employee t1, old_employee t2
 where t1.emp_id = t2.emp_id

## Transact SQL: Finding duplicate rows in a table

This example finds cargo records with have duplicate destination ids.
3> select cargo_id, dest_id
4> from routing t1
5> where
6>     ( select count(*)
7>       from routing t2
8>       where t2.dest_id = t1.dest_id ) > 1
9>
10> go

## Using Temporary Tables

Temp tables allow developers to create and scan tables within a stored procedure - and have the tables totally isolated from all other database connections. This is very valuable when results need to be processed several times within a loop, or when a complex result set is expected (like a crosstab). Note that temp table transactions are logged within tempdb (exception: select into create statements).

create proc proc_gen_report (@region_id   integer) as

declare @total   money


/* standard create */

create table #rpt (
store_id    integer   not null,
store_cd    char(5)   not null,
inv_count   integer   not null,
total_sales money     not null
)


/* create using select into - make sure 'select into' is turned on */

select t1.cus_id, t1.cus_name, sum(t2.inv_amount) 'inv_summary'
into #cus_invoices
from customer t1, invoice t2
where t2.cus_id = t1.cus_id


/* Processing occurs, using temp table(s) where needed. */
/* Temp tables can be used in joins, aggregates, updates, etc. */


drop table #rpt
drop table #cus_invoices

return
go



## Inner/Outer Joins


This will display sales rep's names, and their territory.
It will also display names that do not have a territory.

select t1.srep_name, t2.terr_name from salesrep t1, territory t2 where t1.srep_id *= t2.srep_id
go

select t1.srep_name, t2.terr_name from salesrep t1, territory t2 where t1.srep_id =* t2.srep_id
go

select t1.name, t2.territory_name from salesrep t1, territory t2 where t1.srep_id = t2.srep_id
select t1.srep_name, t2.terr_name from salesrep t1, territory t2 where t1.srep_id = t2.srep_id


## Isolation Levels

Setting the isolation levels can eliminate contention problems, when reports are run on the same database as the online application.

Three flavors to choose from, for troublesome reports, queries, and updates.

1)
select cus_id
from customer_location
where cus_id< 1000000
at isolation  read uncommitted

-- > Allows table to be read (ala Oracle) even when update page locks are pending.


2)
select cus_id from
customer_location noholdlock
where cus_id< 1000000

-- > Allows big queries to run without locking pages / tables.


3)
/* For updates: */

set transaction isolation level 0

begin transation

update invoice_item
set discount_amt = 0
where invoice_id < 2000000

commit transaction


Queries against invoice_item will NOT be blocked.
Updates against invoice_item pages included in the transaction WILL be blocked.



*** Mixing  1 & 2 from above is not recommended



## Reporting: SQL Performance and Tuning

This is a list of some techniques used successfully at several different sites.

Getting Maximum Index Usage

1) Verify tables have had "update statistics" on them ;
   Verify tables have had "sp_recompile" on them.

2) Verify any declared variables have the same data
   type as their corresponding columns - this is a common
   pitfall.

3) Force index usage as follows, with a hint:
        from customer (index idx_customer2)

4) Use SET TABLE COUNT
   Example:   set table count 6
   Then, compile the procedure, in the same session.

5) If temp tables are being used, put the temp table
   creation statements in one procedure, and the
   processing SQL in another procedure.  This allows
   the optimizer to form a query plan on the already
   established tables.
   Example:
     proc_driver  calls    proc_create_temp_tables
   then, 
     proc_driver  calls    proc_generate_report




## General SQL Programming

- Plan for growth.  Assume the driver table doubled or tripled in size; would
  the report still function ?

- Avoid dumb comparisons in the where clause, like 
       where @emp_id > 0

- use "WHERE EXISTS ( )" rather than "WHERE NOT EXISTS"

- use "!=" rather than "<>"

- use "IS NOT NULL" rather than "<>NULL"

- use "IS NULL" rather than "=NULL"

- avoid distinct if possible ; see cursor loop option below

- use meaningful names for temp tables ... don't use #temp (lame)


# Report Structure Approaches   

1) Single query

Single query reports are rare - usually they involve getting a simple list together.  

- Don't try to 'shoehorn' SQL into one statement.  Shorter programs are 
  great for C or Perl applications, but this is not the case in SQL.
  Think "Bigger is Better" (and more maintainable).

- Keep queries from using more than four tables if possible.



2) Cursor on driver table(s), with IF..THEN processing in loop


Using a cursor for complex reports almost always increases performance
when large tables and a lot of joins are involved.

- Keep cursor queries from using more than two tables if possible,
  make sure this query performs well on its own.  

- Try to have a unique key of some sort available within the tables involved.
  Strange results have been known to occur when a cursor is scanning
  rows that are exactly alike.

- Don't use cursors for updating.

- Use IF statements for filtering results even further.  In most cases:

  A code construct like the one below is better than cramming the
  logic in a where clause.


       IF 
           BEGIN

           IF  and 
               .....
           ELSE
               ....           

           END


3) Set processing without cursors

   This technique should be attempted when even a cursor construct fails to 
   achieve the desired performance.

   Basically, the driver query is re-run with each iteration of the loop.

   Sample, with cursor:

        declare cursor1 cursor for
        select emp_id, last_name, salary
        from employee

        open cursor1

        fetch cursor1 into @emp_id, @last_name, @salary

        while (@@sqlstatus = 0)
          begin

          < processing >

          fetch cursor1 into @emp_id, @last_name, @salary
          end

        close cursor1   


   Sample, with set processing:


        select @emp_id = 0, @loop = 1

        while (@loop > 0)
            begin

            set rowcount 1

            select     
            @emp_id      = emp_id, 
            @last_name   = last_name, 
            @salary      = salary
            from employee
            where emp_id > @emp_id
            order  by 1

            select @loop = @@rowcount

            set rowcount 0

            if @loop > 0
               begin

               < processing >

               end


            end


# Transaction Log Filling Up ?

If the transaction log is filling up, for tempdb or the main database, there
is likely something wrong with the report logic.

Things to check:

- Instead of repetitively updating each row, can the values be obtained
  ahead of time, and then inserted with a single transaction ?

- Are the "joined" updates occuring on each row once ?  When updating
  using a join statement, make sure that the tables in question 
  are joined in a way that avoids duplicate rows.  Try running the
  SQL statement as a SELECT - check it out.

- Are you cramming 500,000 rows from a temp table into a db table ?
  Try elminating the temp table.

- Create indexes on updated/inserted tables after the fact.

- Use "set rowcount" along with "waitfor delay" if log problems persist


*** A proper DBA will never extend the log segment, based on the needs of a 
    single process.








## Case Statement

Sample for case statement usage appears below.


SELECT emp_name,
        (CASE WHEN salary = 0 
              THEN "not hired" 
              ELSE "has salary" END) AS salary_note,
       hire_dt
  FROM emp_table 



## Custom query plans

rare occasions, it is necessary to create and use a custom query plan.
/* run the delete, force a table scan */
delete from perm_employee_notes  plan "(t_scan perm_employee_notes)"
go

