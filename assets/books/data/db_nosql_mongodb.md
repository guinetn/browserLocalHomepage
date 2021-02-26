# MongoDB (c++)

http://www.mongodb.org/

C++
NoSQL database (Document-oriented)
Document Store (json): stores values (referred to as documents) in the form of encoded data. The choice of encoded format in MongoDB is JSON. This is powerful, because even if the data is nested inside JSON documents, it will still be queryable and indexable.
Popular, powerful language, easy to integrate
Schemaless (schema-free documents can have different structure) = no structure required
Fewer data relations
Great database which I love and is the main inspiration behind RaptorDB, although I have issues with its 32bit 4Gb database size limit and the memory map file design which could potentially corrupt easily. (Polymorphism has a workaround in mongodb if anyone wants to know).
flexible schema storage, which means stored objects are not necessarily required to have the same structure or fields. MongoDB also has some optimization features, which distributes the data collections across, resulting in overall performance improvement and a more balanced system.

• Nested/Embedded Document
• References

MongoDB Compass
    GUI for MongoDB
    To make smarter decisions about document structure, querying, indexing, document validation...

MongoDB Atlas (free)
    https://docs.atlas.mongodb.com/driver-connection/#node-js-driver-example

    https://cloud.mongodb.com/v2/5a62f...#clusters/security/users
    Security tab → Edit user → check "R/W to any db"
                 → "IP Whitelist" → Add you current ip address   
    !!! Overview tab → Connect → your app → Choose connector method (java, python, ruby, node)
    mongodb+srv://anet:<PASSWORD>@mycluster-bidxb.mongodb.net/test?retryWrites=true

https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4474601-decouvrez-le-fonctionnement-de-mongodb

### Distributed mongo db

Cluster: servers physical architecture distribution 
- Request Routers: mongos
- configuration servers: Config Server
- Data servers: Shard

Min archi: 2 mongos, 3 Config Serversn, 2 shards

- https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4474616-distribuez-vos-donnees-avec-mongodb

### Sample

https://dev.to/rahulku48837211/set-up-mongodb-with-node-js-503a
https://dev.to/rahulku48837211/connect-mongodb-atlas-and-upload-data-4kd9

$ curl https://s3-eu-west-1.amazonaws.com/course.oc-static.com/courses/4462426/tour-Pedia_paris.json.zip    
$ mongoimport --db tourPedia --collection paris tourPedia_paris.json
$ db.paris.find({"services":"blanchisserie", "category":"accommodation"})
$ db.paris.find({"category" : "accommodation"}, {"location.address":1})
$ db.paris.find({"reviews" : {$elemMatch : {"language":"en", "rating" : {$gt : 3}}}})
$ db.paris.aggregate( [ {$group : {_id:"$category", "tot":{$sum:1}} } ] ) ;
$db.paris.aggregate ([
    {$match :  {"category" : "accommodation"} },
    {$unwind : "$services" },
    {$group : {_id:"$services", "tot":{$sum:1}} }
])

- https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/6734731-entrainez-vous-a-creer-et-a-interroger-une-base-de-donnees-mongodb

