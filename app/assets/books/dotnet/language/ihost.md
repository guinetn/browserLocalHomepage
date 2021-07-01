## IHost

Microsoft.Extensions.Hosting

## IHostBuilder
A program initialization abstraction.

- public System.Collections.Generic.IDictionary<object,object> Properties { get; }
central location for sharing state between components during the host building process.

- Build()
- ConfigureAppConfiguration()
- ConfigureContainer()
- ConfigureHostConfiguration()
- ConfigureServices()
- UseServiceProviderFactory()

https://docs.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostbuilder?view=dotnet-plat-ext-5.0

### Host 

Provides convenience methods for creating instances of IHostBuilder with pre-configured defaults.
- CreateDefaultBuilder()	new instance of the HostBuilder class with pre-configured defaults
- CreateDefaultBuilder(String[])

The following defaults are applied to the returned HostBuilder:

- Set ContentRootPath = GetCurrentDirectory()
- Load host IConfiguration from "DOTNET_" prefixed environment variables
- Load app IConfiguration from 'appsettings.json' and 'appsettings.[EnvironmentName].json'
- Load app IConfiguration from User Secrets when EnvironmentName is 'Development' using - The entry assembly
- Load app IConfiguration from environment variables
- Configure the ILoggerFactory to log to the console, debug, and event source output
- EnaBles scope validation on the dependency injection container when EnvironmentName is 'Development'