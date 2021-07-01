# REST - REpresentational State Transfer

web services architectural design way presented by Roy Fielding in 2000 in his [dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf)

Underlying protocol: REST uses HTTP/HTTPS
Stateless
Response can be cached (GET requests)
No limits and contracts, light weight comparing to SOAP.
REST is easier than SOAP

## RESTful APi

A RESTful API is an API that satisfies the REST constraints.
Provide Web resources in a textual representation and allow them to be read and modified with a stateless protocol and a predefined set of operations:

HTTP is the Common protocol for these requests and responses. It provides operations (HTTP methods) GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS, TRACE

Web service APIs that adhere to the REST architectural constraints are called RESTful APIs. HTTP-based RESTful APIs are defined with the following aspects:
- a base URI, such as http://api.example.com/;
- standard HTTP methods (e.g., GET, POST, PUT, and DELETE);
- a media type that defines state transition data elements (e.g., Atom, microformats, application/vnd.collection+json). 

A Web service that follows this standard is called 'RESTful'
Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON...

Using a stateless protocol and standard operations, RESTful systems aim for fast performance, reliability, and the ability to grow by reusing components that can be managed and updated without affecting the system as a whole, even while it is running.

## Constraints

- Client-server
    Separate client application and server application, It’s about separation of concerns, by doing this we improve portability and scalability because it allows those components to evolve independently.

- Stateless
    Each request from a client to server must contain all necessary information, including authentication details, the server cannot store anything about requests, sessions, history, etc.

- Cache
    When possible responses data have to be cacheable, clients have the right to reuse responses data later. This will improve efficiency and scalability, the trade-off, however, is that it can decrease reliability if the cached data differs significantly from the data in the server.

- Uniform interface
    Define the standards of the API interface and follow it, for example, identification of resources and response messages. If it was decided to pluralize resources name on URI, follow this standard in all URIs, it will improve the readability and maintainability.

- Layered system
    The system has to be composed of components in hierarchical layers, each component is only aware of the immediate layer with which they are interacting. For example, a system can have a data layer, cache layer, security layer, etc. And all those layers should not affect the communication between the server and client.

- Code-on-demand
    This is the only optional constraint, the server will provide static representations of resources, but when requested it can send executable code.

## Http verbs/methods 

indicate operations on resources

|HTTP VERBS|||
|---|---|---|
| GET    | Read resources | ​/api​/v2​/articles |
| GET    | | ​/api​/v2​/articles​/{id} |
| GET    | | ​/api​/v2​/articles​/launch​/{id}|
| POST   | Create resources | ​/api​/v2​/articles |
| PUT    | Update or replace resources | ​/api​/v2​/articles​/{id} |
| PATCH  | Modify resources | ​/api​/v2​/articles​/{id} |
| DELETE | Delete resource | ​/api​/v2​/articles​/{id} |
| OPTIONS| |  |

/** Get artists **/
GET api.example.com/artists

/** Get a particular artist **/
GET api.example.com/artists/{id}

/** Create a track **/
POST api.example.com/artists/{id}/albums/{id}/tracks

/** Update an album **/
PUT api.example.com/artists/{id}/albums/{id}

/** Delete a track **/
DELETE api.example.com/artists/{id}/albums/{id}/tracks/{id}

## HTTP STATUS CODES
<div>
<div>100 <br\> <span>In progress</span></div> 		
<div>200 <br\> <span>OK</span></div> 		
<div>201 <br\> <span>Created</span></div> 		
<div>204 <br\> <span>No Content</span></div> 		
<div>300 <br\> <span>Redirect</span></div> 		
<div>400 <br\> <span>Client Error. Bad Request</span></div> 		
<div>401 <br\> <span>Unhautorized</span></div> 		
<div>403 <br\> <span>Forbidden</span></div> 		
<div>404 <br\> <span>Not Found</span></div> 		
<div>405 <br\> <span>Not Allowed</span></div> 		
<div>500 <br\> <span>Server Internal Error</span></div> 		
</div>
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


## Best practices to design an API

to improve readability
    Use hyphens ( - ) instead of underscores ( _ )
    Use only lowercase letters
    Don’t use file extensions

Singular routes     /profile

Pluralize resources
    Plural routes       /posts   /posts/1
    api.example.com/albums      /** Do **/
    api.example.com/album       /** Don't **/

Use nouns to represent resource, not actions
    api.example.com/artists         /** Do **/
    api.example.com/get-artists     /** Don't **/

hierarchical relationship between resources (strategy to improves comprehension)
    api.example.com/artists/{id}/albums
    api.example.com/artists/{id}/albums/{id}/tracks   artists have a collection of albums that have a collection of tracks. This is not required,
    api.example.com/albums
    api.example.com/albums/{id}/tracks

Filter
- /posts?id=1&id=2
- /comments?author.name=typicode

Paginate
    GET /posts?_page=7
    GET /posts?_page=7&_limit=20

Sort + _sort, _order
GET /posts?_sort=views&_order=asc
GET /posts/1/comments?_sort=votes&_order=asc
GET /posts?_sort=user,views&_order=desc,asc

Slice + _start and _end, _limit
GET /posts?_start=20&_end=30
GET /posts/1/comments?_start=20&_end=30
GET /posts/1/comments?_start=20&_limit=10


Operators
Add _gte or _lte for getting a range

GET /posts?views_gte=10&views_lte=20
Add _ne to exclude a value

GET /posts?id_ne=1
Add _like to filter (RegExp supported)

GET /posts?title_like=server
Full-text search
Add q

GET /posts?q=internet


## More

- https://dev.to/ricardo93borges/some-practices-to-design-restful-apis-interfaces-5a5i