### Connect to mongodb
    npm i -S mongodb
	see node_modules\mongodb\README.md  for all explanations

    database.js
        const mongodb = require('mongodb');
        const MongoClient = mongodb.MongoClient;
        let _db;
        const mongoConnect = callback => {
            MongoClient.connect('mongodb+srv://max:9u...be@cluster0-ntrwp.mongodb.net/shop?retryWrites=true')

        mongodb+srv://<user>:<pwd>@mycluster.bidxb.mongodb.net/<dbname>?retryWrites=true&w=majority
        mongodb://root:p123@171.114.12.23:27017/databasename

	.NetCore: MongoDB.Driver

	  "MongoConnection": {
	    //"ConnectionString": "mongodb://admin:abc123!@localhost",
	    "ConnectionString": "mongodb://localhost:27017",
	    "Database": "NotesDb"
	  },


	https://www.w3schools.com/python/python_mongodb_create_db.asp
    import pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    myquery = { "address": "Park Lane 38" }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    

# MongoDB - Mongo DataBase

http://www.mongodb.org/
https://www.sitepoint.com/a-guide-to-serverless-deployment-with-express-and-mongodb/


download.page(data/orm/mongoose.md)

## NoSQL - MongoDB (Document database)

	    Schemaless (documents can have different structure) = no structure required
	    Fewer data relations
	    Document are json
	    
	    • Nested/Embedded Document
	    • References

	    MongoDB Compass
	         GUI for MongoDB, MongoDB Compass allows you to make smarter decisions about document structure, querying, indexing, document validation, and more. 

	    MongoDB Atlas (free)
	    https://docs.atlas.mongodb.com/driver-connection/#node-js-driver-example

	    https://cloud.mongodb.com/v2/5a62f...#clusters/security/users
	    Security tab → Edit user → check "R/W to any db"
	                 → "IP Whitelist" → Add you current ip address   
	    !!! Overview tab → Connect → your app → Choose connector method (java, python, ruby, node)
	    mongodb+srv://anet:<PASSWORD>@mycluster-bidxb.mongodb.net/test?retryWrites=true
	    
	    Connect to mongodb
	    npm i -S mongodb

	    database.js
	        const mongodb = require('mongodb');
	        const MongoClient = mongodb.MongoClient;

	        let _db;

	        const mongoConnect = callback => {
	            MongoClient.connect('mongodb+srv://max:9u...be@cluster0-ntrwp.mongodb.net/shop?retryWrites=true')




	mongodb+srv://<user>:<pwd>@mycluster.bidxb.mongodb.net/<dbname>?retryWrites=true&w=majority
	mongodb://root:p123@171.114.12.23:27017/databasename

	JS: npm i mongodb
		see node_modules\mongodb\README.md  for all explanations

	.NetCore: MongoDB.Driver

	  "MongoConnection": {
	    //"ConnectionString": "mongodb://admin:abc123!@localhost",
	    "ConnectionString": "mongodb://localhost:27017",
	    "Database": "NotesDb"
	  },


	https://www.w3schools.com/python/python_mongodb_create_db.asp
		import pymongo

		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["mydatabase"]
		mycol = mydb["customers"]

		myquery = { "address": "Park Lane 38" }
		mydoc = mycol.find(myquery)
		for x in mydoc:
		  print(x)

	https://github.com/tstringer/MongoDB-by-Example
	https://flaviocopes.com/mongodb

	http://mongodb.org
	https://docs.mongodb.org/getting-started/node/
	https://hackhands.com/how-to-get-started-on-the-mean-stack/
	
	https://university.mongodb.com    MONGODB FOR....training
	http://sanderrossel.com/a-first-look-at-nosql-and-mongodb-in-particular/
	https://medium.freecodecamp.org/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca
	https://www.toptal.com/database/the-definitive-guide-to-nosql-databases


	Open Source (Licence AGPL V3.0)	
	Written in C++ from 2007 by society 1Ogen

	free open source document database that stores JSON-like objects. You can store and retrieve these objects and map them to objects in your application. It also has the usual querying and aggregation capabilities. MongoDB is a good candidate for applications where data consistency is not a primary concern.

	
	
 	* Schemaless 
 		you don’t need to pre-define a structure for the data before storing it, object can have differnet structure
 		adding any field becomes a breeze
 		store any object without having to worry about the particular fields that compose this object and how to store them. 
 		You simply tell MongoDB to store that object.
 		Data is stored in a format similar to JSON, but enhanced to allow storing more than just basic data types.
	
	Document-oriented NoSQL database (do not use the SQL language for querying the data)
	Document Storage format
		No usual rows/cols used in relational database management		
		Data is stored in the form of JSON-style documents called BSON, a binary style of JSON-style documents
 	Scales well
	Auto-sharding feature in order to scale horizontally
	Replication and high availability.
	Rich queries
	JavaScript as a query language
	Index on any field.




	Architecture: Database, Collection, Document
		built on collections and documents

		MongoDB is organized in document format compared to RDBMS.
		RDBMS		MongoDB
		_____________________
		Database	Database 		A database is a container of your collections. A single MongoDB server typically has multiple databases.
		Table		Collection 		A collection is basically a group of documents. It is similar to a table in an RDBMS.
									It stores the data in the collection, which is simply a group of documents.
		Row			Document 		The document is basically a set of key-value pairs. In one document, you can have a different kind of data.
									Databases and collections of objects (called documents)
									You can insert the same field with a different data type.
									Document sample:
										{
										_id:"12...6",
										name:"shubham agrawal",
										email:"shubham@gmail.com",
										courses:{
											course_name:"scala",
											fees:"5000",
											duration:"3"
										}
										}
		Colum		Field
		
		
	PRIMARY KEY

			In RDBMS: PK is used to uniquely identify the data and we explicitly set the column as the primary key.
					  No limitation — any column can be part of the primary key.
			In MongoDB
				_id field is reserved for the primary key
				When we insert the data without the field _id, MongoDB sets the value of it as the unique number by itself to uniquely identify the data.
				If you want to set the primary key for your document, then you need to set the value of the field _id as the primary key. So, basically.

## MongoDB shell		

	At start, Mongo creates a 'test' database
	>db							tell you active database
	>use newname				change the database (database instantly created and the shell switches it)
	>show databases 			list the available databases (not listed if no collection yet in)
	
	Requests with json

	>db.createCollection() 	 	add collection (~table) on the current database
								db.createCollection('cars') { "model": "fiat"}
	
	>db.dogs.insert({ name: 'Roger' })
	>show collections 			list the collection
	>db.dogs.insert({ name: 'Buck' })
	db.dogs.insert({ name: 'Togo' })
	db.dogs.insert({ name: 'Balto' })
	
	>db.dogs.find()
				\__ returns a cursor you need to iterate on
	>db.dogs.findOne()
	>db.dogs.find({name: 'Roger'})
		{ 
			"name": 'Roger',
			"_id": ObjectId("5cabf15e3b26410")
		}      \________ additional _id property automatically generated and added for us by MongoDB 
	
	>db.dogs.update({name: 'Roger'}, {name: 'Tom'})
	
	>db.dogs.remove({name: 'Roger'})
	>db.dogs.remove()  			 remove all the entries from a collection (pass an empty object)



# MongoDB Atlas

The Easiest Way to Deploy, Operate, and Scale MongoDB in the Cloud. Start Free!
https://cloud.mongodb.com/v2/5a62fc643b34b97afd993a31#clusters/detail/palmcluster



MongoDB (CP Constitency/Partition Tolerance, see CAP theorem)
	NoSql Db storing data in one or more Primary node in the form of json files
	Each Primary node has multiple replicas sets that update themselves asynchronously using the operation 
	log file of their respective primary node. The replica sets nodes send a heartbeat (ping) to every other nodes to keeps track if other replicas/primary are alive or dead. No heartbeat 10 sec = marked inaccessible

	If a primary node is inaccessible then one of the secondary nodes is elected as new primary but this
	takes time while the system is unavailable for write queries: Mongo compromise Availability during a partition and behave as Consistency.

MongoDB (c++)
Document Store	
Great database which I love and is the main inspiration behind RaptorDB, although I have issues with its 32bit 4Gb database size limit and the memory map file design which could potentially corrupt easily. (Polymorphism has a workaround in mongodb if anyone wants to know).
flexible schema storage, which means stored objects are not necessarily required to have the same structure or fields. MongoDB also has some optimization features, which distributes the data collections across, resulting in overall performance improvement and a more balanced system.

- Flexibility of Schema
schema-free, document-oriented database written in C++. The database is document store based, which means it stores values (referred to as documents) in the form of encoded data.
# The choice of encoded format in MongoDB is JSON. This is powerful, because even if the data is nested inside JSON documents, it will still be queryable and indexable.

One of the best things about MongoDB is that there are no restrictions on schema design. You can just drop a couple of documents within a collection and it isn’t necessary to have any relations between those documents. The only restriction with this is supported data structures.
But due to the absence of joins and transactions (which we will discuss later), you need to frequently optimize your schema based on how the application will be accessing the data.
MongoDB creates schemaless documents which can store any information you want though it may cause problems with data consistency

VS MySQL
Before you can store anything in MySQL, you need to clearly define tables and columns, and every row in the table should have the same column.
And because of this, there isn’t much space for flexibility in the manner of storing data if you follow normalization.


### KEY FEATURES AVAILABLE IN MONGODB
Shards
partitioning and distributing of data across multiple machines (nodes). A shard is a collection of MongoDB nodes, in contrast to Cassandra where nodes are symmetrically distributed. Using shards also means the ability to horizontally scale across multiple nodes.

. Querying Language: Mongo Query Language	
MongoDB uses a RESTful API. To retrieve certain documents from a db collection, a query document is created containing the fields that the desired documents should match.

MongoDB uses an unstructured query language. To build a query in JSON documents, you need to specify a document with properties you wish the results to match.
It is typically executed using a very rich set of operators that are linked to each other using JSON. MongoDB treats each property as having an implicit boolean AND. It natively supports boolean OR queries, but you must use a special operator ($or) to achieve it.


No Relationships in MongoDB
MongoDB doesn’t support JOIN — at least, it has no equivalent. On the contrary, it supports multi-dimensional data types such as arrays and even other documents. The placement of one document inside another is known as embedding.

Performance and Speed
ability to handle large unstructured data. It is magically faster because it allows users to query in a different manner that is more sensitive to workload.

Security Model
MongoDB uses a role-based access control with a flexible set of privileges. Its security features include authentication, auditing, and authorization.
Moreover, it is also possible to use Transport Layer Security (TLS) and Secure Sockets Layer (SSL) for encryption purposes. This ensures that it is only accessible and readable by the intended client.


Actions
a group of servers called routers. Each one acts as a server for one or more clients. Similarly, The cluster contains a group of servers called configuration servers. Each one holds a copy of the metadata indicating which shard contains what data. Read or write actions are sent from the clients to one of the router servers in the cluster, and are automatically routed by that server to the appropriate shards that contain the data with the help of the configuration servers.



	an open source database that uses a document-oriented data model.
	MongoDB is one of several database types to arise in the mid-2000s under the NoSQL banner.
	xxInstead of using tables and rows as in relational databases, MongoDB is built on an architecture of collections and documents.

	Users: Disney, MTV, Doodle, CERN
	MongoDB allows Foursquare to seamlessly process and store all user check-ins, with hundreds of thousands of input/output operations per second.

	Drivers: C, C++, C#, PHP, Python, Java
	Server: demon (windows service)
	Client: interface terminal
					  gui: MongoHub, php-MoAdmin
	Request: idem js, return json

	Install
		http://www.mongodb.org/downloads
		C:\Program Files\MongoDB\Server\4.2\bin
		C:\Program Files\MongoDB\Server\4.2\data\
		C:\Program Files\MongoDB\Server\4.2\log

		Logs 		/usr/local/var/log/mongodb/mongo.log 
		Database 	/usr/local/var/mongodb

		Set up the MongoDB environment
		MongoDB requires a data directory to store all data. MongoDB’s default data directory path is \data\db: 	'md data\db'
		or alternate path: C:\mongodb\bin\mongod.exe --dbpath "d:\test\mongo db data"

		Start MongoDB		C:\Program Files\MongoDB\Server\3.0\bin\mongod.exe
		Connect to MongoDB  C:\Program Files\MongoDB\Server\3.0\bin\mongo.exe
		Import Example Dataset
			https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/dataset.json 
			
			resto_collection.json
				{
				  "address": {
				     "building": "1007",
				     "coord": [ -73.856077, 40.848447 ],
				     "street": "Morris Park Ave",
				     "zipcode": "10462"
				  },
				  "borough": "Bronx",
				  "cuisine": "Bakery",
				  "grades": [
				     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
				     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
				     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
				     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
				     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
				  ],
				  "name": "Morris Park Bake Shop",
				  "restaurant_id": "30075445"
				}

				have a running mongod instance/service in order to import data into the database.
				Add "C:\Program Files\MongoDB\Server\3.0\bin" to your path
				C:\Dev\Mean\data\db\mongoimport --db test --collection restaurants --drop --file resto_collection.json

				PS H:\assets\Si\45-data\db\DB-NoSQL\MongoDB\Docker_mongo_test> mongoimport.exe --db test --collection restaurants --drop --file resto_collection.json
				2019-11-17T08:57:09.452+0100    connected to: mongodb://localhost/
				2019-11-17T08:57:09.691+0100    dropping: test.restaurants
				2019-11-17T08:57:09.754+0100    1 document(s) imported successfully. 0 document(s) failed to import.
				> db
				test
				> use test
				switched to db test
				> show databases
				admin   0.000GB
				config  0.000GB
				local   0.000GB
				test    0.000GB
				> show collections
				restaurants
				> db.restaurants.find()
				> db.restaurants.find(1) // error
		

		running as a Windows service
		https://hackhands.com/how-to-get-started-on-the-mean-stack/
		C:\>mkdir C:\mongodb\log
		$ echo logpath=C:\mongodb\log\mongo.log > C:\mongodb\mongod.cfg
		$ sc.exe create MongoDB binPath= "\"C:\mongodb\bin\mongod.exe\" --service --config= \"C:\mongodb\mongod.cfg\"" DisplayName= "MongoDB 2.6" start= "auto"
		$ net start MongoDB

		Insert Data
			https://docs.mongodb.org/getting-started/node/insert/		

	NodeJs
	 	Install the MongoDB driver 	'npm install mongodb -g'
	 	if python version issue with gyp: 
	 		if multiple versions of Python installed, then you can set npm´s 'python' config key to the appropriate value:
	 		npm config set python C:\Python27

	Commandes
		db.nomCollection.nomFonction()

	Examples
		db.Voitures.find()
		db.Users.find( {genre: "F", {name:1, surname:1} } )   // select name, surname from users where genre = 'F'
										   |___ Attribut to display (1) or not (0)

		Joins
			user_tmp = db.Users.findOne( { name: "John", surname:"Travers" })
			car = db.Voitures.find( { owner: user_tmp.id })



MongoDB (from "humongous") is an open-source document database, and the leading NoSQL database. Written in C++, MongoDB features:



• DOCUMENT-ORIENTED STORAGE
JSON-style documents with dynamic schemas offer simplicity and power.

• FULL INDEX SUPPORT
Index on any attribute, just like you are used to.

• REPLICATION & HIGH AVAILABILITY
Mirror across LANs and WANs for scale and peace of mind.

• AUTO-SHARDING
Scale horizontally without compromising functionality.

• QUERYING
Rich, document-based queries.

• FAST IN-PLACE UPDATES
Atomic modifiers for contention-free performance.

• MAP/REDUCE
Flexible aggregation and data processing.

• GRIDFS
Store files of any size without complicating your stack.

• PROFESSIONAL SUPPORT BY MONGODB
Enterprise class support, training, and consulting available.


MongoDB is recognized as the leading NoSQL database it delivers faster time to market, higher developer productivity, and better developer experience. Its features include a JSON data model with dynamic schemas, extensive driver support, auto-sharding, built-in replication and high availability, full and flexible index support, rich queries, aggregation, in-place updates and GridFS for large file storage.



## MONGOOSE

	http://mongoosejs.com/
	https://scotch.io/tutorials/using-mongoosejs-in-node-js-and-mongodb-applications

	elegant mongodb object modeling for node.js
	Mongoose adds a schema to your MongoDB objects

Mongoose which primarily enforces a Schema, basic type checks and validation to our documents before saving them to Mongo. It acts as a middleman between Mongo and Node.

	npm install mongoose

	var mongoose = require('mongoose');
	mongoose.connect('mongodb://localhost/test');

	var Cat = mongoose.model('Cat', { name: String });

	var kitty = new Cat({ name: 'Zildjian' });
	kitty.save(function (err) {
	  if (err) // ...
	  console.log('meow');
	});

	

### MONGOVUE  
	http://www.mongovue.com


### NODE & MONGODB		
see H:\assets\Si\45-data\db\DB-NoSQL\MongoDB\Docker_mongo_test\restaurants\node_modules\mongodb  readme.md !!! to read

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// Connection URL
const url = 'mongodb://localhost:27017';

// Database Name
const dbName = 'myproject';

// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  client.close();
});


