### ACID (DataBases)

Atomic Coherent Isolation Durable

The 4 ACID properties garantee a transaction execution reliability
Transaction: operations modifying data
* Atomic
Operations sequence is not divisible: one (or system) fails, all rollback. Change all or nothing
* Consistency (coherent)
Transaction will respect data integrity constrainst: debit if credit
* Isolated
optimist transaction: rollback if r/w order interference
pessimist transaction: locked resources to avoid r/w interference. Perf ↓
* Durable
Succedded transactions are not lost by system faiure. They are permanent.   
Simple disk write is unsufficient: The DBMS must write in logs the changes made.


**Distributed context**
ACID is not possible in distributed context (nosql)
A 5 operations transaction require synchronization between 5 servers = latence (in distributed! that want speed)
Distribution = replication = duplicates synchronization !


