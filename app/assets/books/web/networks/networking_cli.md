## NETWORKING WITH CLI



## ipconfig.exe 
Details on the current TCP/IP network configuration and refresh DHCP and DNS settings
ip, dns, gateway, hostname
>ipconfig 
>ipconfig /all  
Adresse physique . . . . . . . . . . . : AC-2B-6E-68-6E-73    ← MAC address

## nslookup
DNS query to get ip address

>nslookup google.com
    Serveur :   ns1.numericable.net
    Address:  89.2.0.1

    Réponse ne faisant pas autorité :
    Nom :    nc-ass-vip.sdv.fr
    Address:  212.95.74.75
    Aliases:  google.com.numericable.fr

## ping
Test the reachability of a host
>ping google.com

## tracert - tracerout
Network diagnostic commands for displaying possible routes and measuring transit delays of packets
>tracert facebook.com

## netstat -  Network Statistics
Identifies all the active connections
>netstat
 Proto  Adresse locale         Adresse distante       État
  TCP    192.168.0.17:49884     par21s19-in-f10:https  CLOSE_WAIT
  TCP    192.168.0.17:49988     a23-57-5-23:https      ESTABLISHED
  TCP    192.168.0.17:49989     a23-57-5-23:https      ESTABLISHED
  TCP    192.168.0.17:49990     a23-57-5-23:https      ESTABLISHED
  TCP    192.168.0.17:49995     a23-40-113-188:http    ESTABLISHED
  TCP    192.168.0.17:49996     a23-40-113-188:http    ESTABLISHED


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

## netstat

>netstat
>netstat -antp

Windows
>netstat -r
>netsh interface ipv4 show route
>netsh interface ipv6 show route

Linux
>ip route
>netstat -r



## wireshark
Network sniffer 

>apt-get install wireshark
https://www.wireshark.org/


