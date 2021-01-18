# NETWORKS

download.chapter(web/networks/osi_model.md)
::::
download.chapter(web/networks/url.md)
::::

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

::::
download.chapter(web/networks/ports.md)

::::

## DNS - DOMAIN NAME SYSTEM 

Internet directory (phone book)

DNS translate domain names (nytimes.com, www.google.com) into an IP address (like 192.168.2.1) which is used by computers to communicate on a network such as the Internet.
This avoid to memorize IP addresses as 192.168.1.1 (IPv4) or 2400:cb00:2048:1::c629:d7a2 (IPv6)

Browser 'domain name' request
↓
Resolving the hostname:
* Local DNS cache  
    Look for the IP address associated with the domain name
    This cache stores this information that our computer has recently saved. 
* Query another server
    **Recursive DNS servers** 
        Have their local cache too
        It stores the record in its local cache (All DNS records have a TTL (time-to-live value), which shows when a record will expire)
        The Recursive DNS server has the information and returns the A record to your computer. Our computer then stores the record in its local cache. It reads the IP address from the DNS record and passed it to our browser. The web browser will connect to the web server associated with the A records IP and display the website.
        ↓
    **Root server**
        Libraries addresses
        ↓
    **TLD server**   
        ↓ 
* Query the Authoritative DNS Servers
    Query the 'A record' to locate the IP address

![dns-lookup-diagram](assets/chapters/web/assets/dns-lookup-diagram.webp)

## Reverse DNS (rDNS)
    
Resolving an IP address back to a domain name.
- To block spam
Email Servers commonly use rDNS to block incoming SPAM messages. Many mail servers are set to automatically reject messages from an IP address that does not have rDNS in place
- analytics/logging: IP addresses are not human-readable. Addresses are more readable.

Perform a rDNS lookup manually:   
>Linux: $dig -x 8.8.8.8
>8.8.8.8.in-addr.arpa. 21599 IN PTR google-public-dns-a.google.com.
>ip + server_name: 132.254.231.138.in-addr.arpa
## Hosts file

local plain text file
maps servers or hostnames to IP addresses
in use since the time of ARPANET. It was the original method to resolve hostnames to a specific IP address. The hosts file is usually the first process in the domain name resolution procedure (Firefox now uses DNS over HTTPS (or DOH) by default. That means instead of checking your local hosts file or even your DNS resolver)

The hosts file is used to map domain names to IP addresses, and can be used as an alternative to DNS. It also allows you to specify the IP address to which a website resolves on your computer, regardless of what may be published in the site’s DNS zone file.

you view and test a site on one server while the rest of the world continues to see the site on another. That makes it an essential tool when migrating your website. 

* It must be edited with administrative privileges (is a protected file)
* Computer’s hosts file location depends on your operating system

Windows     C:\Windows\System32\drivers\etc\hosts
            Flush your dns cache: ipconfig /flushdns

Linux       /etc/hosts
            Unbutu: service dns-clean restart
            NSCD (Name Service Caching Daemon) may need to use one of the following commands.
                service nscd restart 
                systemctl restart nscd.service
                nscd -I hosts

Mac         /private/etc/hosts
            dscacheutil -flushcache; sudo killall -HUP mDNSResponder

 IP   space or \t    domain(s)  to resolve to the specified IP address
 ↓         ↓         ↓
127.0.0.1           localhosts                              #loopback
127.0.1.1	        mycomputer.localdomain	mycomputer

255.255.255.255     broadcasthost
123.123.123.123     liquidweb.com www.liquidweb.com
#67.225.187.61      liquidweb.com #Liquid Web
72.30.35.10         liquidweb.com #this is the new liquidweb.com

\# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

DOH (DNS over HTTPS): some browser use dns and not hosts file by default (Firefox). Edit options to unable DoH

## DNS Servers

Authoritative DNS Server  

    Stores DNS records (A, CNAME, MX, TXT, etc.) for domain names. Only respond to queries for locally stored DNS zone files. Say a server in our network has stored an A record for example.com. That server is the authoritative server for the example.com domain name.

Recursive Name Server  
    
    Receives queries for informational purposes. 
    Don't store DNS records. When a query is received, it will search the cache memory for an address linked to the IP address. If the recursive name server has the information, then it will return a response to query sender. If it does not have the record, then the query will be sent to other recursive name servers. This continues until it reaches an authoritative DNS server that can supply the IP address.

