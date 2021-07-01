# DISTRIBUTED DATABASE

Cluster: physical servers architecture distribution 

Distribute data on servers
Main server 
- distribute the load (data + requests)
- combine requests results
- manage consistency
- Not fault tolerant
- Availability not guaranteed
- No elasticity

Last tree issue are solve by nosql database with

* ELASTICITY
Capacity of adapation according servers available and data quantity
1 To of data on 1000 servers: 1Go / server. 
    If peak, add 1000 servers = 500 Mo/server
    When off-peak, reduce to initial 1000 servers

* SHARDING
Distribute chunks (file part) on servers
Be elastic (servers/data)
Be fault tolerant

download.page(data/theorem_cap.md)
download.page(data/acid.md)
download.page(data/base.md)

## DISTRIBUTED DATABASE SAMPLES

- https://db-engines.com/en/ranking_trend

MongoDB: popular, powerful language, easy to integrate
Cassandra: ~sql language as constraints, good for elasticity, response time
Redis: Real time cache, simple
ElasticSearch: large volume of documents. To do real time visualisation and textual search


