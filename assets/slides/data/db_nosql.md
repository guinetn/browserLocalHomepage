# NoSQL - Not Only SQL

A new way to store and request data

Relational database cannot manage big data: Volume, Velocity, Variety
NoSql relaxes some ACID constrainsts of RDBMS to allow data distribution
Response to the scale and agility challenges that face modern applications. 
Wide database technologies
More data is being collected and more users are accessing this data concurrently: the way web applications deal with data has changed significantly. Scalability and performance are more of a challenge than ever for relational databases that are schema-based and therefore can be harder to scale.

## NoSQL Families

### KEY-VALUE 
Hash table on the network
Simple, efficient
Key 	→ Hash function → index
Value	→ anyhing
No language possible → CRUD only: 
- Create (key,value)
- Read (key)
- Update (key,value)
- Delete (key) 

**Applications**
Realtime fraud detection
IoT
E-commerce
Cache
Fast transactions
Logs
Chat

**Who?**
- Redis (VMWare) : Vodafone, Trip Advisor, Nokia, Samsung, Docker
- Memcached (Danga) : LiveJournal, Wikipédia, Flickr, Wordpress
- Azure Cosmos DB (Microsoft) : Real Madrid, Orange tribes, MSN, LG, Schneider Electric
- SimpleDB (Amazon)

### COLUMNS ORIENTED
Attribut (column) focus: ignore others columns
**Applications**
Analytics
Aggregations
Not for found a single value
Counter (online voting)
Journalisation
Categorie search
Large reporting 

**Who?**
BigTable (Google)
HBase (Apache, Hadoop)
Spark SQL (Apache)
Elasticsearch (elastic) -> moteur de recherche

### DOCUMENTS

Handle documents containing information with a complex structure (types, lists, nestings). It is based on the key/value principle, but with an extension on the fields that make up this document
Structured approach to each value, thus forming a document
Rich query languages allowing complex manipulations on each attribute of the document (and sub-documents) like in relational but in a distributed fashion.

**Applications**
Content management (digital libraries, product collections, software repositories, multimedia collections, etc.)
Framework for storing objects
Collection of complex events
Management of user histories on social networks.

**Who?**
MongoDB (MongoDB) : ADP, Adobe, Bosch, Cisco, eBay, Electronic Arts, Expedia, Foursquare
CouchBase (Apache, Hadoop) : AOL, AT&T, Comcast, Disney, PayPal, Ryanair
DynamoDB (Amazon) : BMW, Dropcam, Duolingo, Supercell, Zynga
Cassandra (Facebook -> Apache) : NY Times, eBay, Sky, Pearson Education
Cassandra is "wide-column store" = document oriented

### GRAPH
Store nodes: links, attributs
Requests: distance, paths, recommandations

**Applications**
Social networks (recommendation, shortest path, cluster ...)
GIS networks (roads, electricity network, freight ...)
Social web (Linked Data).

**Who?**
Neo4j : eBay, Cisco, UBS, HP, TomTom, The National Geographic Society
OrientDB (Apache) : Comcast, Warner Music Group, Cisco, Sky, United Nations, VErisign
FlockDB (Twitter) : Twitter


https://www.toptal.com/database/the-definitive-guide-to-nosql-databases

* Elasticity
* Sharding

download.md(assets/slides/data/base.md)

## NoSQL candidates
 
|           |   Storage Type|	Query Method	Interface	Programming |Language	|Open |Source Replication|
|Cassandra	|	Column Store|	Thrift API		 |Thrift		|Java		           |Yes			|Async|
|MongoDB	|	Document Store|	Mongo Query		 |TCP/|IP		|C++		           |Yes			|Async|
|HyperTable	|	Column Store|	HQL				 |Thrift		|Java		           |Yes			|Async|
|CouchDB	|	Document Store|	MapReduce		 |REST			|Erlang		           |Yes			|Async|
|BigTable	|	Column Store|	MapReduce		 |TCP/|IP		|C++		           |No			|Async|
|HBase		|	Column Store|	MapReduce		 |REST			|Java		           |Yes			|Async|

**NoSQL candidates selection**
criteria [0-5]
https://db-engines.com/en/ranking_trend

|Score|MongoDB|Cassandra|ElasticSearch|
|---|---|---|---|---|
|Cost|0.5|4|4|4|
|Consistency|1|4|2|2|
|Availability|0.5|2|4|3|
|Language|1|4|2|3|
|Functionalities|2|4|2|4|
|Total|5|19|12|16.5|

constitency + rich language → MongoDB
ElasticSearch good but bad for consistency

