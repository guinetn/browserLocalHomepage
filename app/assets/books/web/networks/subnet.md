## Subnet notation (IPv4)

A subnet is a sub section of a network, a 'logical' partition.
Break a network into multiple small Network Segments called subnets.
Series of ip addresses reserved wich are not available for everyone, separating a part of the network for a private usage. Private ip addresses not accesibles from Internet.
Split IPv4 addresses: wich octets are part of the network and which are available for devices

IP Address = subnet + host
Allowed subnet mask bytes: 0, 128, 192, 224, 240, 248, 252, 254, 255

Network administrators need to know the IP addresses range: computed with IP + subnet mask.
| Subnet Mask   | IP          | ||
|---|---|---|---|
| 255.255.255.0 | 192.168.0.x | 192.168.0.0 → 192.168.0.255 | 1 unic IP range. only hosts in this range can communicates together|
| 255.255.254.0 | 192.168.0.x | 192.168.0.0 → 192.168.1.255 |2 IP address range. Hosts in 192.168.0.x and 192.168.1.x can communicates together| 
| 255.255.128.0 | 192.168.0.x | 192.168.0.0 → 192.168.127.255 |128 IP address range. All hosts in 192.168.0.x and 192.168.127.x can communicates together|

magic number: -2, -4, -8, -16, -32, -64, -128. Error for others values (beyond 1 byte)
 
IP addresses range in a VPC

**Public subnet**
For resources accessible from Internet 

**Private subnet**
For resources accessible from a vpn (private = isolated: dedicated to client with sensible data)

* CIDR (Classless Inter-Domain Routing)
A way to represent a Subnet mask: ***/subnet mask's number of bits***

|   |   | 
|---|---|
|1st Network||
|192.168.1.0/24 | First three octets (8×3=24 bits) make up the network portion|
|               | Leaving only the fourth octet for device addresses (256)|
|2nd network (subnet)|  |
| 192.168.2.0/24     |  |                

| IP | MASK | → | CIDR |
|---|---|---|---|
|IP 10.0.0.0 | 255.0.0.0        | → | 10.0.0.0/8 |
|IP 10.1.0.0 | 255.255.0.0      | → | 10.1.0.0/16 |
|IP 10.10.1.1 | 255.255.255.255 | → | 10.10.1.1/32 |

* Netmask

- https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip/856843-on-recapitule-tout-de-a-a-z