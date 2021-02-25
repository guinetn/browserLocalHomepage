## ROUTER: IPV4 addressing

Allow you to share a single IP address among multiple network devices

A router is hardware—a small piece of computer/network-related equipment that connects you to the Internet. A gateway is often associated with a router. 
A router can be connected to two or more networks at a time, but for home networks, that’s generally not the case
Ethernet switch creates networks and the router allows for connections between networks.
 
Host A ----> Router ----> Router ----> Host B

* Has a public IP address of 183.23.100.34 to which all incoming and outgoing traffic is associated.
* Acts as a Dynamic Host Configuration Protocol (DHCP) server
Assigning private IP addresses to all the PCs, laptops, smartphones, and servers in the house. The devices will use those addresses whenever they talk to each other.
* Traffic requests directed at your devices from external networks will be scanned and filtered to help prevent unauthorized and potentially dangerous access.

A router is connected to 2+ data lines from different IP networks. When a data packet comes in on one of the lines, the router reads the network address information in the packet header to determine the ultimate destination. Then, using information in its routing table or routing policy, it directs the packet to the next network on its journey.

## LAN / WAN
* Local Network (private IP) = LAN - local area network 

* Internet = WAN - wide area network
- border router
- gateway router
 
```txt

   ------------         ---------------------
   LAN                                WAN
   ------------         ---------------------
                ROUTER
- IP       ←→  GATWEWAY    ☐☐☐ ←→ INTERNET
- SWITCH        - NAT      ☐☐☐      
- SUBNET                   ☐☐☐     
                           ☐☐☐     
                          Firewall
                        - DMZ
                        - Port forward
```

```txt
  
  Google, server...
      ↑ ↓ 
     World     
      ↑ ↓
    INTERNET 
      ↑ ↓
PUBLIC IP: 82.10.250.19         
    ROUTER  
      ↑ ↓
      GATEWAY: ip address of the router
      ↑ ↓
      NAT: router changes private IP ---> public so it can send your traffic over Internet 
           When response comes back to the router, it reverses: real IP address → private one—and forwards the traffic back to your computer.      
      ↑ ↓        
    PRIVATE IP: passport to Internet but is just for your router, your network, and you      
    192.168.0.1 _______ Manufacturer's Routers Private IP:
                |                     - Linksys: 192.168.1.1
                |                     - D-Link/NETGEAR: 192.168.0.1
                |                     - Cisco: 192.168.10.2, 192.168.1.254 or 192.168.1.1
                |                     - Belkin/SMC: 192.168.2.1                
                |
            DHCP Server 
                |
                |____ Computers linked to a router share the same public IP address: you can join me on the 78.32.35.68
                |
                |    Local devices using NAT (Translate Private IP ←-→ Public IP)            
                |
              SWITCH
                |
                ├─── 192.168.1.24  PC #1 ......... Url in Browser http://www.google.com = Public IP address 75.25.6.7
                ├─── 192.168.1.25  PC #2
                ├─── 192.168.1.4   WebServer
                |
              SWITCH
                |
                ├─── 192.168.1.19  Printer
                └─── 192.168.1.12  Smartphone                           

```

Get my public IP: https://httpbin.org/ip
Get my private IP: 

## FIREWALL
Set of passive rules to protect network from unhautorized access
Allow only specific communications LAN ←→ WAN
## 2 options to allow communications WAN →→→ LAN:
* DMZ 
Demilitarized zone: 
A subnetwork containing & exposing a device to an untrusted network such as the Internet
Router transmit WAN request to the DMZ

* Port Forwarding
Allow communications LAN ←→ WAN through router & firewall
Just specify machine+port
## Switch

a network switch can connect multiple devices and networks to expand the LAN
a switch is useful if your router doesn't have enough Ethernet ports

Switches facilitate the sharing of resources by connecting together all the devices, including computers, printers, and servers, in a small business network. Thanks to the switch, these connected devices can share information and talk to each other, regardless of where they are in a building or on a campus.

They connect multiple devices, such as computers, wireless access points, printers, and servers; on the same network within a building or campus. A switch enables connected devices to share information and talk to each other.

networking hardware connecting network devices by using packet switching to receive and forward data to the destination

## Gateway - Passerelle

Ip address of the router
Allows data to flow from one discrete network to another (provides interoperability between networks)
Usually also acts as a proxy server and a firewall.

Adresse de l'élément permettant la discussion entre deux hôtes: un routeur, serveur, box 

Default gateway: est toujours un routeur qui peut se connecter à plusieurs réseaux IP et acheminer le trafic entre ces réseaux IP. Le routeur aura sa propre adresse IP sur chaque réseau IP auquel il se connecte.

Routeur: connexion au sein des réseaux locaux comme une usine et un réseau de bureau. Passerelle: connexion entre des réseaux qui ne sont pas nécessairement sur le réseau local et qui sont externes à l'organisation

On an Internet Protocol (IP) network, IP packets with a destination outside a given subnet mask are sent to the network gateway:
* private network base IPv4 address of 192.168.1.1 + subnet mask of 255.255.255.0
* any data addressed to an IP address outside of 192.168.1.0 is sent to the network gateway.  While forwarding an IP packet to another network, the gateway may perform network address translation.

A node (router) in a computer network that routes traffic from a workstation to the outside network
Enable instances inside Public Subnet to get Internet access.
Enables Public Subnet, publicly accessible over the Internet.
Instances behind Internet Gateway can send outgoing traffic as well as can receive incoming traffic.

For basic Internet connections at home, the gateway is the ISP (Internet Service Provider) that gives you access to the entire Internet.
Internet Gateway is the only component that allows communication between your VPC and Internet.
It is attached to route table of NAT gateway and Public Subnet to enable them to communicate with Internet.

download.page(web/networks/proxy.md)
download.page(web/networks/proxy_reverse.md)