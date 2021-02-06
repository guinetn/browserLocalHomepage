## DNS Servers

### Authoritative DNS Server  

Stores DNS records (A, CNAME, MX, TXT, etc.) for domain names. Only respond to queries for locally stored DNS zone files. Say a server in our network has stored an A record for example.com. That server is the authoritative server for the example.com domain name.

### Recursive Name Server  

Receives queries for informational purposes. 
Don't store DNS records. When a query is received, it will search the cache memory for an address linked to the IP address. If the recursive name server has the information, then it will return a response to query sender. If it does not have the record, then the query will be sent to other recursive name servers. This continues until it reaches an authoritative DNS server that can supply the IP address.

### DNS Zones

Administrative space within the Domain Name System. A zone forms one part of the DNS namespace delegated to administrators or specific entities. Each zone contains the resource records for all of its domain names.

### DNS Zone File

A text file stored on a server. 
It contains all the records for every domain within that zone. 
It is mandatory for the zone file to have the TTL (Time to Live) listed before any other information. The TTL specifies how long a DNS record is in the server’s cache memory. The zone file can only list one record per line. It will display the Start of Authority (SOA) record listed first. The SOA record contains essential domain name information including the primary authoritative name server for the DNS Zone.