## ROUTER: IPV4 addressing

Host A ----> Router ----> Router ----> Host B

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

## Internet Gateway

Enable instances inside Public Subnet to get Internet access.
Enables Public Subnet,  publicly accessible over the Internet.
Instances behind Internet Gateway can send outgoing traffic as well as can receive incoming traffic.

Internet Gateway is the only component that allows communication between your VPC and Internet.
It is attached to route table of NAT gateway and Public Subnet to enable them to communicate with Internet.