# TLS - Transport Layer Security

Replace the old SSL layer

"Protocol" = we've agreed to do things like this
Cryptographic protocol for providing secure Host-to-Host communication, ie client-server

Can use for 
- Serve websites: HTTPS communication protocol is encrypted using TLS (lock icon in url)
- Internal inter-datacenter communication on our backend

**Authenticity**
the server needs to prove to the client that it is the real server (and optionally, the client can prove to the server that it's the real client)
Authenticity protects against active attackers

**Key agreement**
the server and client need to agree, over an insecure connection, on a temporary shared secret known only to them

**Symmetric encryption**
the server and client need to use their shared secret to encrypt the data they want to send over a secure connection


1. TLS HANDSHAKE: Hi! Hola! Exchange encryption keys

Establishes a shared session key (symmetric key) with the one way trip Asymmetric Cryptography (a pair of keys in order to achieve authentication). During the TLS handshake, the server will provide its public key via its digital certificate (SSL certificate provided and verified by trusted third parties known as Certificate Authorities CA).
While anyone may encrypt a message using your public key, only your private key can then decrypt that message.

Client → ClientHello msg        → Server                
          + TLS version 
          + cipher supported (set of algorithms that can be used to secure communications)
 
       ← Server Hello msg
        Server chooses the protocol version and cipher suite to use from the choices offered
        establish a shared secret

## SECURE SESSIONS
Once the session key is established the session begins.

A TLS handshake begins with an asymmetric exchange, the client and server will use this initial communication to establish a shared secret, sometimes called a session key. This key is symmetric, meaning that both parties use the same shared secret and must maintain that secrecy for the encryption to be secure.
By using the initial asymmetric communication to establish a session key, the client and server can rely on the session key being known only to them. For the rest of the session, they'll both use this same shared key to encrypt and decrypt messages, which speeds up communication.

Session
    Is the duration of encrypted communication between the client and server. 
    During this time, messages are encrypted and decrypted using the session key that only the client and server have.
    Sessions are temporary, and once ended, must be re-established or resumed.

The session key is used to 
    secure messages (encryption)
    provide message integrity (checksum, parties can detect a message changed before its reception)

## SESSION END
Network disconnection
Client staying idle for too long
Re-established via a new handshake or resumed with previously established secrets (session IDs) 