#### Private (virtual) networks (IPv4)
Because of the limited number of IPv4 addresses 
Devices using any address from those ranges will 
    * Not be directly reachable from the public internet 
    * Not be able to access internet resources

IPv4 addresses used exclusively in private networks:
||Private address range||
|---|---|---|
|Class|Start|End|
|A|10.0.0.0|10.255.255.255|
|B|172.16.0.0|172.31.255.255|
|C|192.168.0.0|192.168.255.255|

A NAT-enabled router will take the private IP addresses used in traffic requests between the LAN and the internet and "Translate" them to the router's own public address. The router, true to its name, will then route those requests to their appropriate destinations.