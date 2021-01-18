# Cassandra

Column Store
Developed by Facebook
~sql language as constraints, good for elasticity, response time
includes a lot of features aimed at reliability and fault tolerance.
The goal behind Cassandra was to create a DBMS that has no single point of failure and provides maximum availability.
Inspired by Google’s BigTable, which is a column store database, and Amazon’s DynamoDB, which is a key-value database.
by providing a key-value system, but the keys in Cassandra point to a set of column families, with reliance on Google’s BigTable distributed file system and Dynamo’s availability features (distributed hash table).

designed to store huge amounts of data distributed across different nodes. Cassandra is a DBMS designed to handle massive amounts of data, spread out across many servers, while providing a highly available service with no single point of failure, which is essential for a big service like Facebook.
