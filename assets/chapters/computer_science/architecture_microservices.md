# MICROSERVICES ARCHITECTURE: "MONOLITH BREAKING"

- hot topic in the industry
- distributed architecture based

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

## Tools for Microservices Architecture

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


download.md(assets/slides/data/theorem_cap.md)

## Making a reporting service in Microservice architecture
one service has a DB.orders and the other has DB.customers
Solutions to join data for a report:

### 1. Aggregation Service

A service aggregating data from all other services and return desired results
- REST API call (to both orders and customer service)
- Circuit breakers are essentials for this kind of technique else we get 504 + performance issues
- Breaks the business bounded context
### 2. Batch Pull with Dedicated Database
- How to populate the dedicated DB timely?
- Batch Pull model technique: regularly bulk pull microservices's databases
- Breaks the business bounded context
- Valid updated data
- Change one schema = change reporting service

### 3. Event Push Model with Dedicated Database

- CAP Theorem
- State of an application changed → published event → event processor (Kafka) that is consumed by multiple application.
- master listener: reads Kafka each topic and update the dedicated reporting database correctly.
- maintain the eventual consistency of data without disturbing the microservices principals


- https://github.com/AleksK1NG/Go-gRPC-RabbitMQ-microservice
- https://medium.com/@muneeb.ahmed20/building-a-reporting-service-in-microservice-architecture-8d5bf3b90fb7
- https://medium.com/@muneeb.ahmed20/6-questions-to-answer-before-moving-to-a-microservices-architecture-ad3cfd0e700f
- https://medium.com/@muneeb.ahmed20/essentials-tools-for-microservices-architecture-f8a91c02909a