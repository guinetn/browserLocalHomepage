# SOA - SERVICES ORIENTED ARCHITECTURE

Service based architecture model: services allow components and applications to comunicate
It comprise of the 5 elements namely
- Services
- Service Bus
- Service Repository catalogue of services
- SOA Security
- SOA Governance

Client sends a request using a standard protocol and data format through the network. This request handled by the ESB which can be considered as the heart of SOA. ESB holds the responsibility of orchestration and routing. ESB directs the request to a dedicated service using a service repository. This dedicated service may interact with other services or database to compose the response payload (response data).
Complete request response call is in compliance with SOA governance and security rule in order to fulfil the transaction ensuring security and correctness.

https://www.udemy.com/course/software-architecture-and-design-essentials/

Services are generally classified as two types
***Atomic services***
Provides functionality which can not be decomposed further

***Composite services***
An aggregate of multiple atmoic services to provide a complex composite functionality

Types of Services
- Entity service
- Domain Service
- Utility Service
- Integrated Service
- Application Service
- Security Service

download.page(api/soap.md)