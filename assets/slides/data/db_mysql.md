# MySQL

Save index in memory to speed up search
Use only one storage engine or different storage engines for different tables 
in the same database.

### Index Types
primary: unique, one per table.
unique: unique, no two rows have the same combination of the values.
index: may not be unique, but improves lookup efficiency.
fulltext: for full text search, by creating an index for each word in that column.
Stored in B+trees

Spatial data types use R-trees;

### Auth
x509 for authentication, away from username + pw

### Install

>$ sudo apt-get install mysql-server
>$ mysql -u root -p

### Engines
 
mysql> SHOW ENGINES;
+---+---+---+---+---+---+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+---+---+---+---+---+---+
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| ARCHIVE            | YES     | Archive storage engine                                         | NO           | NO   | NO         |
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
+---+---+---+---+---+---+

## Log in to MySQL database server:
>mysql -u root -p
>Enter password: **********
> CREATE DATABASE classicmodels_backup;
> SHOW DATABASES;

## LOCAL DUMP
	>mysqldump -u root -p classicmodels > d:\db\classicmodels.sql
	Enter password: **********
	This log in to the MySQL server using the root user account with a password and exports the database objects and data of the classicmodels database to d:\db\classicmodels.sql. 
	operator (>) means exporting

	>mysql -u root -p classicmodels_backup < d:\db\classicmodels.sql
	Enter password: **********
	Note that the operator ( <) means importing.
	Import the d:\db\classicmodels.sql file into classicmodels_backup database.
	> SHOW TABLES FROM classicmodels_backup;


## COPY A MYSQL DATABASE FROM A SERVER TO ANOTHER
	.Export the database on the source server to a SQL dump file.
	.Copy the SQL dump file to the destination server
	.Import the SQL dump file to the destination server

								 _______include both CREATE DATABASE and USE statements in the SQL dump file
								/			
	>mysqldump -u root -p --databases classicmodels > d:\db\db.sql
	Enter password: ********** 			
	. These statements will create the classicmodels database in the destination server and make the new database as the default database for loading the data.
	>CREATE DATABASE `classicmodels`
	>USE `classicmodels`;

	>mysql -u root -p classicmodels < c:\tmp\db.sql
	import the db.sql file to the database server with the assumption that the db.sql file was copied to c:\tmp\ folder.


## DOING A BACKUP - DUMP DATABASE
		
DataBases > phpMyAdmin > Exporter

	Méthode d´exportation > Personnalisée
		Select Tables
		Format: SQL
		structure et données

	Click Exporter
	NB: add   USE `twitterDB`;  at the top of the file
	You can also add CREATE DATABASE  IF NOT EXISTS `twitterDB`

	CREATE DATABASE  IF NOT EXISTS `jmc`;
	USE `jmc`;

	Import into MySqlWorkbench
	Import from MySql HostExcellence

	Tip:
		MySqlWorkBench add a header to the dump file:
		CREATE DATABASE  IF NOT EXISTS `nguinet_wordpress`
		USE `nguinet_wordpress`;

## Method #1

		Admin screen -> Manage Import - Export > Data Export / Restore
		Import from self contained File
		choose file in G:\Setup\Install\Database_Backups\MySql_Backups
		Add 	USE `twitterDB`;
		CREATE DATABASE  IF NOT EXISTS `twitterDB` /*!40100 DEFAULT CHARACTER SET utf8 */;
		USE `twitterDB`;

	Method #2
		upload in workbench
		create db
		create user
		double-click to activate the db
		play the sql


## MySQL commands:

	Note that all text commands must be first on line and end with ';'
	?         (\?) Synonym for `help'.
	clear     (\c) Clear the current input statement.
	connect   (\r) Reconnect to the server. Optional arguments are db and host.
	delimiter (\d) Set statement delimiter.
	edit      (\e) Edit command with $EDITOR.
	ego       (\G) Send command to mysql server, display result vertically.
	exit      (\q) Exit mysql. Same as quit.
	go        (\g) Send command to mysql server.
	help      (\h) Display this help.
	nopager   (\n) Disable pager, print to stdout.
	notee     (\t) Don't write into outfile.
	pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
	print     (\p) Print current command.
	prompt    (\R) Change your mysql prompt.
	quit      (\q) Quit mysql.
	rehash    (\#) Rebuild completion hash.
	source    (\.) Execute an SQL script file. Takes a file name as an argument.
	status    (\s) Get status information from the server.
	system    (\!) Execute a system shell command.
	tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
	use       (\u) Use another database. Takes database name as argument.
	charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
	warnings  (\W) Show warnings after every statement.
	nowarning (\w) Don't show warnings after every statement.

### Reset lost password

# /etc/init.d/mysql stop


2) On va redémarrer MySQL en désactivant l'identification et l'écoute du réseau pour que personne ne puissent y accéder sans mot de passe pendant l'exécution de notre petite opération:
 mysqld --skip-grant-tables --skip-networking &

 [1] 11580
 root@pc-octetmalin:/home/cedric/# 110607 12:21:43 [Note] Plugin 'FEDERATED' is disabled.
 110607 12:21:43  InnoDB: Started; log sequence number 0 294267
 110607 12:21:43 [Note] mysqld: ready for connections.
 Version: '5.1.49-3'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  (Debian)


3) Maintenant on va ce connecter à la base de données système "mysql" de MySQL:
 mysql mysql -u root
 mysql>


4) Voici la commande pour mettre à jour le mot de passe du compte root:
Dans mon exemple le nouveau mot de passe sera "tototiti".
 mysql> UPDATE user SET password=PASSWORD('tototiti') WHERE user="root";


5) On valide les changements:
 mysql> FLUSH PRIVILEGES;


6) On peut maintenant redémarrer le serveur MySQL:
 /etc/init.d/mysql restart
## More
- http://www.mysqltutorial.org
- http://www.mysqltutorial.org/mysql-copy-database/
- https://devopsmyway.com/install-mysql-ubuntu/
- https://dev.to/rahulku48837211/set-up-mysql-with-sequelize-in-nodejs-3a59