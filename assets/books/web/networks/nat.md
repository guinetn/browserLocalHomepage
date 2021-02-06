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