![](assets/slides/data/assets/nosql-store-decision-flow.png)

* 1970 	Relational model: SQL
	Not for high volumes (slow responses, heavy and complex data distribution)
	Ex: Sql Server
	+
		Rules for data coherence
		Locks for concurrents access
		ACID respect (Atomic Coherent Isolation Durable)
		Tools to modelise
	-
		Less performance when volume increase
		Data distribution of a base problems

* 2000	NoSQL - Not Only SQL
	For high volumes (Google, Facebook)
	Ex: MongoDB, Cassandra, CouchDB, DynamoDB
	NoSQL is a form of unstructured storage, NoSQL databases do not have a fixed table structure like the ones found in relational databases.

	First, there were proprietary (closed source) types of NoSQL databases: SQL scalability issue was recognized by Web 2.0 companies with huge, growing data and infrastructure needs, such as Google, Amazon, and Facebook
	https://cloud.google.com/bigtable/
    https://aws.amazon.com/dynamodb/

    Success of these proprietary systems initiated development of a number of similar open-source and proprietary database systems, the most popular ones being 
    Hypertable
    Cassandra   http://cassandra.apache.org/
    MongoDB
    DynamoDB
    HBase
    Redis

	+
		.Good response with high volumes			
		.Flexible when issue (partial/full availability)
		.Schema-free = simple and flexible structure
		.Based on key-value pairs. Usually, each value has a key.
		.Store types:column store, document store, key value store, graph store, object store, XML store and other data store modes.
		.Open-source NoSQL databases don’t require expensive licensing fees 
		.Easy to distribute
		.Expansion is easier and cheaper than when working with relational databases. This is because it’s done by horizontally scaling and distributing the load on all nodes, rather than the type of vertical scaling that is usually done with relational database systems, which is replacing the main host with a more powerful one.
	-	
	    .Dont support reliability features that are natively supported by relational database systems: Not full ACID, only Coherence, availability, split resistance. This also means that NoSQL databases, which don’t support those features, trade consistency for performance and scalability. To support reliability and consistency features, developers must implement their own proprietary code. This limit the number of applications that can rely on NoSQL databases for secure and reliable transactions, like banking systems.
		.No join. Client must do it: forms of complexity found in most NoSQL databases include incompatibility with SQL queries. This means that a manual or proprietary querying language is needed, adding even more time and complexity.
		.Locks are not always available for some bases




The NoSQL database movement came about to address the shortcomings of relational databases and the demands of modern 
software development. MongoDB is the leading NoSQL database 

The relational data model relies on rigid adherence to a database schema, normalization of data and joins to store 
data and perform complex queries. But changes in application, user and infrastructure characteristics have led 
application developers and architects to seek alternative distributed document database technologies like 

NoSQL (Not only SQL). As a result, relational database developers accustomed to relational data modeling must 
approach their development in new ways.

Navigating the Transition From Relational to NoSQL Technology looks at the differences between relational and 
document database technology, highlights the implications of those differences for application developers, and 
provides guidance that can ease the transition from relational to NoSQL. Specifically you will learn:

•Relational versus document-oriented models
•Scaling model, data model and why you should transition
•Document Model Rules of Thumb
•The MVC model
•Using view collation to simplify queries.
•Concurrency, Scaling and performance issues

http://www.infoq.com/vendorcontent/show.action;jsessionid=B85B21FC3FC98657E9C6EDCA72E92FF0?vcr=1739





|Feature|      NoSQL Databases |			Relational Databases|
|---|---|---|
|Performance| 		High|						Low|
|Reliability| 		Poor|						Good|
|Availability| 		Good|						Good|
|Consistency| 		Poor|						Good|
|DataStorage| 		Optimized for huge data|		Medium sized to large|
|Scalability| 		High|						High (but more expensive)|



## NoSQL STOCKAGE MODELS (Data Store Types)


### KEY/VALUE MODEL

A hash table is used in which a unique key points to an item.
Data is stored in a form of a string, JSON, or BLOB (Binary Large OBject).

Keys can be organized into logical groups of keys, only requiring keys to be unique within their own group. This allows for identical keys in different logical groups
Some implementations provide caching mechanisms for enhancing performance

	id <---> Value (simple or object)
	Only 4 operations: CRUD
	DataSmart is at client level

biggest flaws in this form of database is the lack of consistency at the database level. This can be added by the developers with their own code

. Amazon’s DynamoDB


### DOCUMENTARY BASE MODEL (Document Store)

