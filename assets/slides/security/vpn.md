## VPN - VIRTUAL PRIVATE NETWORK 

Remote locations are by their nature insecure
VPN permit secure and invisible remote connections
Provides a direct connection between remote clients and a server in a way that hides data as it’s transferred across an insecure network

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

[OpenVPN](https://openvpn.net/)
. the best known
. open source 
. TLS/SSL encryption
. install on one of you're VM: https://www.freecodecamp.org/news/securing-your-network-connections-using-openvpn/

### More
- https://devopsmyway.com/openvpn-server-setup-aws/
- [Build your own VPN server on azure (for FREE or on the cheap)](https://www.youtube.com/watch?v=pU2y9_7vrII)