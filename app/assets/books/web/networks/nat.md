### NAT - Network Address Translation

Translate network addresses from Private IP ---→ Public IP for connections to public Internet

Process in which your router changes your private IP Address into a public one so that it can send your traffic over the Internet, keeping track of the changes in the process.
When the information comes back to your router, it reverses the change—from a real IP address into a private one—and forwards the traffic back to your computer.

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

- https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip/856345-la-nat-et-le-port-forwarding
- https://learn.g2.com/port-forwarding