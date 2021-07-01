# Akka.net - actor model

- https://getakka.net/
- https://getakka.net/articles/intro/what-problems-does-actor-model-solve.html
- https://medium.com/swlh/getting-started-with-microsoft-orleans-882cdac4307f


Toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications on .NET & Mono.
A set of open-source libraries for designing scalable, resilient systems that span processor cores and networks. Akka allows you to focus on meeting business needs instead of writing low-level code to provide reliable behavior, fault tolerance, and high performance.

Locking result in a no-win situation:
- Without sufficient locks, the state gets corrupted.
- With many locks in place, performance suffers and very easily leads to deadlocks.

locks only really work well locally. When it comes to coordinating across multiple machines, the only alternative is distributed locks. Unfortunately, distributed locks are several magnitudes less efficient than local locks and usually impose a hard limit on scaling out. Distributed lock protocols require several communication round-trips over the network across multiple machines, so latency goes through the roof.

common programming practices cannot properly address the needs of modern concurrent and distributed systems. Thankfully, we don't need to scrap everything we know. Instead, the actor model addresses these shortcomings in a principled way, allowing systems to behave in a way that better matches our mental model.

In particular, we would like to:

Enforce encapsulation without resorting to locks.
Use the model of cooperative entities reacting to signals, changing state and sending signals to each other to drive the whole application forward.
Stop worrying about an executing mechanism which is a mismatch to our world view.
The actor model accomplishes all of these goals



download.page(dotnet/threading/g_actor_model/actor_model.md)



Distributed by Default
Everything in Akka.NET is designed to work in a distributed setting: all interactions of actors use purely message passing and everything is asynchronous.

Actors form a tree with actors being parents to the actors they've created.

As a parent, the actor is responsible for handling its children’s failures (so-called supervision), forming a chain of responsibility, all the way to the top. When an actor crashes, its parent can either restart or stop it, or escalate the failure up the hierarchy of actors. This enables a clean set of semantics for managing failures in a concurrent, distributed system and allows for writing highly fault-tolerant systems that self-heal.