DNS Zones
    
    Administrative space within the Domain Name System. A zone forms one part of the DNS namespace delegated to administrators or specific entities. Each zone contains the resource records for all of its domain names.

DNS Zone File
    
    A text file stored on a server. 
    It contains all the records for every domain within that zone. 
    It is mandatory for the zone file to have the TTL (Time to Live) listed before any other information. The TTL specifies how long a DNS record is in the server’s cache memory. The zone file can only list one record per line. It will display the Start of Authority (SOA) record listed first. The SOA record contains essential domain name information including the primary authoritative name server for the DNS Zone.

## DNS RECORD (A, CNAME, MX, TXT…)
	
- Stored in authoritative servers
- Information about a domain (associated IP address)

	A - ADDRESS RECORD
        Assigns an IP address to a domain or subdomain name
        web browser "www.google.com" → the DNS system will translate that domain name to the IP address of 172.217.12.46 using the A record information stored in a DNS Zone file.

	CNAME - CANONICAL NAME
        Forwards a domain name to a different domain name (alias)
		The CNAME record makes one domain name an alias of another. The aliased domain gets all the subdomains and DNS records of the original. To put this in simple terms, a CNAME redirects requests to another record.  A CNAME record will always be a fully qualified domain name.

	MX - MAIL EXCHANGE RECORD 
        To set email servers and their priority.
        Routes email messages to a specific mail server linked to a domain from a designated mail host on a different server. MX records use a priority system if there is more than one MX record used for a domain that is using more than one mail server. The lower the number is, the higher the priority
		The MX record state the location that mail directed at the domain will be sent. MX records should always be fully qualified domain names, never just an IP address.

	TTL - TIME TO LIVE
		The time to live value sets how long this information will be good for when a recursive DNS server queries for information on your domain name.  The value is typically set in seconds.

        A record has a default TTL value of 86400 seconds (24 hours). If we update the an A record, propagation will take 24  to 48 hours to disperse. It is better to change the TTL value to 300 seconds which is 5 minutes

	SOA - SATE OF AUTHORITY
		The state of authority record specifies the DNS server providing authoritative information about an Internet domain, the email of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.

	NS - NAMESERVER
        Store the authoritative nameserver
		The servers listed in the NS record are the authoritative nameservers for the domain.

    PTR record (Reverse DNS)
        opposite of an A record. It resolves an IP address to a domain name. The purpose of this record is mainly administrative. It verifies that an IP address links to a domain name. Not all DNS hosting providers offer this type of record.

	TXT - TEXT RECORD
		A TXT record allows an administrator to insert arbitrary text into a DNS record.  The most common implementation of TXT records are for adding SPF records to a domain.

    SRV - SERVICE RECORD
        Establish connections between services and hostnames
        For example, if an application is searching for a location of a service that it needs, it will look for an SRV record with that information.  When the app finds the correct SRV record, it will filter through the list of services to find the following information:
        Hostname
        Ports
        Priority and Weight
        IP Addresses

        _sip._tcp.example.com.   3600 IN SRV 10 50 5060 serviceone.example.com.
        _sip is the name of the service and _tcp is the transport protocol.

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

::::

### TCP - Transmission Control Protocol
A connection-based protocol that provides a reliable flow of data between two computers.
Example: HTTP, FTP, Telnet
Use socket

TCP job is merely to take a stream of messages produced by one HOST and reproduce the stream on a remote receiving HOST without change.
TCP breaks data into packets and distribute them. Those packets travel from router to router over the Internet. During this time the IP protocol is in charge of the addressing and forwarding of those packets. At the end, TCP reassembles the packets to their original state.


### UDP - User Datagram Protocol
A protocol that sends independent packets of data, called datagrams, from one computer to another with no guarantees about arrival. UDP is not connection-based like TCP.
Example: time request, ping
Use datagram

## ROUTER: IPV4 addressing

* Has a public IP address of 183.23.100.34 to which all incoming and outgoing traffic is associated.
* acts as a Dynamic Host Configuration Protocol (DHCP) server
Assigning private IP addresses to all the PCs, laptops, smartphones, and servers in the house. The devices will use those addresses whenever they talk to each other.
* Traffic requests directed at your devices from external networks will be scanned and filtered to help prevent unauthorized and potentially dangerous access.

