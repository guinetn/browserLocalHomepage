# REDIS

https://redis.io/

Fast key/value database: retrieved data if we know the exact key used to store it.
Real time cache, sessions storage 
Data structure server

Open source *in-memory data structure store*, used as a *database, cache, and message broker*
Data structures:s strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, streams
Built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster

|||
|---|---|
|Store|SET server:name "fido"|
|Retrieve|GET server:name => "fido"|
|Check existence|EXISTS server:name => 1<br/>EXISTS server:blabla => 0|

```redis
SET connections 10
INCR connections        => 11
INCR connections        => 12
DEL connections
INCR connections        => 1

INCRBY connections 100  => 101
DECR connections        => 100
DECRBY connections 10   => 90
```

INCR command in Redis is an atomic operation: don't think about concurrent access.

## Key lifetime:  EXPIRE - TTL commands

SET resource:lock "Redis Demo"
EXPIRE resource:lock 120           key 'resource:lock' to be deleted in 120 seconds
TTL resource:lock   => 113         Test ttl 
TTL resource:lock   => -2          ttl after 113s: doesn't exists (negative)

SET resource:lock "Redis Demo 1"
EXPIRE resource:lock 120
TTL resource:lock           => 119
SET resource:lock "Redis Demo 2"
TTL resource:lock           => -1   -1 = never expire

SET resource:lock "Redis Demo 3" EX 5   Shorthand
TTL resource:lock => 5

SET resource:lock "Redis Demo 3" EX 5
PERSIST resource:lock                   Cancel TTL
TTL resource:lock => -1