## BCRYPT

A slow hash function that is resistant to brute-force cracks. Commonly used in some Linux distributions. Considered very secure.



```python
import bcrypt  # https://pypi.org/project/bcrypt/

# this will create the hash that you need to store in your database
def create_bcrypt_hash(password):
    # convert the string to bytes
    password_bytes = password.encode()      
    # generate a salt
    salt = bcrypt.gensalt(14)               
    # calculate a hash as bytes
    password_hash_bytes = bcrypt.hashpw(password_bytes, salt)   
    # decode bytes to a string
    password_hash_str = password_hash_bytes.decode()            

    # the password hash string should similar    
    return password_hash_str        

# this will return true if the user supplied a valid password and 
# should be logged in, otherwise false
def verify_password(password, hash_from_database):
    password_bytes = password.encode()
    hash_bytes = hash_from_database.encode()

    # this will automatically retrieve the salt from the hash, 
    # then combine it with the password (parameter 1)
    # and then hash that, and compare it to the user's hash
    does_match = bcrypt.checkpw(password_bytes, hash_bytes)

    return does_match
```