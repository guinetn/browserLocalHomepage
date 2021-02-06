# REST - REpresentational State Transfer

Underlying protocol: REST uses HTTP/HTTPS
Stateless
Response can be cached (GET requests)
No limits and contracts, light weight comparing to SOAP.
REST is easier than SOAP

## Http verbs

|HTTP VERBS||
|---|---|
| GET    | ​/api​/v2​/articles |
| GET    | ​/api​/v2​/articles​/{id} |
| GET    | ​/api​/v2​/articles​/launch​/{id}|
| POST   | ​/api​/v2​/articles |
| PUT    | ​/api​/v2​/articles​/{id} |
| PATCH  | ​/api​/v2​/articles​/{id} |
| DELETE | ​/api​/v2​/articles​/{id} |
| OPTIONS|  |



Singular routes     /profile
Plural routes       /posts   /posts/1
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