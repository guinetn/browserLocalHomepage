# ARCHITECTURE

Endpoints names =  name of your resources
    /dogs
Endpoints Plural: Consistency is the key 
    - GET /cat
    - GET /cat/:id
    + GET /cats
    + GET /cats/:id
Filter, sort, and pagination support    
    GET /cats?race=misumisu&age=1 -> Filtering, retrieve all the cats that have the following properties: race is misumisu and the age is 1.
    GET /cats?limit=15&offset=0 -> Pagination, return 15 rows starting with the 0 row.
    GET /cats?sort=descending 
Resource hierarchy
    GET /authors/betoyanes/articles/create_cat_memes
    GET /articles?author=betoyanes&name=create_cat_memes
Versioning: GET /v2/dogs
Caching (redis)
Documentation
    leaner to use a query string than expanding the current path. The more the application scales, we will surely have a greater hierarchy and in turn, the route will expand.
https://levelup.gitconnected.com/software-architecture-the-important-architectural-patterns-you-need-to-know-a1f5ea7e4e3d

::::
download.page(api/architecture/architecture_microservices.md)
::::
download.page(api/architecture/architecture_serverless.md)
::::
download.page(api/architecture/architecture_event_driven.md)
::::
download.page(api/architecture/architecture_hexagonal.md)
::::
download.page(api/architecture/architecture_mvc_mvvm_mvp.md)
::::
download.page(api/architecture/architecture_client_server.md)
::::
download.page(api/architecture/architecture_layered.md)
::::
download.page(api/architecture/architecture_pipefilter.md)
::::
download.page(api/architecture/architecture_driven_design.md)

## MESSAGING & QUEUING
messaging-pubsub

### tech stack

* Web
package manager (npm or yarn), language (JavaScript or Typescript), linting and formatting rules (ESLint presets or Prettier), unit testing framework (jest or jasmine), CSS preprocessor (Sass or Less).

* ADR - ARCHITECTURE DECISION RECORD
Document capturing an important architectural decision made along with its context and consequences.
https://github.com/joelparkerhenderson/architecture_decision_record