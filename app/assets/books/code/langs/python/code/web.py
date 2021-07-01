# https://scrimba.com/p/pRB9Hw/cd9kPfE

# Python 2.x:
import urllib2
urllib2.urlopen("http://example.com/foo/bar").read()

# Python 3.x:
import urllib.request
fileobject = urllib.request.urlopen("http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt")
fileobject

import json
import urllib
url_mag="https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json"
url_plasma="https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"
mag=urllib.request.urlopen(url_mag)
mag_json=json.loads(mag.read())
plasma=urllib.request.urlopen(url_plasma)
plasma_json=json.loads(plasma.read())



#Used to make requests
import urllib.request
x = urllib.request.urlopen('https://www.google.com/')
print(x.read())

# used to parse values into the url
import urllib.parse
url = 'https://www.google.com/search'
values = {'q' : 'python programming tutorials'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)



try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    #print(x.read())

    saveFile = open('noheaders.txt','w')
    saveFile.write(str(x.read()))
    saveFile.close()
except Exception as e:
    print(str(e))
    
    
    
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
    
    
    
    
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://www.thenewboston.com/images/homepage_images/main_homepage_01.png")



from urllib import request
oog_url = http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=8&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)


1. use urllib2
http://docs.python.org/2/library/urllib2.html

import urllib2
f =  urllib2.urlopen(url)
print f.read()

import urllib2
content = urllib2.urlopen(some_url).read()
print content

1. use httplib

import httplib
conn = httplib.HTTPConnection("www.python.org")
conn.request("HEAD","/index.html")
res = conn.getresponse()
print res.status, res.reason
# Result:
200 OK

3. 'requests' library

import requests
r = requests.get("http://linuxfr.org/")
print(r.text)

r = requests.put("http://linuxfr.org/")
r = requests.delete("http://linuxfr.org/")
r = requests.patch("http://linuxfr.org/")
r = requests.post("http://linuxfr.org/")
r = requests.head("http://linuxfr.org/")
r = requests.options("http://linuxfr.org/")
    
proxy = {"http":"http://username:password@proxy:port"}
r = requests.get("http://linuxfr.org/", proxies = proxy)


r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code # 200

import requests
r = requests.get("http://example.com/foo/bar")
# Read response:
r.text          #Retourne le contenu en unicode
r.content       #Retourne le contenu en bytes
r.json          #Retourne le contenu sous forme json
r.headers       #Retourne le headers sous forme de dictionnaire 
r.status_code   #Retourne le status code

#Send Data:
data = {"first_name":"Richard", "second_name":"Stallman"}
r = requests.post("http://linuxfr.org", data = data)

#Send image:
file = {'file': open("photo.png", "rb")}
r = requests.post("http://linuxfr.org", files = file)


https://www.dataquest.io/blog/python-api-tutorial/        
# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# Bytes version
print(response.content)
response is a string (although it was shown as a bytes object, we can easily convert the content to a string using response.content.decode("utf-8")).
Strings are the way that we pass information back and forth to APIs, but it's hard to get the information we want out of them. 

# JSON version
Python has great JSON support, with the json package. The json package is part of the standard library, so we don't have to install anything to use it. We can both convert lists and dictionaries to JSON, and convert strings to lists and dictionaries.

# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)



#%%
# python.exe xxxx.py

# Networking and Connectivity
# https://pythonprogramming.net/python-sockets/?completed=/ftp-transfers-python-ftplib/

import socket 			#  socket class that provides a way of accessing the network at a low level, it has to support many networking protocols.
host = '192.168.1.5'
port = 5050
m_sock = socket.create_connection((host, port)) # establish a connection to a host on IP 192.168.1.5 on port 5050

# Once a socket has been opened, you can send and receive data.
m_sock.sendall(b 'Hello World')
			   \___ b character before the string because data needs to be a byte string

# Bigger message you should iterate over your message like this:
msg = b'Longer Message Goes Here'
mesglen = len(msg)
total = 0
while total < msglen:
	sent = m_sock.send(msg[total:])
	total = total + sent

# For receiving data, you need to tell the methods how many bytes to read in at a time.
data_in = m_sock.recv(2000)
#This works because you know for sure that the message being sent is less than 2000 bytes long.
# If the message is big, you must loop over and over until you collect all of the separate chunks.
buffer = bytearray(b' ' * 2000)
m_sock.recv_into(buffer)
#Here we define an empty buffer, then we start to write the message into the buffer.



# Reading an E-Mail from POP mail server

import getpass,poplib 					# poplib module enables you to communicate with a POP server
										# If you need a secure connection, use the POP3_SSL class instead.
										# getpass module asks the end user for passwords securely
pop_serv = poplib.POP3('192.168.1.5')
pop_serv.user("myuser")
pop_serv.pass_(getpass.getpass()) 		

# To get the message list and the message count, you can do it like this:
msg_list = pop_serv.list()              # to list the messages
msg_count = pop_serv.msg_count()        # to get message count

# Don’t forget to close any open connections after you finish working with the POP server.
pop_serv.quit()


# Reading an E-Mail from IMAP mail server

import imaplib, getpass 						# work with an IMAP email server using the imaplib module.
												# If you are using SSL on your IMAP server, you should use the IMAP4_SSL class instead.
my_imap = imaplib.IMAP4('imap.server.com')
my_imap.login("myuser", getpass.getpass())

# To get a list of e-mails, you need to actually do a search like this:
data = my_imap.search(None, 'ALL')
# Then you can iterate over the returned e-mail indices in the data variable and fetch the message
msg = my_imap.fetch(email_id, '(RFC822)')
my_imap.close()
my_imap.logout()


# Sending an E-Mail
# E-mails are sent using the SMTP protocol. The smtplib in Python is used to handle this.
# If you are using SSL on your SMTP server, you should use the SMTP_SSL class instead.
import smtplib, getpass
my_smtp = smtplib.SMTP(smtp.server.com')
my_smtp.login("myuser", getpass.getpass())

# Once the connection is opened, you can send the message like this:
from_addr = 'me@example.com'
to_addr = 'you@example.com'
msg = 'From: me@example.com\r\nTo: you@example.com\r\n\r\nHello, this is a test message'
my_smtp.sendmail(from_addr, to_addr, msg)


# Web Crawling

import urllib.request 		#To talk to a web server, you need to use urllib.request submodule
my_web = urllib.request.urlopen('https://www.google.com')
print(my_web.read())

# Post to a Web Page
# If you need to submit a web form, you know that you should send POST request to the web page and that’s what we will do.

import urllib.request
my_data = b'Your Data Goes Here'
my_req = urllib.request.Request('http://localhost', data=my_data,method='POST')
my_frm = urllib.request.urlopen(my_req)
print(my_frm.status)

# Note that we can use mechanize or urllib2, there are many ways to achieve that.

