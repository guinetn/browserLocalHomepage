# Http

## SPEAKING THE HTTP PROTOCOL

### curl - Client URL Request Library
https://github.com/curl

    curl -X POST "http://localhost:8000/login" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"email\":\"string\",\"password\":\"string\"}"
          \___ Request                          \___ Headers                                                        \___ data

curl is included in almost every modern device–smartphones, cars, TVs, laptops, servers, gaming consoles, printers and beyond.

### jq - command-line JSON processor
https://stedolan.github.io/jq/
https://jqplay.org/
for handling JSON; I use it with curl and this talk was about CouchDB which speaks JSON for its data format so I had to mention it here!

### http-console 
https://github.com/cloudhead/http-console
intuitive interface for speaking the HTTP protocol.
is a cross-platform interactive HTTP prompt, I like it and use it a lot with 
CouchDB particularly.

### HTTPie 
https://httpie.org/
is more like curl but humane and with gorgeous colorful output that makes everything easier to read! This should be my favorite, but I have the muscle memory for curl.

### Postman 
https://www.getpostman.com/
is a cross-platform friendly graphical interface for making and inspecting HTTP requests. I usually recommend this to anyone who finds this a more approachable way to use a computer than from the command line. It's a very, very good tool and works on all platforms.
