### HEALTH CHECK

Healthchecks are very important when it comes to complex backend setups. In a nutshell, a health check in the realm of web development usually consists of a special address, for example, https://my-website.com/health/readiness. A service, or a component of your infrastructure (e.g., Kubernetes) checks this address continuously. Depending on the HTTP status code returned from a GET request to this address the service will take action when it receives an "unhealthy" response. Since the definition of "healthy" or "unhealthy" varies with the type of service you provide, the NestJS Terminus integration supports you with a set of health indicators.

As an example, if your web server uses MongoDB to store its data, it would be crucial information whether MongoDB is still up and running. In that case, you can make use of the MongooseHealthIndicator. If configured correctly - more on that later - your health check address will return a healthy or unhealthy HTTP status code, depending on whether MongoDB is running.





As part of .NET Core SDK, Microsoft has delivered an amazing healthcheck runtime.
Setup in your Startup class, your app will host a set of health check endpoints that you can query to assert its health.
- https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-3.1

```c#
using System.Threading;
using System.Threading.Tasks;

namespace Microsoft.Extensions.Diagnostics.HealthChecks
{
    /// <summary>
    /// Represents a health check, which can be used to check the status of a component in the application, such as a backend service, database or some internal
    /// state.
    /// </summary>
    public interface IHealthCheck
    {
        /// <summary>
        /// Runs the health check, returning the status of the component being checked.
        /// </summary>
        /// <param name="context">A context object associated with the current execution.</param>
        /// <param name="cancellationToken">A <see cref="CancellationToken"/> that can be used to cancel the health check.</param>
        /// <returns>A <see cref="Task{HealthCheckResult}"/> that completes when the health check has finished, yielding the status of the component being checked.</returns>
        Task<HealthCheckResult> CheckHealthAsync(HealthCheckContext context, CancellationToken cancellationToken = default);
    }
}

```


## More

- https://medium.com/swlh/how-to-implement-healthcheck-api-in-microservices-architecture-with-net-core-a5882369b016
- https://medium.com/@alm.ozdmr/signalr-core-heartbeat-and-redis-6ed351c2d6f7