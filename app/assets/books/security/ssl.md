# SSL (Secure Sockets Layer)

Deprecated protocol. Now use TLS.

Couche additionnelle à TCP ajoutant une propriété de confidentialité à la connexion en chiffrant les échanges lors de son établissement.
 
- Building customer trust
- Obtaining customers’ confidence in your business website
= install an SSL certificate

When the SSL certificate gets installed to a website, the URL changes from HTTP to HTTPS. A padlock appears in the URL address bar

to secure website pages when submitting necessary sensitive information. Sensitive information can be in the form of payment methods, online services such as online banking, and account login websites

SSL Certificates keep your site and online transactions secure with strong encryption, protecting any sensitive data your site may be collecting.

Let's Encrypt: free, auto-renewing SSL solution
GlobalSign: purchase a universally trusted SSL certificate

A Certificate Authority (CA) is a trusted third party which generates and issues SSL certificates for websites. There are a variety of types of SSL validation levels. 

- Extended Validation Certificates (EV SSL)
- Organization Validated Certificates (OV SSL)
- Domain Validated Certificates (DV SSL)
- Wildcard SSL Certificate
- Multi-Domain SSL Certificate (MDC)
- Unified Communications Certificate (UCC)

> mkdir /etc/ssl
> cd /etc/ssl
> openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 3650 -nodes

This generates 2 files:
- key.pem (clé privée)
- cert.pem (certificat contenant la clé publique)

Comme le certificat est autosigné, le fichier cert.pem fait également office de CA (Certificate Authority). En résumé, ce qui est chiffré avec la clé privée est déchiffrable avec la clé publique et ce qui est chiffré avec la clé publique est déchiffrable par la clé privée.

En conséquence, le serveur présentera le certificat au client souhaitant se connecter (xxx over SSL). Le client extraira la clé publique du certificat et utilisera cette clé pour discuter de façon chiffrée avec le serveur afin de se mettre d'accord sur les modalités d'établissement d'une session SSL par laquelle faire passer les données. Les données circuleront donc chiffrées sur le réseau. Une fois cette commande validée, elle nous demande un certain nombre d'informations :
Country Name (2 letter code) [AU]:FR
State or Province Name (full name) [Some-State]:IdF
Locality Name (eg, city) []:Paris
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Université Paris 13
Organizational Unit Name (eg, section) []:DSI
Common Name (e.g. server FQDN or YOUR name) []:serveur.univ-paris13.fr

On peut répondre ce qu'on veut partout SAUF la dernière concernant le Common Name. Il faut absolument mettre le nom d'hôte complet (FQDN) de la machine faisant office de serveur 