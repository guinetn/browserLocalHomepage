# CRYPTOGRAPHY

Secure against an adversary with enormous amounts of computational power. Estimating how much work certain computations (number factoring, finding a discrete logarithm) require, and choosing cryptographic parameters based on our best estimate of how much work would be required to break the system.

To protect against pirate, nation-state adversary ("NSA" for short..) 

## PKI - Public key infrastructure 
Umbrella term for all of the stuff we need in order to issue, distribute, store, use, verify, revoke, and otherwise manage and interact with certificates and keys. 

## ASYMMETRIC CRYPTOGRAPHY (public-key encryption)
Uses key pairs for authentication (certificates and PKI)

Security of a public key cryptosystem depends on keeping private keys private.

|A pair of keys|||
|---|---|---|
|Public key|Distributed and shared to anyone (the world)|To encrypt some data. The only way to decrypt that data is with the corresponding private key|
|Private key|Hidden from public. Don’t share it with anyone.|To decrypt. Private key allow to sign some data. Anyone who knows the corresponding public key can verify the signature, proving which private key produced it.|

Asymmetric: it's a one-way trip
Alice can send messages encrypted with your public key to you, but neither of your keys will help you send an encrypted message to Alice.

In an asymmetric key encryption scheme, anyone can encrypt messages using the public key, but only the holder of the paired private key can decrypt. Security depends on the secrecy of the private key.

The idea of an asymmetric public-private key cryptosystem is attributed to Whitfield Diffie and Martin Hellman, who published this concept in 1976. They also introduced digital signatures

## SYMMETRIC CRYPTOGRAPHY

Algorithms for cryptography that use the same cryptographic keys for both encryption of plaintext and decryption of ciphertext. 

The keys may be identical or there may be a simple transformation to go between the two keys. The keys, in practice, represent a shared secret between two or more parties that can be used to maintain a private information link. This requirement that both parties have access to the secret key is one of the main drawbacks of symmetric key encryption


download.md(assets/slides/security/rsa.md)
