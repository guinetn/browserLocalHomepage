# hashtables

Hash tables are a complex data structure capable of storing large amounts of information and retrieving specific elements efficiently.
This data structure uses key/value pairs, where the key is the name of the desired element and the value is the data stored under that name.


42,Paris → HASH FUNCTION → INDEX → HASH TABLE
K/V pair

Each input key goes through a hash function that converts it from its starting form into an integer value, called a hash. Hash functions must always produce the same hash from the same input, must compute quickly, and produce fixed-length values. Python includes a built-in hash() function that speeds up implementation.
The table then uses the hash to find the general location of the desired value, called a storage bucket. The program then only has to search this subgroup for the desired value rather than the entire data pool.
Beyond this general framework, hash tables can be very different depending on the application. Some may allow keys from different data types, while some may have differently setup buckets or different hash functions.
Here is an example of a hash table in Python code:


import pprint
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)
    def _assign_buckets(self, elements):
        for key, value in elements: #calculates the hash of each key
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size # positions the element in the bucket using hash
            self.buckets[index].append((key, value)) #adds a tuple in the bucket
    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    def __str__(self):
        return pprint.pformat(self.buckets) # pformat returns a printable representation of the object
if __name__ == "__main__":
     capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]

hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")

Advantages:
Can covert keys in any form to integer indices
Extremely effective for large data sets
Very effective search function
Constant number of steps for each search and constant efficiency for adding or deleting elements
Optimized in Python 3
Disadvantages:
Hashes must be unique, two keys converting to the same hash causes a collision error
Collision errors require a full overhaul of the hash function
Difficult to build for beginners
Applications:
Used for large, frequently-searched databases
Retrieval systems that use input keys
Common hash table interview questions in Python
Build a hash table from scratch (without built-in functions)
Word formation using a hash table
Find two numbers that add up to “k”
Implement open addressing for collision handling
Detect if a list is cyclical using a hash table
