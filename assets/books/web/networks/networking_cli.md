## NETWORKING WITH CLI
// check the DNS solution
$ nslookup www.dgate.org
// get the laptop's host name
$ hostname

// connect via telnet and then send a request
$ telnet www.dgate.org 80
GET / HTTP/1.1
Host: www.dgate.org
$telnet www.openpayments.us 80
GET / HTTP/1.1
Host: www.openpayments.us
$ telnet stackoverflow.com 80
GET / HTTP/1.1
Host: stackoverflow.com     → 300 Moved Permanently, switch to https:
$ telnet stackoverflow.com 80
GET / HTTPS/1.1
Host: stackoverflow.com


// Create a socket that can be used to communicate the different processes
$ nc -l 11223       this    Set a process that listens to port 11213
$ nc localhost 11211    Then we open another terminal and write


// get and save an webpage
$ curl https://www.cnn.com > cnn.html  

$ wget -O cnn.html https://www.cnn.com  // note that wget not support socket5
// recursively wget a server
$ wget -r -np -R "index.html*" {{URL}}  

// find IP address assigned by NAT (internal IP)
$ ipconfig getifaddr en0
// find external IP address
$ curl ifconfig.me


// SSH connection (especially for AWS)
$ ssh -i foo.pem ubuntu@xyz.com
// SSH copy (especially for AWS)
$ scp /path/to/file username@a:/path/to/destination


// Open SSL
$openssl s_client -connect stackoverflow.com:443  

// Python
import requests
cnn = requests.get('http://www.cnn.com')
print(cnn.text)
