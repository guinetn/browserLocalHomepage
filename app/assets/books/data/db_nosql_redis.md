# REDIS

https://redis.io/
https://docs.nestjs.com/microservices/redis

Fast key/value database: retrieved data if we know the exact key used to store it.
Real time cache, sessions storage, ephemeral storage
Data structure server

Open source *in-memory data structure store*, used as a *database, cache, and message broker*
Data structures:s strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, streams
Built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster

Redis transporter implements the publish/subscribe messaging paradigm and leverages the Pub/Sub feature of Redis. Published messages are categorized in channels, without knowing what subscribers (if any) will eventually receive the message. Each microservice can subscribe to any number of channels. In addition, more than one channel can be subscribed to at a time. Messages exchanged through channels are fire-and-forget, which means that if a message is published and there are no subscribers interested in it, the message is removed and cannot be recovered. Thus, you don't have a guarantee that either messages or events will be handled by at least one service. A single message can be subscribed to (and received) by multiple subscribers.
 
 
|||
|---|---|
|Store|SET server:name "fido"|
|Retrieve|GET server:name => "fido"|
|Check existence|EXISTS server:name => 1<br/>EXISTS server:blabla => 0|

```md
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

## more

- https://github.com/davidfowl/A-sync-RedisClient
- https://www.youtube.com/watch?v=UrQWii_kfIE&t=29s