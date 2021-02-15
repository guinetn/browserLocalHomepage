## MICROSERVICES ARCHITECTURE

- hot topic in the industry
- distributed architecture based

Classic Server-side enterprise application:
- Variety of clients (desktop, browsers, mobile...)
- Exposing APIs
- Integrates with other applications via web services/ message broker
- Handles HTTP requests/messages by executing business logic: 
>accessing a database
>exchanging messages with other systems
>returning an HTML/JSON/XML response

2. Solution
Application = a set of loosely coupled interacting services
"MONOLITH BREAKING" 

- Services communicate using technology-agnostic protocols such as HTTP/REST or AMQP — thus, data contracts are constant
- Services are developed and deployed independently — it enables a team to develop and deploy a service without having to coordinate with other services and teams
- Each service has its own database — in order to be decoupled from other services. 
- Business transactions implemented as a sequence of local transactions (service-to-service) through event channels or message brokers.


![](assets/books/api/architecture/microservices/microservices03.png)

download.page(api/architecture/api_gateway.md)

Backend services: Service A + Service B are business logic execution units with their own PRIVATE databases (others services has no access to it). They communicate via a message broker.


Core idea of a microservices architecture is to split the application backend into a set of loosely coupled services that are developed, deployed, tested, scaled independently.

Benefits
- enabling continuous delivery and deployment of large, complex applications
- no long-term commitment to a technology stack
- simpler maintenance
- increased failure tolerance

Drawbacks
- increased complexity of development and deployment
- increased memory consumption
- Apply microservice architecture pattern in the later stages of development, when scaling becomes the most important issue.




building single-function modules that have well-defined interfaces and operations.
Applications can be arranged as a collection of loosely coupled services
Ex: Amazon. To reach the requirements of its rapidly growing customer base, Amazon developers had to break down the monolithic applications into smaller, independently-running, and service-specific applications. Hence, microservices.




- What value it will add to the business?
- Do we have enough resources?
- Experience needed
    Converting monolith to microservice requires some experience in 
    - database migration
    - microservices architecture knowledge
    - alternative DevOps tools
    - communication protocol
    - distributed messaging
    - domain driven design
    - data consistency vs availability and performance bounded service.
- Do we have domain experts?
They understand each component of the monolith system and know why and where each business logic of the system exists
Mapping business logic from monolith to microservice requires a complete understanding of business logic and domain driven design: DDD for decomposition from monolith to microservices.

- one microservices = business bounded context 
- one database per service. Use API to access data to another service

### Tools for Microservices Architecture

