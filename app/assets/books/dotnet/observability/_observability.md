## observability - production diagnostics

Important when building a distributedd system


## Observability in .net
Monitory systems that do alerting (see exceptions in logs or spikes in metrics) and debugging an application uses these things:

- Logs
>EventSource  
DiagnosticSource  
Microsoft.Extensions.Logging.Abstractions

- Metrics
In runtime: EventCounter (previously Perfromance counters)
In App: OpenTelemetry

- Tracing/distributed tracing
In rutime: Activity, EventSource, DiagnosticSource
In apps: Activity; OpenTelemetry

- Health check
- Memory dumps, try attaching a debugger to your process in production

Distributed = you can't just attach a debugger your entire application → need to define specific areas of observability. 

Logs & metrics don't tend to go over the network
tracing: identify both side of a system. OpenTelemetry

Diagnostics
    What caused this stack trace?
    What was the sequence of events that led up to this request failing unexpectedly?
Analytics
    Who is using our service?
    What does usage look like over time?
    What are our customers using our system to do?
Monitoring
    How long is it taking to process a request?
    How much available memory is there?





download.page(dotnet/observability/metrics.md)
::::
download.page(dotnet/observability/logging.md)
download.page(dotnet/observability/logging_distributed.md)
::::
download.page(dotnet/observability/structured_logging.md)
::::
download.page(dotnet/observability/diagnostics.md)
::::
download.page(dotnet/observability/tracing.md)
download.page(dotnet/observability/tracing_distributed.md)

## more

- https://channel9.msdn.com/Shows/On-NET/Setting-up-Observability-in-Orleans
- https://devblogs.microsoft.com/aspnet/monitoring-and-observability-in-cloud-native-asp-net-core-apps/
- https://docs.microsoft.com/aspnet/core/host-and-deploy/health-checks