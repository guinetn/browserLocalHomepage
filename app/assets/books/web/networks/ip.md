## IP - Internet Protocol

Unique number assigned to the network connection on the computer.
Heart of the network connectivity. Any device on a network has and needs an IP Address.
TCP/IP Protocols
UDP/IP Protocols


#### IPv4
  
  172   .   16   .  254   .  1
   ↓        ↓        ↓       ↓   
10101100.00010000.11111110.00000001
________
1 byte  = 8 bits
___________________________________
     4 * 8 = 32 bits = 4 bytes

32-bit length: 192.168.0.16
Limit: 4.3 billion unique IP addresses
Exponential growth in mobile devices including mobile phones, notebook computers, wireless handhled devices has created a need for additional blocks of IP addresses.

IP Addresses classes
| From | To |
|---|---|
|Class A||
| 0.0.0.0 | 127.255.255.255 |
| Default Subnet mask | 255.0.0.0 |
|Class B||
| 128.0.0.0 | 191.255.255.255 |
| Default Subnet mask | 255.255.0.0 |
|Class C||
| 192.0.0.0 | 223.255.255.255 |
| Default Subnet mask | 255.255.255.0 |
|Class D multicast||
| 224.0.0.0 | 239.255.255.255 |
| Default Subnet mask | undefined |
|Class E reserved||
| 240.0.0.0 | 255.255.255.255 |
| Default Subnet mask | undefined |

0.0.0.0 : not valid detination
127.0.0.0: localhost (loop) 

***Public IP***
Unic address at Internet level (WAN)

***Private IP***
Unic local IP address on a LAN: vpn, local network, when no need worlwide IP address for each device (host)

Reserved IPv4 addresses for private networks (addresses used exclusively in private networks)
||Private address range|||
|---|---|---|---|
|Class|Start|End|IP addresses|
|A|10.0.0.0|10.255.255.255| 16 777 216 |
|B|172.16.0.0|172.31.255.255| 1 048 576 |
|C|192.168.0.0|192.168.255.255| 65 536 |

The private address ranges in a network don’t have to be synchronized with the rest of the world and the Internet. Because of the limited number of IPv4 addresses 
Devices using any address from those ranges will 
* Not be directly reachable from the public internet 
* Not be able to access internet resources
    
A NAT-enabled router will take the private IP addresses used in traffic requests between the LAN and the internet and "Translate" them to the router's own public address. The router, true to its name, will then route those requests to their appropriate destinations.

   
#### IPv6
128-bit length: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Limit: 2^128: 340,282,366,920,938,463,463,374,607,431,768,211,456
Increased address space. We will never run out of IP addresses 

1998 - Internet Engineering Task Force (IETF): RFC 2460
 
Mobile native support: Mobile IPv6 (MIPv6) enables mobile devices to switch between networks and receive a roaming notification regardless of physical location. 
The size of the IPv6 address space makes it less vulnerable to malicious activities such as IP scanning.
IPv6 packets can support a larger payload than IPv4 packets resulting in increased throughput and transport efficiency.
IPv6 devices can independently auto-configure themselves when connected with other IPv6 devices
IPv6 increased authentication and privacy: 
- IPSec: (embedded IPv6 specification) manage encryption and authentication between hosts
This built in security framework enables secure data traffic between hosts that is independent of any applications on either host. In this way, IPv6 provides an efficient end to end security framework for data transfer at the host or the network level. 

## My IP

- https://whatismyipaddress.com/ip/79.91.122.17

HostName lookup
    https://whatismyipaddress.com/ip-hostname
    Lookup IP Address: 79.91.122.17
    Lookup Hostname: 55.213.27.88.rev.sfr.net

Speed-Test    
    https://whatismyipaddress.com/speed-test

## Hide my IP

Reasons: Hiding your geographical location, preventing Web tracking, avoiding a digital footprint, bypassing any content filters, bans, or blacklisting.

- Use a VPN Service (many of them shady or poor quality)
- Use the Tor Browser
- Use a Proxy Server: re-route your browser around a company or school content filters.
- Use Public WiFi: temporarily hide your usual IP address. However, if you don’t use a VPN, your Internet activity is at risk of being spied on or intercepted by a bad guy without your knowing it

## IP LOOKUP

- https://whatismyipaddress.com/get-ip

- ISP and organization's name
- IP's host name
- country it's in
- region/state
- city (see below)
- latitude and longitude of location (a best guess)
- area code for that region
- any known services running on that IP

## More

- https://www.cbouba.fr/adresses-ip-masque-de-sous-reseau-passerelle-par-defaut-et-serveur-dns/