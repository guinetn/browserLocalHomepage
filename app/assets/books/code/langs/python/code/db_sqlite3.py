
# https://www.analyticsvidhya.com/blog/2020/10/space-weather-dashboard-build-your-own-custom-dashboard-to-analyze-and-predict-space-weather

import sqlite3
conn = sqlite3.connect("space.db", isolation_level=None)
cur = conn.cursor()cur.execute('''
    CREATE TABLE sunspots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    sunspot_count INTEGER,
    sunspot_sd REAL,
    sunspot_obs_no INTEGER
    );
    ''')

import urllib.requestfileobject = urllib.request.urlopen("http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt")

for line in fileobject:
    row_bytes = line.split()

    date = row_bytes[0].decode("utf-8") + "-" + row_bytes[1].decode("utf-8") + "-" + row_bytes[2].decode("utf-8")    
    row_txt = [date, row_bytes[4].decode("utf-8"), row_bytes[5].decode("utf-8"), row_bytes[6].decode("utf-8")]    
    a_series = pd.Series(row_txt, index = df.columns)
   
    query = 'INSERT INTO sunspots (date, sunspot_count, sunspot_sd, sunspot_obs_no) VALUES ("%s", "%s", "%s", "%s")' % (a_series["Date"], a_series["Sunspot_count"], a_series["Sunspot_sd"], a_series["Observ_No"])    
    cur.execute(query)

conn.commit()

exit

#https://www.tutorialsteacher.com/python/database-crud-operation-in-python

https://www.sqlite.org/download.html
sqlite> create table student(name text, age int, marks real);
sqlite> insert into student values('Ramesh', 21, 55.50);
sqlite> select * from student;
Ramesh|21|55.5

.connect() 	returns a connection object referring to the existing database or a new database if it doesn't exist
	cursor() 	Returns a Cursor object which uses this Connection.
		execute()	Executes the SQL query in a string parameter
		executemany()	Executes the SQL query using a set of parameters in the list of tuples
		fetchone()	Fetches the next row from the query result set.
		fetchall()	Fetches all remaining rows from the query result set.
		callproc()	Calls a stored procedure.
		close()	Closes the cursor object.
	commit()	Explicitly commits any pending transactions to the databse. 
			The method should be a no-op if the underlying db does not support transactions.
	rollback()	This optional method causes a transaction to be rolled back to the starting point. 
			It may not be implemented everywhere.
	close()		Closes the connection to the database permanently. 
			Attempts to use the connection after calling this method will raise a DB-API Error.

try:
    cur=db.cursor()
    cur.execute("Query")
    db.commit()
    print ("success message")
except:
    print ("error")
    db.rollback()
db.close()
