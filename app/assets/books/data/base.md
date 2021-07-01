### BASE

As ACID is not possible in distributed context (NoSQL)

* Basically Available
Whatever the database load (data/queries), the system guarantees a data availability rate

* Soft-state
Database can change during updates or when adding/removing servers. 
The NoSQL database doesn't have to be consistent at all times

* Eventually consistent
Ultimately, the base will reach a consistent state

NoSQL database relaxes unsupportable acid constraints: replicas synchronization and  promote efficiency. 
Transactions managed hell => Eventually consistent