```txt
    INTERNET ←---→ Public IP: 183.23.100.34     ROUTER  
                                            DHCP Server 
                                                |
                                        Private IP: 192.168.1.1 
                                                |
                                                ├─── 192.168.1.24  PC
                                                ├─── 192.168.1.4   WebServer
                                                └─── 192.168.1.12  Smartphone
                                            
                                            Local devices using NAT IP Addresses
```

Get my public IP: https://httpbin.org/ip
Get my private IP: 

### LAN - LOCAL AREA NETWORK

Local network or group of devices connected without usig Internet
Organize and protect network communications for devices running within a single home or office.

### VLAN 
Local virtual network
Split a network at osi layer level

### NAT - Network Address Translation

Translate network addresses from Private IP ---→ Public IP for connections to public Internet

Organize devices within a private LAN
Enables instances inside Private Subnet to get Internet access.
Instances behind NAT Gateway cannot send outgoing traffic but can receive incoming traffic.

IPv4 addresses are 32-bit: 192.168.1.10
4 billion unique addresses  1.0.0.0 - 255.255.255.255

IPv6 addresses are 128-bit: 2002:0df6:0001:004b:0100:6c2e:0370:7234
Hexadecimal
Forever we won't running out of addresses 
That means from the perspective of address allocation, there's no longer any need for private NAT networks. But, for security, you can give your devices some protection within your LAN.

**NAT gateway** 
gateway translating network address to allow private subnet instances to connect to Internet while blocking inbound connections from Internet.

**Internet gateway**
Allow communication instances ←--→ Internet.

#### Subnet notation (IPv4)
A subnet is a sub section of a network, a 'logical' partition.
Break a network into multiple small Network Segments called subnets.
Series of ip addresses reserved wich are not available for everyone, separating a part of the network for a private usage. Private id addresses not accesbiles from Internet.
Split IPv4 addresses: wich octets are part of the network and which are available for devices

IP addresses range in a VPC

**Public subnet**
For resources accessible from Internet 

**Private subnet**
For resources accessible from a vpn (private = isolated: dedicated to client with sensible data)

* CIDR (Classless Inter-Domain Routing)
A way to represent a Subnet mask: / + subnet mask's number of bits

1st Network
192.168.1.0/24  First three octets (8×3=24 bits) make up the network portion
                Leaving only the fourth octet for device addresses (256)
2nd network (subnet)
    192.168.2.0/24                    

IP 10.0.0.0 + mask 255.0.0.0        → CIDR 10.0.0.0/8
IP 10.1.0.0 + mask 255.255.0.0      → CIDR 10.1.0.0/16
IP 10.10.1.1 + mask 255.255.255.255 → CIDR 10.10.1.1/32

* Netmask

#### Private (virtual) networks (IPv4)
Because of the limited number of IPv4 addresses 
Devices using any address from those ranges will 
    * Not be directly reachable from the public internet 
    * Not be able to access internet resources

IPv4 addresses used exclusively in private networks:
10.0.0.0    - 10.255.255.255
172.16.0.0  - 172.31.255.255
192.168.0.0 - 192.168.255.255

A NAT-enabled router will take the private IP addresses used in traffic requests between the LAN and the internet and "Translate" them to the router's own public address. The router, true to its name, will then route those requests to their appropriate destinations.

#### VPC - Virtual Private Cloud 

![](assets/chapters/cloud/assets/vpc.png)

A private cloud isolated and securized hosted in a public cloud (a cloud in a cloud)
Isolate resources from public cloud
Configure subnets with IP addresses range, configure routage tables and gateways

**Applications**
- More secure (isolate instances in private subnets not accessible from Internet)
- For networks interconnetion
- Database
- Recovery

Some VPC has a NAT: a public website/app can works in a VPC

Amazon Virtual Private Cloud create connections between Amazon EC2 (Elastic Compute Cloud) and others networks trough a VPN ( IPsec protocol)

download.chapter(security/vpn.md)

### Internet Gateway

Enable instances inside Public Subnet to get Internet access.
Enables Public Subnet,  publicly accessible over the Internet.
Instances behind Internet Gateway can send outgoing traffic as well as can receive incoming traffic.

Internet Gateway is the only component that allows communication between your VPC and Internet.
I is attached to route table of NAT gateway and Public Subnet to enable them to communicate with Internet.

### Route Table

Every VPC has an implicit Router and that router use route table to controls  network traffic or directs the traffic to a destination.
You can associate the Route Table with an Internet Gateway or Nat Gateway for Internet access.