## Install the MongoDB driver 	'npm install mongodb'

	var app = require('express')();
	var MongoClient = require('mongodb').MongoClient;
	     
	var urlWithCreds = 'mongodb://user:password@localhost:27017/local';
	var url = 'mongodb://localhost:27017/local';
	MongoClient.connect(url, function (err, db) {
	    if (err) {
	        console.log(err);
	    } else {
	        console.log('Connected to the database.');

	        var artist = {
            	name: 'Massive Attack',
            	countryCode: 'GB'
	        };
	        var collection = db.collection('artists');
	        collection.insertOne(artist);
	        console.log(artist._id);
	        db.close();
	    }
	});
	var server = app.listen(80, '127.0.0.1');

	use the MongoClient to connect to the database using the connect function, which takes a URI and a callback function.
 	use the Db object to do all kinds of stuff like creating and dropping databases, collections and indices and do our CRUD operations 

 	 use the db parameter to get a collection (the MongoDB variant of a database table) using the collection function. 
 	 If the collection does not exist it will create one automatically. 
 	 We can then simply insert an object using the insertOne function of the collection. 
 	 Now something funny has happened. After calling insertOne our artist object suddenly has an _id property. 
 	 MongoDB uses this _id to uniquely identify objects.	

 	 INSERT MANY

			collection is a group of documents (a document = a set of key-value pairs)
			
 	 		collection.insertMany([
			{
			    name: 'The Beatles',
			    countryCode: 'GB',
			    members: [
			        'John Lennon',
			        'Paul McCartney',
			        'George Harrison',
			        'Ringo Starr'
			    ]
			},
			{
			    name: 'Justin Bieber',
			    countryCode: 'No one wants him'
			},
			{
			    name: 'Metallica',
			    countryCode: 'USA'
			},
			{
			    name: 'Lady Gaga',
			    countryCode: 'USA'
			}
			], function (err, result) {
			    if (err) {
			        console.log(err);
			    } else {
			        console.log(result);
			    }
			});

 	 FIND

		 	 MongoClient.connect(url, function (err, db) {
				    if (err) {
				        console.log(err);
				    } else {
				        var collection = db.collection('artists');
				        collection.findOne({ name: 'Massive Attack' }, function (err, artist) {
				            if (err) {
				                console.log(err);
				            } else {
				                console.log(artist);
				            }
				            db.close();
				        });
				    }
				});



		 	 var findCallback = function (err, artists) {
			    if (err) {
			        console.log(err);
			    } else {
			        console.log('\n\nFound artists:');
			        artists.forEach(function (a) {
			            console.log(a);
			        });
			    }
			};

			// All documents.
			collection.find().toArray(findCallback);

			// Name not equal to Justin Bieber.
			collection.find({ name: { $ne: 'Justin Bieber' } }).toArray(findCallback);

			// Name equal to Massive Attach or name equal to The Beatles.
			collection.find({ $or: [{ name: 'Massive Attack' }, { name: 'The Beatles' }] }).toArray(findCallback);

			// Members contains John Lennon.
			collection.find({ members: 'John Lennon' }).toArray(findCallback);

