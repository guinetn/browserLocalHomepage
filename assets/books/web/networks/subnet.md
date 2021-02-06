## Subnet notation (IPv4)
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