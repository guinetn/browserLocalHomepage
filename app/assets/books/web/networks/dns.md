# DNS - DOMAIN NAME SYSTEM 

Internet directory (phone book)

DNS translate domain names (nytimes.com, www.google.com) into an IP address (like 192.168.2.1) which is used by computers to communicate on a network such as the Internet.
This avoid to memorize IP addresses as 192.168.1.1 (IPv4) or 2400:cb00:2048:1::c629:d7a2 (IPv6)

Browser 'domain name' request
↓
Resolving the hostname:
* Local DNS cache  
    Look for the IP address associated with the domain name
    This cache stores this information that our computer has recently saved. 
* Query another server
    **Recursive DNS servers** 
        Have their local cache too
        It stores the record in its local cache (All DNS records have a TTL (time-to-live value), which shows when a record will expire)
        The Recursive DNS server has the information and returns the A record to your computer. Our computer then stores the record in its local cache. It reads the IP address from the DNS record and passed it to our browser. The web browser will connect to the web server associated with the A records IP and display the website.
        ↓
    **Root server**
        Libraries addresses
        ↓
    **TLD server**   
        ↓ 
* Query the Authoritative DNS Servers
    Query the 'A record' to locate the IP address

![dns-lookup-diagram](assets/books/web/assets/dns-lookup-diagram.webp)

## Reverse DNS (rDNS)
    
Resolving an IP address back to a domain name.
- To block spam
Email Servers commonly use rDNS to block incoming SPAM messages. Many mail servers are set to automatically reject messages from an IP address that does not have rDNS in place
- analytics/logging: IP addresses are not human-readable. Addresses are more readable.

Perform a rDNS lookup manually:   
>Linux: $dig -x 8.8.8.8
>8.8.8.8.in-addr.arpa. 21599 IN PTR google-public-dns-a.google.com.
>ip + server_name: 132.254.231.138.in-addr.arpa