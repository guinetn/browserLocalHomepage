## Distributed Tracing

### W3C Trace Context
Standard of HTTP headers and value formats for distributed tracing

### System.Diagnostic.Activity
- .Net class for trakking operations for tracing/logging
- Support W3C Trace Context format

### OpenTelmerty
- Open Standard to unify tracing & metrics (interface, conventions)
- Plugins for .Net

https://devblogs.microsoft.com/aspnet/monitoring-and-observability-in-cloud-native-asp-net-core-apps/

Enabling distributed tracing in your app could be as simple as adding a corresponding distributed trace provider’s SDK into every microservice. E.g., With the Application Insights SDK installed and configured in your app, tracing information is automatically collected for popular frameworks, libraries, and technologies by SDK dependency auto-collectors.

https://docs.microsoft.com/azure/azure-monitor/app/distributed-tracing#how-to-enable-distributed-tracing

https://opentelemetry.io/
There is a need for standardization with several different systems and tooling in place for observability. OpenTelemetry standardizes how different applications and frameworks collect and emit observability telemetry. OpenTelemetry provides a vendor-neutral specification, a set of APIs, SDKs and tooling and integration for observability telemetry (distributed tracing, metrics, etc.). Check out the blog post OpenTelemetry .NET reaches v1.0 for detailed insights.