# OpenSSL

Open-source software cryptography library  
Secure internet communication by providing cryptographic functionality to applications
Widely used on many server applications (Solaris, Linux, Mac OS X, BSD, OpenVMS, Windows)

OpenSSL is used to encrypt 66% (estimated) of the web: Facebook, Google, Netflix…

Besides that, OpenSSL is also a fully equipped instrumentation for implementation of the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols.

Cryptographic functions to perform SSL tasks with 
- Generate CSRs (Certificate Signing Requests) 
- Generate private keys
- File encryption and decryption purposes along with generating password hashes.
- Perform an SSL certificate installation
- Convert certificates into different formats
- Verify its details or even extract information about the certificate.

# install
Unix/Linux: include the OpenSSL program by default
Windows: intall from 

openssl version
openssl version -a
openssl help
    Standard commands: rsa pkey...
    Message Digest commands: md5 sha256 sha1...
    Cipher commands: aes-128-cbc  des3...
man openssl

PS>Get-ChildItem -Path Cert:\LocalMachine\CA
## More
- https://github.com/openssl
- https://www.liquidweb.com/kb/how-to-verify-a-connection-is-secure-using-openssl