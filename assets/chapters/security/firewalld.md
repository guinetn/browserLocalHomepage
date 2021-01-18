# firewalld

firewalld on systemd systems is easier to manage and configure than iptables.

systemctl enable firewalld      Be sure it started automatically with the server
systemctl start firewalld       Start it manually the first time
systemctl stop firewalld        When troubleshooting rules and connection issues
systemctl restart firewalld
systemctl status firewalld      is enabled, active, and running ?

### Configuring Rules

open ports, allow services, whitelist IPs for access…
include the `--permanent` flag:  rule is saved even after you restart/reboot

* Add a Port for TCP or UDP
firewall-cmd --permanent --add-port=22/TCP          open a port. Need to add rules for each protocol tcp/udp
firewall-cmd --permanent --add-port=53/UDP

* Remove a Port for TCP or UDP
firewall-cmd --permanent --remove-port=444/tcp      remove a currently open port, closing off that port

* Add a Service
These services assume the default ports configured within the /etc/services configuration file; if you wish to use a service on a non-standard port, you will have to open the specific port, as in the example above.
firewall-cmd --permanent --add-service=ssh
firewall-cmd --permanent --add-service=http

* Remove a Service
firewall-cmd --permanent --remove-service=mysql     Then close off the port that is defined for that service.

* Whitelist an IP Address
firewall-cmd --permanent --add-source=192.168.1.100     add a trusted source
firewall-cmd --permanent --add-source=192.168.1.0/24    a range of IPs using what is called CIDR notation

* Remove a Whitelisted IP Address
firewall-cmd --permanent --remove-source=192.168.1.100

* Block an IP Address
firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='192.168.1.100' reject"
firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='192.168.1.0/24' reject"   CIDR notation

* Whitelist an IP Address for a Specific Port (More Rich Rules)
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100" port protocol="tcp" port="3306" accept'

* Removing a Rich Rule
firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="192.168.1.100" port protocol="tcp" port="3306" accept'

* Saving Firewall Rules
After you have completed all the additions and subtraction of rules, you need to reload the firewall rules to make them active. 
firewall-cmd --reload

* Viewing Firewall Rules
After reloading the rules, you can confirm if the new rules are in place correctly with the following.
firewall-cmd --list-all

https://www.liquidweb.com/kb/an-introduction-to-firewalld/

### iptables
Every network packet arriving at or leaving from the computer traverses at least one chain.
Root user define tables containing chains of rules for the treatment of packets

Each table is associated with a different kind of packet processing. 
Packets are processed by sequentially traversing the rules in chains. 
A rule in a chain can cause a goto or jump to another chain, and this can be repeated to whatever level of nesting is desired. 

The origin of the packet determines which chain it traverses initially. There are five predefined chains

|||
|---|---|
|PREROUTING | Packets will enter this chain before a routing decision is made|
|INPUT | Packet is going to be locally delivered. It does not have anything to do with processes having an opened |socket | local delivery is controlled by the "local-delivery" routing table: ip route show table local|
|FORWARD | All packets that have been routed and were not for local delivery will traverse this chain|
|OUTPUT | Packets sent from the machine itself will be visiting this chain|
|POSTROUTING | Routing decision has been made. Packets enter this chain just before handing them off to the|hardware.

    [ec2-user@ip-172-15-55-125 ~]$ sudo iptables -L -v -n
    Chain INPUT (policy ACCEPT 593K packets, 147M bytes)
    pkts bytes target     prot opt in     out     source               destination

    Chain FORWARD (policy DROP 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination
    3812   33M DOCKER-USER  all  --  *      *       0.0.0.0/0            0.0.0.0/0
    3812   33M DOCKER-ISOLATION-STAGE-1  all  --  *      *       0.0.0.0/0            0.0.0.0/0
    2446   33M ACCEPT     all  --  *      docker0  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
        0     0 DOCKER     all  --  *      docker0  0.0.0.0/0            0.0.0.0/0
    1366 86818 ACCEPT     all  --  docker0 !docker0  0.0.0.0/0            0.0.0.0/0
        0     0 ACCEPT     all  --  docker0 docker0  0.0.0.0/0            0.0.0.0/0

    Chain OUTPUT (policy ACCEPT 523K packets, 85M bytes)
    pkts bytes target     prot opt in     out     source               destination

    Chain DOCKER (1 references)
    pkts bytes target     prot opt in     out     source               destination

    Chain DOCKER-ISOLATION-STAGE-1 (1 references)
    pkts bytes target     prot opt in     out     source               destination
    1366 86818 DOCKER-ISOLATION-STAGE-2  all  --  docker0 !docker0  0.0.0.0/0            0.0.0.0/0
    3812   33M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0

    Chain DOCKER-ISOLATION-STAGE-2 (1 references)
    pkts bytes target     prot opt in     out     source               destination
        0     0 DROP       all  --  *      docker0  0.0.0.0/0            0.0.0.0/0
    1366 86818 RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0

    Chain DOCKER-USER (1 references)
    pkts bytes target     prot opt in     out     source               destination
    3812   33M RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0

https://en.m.wikipedia.org/wiki/Iptables