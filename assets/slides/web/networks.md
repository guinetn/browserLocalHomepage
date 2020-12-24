# NETWORKS

## Concepts
|Computer Network Concepts||
|---|---|
|Socket | A socket is one endpoint of a two-way communication link between two programs running on the network. |
|Physical layer | The electrical physical plumbing of the Internet used for transmitting data. |
|Ethernet | Ethernet is a way of connecting computers and Other network devices in a physical space. (hardware interface) |
|IP | IP is an addressing and fragmentation protocol. (Iowest level abstraction above the hardware) |
|IP Address | The IP address is used to define the target and the source in the internet. |
|port | A port is a communication ending point. |
|localhost | The IP address of my local machine, which is 127.0.0.1. |
|NAT | Network Address Translation is used for the firewall to translate a outside IP to a special IP behind the wall. |
|DHCP | The Dynamic Host Configuration Protocol dynamically assigns an IP address to the network devices. |
|DNS | Domain Name Service is a distributed database that maps domain names to IP addresses. |
|TCP | Transmission Control Protocol is a protocol defines how to establish and maintain a network conversation. |
|HTTP | Hypertext Transfer Protocol (HT TP) is an application-layer protocol for transmitting hypermedia documents. |
|POP/SMTP | These are mailing protocols that are used for sending and receiving emails. |
|SSH | Secure Shell is a cryptographic network protocol for operating network services securely. |
|Cookies | An HT TP cookie is a small piece of data from a website stored on the user's computer by the browser. |
|API | An Application Programming Interface is a computing interface to extract data from a website. |

## Ports
|Port range|Group|
|---|---|
|0 - 1 023|Well known ports|
|1 024 - 49 151|Registered ports (iana)|
|49 152 - 65 535|Private and/or dynamic ports|

<br/>
Common Ports to Remember
- 80: HTTP (web)
- 443: HTTPS (web)
- 110: POP (mail)
- 25: SMTP (mail)
- 22: SSH (remote shell connections)

download.iframe(https://packetlife.net/media/library/23/common_ports.pdf,800,300)

## Computer Network cli
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