Document stores are similar to key value stores in that they are schema-less and based on a key-value model. 
Values (documents) provide encoding for the data stored. Those encodings can be XML, JSON, or BSON (Binary encoded JSON).
Querying based on data can be done.

. MongoDB

	Collection: group of documents
		|
		|
		| ______	each entry is a document (a group of fields + id added by the sgbd)
															|
															|_____ each field could be a document
     -------|	doc#1	{id:"1", name:"john", age:"22" }													
	|		|	doc#2	{id:"1", name:"john", age:"22", city:"London" }   <--- structure dont have to be identical				
	|
	 ------> could be in the same collection (no strict structure to respect) 


###	COLUMNS ORIENTED MODEL (Column Store)

data is stored in columns, as opposed to being stored in rows as is done in most relational database management systems.
A Column Store is comprised of one or more Column Families that logically group certain columns in the database. A key is used to identify and point to a number of columns in the database, with a keyspace attribute that defines the scope of this key. Each column contains tuples of names and values, ordered and comma separated.

Column Stores have fast read/write access to the data stored. In a column store, rows that correspond to a single column are stored as a single disk entry. This makes for faster access during read/write operations.

. Google’s BigTable
. HBase
. Cassandra

	Add data is easy
	null are limited

	relational model: data in rows 		1. guitar, flamenco
										2. piano, classic
										3. flute, irlandais	
	in a columns oriented model:
										1,2,3
										guitar, piano, flute
										flamenco, classic, irlandais	

### GRAPH MODEL (Graph Base)

	From the "Graph Theory"
	Data are nodes with a document structure (see above)
	Arcs oriented and named links the nodes

Typically used in social networking applications: allow developers to focus more on relations between objects rather than on the objects themselves. 

A graph base database uses edges and nodes to represent and store data. These nodes are organized by some relationships with one another, which is represented by edges between the nodes. Both the nodes and the relationships have some defined properties.

A graph structure (a set of objects connected by links) comprising edges ans nodes
The interconnected objects are represented by mathematical abstractions, called vertices, and the links that connect some pairs of vertices are called edges. A set of vertices and the edges that connect them is said to be a graph.

Point = sommet = vertex. (vertices if ++)

nodes are organized by some relationships with one another, which is represented by edges between the nodes. Both the nodes and the relationships have some defined properties.

.InfoGrid
.InfiniteGraph





## INDEXING STRUCTURES FOR NOSQL DATABASES

Indexing is the process of associating a key with the location of a corresponding data record in a DBMS. There are many indexing data structures used in NoSQL databases. 

### B-Tree Indexing

B-Tree is one of the most common index structures in DBMS’s.
In B-trees, internal nodes can have a variable number of child nodes within some predefined range.
One major difference from other tree structures, such as AVL, is that B-Tree allows nodes to have a variable number of child nodes, meaning less tree balancing but more wasted space.
The B+-Tree is one of the most popular variants of B-Trees. The B+-Tree is an improvement over B-Tree that requires all keys to reside in the leaves.

### T-Tree Indexing

The data structure of T-Trees was designed by combining features from AVL-Trees and B-Trees.
AVL-Trees are a type of self-balancing binary search trees, while B-Trees are unbalanced, and each node can have a different number of children.
In a T-Tree, the structure is very similar to the AVL-Tree and the B-Tree.
Each node stores more than one {key-value, pointer} tuple. Also, binary search is utilized in combination with the multiple-tuple nodes to produce better storage and performance.
A T-Tree has three types of nodes: A T-Node that has a right and left child, a leaf node with no children, and a half-leaf node with only one child.

It is believed that T-Trees have better overall performance than AVL-Trees.

### O2-Tree Indexing

The O2-Tree is basically an improvement over Red-Black trees, a form of a Binary-Search tree, in which the leaf nodes contain the {key value, pointer} tuples.
O2-Tree was proposed to enhance the performance of current indexing methods. An O2-Tree of order m (m ≥ 2), where m is the minimum degree of the tree, satisfies the following properties:
Every node is either red or black. The root is black.
Every leaf node is colored black and consists of a block or page that holds “key value, record-pointer” pairs.
If a node is red, then both its children are black.
For each internal node, all simple paths from the node to descendant leaf-nodes contain the same number of black nodes. Each internal node holds a single key value.
Leaf-nodes are blocks that have between ⌈m/2⌉ and m “key-value, record-pointer” pairs.
If a tree has a single node, then it must be a leaf, which is the root of the tree, and it can have between 1 to m key data items.
Leaf nodes are double-linked in forward and backward directions.

