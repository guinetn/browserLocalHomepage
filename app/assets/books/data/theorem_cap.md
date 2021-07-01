## CAP Theorem

2000, Eric A. Brewer

Fondamentals database properties (relationnal, NoSQL...)

How to scale?
- How to index quantities of documents?
- How to replicate data to ensure resistance to failure?

Distributed database system has to make a tradeoff between consistency and availability

* consistency
    latest data (fresh data)
* availability
    a search engine is expected to respond with guaranteed maximum latency, but not necessarily that results will update very quickly.
    Ex: logs (good when acceptable latency)

* ElasticSearch: availability over consistency (has a maximum guarented delay to respond even in a partitioned network)
* MongoDb: consistency over availability (ensures consistency but not availability of data)

Pick 2 out of these 3: only 2 of the 3 are possible at the same time: 
* CONSISTENCY - COHÉRENCE
All client has same view of data irrespective of delete or update .
A data has only one visible state whatever the number of replicas
All the nodes in the system see exactly the same data at the same time
User retrieves the same information no matter wich node he connect to
Important for: finance (accounts) 
* AVAILABILITY
Guarantee that all queries are answered.
Every user is able to get the data
Each client can always read and write.
Response of the system even if its a "unsuccessful" operation
Important when need to access a data at all times (whatsapp status when offline...)
As long as the system is running (distributed or not), the data must be available
* PARTITION TOLERANCE (DISTRIBUTION)
All system works well despite of physical network partitioned.
Regardless of the number of servers, any request must provide a correct result
No less important failure than a total cut-off of the network must prevent the system from responding correctly (or again: in the event of division into subnets, each must be able to operate independently).
Partition = communication break between nodes (network failure, server crash)
The system should still be able to work even if there is a partition meaning that if a node fails to communicate, then one of the replicas of the nodes should be able to retrieve the data

![cap_theorem](assets/books/data/assets/cap_theorem.png)    
![cap_theorem](assets/books/data/assets/cap_theorem_couples.jpg)    
![cap_theorem](assets/books/data/assets/cap-theorem-triangle.png)    

## Couples

* CA (Consistency-Availability)
Concurrents operations on the same data return the new version without delay.
SGBDR only

* CP (Consistency-Partition Tolerance)
Distribute data on servers being fault tolerant (replication). Data consistency, wich guarenteed the value returned despite concurrents update imply some latency because a replicas synchronisation protocol is needed.
NoSQL: MongoDB

* AP (Availability-Partition Tolerance)
Quick response time with distributed data (réplicas) = asynchronous network updates, data is  "Eventually Consistent"
Ex: Cassandra, fast but value not guarenteed in the context of many simultaneous updates