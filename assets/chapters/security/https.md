# Https

Hypertext Transfer Protocol Secure (HTTPS) is an extension of the Hypertext Transfer Protocol (HTTP). It is used for secure communication over a computer network, and is widely used on the Internet. In HTTPS, the communication protocol is encrypted using Transport Layer Security (TLS) or, formerly, Secure Sockets Layer (SSL). The protocol is therefore also referred to as HTTP over TLS, or HTTP over SSL.

The principal motivations for HTTPS are authentication of the accessed website, and protection of the privacy and integrity of the exchanged data while in transit. It protects against man-in-the-middle attacks, and the bidirectional encryption of communications between a client and server protects the communications against eavesdropping and tampering. In practice, this provides a reasonable assurance that one is communicating with the intended website without interference from attackers.

The authentication aspect of HTTPS requires a trusted third party to sign server-side digital certificates. This was historically an expensive operation, which meant fully authenticated HTTPS connections were usually found only on secured payment transaction services and other secured corporate information systems on the World Wide Web. In 2016, a campaign by the Electronic Frontier Foundation with the support of web browser developers led to the protocol becoming more prevalent. HTTPS is now used more often by web users than the original non-secure HTTP, primarily to protect page authenticity on all types of websites; secure accounts; and to keep user communications, identity, and web browsing private.

## CERTIFICATES

Data structure containing a public key and a name
The data structure is then signed (signature binds the public key to the name)
The entity that signs a certificate is called the issuer (or certificate authority)
The entity named in the certificate is called the subject.

To enable HTTPS on your website, you need to get a certificate (a type of file) from a Certificate Authority (CA). Let’s Encrypt is a CA. In order to get a certificate for your website’s domain from Let’s Encrypt, you have to demonstrate control over the domain. With Let’s Encrypt, you do this using software that uses the ACME protocol which typically runs on your web host.

Certificate formats
- SSH
- PGP 
- X.509 v3  (when people talk about certificates without additional qualification)

PEM (Privacy Enhanced EMail)
Most certificates are packaged up in PEM files (.pem, .crt, .cer, .der) 
a base64 encoded payload sandwiched between a header and a footer. The PEM header has a label that’s supposed to describe the payload. A PEM-encoded X.509 v3 certificate looks like:
-----BEGIN CERTIFICATE-----
MIIBwzCCAWqgAwIBAgIRAIi5QRl9kz1wb+SUP20gB1kwCgYIK...
NmrsQD3/ItjUN1f1ouY=
-----END CERTIFICATE-----

- https://tools.ietf.org/html/rfc5280

#### Tool
- [letsencrypt](https://letsencrypt.org/getting-started/)
A nonprofit Certificate Authority providing TLS certificates to 225 million websites.
- https://certbot.eff.org/


1. Generate PKCS: Certification Request Syntax Specification
https://tools.ietf.org/html/rfc2986
2. Cut and paste the CSR into a CA's web page
CSR: Certificate Signing Request
3. Prove ownership of the domain(s) in the CSR by one of the following methods:
*  Put a CA-provided challenge at a specific place on the web server.
*  Put a CA-provided challenge in a DNS record corresponding to the target domain.
*  Receive a CA-provided challenge at (hopefully) an administrator-controlled email address corresponding to the domain, and then respond to it on the CA's web page.
4. Download the issued certificate and install it on the user's Web Server.
       


## ACME - Automatic Certificate Management Environment

Public Key Infrastructure using X.509 (PKIX) certificates for
- authentication of domain names
- ...

https://tools.ietf.org/html/rfc8555
Certification authorities (CAs) in the Web PKI are trusted to verify that an applicant for a
certificate legitimately represents the domain name(s) in the
certificate.  As of this writing, this verification is done through a
collection of ad hoc mechanisms.  This document describes a protocol
that a CA and an applicant can use to automate the process of
verification and certificate issuance.  The protocol also provides
facilities for other certificate management functions, such as
certificate revocation.
