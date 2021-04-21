## SQLITE

$ sqlite3 db1
create table names (id varchar(10) primary key, first_name text, last_name text);
insert into names values('2','john','doe');
insert into names values('3','jenny','doe');
Exit sqlite.

$ sqlite3 db2
create table salaries (id varchar(10) primary key, salary integer);
insert into salaries values('1',10000);
insert into salaries values('2',13000);
insert into salaries values('3',23000);
Exit sqlite.