## TIERED ARCHITECTURE

Divided the software into tiers based on client server communication principle. Architecture can have one, two of n-tiered system separating the responsibilities among data provider and the consumer.
It utilises Request Response pattern for communication among the defined tiers. 
Offers scalability which can either be horizontal (scaling the network with high performance nodes) or vertical (scaling each node by increasing individual performance )

***Single Tiered System***
In this approach, single system is responsible to work as client as well as server and can offer ease of deployment eliminating the need of inter system communications (ISC). Hence, offers great communication speed.
Such system are suitable only for small scale single user application and should not be used for multi user complex applications.

***2-Tiered Architecture***
![](assets/books/api/assets/2-tiered-architecture.png)

Such system consist of two physical machines as server as well as client. It provides isolation among the data management operations and data processing and representation operations.
Client holds Presentation, Business Logic and Data link layer.
Server holds the Data stores such as Databases

***3-Tiered Architecture***

![](assets/books/api/assets/3-tiered-architecture.png)
Such architectures are highly scalable both horizontally and vertically. Implementing n-tiered architecture is generally costlier but offer high performance. Hence it is preferred in large complex software solutions.
It can be combined with advanced service oriented architectural style to generate highly sophisticated model. It is recommended to use this architecture when the software is complex and requires performance as well as scaling as it can be a costlier approach in terms of resources as well as time.