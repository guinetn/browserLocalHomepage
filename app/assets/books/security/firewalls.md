# FIREWALLS

First line of defense in network security
Protective layer for your server (prevent unauthorized use)
Monitors and filters incoming and outgoing network traffic
A set of rules allow or block specific network traffic
Can be hardware or software based
Can examine individual packets of traffic and test the packets to determine if they are safe.

### Types of Firewalls

* Web application firewalls A (WAF) 

Used for HTTP applications. 
Sets of rules that are applied to monitor or block data packets from http network traffic. For example, these rules can help block cross-site scripting (XSS) and SQL injections.

* Stateful firewalls (network firewalls)

inspect traffic and tracks the operating state and characteristics of a network connection to provide a universal firewall. For example, the packets from certain traffic will be allowed to access certain users while blocking the same traffic to other users. Known active connections with matching packets will be allowed to pass through the firewall.

* Proxy-based firewalls 

intermediary between the requested data by end users and the source servers. The proxy filters all network traffic and will block or allow traffic based on its rule set. The proxy also has the ability to examine the entire network packet besides the network address and the port number. This type of firewall is labeled as the most secured as it prevents direct network contact between systems.

* Firewall hardware

Device that has firewall software installed that is connected between the network and the device for connecting to the internet. For example, a broadband router is placed in front of a home network that has firewall software installed. It is filtering traffic only allowing connections that are based on its rule set. An end user with common PC knowledge can plug in a firewall, configure the settings, and have it work. Always confirm that your firewall is configured for optimal security.

* Firewall software

To manage the deployment of firewall hardware. This is a central system that has policies and features that are configured, as well as analysis of threats is performed.


download.page(security/firewalld.md)
