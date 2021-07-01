# Health checks

implemented in microservices
HTTP endpoints that various real-time monitoring systems can query. At a very minimum, the health check endpoints should respond to:
- Is the system running?
- Can it perform tasks?

Kubernetes world = liveness (periodical queries) and readiness probes (service is ready?)