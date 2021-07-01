## curl - Client URL Request Library

Tool to transfer data to and from a server
To pull the information from the internet without a graphical interface
Protocols: HTTP, FTP, IMAP, LDAP, POP3, SCP, SFTP, SMB, SMTP...

https://github.com/curl

    curl -X POST "http://localhost:8000/login" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"email\":\"string\",\"password\":\"string\"}"
          \___ Request                          \___ Headers                                                        \___ data

curl is included in almost every modern device–smartphones, cars, TVs, laptops, servers, gaming consoles, printers and beyond.
