# .Net Core 2.x

### NET CORE 2.1
* build x 10
* Span<T> memory efficient type (isolated view of a part of a larger array without any memory operations)
* The Windows compatibility pack includes 20 thousand APIs from the .NET framework which are not included in .NET Core itself (e.g. System.Drawing) available not just for Windows but about half of the APIs are also implemented on other platforms. The rest throw an exception (as of this writing) when invoked on a nonWindows OS.
* .NET Core Tools 
.NET Core CLI Extensions - npm like tools
represent a new (NuGet based) way for deploying command line (CLI) tools written in .NET Core. They are modelled after NPM (Node Package Manager) global tools. A tool can be installed using the following command: dotnet tool install -g dotnet-serve It will be added to the path and can later be invoked using only its name: dotnet-serve The dotnet-serve tool mentioned here is a simple HTTP server. A list of available tools is maintained on [GitHub](https://github.com/natemcmaster/dotnet-tools/blob/master/README.md)

### .NET CORE 2.2
Better support for Open API (Swagger) descriptors for HTTP (REST) services
Entity Framework Core was also expanded with support for spatial data.



