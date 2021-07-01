# EVENT SOURCING

Capture all changes to an application state as a sequence of events.

ES is persisting changes that are happening in the application as a sequence of events (a stream) that can be used to reconstruct the current state, so that any subsequent requests can be handled.

Event sourcing persists the state of a business entity such an Order or a Customer as a sequence of state-changing events. Whenever the state of a business entity changes, a new event is appended to the list of events. Since saving an event is a single operation, it is inherently atomic.

An architectural pattern that records all changes made to an application's state, in the sequence in which the changes were originally applied.

Event Sourcing deals with an event store of immutable log of events, in which each log (a state change made to an object) represents an application state. An event store is like a version control system. In a microservices architecture, we can persist aggregates as a sequence of event.
 
Event Sourcing ensures that all changes to application state are stored as a sequence of events. ... Not just can we query these events, we can also use the event log to reconstruct past states, and as a foundation to automatically adjust the state to cope with retroactive changes

### Projections
one of the core patterns used in Event Sourcing. 
ES is persisting changes that are happening in the application as a sequence of events. Then this sequence (also called a stream) of events can be used to reconstruct the current state, so that any subsequent requests can be handled.

### Aggregate
has its internal state, which is a projection of a single fine-grained event stream. On the other hand - the Write Stack Projections can subscribe to streams containing all (or subset of all) events, and be used to create read models or support process managers

Problem
How to reliably/atomically update the database and publish messages/events?

Solution
Use event sourcing: it persists the state of a business entity such an Order or a Customer as a sequence of state-changing events. Whenever the state of a business entity changes, a new event is appended to the list of events. Since saving an event is a single operation, it is inherently atomic. The application reconstructs an entity’s current state by replaying the events.

Applications

Version control systems are good examples of event sourcing - particularly Git. Each commit is stored as an event representing a change of state - files/lines to be added/removed



- https://martinfowler.com/eaaDev/EventSourcing.html
- https://microservices.io/patterns/data/event-sourcing.html
- https://github.com/oskardudycz/EventSourcing.NetCore