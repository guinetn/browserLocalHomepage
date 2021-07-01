## DHCP - Dynamic Host Configuration Protocol)

simplify the management of IP addresses on networks. No two hosts can have the same IP address, and configuring them manually will likely lead to errors. ... Also, most users aren't technically proficient enough to locate the IP address information on a computer and assign it


Static IP addresses allow network devices to retain the same IP address all the time, A network administrator must keep track of each statically assigned device to avoid using that IP address again. ... While DHCP is a protocol for automating the task of assigning IP addresses.

static IP addresses are best for businesses, which host their own websites and internet services. Static IP addresses also work well when you have remote workers logging into work via a VPN. Dynamic IP addresses are usually fine for most consumers

Dynamic IP addresses changes with each session on the network and is more difficult for hackers to compromise data security. As static IP addresses never change, they can become a security risk as it is easier to track the computer it is linked to.

Network management protocol used on Internet Protocol (IP) networks
A DHCP server 
- dynamically assigns an IP address and other network configuration parameters to each device on the network, so they can communicate with other IP networks
- enables computers to request IP addresses and networking parameters automatically from the Internet service provider (ISP), reducing the need for a network administrator or a user to manually assign IP addresses to all network devices.

In the absence of a DHCP server, a computer or other device on the network needs to be manually assigned an IP address, or to assign itself an APIPA address, the latter of which will not enable it to communicate outside its local subnet.

DHCP server may have three methods of allocating IP addresses:

Client                    Server
    --- discovery    --->
    <---   offer     ---
    ---   request    --->
    <--- acknowledge ---
    
* Dynamic allocation
A network administrator reserves a range of IP addresses for DHCP, and each DHCP client on the LAN is configured to request an IP address from the DHCP server during network initialization. The request-and-grant process uses a lease concept with a controllable time period, allowing the DHCP server to reclaim and then reallocate IP addresses that are not renewed.

* Automatic allocation
The DHCP server permanently assigns an IP address to a requesting client from the range defined by the administrator. This is like dynamic allocation, but the DHCP server keeps a table of past IP address assignments, so that it can preferentially assign to a client the same IP address that the client previously had.

* Manual allocation

Also commonly called static allocation and reservations. The DHCP server issues a private IP address dependent upon each client's client id (or, traditionally, the client MAC address), based on a predefined mapping by the administrator. This feature is variously called static DHCP assignment by DD-WRT, fixed-address by the dhcpd documentation, address reservation by Netgear, DHCP reservation or static DHCP by Cisco and Linksys, and IP address reservation or MAC/IP address binding by various other router manufacturers. If no match for the client's client ID (if provided) or MAC address (if no client id is provided) is found, the server may or may not fall back to either Dynamic or Automatic allocation.


## More

https://h30434.www3.hp.com/t5/Printing-Errors-or-Lights-Stuck-Print-Jobs/Assign-static-address-to-HP-Printer/td-p/6313948

setting up your wireless or wired printers to:

* Stay connected to your router
* Fix printer ‘offline’ status
* Wake from sleep mode
* Speed up wireless printing
While DHCP is convenient, devices such as printers (wired and wireless) should always be assigned a static (fixed) IP address manually to avoid conflicts on your wireless network and MUST be outside the DHCP address range of the router. This is because printers are the only external devices that do not have the ability to automatically interrupt the router for a new DHCP address once the least time expires.  


1. Set a static IP in the printer outside the DHCP range of the router (check your manual).  This Static IP is important as DHCP IP addresses will change upon different power up sequences of your devices.  You always want your printer to come up with the same IP address all the time. 

After setting the static IP, the computer(s) must be updated under Printer Properties/Ports to show a Standard TCP/IP port with the printers’ new static IP address.


Router: http://192.168.0.1
Select config
    DHCP :	Activé
        Parameters
        
        Adresse IP LAN : 192.168.0.1
            Masque de sous-réseau : 255.255.255.0
            Serveur DHCP :	 Oui
                Adresse IP de départ : 192.168.0. 10
                Adresse IP de fin : 192.168.0.50
                Durée du bail : 86 400 = 24 h = 24*60*60
            
        Infos de location/réservation DHCP
            Adresse MAC	…	
            Adresse IP	192.168.0. …	
        
        Infos de location client DHCP
        
        	Adresse MAC	   Vitesse	            Adresse IP	            Expire
            2bb590516e6f		                    192.168.0.17	Jan 25 07:05:55
            aca5b65fe5a9	(100 Base-T) / 100Mbps	192.168.0.18	Jan 25 09:15:47    TV (Ethernet cable)
            108b201ef451		                    192.168.0.19	Jan 25 09:15:14    HP ENVY
            4f42281a89b9		                    192.168.0.21	Jan 25 03:02:55
            
            