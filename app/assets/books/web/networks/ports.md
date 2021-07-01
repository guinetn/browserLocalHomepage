## Ports

Port = address = address of AN application on a machine
Port = 2^16 = 65536 values

MySQL 127.0.0.1 + port 3306
To view ports: 
>netstat


|Port range|Group|
|---|---|
|0 - 1 023| System / Well known ports|
||Above 1024, randomly attributed by the OS:|
|1 024 - 49 151| User ports / Registered ports (iana)|
|49 152 - 65 535| Private/ Dynamic  ports|

Open ports are how services on a computer communicate with another server over a network

### Port Forwarding - Port mapping

Let Internet have an access to machines on private networks using public ip + port

rediriger un port du routeur vers un port donné sur une machine locale.
Ex: tout paquet arrivant sur le port 80 du routeur devra être redirigé vers la machine d'adresse 192.168.0.1 sur le port 80 = être joignable depuis l'extérieur (internet)

Mapping router’s public address <----> private IP address for a device on that private network

Alows computers or services in private networks to connect over the internet with other public or private computers or services.
When? a machine on the Internet needs to initiate a connection to a machine that's behind a firewall or NAT router. ... Put another way: you need port forwarding if you want to run a server behind the NAT firewall/router, you don't need it if you're just running a client.
- https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip/856345-la-nat-et-le-port-forwarding
- https://learn.g2.com/port-forwarding

- SSH port forwarding: https://opensource.com/sites/default/files/gated-content/6_surprising_ways_to_use_jupyter_0.pdf
simple SSH command with port forwarding to forward a local port to a remote local connection. When you run an SSH port-forwarding command like
-L 8111:127.0.0.1:8888, you are telling SSH to forward your
local port 8111 to what the remote host thinks 127.0.0.1:8888
is. The remote host thinks 127.0.0.1 is itself

- https://www.youtube.com/watch?v=ZFp-FKPpUQc&t=162s