## UPDATE


	 Update a record:  findOneAndUpdate, updateOne, updateMany

			collection.findOneAndUpdate({ name: 'Massive Attack' },
			    { $set: {
			        cds: [
			            {
			                title: 'Collected',
			                year: 2006,
			                label: {
			                    name: 'Virgin'
			                },
			                comment: 'Best Of'
			            },
			            {
			                title: 'Mezzanine',
			                year: 1998,
			                label: 'Virgin'
			            },
			            {
			                title: 'No Protection: Massive Attack v Mad Professor',
			                year: 1995,
			                label: 'Circa Records',
			                comment: 'Remixes'
			            },
			            {
			                title: 'Protection',
			                year: 1994,
			                label: {
			                    name: 'Circa'
			                }
			            }
			        ]
			        }
			    }, function (err, result) {
			    console.log('\n\nUpdated artist:');
			    if (err) {
			        console.log(err);
			    } else {
			        console.log(result);
			    }
			});

### DELETE: findOneAndDelete, deleteOne, deleteMany

		collection.findOneAndDelete({ name: 'Justin Bieber' }, function (err, result) {
		    console.log('\n\nDeleted artist:');
		    if (err) {
		        console.log(err);
		    } else {
		        console.log(result);
		    }
		});




LOCAL
C:\Program Files\MongoDB\Server\3.2\README


### COMPONENTS

  bin/mongod - The database process.
  bin/mongos - Sharding controller.
  bin/mongo  - The database shell (uses interactive javascript).

### UTILITIES

  bin/mongodump         - MongoDB dump tool - for backups, snapshots, etc..
  bin/mongorestore      - MongoDB restore a dump
  bin/mongoexport       - Export a single collection to test (JSON, CSV)
  bin/mongoimport       - Import from JSON or CSV
  bin/mongofiles        - Utility for putting and getting files from MongoDB GridFS
  bin/mongostat         - Show performance statistics

### RUNNING

  For command line options invoke:

    $ ./mongod --help

  To run a single server database:

    $ mkdir /data/db
    $ ./mongod
    $
    $ # The mongo javascript shell connects to localhost and test database by default:
    $ ./mongo 
    > help


32 BIT BUILD NOTES

  MongoDB uses memory mapped files.  If built as a 32 bit executable, you will
  not be able to work with large (multi-gigabyte) databases.  However, 32 bit
  builds work fine with small development databases.



## More

- https://devopsmyway.com/install-mongodb-on-ec2/
