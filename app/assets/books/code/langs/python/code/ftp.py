import ftplib #Open ftp connection

ftp = ftplib.FTP('ftp.seismo.nrcan.gc.ca', 'anonymous', 'user') # List the files in the current directory
print("File List:")
files = ftp.dir()

import datetime
now=datetime.datetime.now()
ftp.cwd("intermagnet/minute/provisional/IAGA2002/" + str(now.year) + "/" + str(now.strftime("%m")))
files = ftp.dir()

file_list = ftp.nlst()import pandas as pd
import numpy as npdf = pd.DataFrame(columns = ["Date_time", "Bx", "By", "Bz", "Bf"])import sqlite3

for file in file_list:
    station = ''
    lat = 0
    long = 0
    
    date_today = str(now.year) + str(now.strftime("%m")) + str(now.strftime("%d"))
    
    if(date_today in file):
        ftp.retrbinary("RETR " + file, open(file, 'wb').write)
        temp=open(file, 'rb')
        
        data_rows = 0        for line in temp:    
            if(data_rows == 1):
                row_bytes = line.split()
                date_time = row_bytes[0].decode("utf-8") + " " + row_bytes[1].decode("utf-8")[:8]
                row_txt = [date_time, row_bytes[3].decode("utf-8"), row_bytes[4].decode("utf-8"), row_bytes[5].decode("utf-8"), row_bytes[6].decode("utf-8")]
                
                a_series = pd.Series(row_txt, index = df.columns)
    
                query = 'INSERT INTO geo_mag (station, lat, long, date_time, bx, by, bz, bf) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (station, lat, long, a_series["Date_time"], a_series["Bx"], a_series["By"], a_series["Bz"], a_series["Bf"])                cur.execute(query)else:
                if('IAGA Code' in line.decode("utf-8") or 'IAGA CODE' in line.decode("utf-8")):
                    station = line.decode('utf-8').split()[2]
                    print(station)
                elif('Latitude' in line.decode("utf-8")):
                    lat = line.decode('utf-8').split()[2]
                elif('Longitude' in line.decode("utf-8")):
                    long = line.decode('utf-8').split()[2]
                elif('DATE       TIME' in line.decode("utf-8")):
                    data_rows = 1        conn.commit()