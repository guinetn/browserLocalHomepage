## VPN - VIRTUAL PRIVATE NETWORK 

Remote locations are by their nature insecure
VPN permit secure and invisible remote connections: bypassing censorship rules to streaming TV shows and torrenting music. 
Provides a *direct connection between remote clients and a server* in a way that hides data as it’s transferred across an insecure network
Has a dedicated subnet and VLAN accessible only from VPC's client.

Use a VPN to...
- Security: have an extra-secure Internet connection. Hackers protection on public wi-fi and unsecured networks
- Privacy: more online privacy and stop spying and tracking. Prevent gov/isp/advertisers from tracking me
- Access: get around Internet restrictions, geo-location blocks and filters: netflix...

Use a VPN service for high-speed bandwidth, usability, a secure connection, private access to blocked sites, and the ability to choose the country and city where you appear to be.

||| 
|---|---| 
|SSH and SCP|protect data transferred through remote connections |
|File encryption|protect data at rest|
|TLS/SSL certificates| protect data between websites / client browsers|
|VPN|protection across a broader range of connections|

1. Have a tunnel
Don't guarantee security
once you’ve opened a tunnel, it’s possible to connect remote networks as though they’re all together locally
2. Add encryption
Choose one of a number of encryption standards

https://cybershield.cc
https://www.linkev.com
https://nordvpn.net
https://surfshark.net

[OpenVPN](https://openvpn.net/)
. the best known
. open source 
. TLS/SSL encryption
. install on one of you're VM: https://www.freecodecamp.org/news/securing-your-network-connections-using-openvpn/

### Malicious VPN Apps

A VPN keep your online activities private and secure. Even if a hacker could intercept data from the network, it would take them longer than the age of the universe to begin to decrypt it.

The primary assumption is that a network is keeping web browsing and personal data safe—but this may not always be the case.

Some apps have critical vulnerabilities (SuperVPN app), making it susceptible to dangerous man-in-the-middle (MITM) attacks, which allow hackers to intercept all communication between the user and the VPN provider 

At risk for having their credit card details stolen, private photos and videos leaked or sold online, or private conversations recorded and sent to a secret server. 
 
10 free VPN apps appear to have critical vulnerabilities:
* SuperVPN Free VPN Client (100 million installs)
* TapVPN Free VPN (10 million installs)
* Best Ultimate VPN — Fastest Secure Unlimited VPN (5 million installs)
* Korea VPN — Plugin for OpenVPN (1 million installs)
* Wuma VPN-PRO (1 million installs)
* VPN Unblocker Free unlimited/best anonymous secure (1 million installs)
* VPN Download: Top, Quick & Unblock Sites (500,00 installs)
* Super VPN 2019 USA — Free VPN, Unblock Proxy VPN (50,000 installs) 

### More
- https://devopsmyway.com/openvpn-server-setup-aws/
- [Build your own VPN server on azure (for FREE or on the cheap)](https://www.youtube.com/watch?v=pU2y9_7vrII)


