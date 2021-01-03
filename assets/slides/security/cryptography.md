# CRYPTOGRAPHY

## ASYMMETRIC CRYPTOGRAPHY (public-key encryption)
For authentication

|A pair of keys|||
|---|---|---|
|Public key|Distribute to anyone|To encrypt|
|Private key|hidden from public. Don’t share it with anyone.|To decrypt|

Asymmetric: it's a one-way trip
Alice can send messages encrypted with your public key to you, but neither of your keys will help you send an encrypted message to Alice.

In an asymmetric key encryption scheme, anyone can encrypt messages using the public key, but only the holder of the paired private key can decrypt. Security depends on the secrecy of the private key.

The idea of an asymmetric public-private key cryptosystem is attributed to Whitfield Diffie and Martin Hellman, who published this concept in 1976. They also introduced digital signatures

## SYMMETRIC CRYPTOGRAPHY

Algorithms for cryptography that use the same cryptographic keys for both encryption of plaintext and decryption of ciphertext. 

The keys may be identical or there may be a simple transformation to go between the two keys. The keys, in practice, represent a shared secret between two or more parties that can be used to maintain a private information link. This requirement that both parties have access to the secret key is one of the main drawbacks of symmetric key encryption


download.md(assets/slides/security/rsa.md)
