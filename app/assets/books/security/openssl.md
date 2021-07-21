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
Windows: intall from the web

openssl version
openssl version -a
openssl help
    Standard commands: rsa pkey...
    Message Digest commands: md5 sha256 sha1...
    Cipher commands: aes-128-cbc  des3...
man openssl

>Get-ChildItem -Path Cert:\LocalMachine\CA

## Generate the certificate

Certificate is invalid exception on Linux
dotnet dev-certs ... doesn't fully work on Linux so you need to generate and trust your own certificate.

- https://stackoverflow.com/questions/55485511/how-to-run-dotnet-dev-certs-https-trust
- https://github.com/dotnet/tye/blob/main/docs/tutorials/hello-tye/00_run_locally.md

cat << EOF > localhost.conf
[req]
default_bits       = 2048
default_keyfile    = localhost.key
distinguished_name = req_distinguished_name
req_extensions     = req_ext
x509_extensions    = v3_ca

[req_distinguished_name]
commonName                  = Common Name (e.g. server FQDN or YOUR name)
commonName_default          = localhost
commonName_max              = 64

[req_ext]
subjectAltName = @alt_names

[v3_ca]
subjectAltName = @alt_names
basicConstraints = critical, CA:false
keyUsage = keyCertSign, cRLSign, digitalSignature,keyEncipherment

[alt_names]
DNS.1   = localhost
DNS.2   = 127.0.0.1

EOF

Generate certificate from config:  
>openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -config localhost.conf
>openssl pkcs12 -export -out localhost.pfx -inkey localhost.key -in localhost.crt     // Export pfx
Import CA as trusted: 
>sudo cp localhost.crt /usr/local/share/ca-certificates/
>sudo update-ca-certificates 
Validate the certificate
>openssl verify localhost.crt

## More
- https://github.com/openssl
- https://www.liquidweb.com/kb/how-to-verify-a-connection-is-secure-using-openssl
- https://github.com/dotnet/tye/blob/main/docs/tutorials/hello-tye/00_run_locally.md