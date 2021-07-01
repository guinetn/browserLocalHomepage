# DISTRIBUTED SYSTEM -  system design

Distributed systems: collections of computers + data centers that act as one computer for the end-user.
Distributed design patterns: outline a software architecture for how different nodes communicate with each other, which nodes handle each task, and the process flow for different tasks.

Distributed applications 
- WHAT: allow web applications of massive scale to stay reactive
- HOW: use cloud storage services

These systems need fundamental building blocks as a starting point and to communicate in a shared vocabulary, these are distributed system design patterns. Design patterns are building blocks solution to a common problem ans allow programmers to pull from existing knowledge rather than starting from scratch with every system.

## Types of distributed design patterns
- Creational design patterns: baseline when building new objects
- Structural patterns: define the overall structure of a solution
- Behavioral patterns: describe objects and how they communicate with each other

Object communication: Describes the messaging protocols and permissions for different components of the system to communicate.
Event-driven: Patterns that describe the production, detection, consumption, and response to system events.
Security: Handles confidentiality, integrity, and availability concerns to ensure the system is secure from unauthorized access.

## Command and Query Responsibility Segregation
download.page(computer_science/software_design_rules/cqrs.md)

## 2PC - Two-Phase Commit

Deal with high-stakes transaction operations that favor accuracy over resource efficiency. It is resistant to error and it is easy to track mistakes when they occur, even at scale.

~ CQRS in its transactional approach and reliance on a central command, but partitions are processed by their type and what stage of completion they’re on. The two phases are the Prepare phase (in which the central control tells the services to prepare the data) and the Commit phase (which signals the service to send the prepared data).
All services in a 2PC system are locked by default, meaning they cannot send data. While locked, services complete the Prepare stage so they’re ready to send once unlocked. The coordinator unlocks services one by one and requests their data. If the service is not ready to submit its data, the coordinator moves on to another service. Once all prepared data has been sent, all services unlock to await new tasks from the coordinator.
2PC essentially ensures that only one service can operate at a time, which makes the process more resistant and consistent than CQRS.

PRO
- Consistent and resistant to errors due to lack of concurrent requests.
- Scalable — can handle big data pools as easily as it can handle data from a single machine.
- Allows for isolation and data sharing at the same time.
CONS
- Not fault-tolerant, prone to bottlenecks and blocking due to its synchronous nature.
- Requires more resources than other design patterns.

## Saga

Great for scalable serverless functions that handle many parallel requests at once. AWS uses Saga-based designs in many functions like step and lambda functions.

Asynchronous pattern that does not use a central controller and instead communicates entirely between services

Saga uses an Event Bus to allow services to communicate with each other in a microservice system. The bus sends and receives requests between services, and each participating service creates a local transaction. The participating services then each emit an event for other services to receive. Other services all listen for events. The first service to receive the event will perform the required action. If that service fails to complete the action, it’s sent to other services.
This structure is similar to the 2PC design in that services are cycled if one cannot complete a task. However, Saga removes the central control element to better manage the flow and reduce the amount of back-and-forth communication required.

PRO
- Individual services can handle much longer transactions.
- Great for the distributed system due to decentralization.
- Reduces bottlenecks thanks to peer-to-peer communication between services.
CONS
- Asynchronous autonomy makes it difficult to track which services are doing individual tasks.
- Difficult to debug due to complex orchestration.
- Less service isolation than previous patterns.

## RLBS - Replicated Load-Balanced Services
Great for front-facing systems that have inconsistent workloads throughout the day but must maintain low latency, such as entertainment web apps like Netflix or Amazon Prime.

Consists of multiple identical services that all report to a central load balancer. Each service is capable of handling tasks and can replicate if they fail. The load balancer receives requests from the end-user and distributes them to the services either in a round-robin fashion or sometimes by using a more complex routing algorithm.
The duplicate services ensure the application maintains a high availability for user requests and can redistribute work if one instance of the service should fail.

## Sharded Services

## Sidecar Pattern
## Write-Ahead Log
## Split-Brain Pattern
## Hinted Handoff
## Read Repair

### more

- https://betterprogramming.pub/top-5-distributed-system-design-patterns-ae9482f49128