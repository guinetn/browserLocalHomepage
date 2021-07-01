# LDAP - Lightweight Directory Access Protocol

***A directory ***
similar to a database, but tends to contain more descriptive, attribute-based information. The information in a directory is generally read much more often than it is written. Directories are tuned to give quick-response to high-volume lookup or search operations. They may have the ability to replicate information widely in order to increase availability and reliability, while reducing response time. When directory information is replicated, temporary inconsistencies between the replicas may be OK, as long as they get in sync eventually.

There are many different ways to provide a directory service. Different methods allow different kinds of information to be stored in the directory, place different requirements on how that information can be referenced, queried and updated, how it is protected from unauthorized access, etc. Some directory services are local, providing service to a restricted context (e.g., the finger service on a single machine). Other services are global, providing service to a much broader context.

## LDAP

standards-based mechanism for interacting with directory servers. It’s often used for authentication and storing information about users, groups, and applications, but an LDAP directory server is a fairly general-purpose data store and can be used in a wide variety of applications.

1. Install and configure a directory server (or multiple servers configured in a replicated topology
https://ldap.com/directory-servers/
- Microsoft Active Directory
- ApacheDS
- OpenLDAP
- Oracle Internet Directory
...
2. Write software to interact with a directory server over LDAP. 
https://ldap.com/client-apis/

LDAP is a lightweight client-server protocol for accessing directory services, specifically X.500-based directory services. LDAP runs over TCP/IP or other connection oriented transfer services. 
LDAP is defined in [RFC2251](ftp://ftp.isi.edu/in-notes/rfc2251.txt) "The Lightweight Directory Access Protocol (v3)

LDAP directory service is based on a client-server model

***object class***
defines the collection of attributes that can be used to define an entry. LDAP basic types of object classes:
- Groups in the directory, including unordered lists of individual objects or groups of objects.
- Locations, such as the country name and description.
- Organizations in the directory.
- People in the directory.

An entry can belong to more than one object class.

commonName/cn attribute is used to store a person's name. A person named Jonas Salk can be represented in the directory as
cn: Jonas Salk
givenname: Jonas
surname: Salk
mail: jonass@airius.com

### LDAP Linux HOWTO

* Slapd
LDAP server daemon
supports a variety of different database backends which you can use.

https://tldp.org/HOWTO/LDAP-HOWTO/index.html

# OpenLDAP 

- https://ldap.com/