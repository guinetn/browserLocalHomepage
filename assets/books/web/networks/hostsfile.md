## Hosts file

local plain text file
maps servers or hostnames to IP addresses
in use since the time of ARPANET. It was the original method to resolve hostnames to a specific IP address. The hosts file is usually the first process in the domain name resolution procedure (Firefox now uses DNS over HTTPS (or DOH) by default. That means instead of checking your local hosts file or even your DNS resolver)

The hosts file is used to map domain names to IP addresses, and can be used as an alternative to DNS. It also allows you to specify the IP address to which a website resolves on your computer, regardless of what may be published in the site’s DNS zone file.

you view and test a site on one server while the rest of the world continues to see the site on another. That makes it an essential tool when migrating your website. 

* It must be edited with administrative privileges (is a protected file)
* Computer’s hosts file location depends on your operating system

Windows     C:\Windows\System32\drivers\etc\hosts
            Flush your dns cache: ipconfig /flushdns

Linux       /etc/hosts
            Unbutu: service dns-clean restart
            NSCD (Name Service Caching Daemon) may need to use one of the following commands.
                service nscd restart 
                systemctl restart nscd.service
                nscd -I hosts

Mac         /private/etc/hosts
            dscacheutil -flushcache; sudo killall -HUP mDNSResponder

 IP   space or \t    domain(s)  to resolve to the specified IP address
 ↓         ↓         ↓
127.0.0.1           localhosts                              #loopback
127.0.1.1	        mycomputer.localdomain	mycomputer

255.255.255.255     broadcasthost
123.123.123.123     liquidweb.com www.liquidweb.com
#67.225.187.61      liquidweb.com #Liquid Web
72.30.35.10         liquidweb.com #this is the new liquidweb.com

\# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

DOH (DNS over HTTPS): some browser use dns and not hosts file by default (Firefox). Edit options to unable DoH