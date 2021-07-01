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

## Hash Functions

To hash user's passwords, hashtable keys...

If H is a hash function, given some data d, it's trivial to compute H(d) but given only the hash H(d), it's nearly impossible to compute d. Note that even a one-byte difference in d will result in a completely different hash H(d).
It is more secure to hash passwords before storing them in the database. When a user tries to log in, we hash the password that the user tried to log in with, and compare it to the hash in the database. If the two match, then the password is valid
 
There are a myriad of them, some fast, some slow...
Fast hashing algorithms are great for building data structures (hash tables)
Slow hash functions for password hashing make brute force attacks more difficult. 

```js
 should be called when a user signs up or changes their password
function calculate_hash(password) 
    salt = random_bytes(14) // salt should be at least 8 bytes long, but longer is more secure.
    hash = bcrypt_hash(password, salt)

    // store this with the user in your database
    return hash 

// called whenever a user tries to login
function login_user(username, password) 
    user = get_user_from_database(username)

    // bcrypt stores the salt with the hash, your library should manage this for you
    salt = get_salt(user.hash) 
    new_hash = bcrypt_hash(password, salt)
    if new_hash == user.hash
        login_user()
    else 
        dont_login_user()
```

For hashing, we recommend using either bcrypt or argon2 

download.page(security/cryptography/bcrypt.md)
download.page(security/cryptography/argon2.md)
download.page(security/cryptography/rsa.md)
download.page(security/cryptography/md5.md)
download.page(security/cryptography/sha.md)
download.page(security/cryptography/ntlm.md)