![](https://learn.g2.com/hs-fs/hubfs/request-reply-path.png?width=666&name=request-reply-path.png)

<br/>
Common Ports to Remember
- 53: DNS
- 80: HTTP (web)
- 443: HTTPS (web)
- 110: POP (mail)
- 143: IMAP
- 20/21: FTP
- 25: SMTP (mail)
- 22: SSH (remote shell connections)
- 8080: Proxy

- 20: FTP
- 21: FTP
- 22: SSH
- 23: Telnet
- 25: SMTP
- 26: Common Alternate SMTP port
- 37: cPanel’s time servers (tcp out)
- 53: DNS/Named
- 80: HTTP
- 110: POP3
- 123: NTP
- 143: IMAP
- 443: HTTPS (SSL)
- 465: SMTPs (Secure SMTP)
- 993: IMAPs (Secure IMAP)
- 995: POP3s (Secure POP3)
- 1167: Guardian (buagent)
- 1433: Microsoft SQL Server
- 2073: cPanel Razor
- 2077: cPanel WebDAV
- 2078: cPanel WebDAV Secure port
- 2079: cPanel CalDAV and CardDAV
- 2080: cPanel CalDAV and CardDAV Secure port
- 2082: cPanel non-secure port
- 2083: cPanel secure port
- 2086: WHM non-secure port
- 2087: WHM secure port
- 2089: cp license
- 2095: cPanel webmail non-secure port
- 2096: cPanel webmail secure port
- 2443: Nodeworx/SiteWorx
- 3306: MySQL
- 3389: Remote Desktop Protocol (rdp)
- 4643: Virtuozzo Control Panel
- 6660-6669: IRC
- 8000: SHOUTcast
- 8080: Tomcat
- 8306: Plesk MySQL
- 8443: Plesk
- 49152:65534: Standard Passive FTP ports

http://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-ports.html

download.iframe(https://packetlife.net/media/library/23/common_ports.pdf,800,300)

## Finding Local Open Ports

### Nmap

Nmap (Network Mapper) is an open-source network scanner used to discover services and hosts on a network. It sends packets of information to devices attached to the network and analyzes the responses. Nmap has many features for probing networks, including host discovery, service detection, and OS sensing. To install Nmap, we use the following commands.

yum update -y
yum install nmap -y
nmap --version 
nmap localhost

### lsof
linux command meaning list open files and is used in many Unix-like systems to report a list of all open files and the processes that opened them.
yum update -y
yum install lsof
lsof -v 
lsof -i -P | grep -i "listen"     Check open ports 
lsof -i | awk '{print $8}' | sort | uniq -c | grep 'TCP\|UDP'    lists the total number of TCP/UDP connections
lsof -a -i4 -itcp   see all IPv4 ports using TCP connections
lsof -i :80         lists the process tied to an open port

### netstat

displays TCP network connections, routing tables, active network interfaces, and other network protocol statistics. To install netstat, run these commands.

yum update -y
yum net-tools -y
netstat --version
netstat --listen
netstat -tulpn | grep LISTEN
netstat -plnt | awk '{print $1, $3, $7}'

### ss
netstat replacement
return and display various network-related information.
ss -s    summary of network statistics
ss -lu   UDP connections that are listening. 
ss -lt   TCP connections
ss -4 state listening | awk '{print $1, $4}'
ss -tulwn | awk '{print $1, $5}'
ss -stplu | awk '{print $1, $2, $5}'

### Bash

HOST=127.0.0.1;for((port=1;port<=65535;++port)); do echo -en "$port ";if echo -en "open $HOST $port\nlogout\quit" | telnet 2>/dev/null | grep 'Connected to' > /dev/null; then echo -en "\n\nport $port/tcp is open\n\n";fi;done | grep open

## Finding Remote Open Ports

### nc or netcat
Uses TCP to read and write data across network connections

details about open ports on an external server
nc -vz [host] [port ranges] 2>&1 | grep succeeded
netcat -zv [host] [port ranges] 2>&1 | grep succeeded
telnet
Telnet is an application protocol and command to provide text-based communication using a virtual terminal (VT) connection. 
yum install telnet telnet-server -y
telnet 192.168.0.1 22
Because Linux treats everything like a file, we can use this to locate a port’s status and availability. 

echo > /dev/tcp/[host]/[port] && echo "The port is open!"
echo > /dev/udp/[host]/[port] && echo "The port is open!"

cat /etc/services | grep port#

### Bash
</dev/tcp/127.0.0.1/80) &>/dev/null && echo "OPEN" || echo "CLOSED"

for i in {1..65535}; do (echo < /dev/tcp/127.0.0.1/$i) &>/dev/null && printf "\n[+] Open Port at\n: \t%d\n" "$i" || printf "."; done

ip=192.168.1.254;for i in {1..65535}; do (echo < /dev/tcp/$ip/$i) &>/dev/null && printf "\n[+] Open TCP Port at: \t%d\n" "$i"; done

declare -a array=($(tail -n +2 /proc/net/tcp | cut -d":" -f"3"|cut -d" " -f"1")) && for port in ${array[@]}; do echo $((0x$port)); done

for p in {1..1023}; do(echo >/dev/tcp/localhost/$p) >/dev/null 2>&1 && echo "$p open"; done
We can also use a Python socket module or one of the curl, telnet, or wget commands.

### etc/services
/etc/services file is utilized by server software to render service names to associated port numbers. Typically, the file includes the service name, the port and protocol used, aliases, and any related comments.

cat /etc/services | grep tcp
cat /etc/services | grep udp

###  Locate the Port a Service is Running On
To identify the PID (or process ID number), we first use the ps command.
ps aux | grep <PROCESS NAME>
ps aux | grep ssh
Once we have the PID, run the following netstat command.
netstat -plnt | grep <PID>
netstat -plnt | grep 101650
This will give us the port(s) that the process is listening on. In this case, we can see that the ssh PID (101650) is listening on port 22.

### Which Process is Listening on a Port?
lsof -i -P -n | grep LISTEN | grep ftp
netstat -tulpn |grep ftp
ss -tulpn | grep ftp