## DNS RECORD (A, CNAME, MX, TXT…)

- Stored in authoritative servers
- Information about a domain (associated IP address)

### A - ADDRESS RECORD
Assigns an IP address to a domain or subdomain name
web browser "www.google.com" → the DNS system will translate that domain name to the IP address of 172.217.12.46 using the A record information stored in a DNS Zone file.

### CNAME - CANONICAL NAME
Forwards a domain name to a different domain name (alias)
The CNAME record makes one domain name an alias of another. The aliased domain gets all the subdomains and DNS records of the original. To put this in simple terms, a CNAME redirects requests to another record.  A CNAME record will always be a fully qualified domain name.

### MX - MAIL EXCHANGE RECORD 
To set email servers and their priority.
Routes email messages to a specific mail server linked to a domain from a designated mail host on a different server. MX records use a priority system if there is more than one MX record used for a domain that is using more than one mail server. The lower the number is, the higher the priority
The MX record state the location that mail directed at the domain will be sent. MX records should always be fully qualified domain names, never just an IP address.

### TTL - TIME TO LIVE
The time to live value sets how long this information will be good for when a recursive DNS server queries for information on your domain name.  The value is typically set in seconds.

A record has a default TTL value of 86400 seconds (24 hours). If we update the an A record, propagation will take 24  to 48 hours to disperse. It is better to change the TTL value to 300 seconds which is 5 minutes

### SOA - SATE OF AUTHORITY
The state of authority record specifies the DNS server providing authoritative information about an Internet domain, the email of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.

### NS - NAMESERVER
Store the authoritative nameserver
The servers listed in the NS record are the authoritative nameservers for the domain.

PTR record (Reverse DNS)
opposite of an A record. It resolves an IP address to a domain name. The purpose of this record is mainly administrative. It verifies that an IP address links to a domain name. Not all DNS hosting providers offer this type of record.

### TXT - TEXT RECORD
A TXT record allows an administrator to insert arbitrary text into a DNS record.  The most common implementation of TXT records are for adding SPF records to a domain.

### SRV - SERVICE RECORD
Establish connections between services and hostnames
For example, if an application is searching for a location of a service that it needs, it will look for an SRV record with that information.  When the app finds the correct SRV record, it will filter through the list of services to find the following information:
Hostname
Ports
Priority and Weight
IP Addresses

_sip._tcp.example.com.   3600 IN SRV 10 50 5060 serviceone.example.com.
_sip is the name of the service and _tcp is the transport protocol.