* Containerization
saves the time of deployment and improves release lifecycle. An engineer is responsible to write container related scripts that boost deployment lifecycle. [Kubernetes](https://kubernetes.io/) are one of the best ways to containerize your application in production. 

* Deployment Pipeline
have a deployment pipeline set for your staging, development and production branch from version control. Deployment pipeline should have tests scripts inside it that make sure the new version is stable
- https://jenkins.io/
- use infrastructure as code which is super helpful in deployment pipeline and managing infrastructure as code.

* Monitoring and Alerting
Allo to find root cause of the problem in the large distributed system.  
Create alerts. Critical flows can generate a phone call to the stakeholder of that service
- https://grafana.com
- https://newrelic.com

* Distributed Tracking
observe traffic (requests), control flow using a circuit breaker and use them as a service mesh
- https://istio.io
- https://www.kiali.io

* Application Logging
build a common object of logging and everyone uses that to log in their application. These logs are then pushed in logging system e.g Elastic Search, logz.io e.t.c with a separate index of each application name.
- https://logz.io/

* Communication
Microservice communicate via Rest protocol.
To communicate more over: publisher-subscriber model that fulfills our need data to send and read asynchronously without thread blocked on network calls. Based on company-wide skillsets, needs and requirements we can use Kafka, Rabbitmq e.t.c.


download.page(data/theorem_cap.md)



### Making a reporting service in Microservice architecture
one service has a DB.orders and the other has DB.customers
Solutions to join data for a report:

#### 1. Aggregation Service

A service aggregating data from all other services and return desired results
- REST API call (to both orders and customer service)
- Circuit breakers are essentials for this kind of technique else we get 504 + performance issues
- Breaks the business bounded context
#### 2. Batch Pull with Dedicated Database
- How to populate the dedicated DB timely?
- Batch Pull model technique: regularly bulk pull microservices's databases
- Breaks the business bounded context
- Valid updated data
- Change one schema = change reporting service

#### 3. Event Push Model with Dedicated Database

- CAP Theorem
- State of an application changed → published event → event processor (Kafka) that is consumed by multiple application.
- master listener: reads Kafka each topic and update the dedicated reporting database correctly.
- maintain the eventual consistency of data without disturbing the microservices principals

#### Architecture

![](assets/books/api/architecture/microservices/microservices01.png)
![](assets/books/api/architecture/microservices/microservices02.png)

If you are running anything in production, it is most likely you are running many instances of any given service. In this case, we are making the following changes:
Running three instances of our service on different ports
We are using NGINX as a load balancer

### Services Communication 

synchronous (HTTP1.1 / gRPC) or asynchronous
Good recap: https://docs.nestjs.com/microservices/basics

Redis
MQTT
NATS
RabbitMQ
Kafka
gRPC
Custom transporters
Exception filters
Pipes
Guards
Interceptors


#### Retry pattern 

Localized to a single request
If a service is sending multiple requests to a single service, each one of them is handled independently of the others. 
However, if a request to a service is failing, it’s very likely that other requests to the same service will be failing as well.
This is where other patterns (circuit breaker...) are needed

#### Circuit breaker

Once serviceA “knows” that serviceB is down, there is no need to make request to serviceB. serviceA should return cached data or timeout error as soon as it can. This is the OPEN state of the circuit
Once serviceA “knows” that serviceB is up, we can CLOSE the circuit so that request can be made to serviceB again.
Periodically make fresh calls to serviceB to see if it is successfully returning the result. This state is HALF-OPEN.

Common proxy monitoring for all requests to a particular service
Failing requests (based on preconfigured rules) make it transitioning between three states:
* CLOSED
The called service is operating normally. All requests are passed to it.
* OPEN
The called service is currently failing. Any requests to it are not passed to the service and fail immediately.
* HALF-OPEN
After a certain period in the open state, the requests to the service are again passed to it.

However, the tolerance for failure is reduced. If any requests fail, the state will switch back to open. 
Only after the service seems to operate normally for some time, the circuit breaker returns into the closed state.

A pattern like circuit breaker can significantly reduce the number of requests sent to a service with transient issues. 
This can be helpful in its recovery as it isn’t overwhelmed with incoming requests which it can’t handle.
As for the retry pattern, the Polly library includes an easy-to-use implementation of the circuit breaker 

pattern:
var circuitBreakerPolicy = Policy
 .Handle<HttpRequestException>()
 .CircuitBreaker(2, TimeSpan.FromMinutes(1));

It makes perfect sense to combine both patterns: retry the requests as needed, but also track the failures
and eventually switch the circuit breaker to open state. The library supports that as well:
var combinedPolicy = Policy
 .Wrap(retryPolicy, circuitBreakerPolicy);

Using appropriate error handling mechanisms can noticeably contribute to the overall reliability of a
distributed cloud application.

![circuit breaker](assets/books/api/architecture/microservices/circuit-breaker/circuit_breaker.png)

- https://github.com/abhinavdhasmana/circuitBreaker
- https://itnext.io/understand-circuitbreaker-design-pattern-with-simple-practical-example-92a752615b42
- https://dncmagazine.blob.core.windows.net/edition49/DNCMag-Issue49.pdf
- https://docs.microsoft.com/sl-si/azure/architecture/patterns/circuit-breaker


### Tools

Progressive microservices framework for Node.js.
https://moleculer.services/

https://docs.nestjs.com/microservices/basics

#### More

- https://dncmagazine.blob.core.windows.net/edition49/DNCMag-Issue49.pdf ***

- https://github.com/AleksK1NG/Go-gRPC-RabbitMQ-microservice
- https://medium.com/@muneeb.ahmed20/building-a-reporting-service-in-microservice-architecture-8d5bf3b90fb7
- https://medium.com/@muneeb.ahmed20/6-questions-to-answer-before-moving-to-a-microservices-architecture-ad3cfd0e700f
- https://medium.com/@muneeb.ahmed20/essentials-tools-for-microservices-architecture-f8a91c02909a
- https://medium.com/transferwise-engineering/learnings-from-migrating-legacy-to-microservices-2ef4c0f6a766
- https://itnext.io/effectively-communicate-between-microservices-de7252ba2f3c
- https://itnext.io/designing-microservices-with-expressjs-eb23e4f02192?source=post_internal_links---------6----------------------------
- https://medium.com/transferwise-engineering/learnings-from-migrating-legacy-to-microservices-2ef4c0f6a766
-https://medium.com/younited-tech-blog/a-pattern-for-smooth-and-live-microservice-migrations-25e01d5cc59b
- https://blog.revdebug.com/top-issues-with-microservices
- [ Ambassador Pattern)](https://youtu.be/hrKUZ1jQCqI)
- https://levelup.gitconnected.com/microservices-architecture-74c26df8688
- https://martinfowler.com/articles/microservices.html