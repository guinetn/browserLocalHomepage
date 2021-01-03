# CSR - CERTIFICATE SIGNING REQUEST

Block of encoded text shared to a CA (Certificate Authority) for purchasing or renewing an SSL Certificate for a Domain/Website.

## CSR Generation

Private Key (keep safe, never public)
Needed to install SSL Certificate on the server (after SSL Certificate purchase)

$ sudo apt-get install openssl*     Ubuntu/Debian
$ sudo yum install openssl*         Amazon Linux/Centos/RHEL
$ openssl version -a
$openssl req -out myxxx.csr -new -newkey rsa:2048 -nodes -keyout myxxx.private.key
    Generating a RSA private key...
    Country Name (2 letter code) [AU]:IN
    State or Province Name (full name) [Some-State]:DL
    Locality Name (eg, city) []:DELHI
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:MYXXX PVT. LTD.
    Organizational Unit Name (eg, section) []:IT
    Common Name (e.g. server FQDN or YOUR name) []:myXXX.com
    Email Address []:

    For Wild Card SSL Certificate: Common Name: *.myxxxx
$ ls  
myxxx.csr           → Verify on https://www.sslshopper.com/csr-decoder.html
myxxx.private.key   → don’t share it with anyone 

Share the CSR file to Certificate Authority to generate/renew SSL Certificate for your Website.