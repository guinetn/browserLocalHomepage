# .Net Core

There is No More .NET Core, it’s .NET 5

.Net 5.0
.NET Core 4.0   ❌ Team omit 4.x and go straight to .NET 5.0 to avoid confusion with .NET Framework 4.x
.NET Core 3.0	2019 September
.NET Core 2.2	2018 December 
.NET Core 2.0	2017 August
.NET Core 1.1	2016 November 	
.NET Core 1.0   2016 June

- Set of runtime, library and compiler component*
- Open source GitHub sous la licence MIT
- Cross-platform
- Releases:  
> major (highly stable), supported for three years after it ships, or 12 months after the next major release ships
> minor (faster rate of change and innovation)

Component*:  
Set of files or features included with a Microsoft product. May be shipped with it or updated/released later

https://github.com/dotnet/core
https://docs.microsoft.com/en-us/dotnet/core/tools

## project.json
App portable or self-contained application using type property of Microsoft.NETCore.App dependency in project.json.
For the self-contained application, remove type-platform from the dependency. This makes it a self-contained application which means .NET Core will be included when you build and publish an application.

<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp2.0</TargetFramework>
    <TargetFrameworks>netcoreapp2.0;net45;net46</TargetFrameworks>  <--- To target multiple frameworks
  </PropertyGroup>

  <ItemGroup Condition=" '$(TargetFramework)' == 'net40' ">
    <Reference Include="System.Net" />
  </ItemGroup>
  <ItemGroup Condition=" '$(TargetFramework)' == 'net45' ">
    <Reference Include="System.Net" />
  </ItemGroup>


</Project>


using System;

namespace MultiFrameworkConsole
{
    public class Program
    {
        public static void Main(string[] args)
        {
                    
        #if NET40
                Console.WriteLine("Target framework: .NET Framework 4.0");
        #elif NET45
                Console.WriteLine("Target framework: .NET Framework 4.5");
        #else
                Console.WriteLine("Target framework: .NET Core 2.0");
        #endif
                Console.ReadKey();
        }
    }
}

## Environment Variable

Debug tab --> Environment Variables

IHostingEnvironment service includes EnvironmentName property which contains the value of ASPNETCORE_ENVIRONMENT variable. ASP.NET Core also includes extension methods to check the environment such as IsDevelopment(), IsStating(), IsEnvironment() and IsProduction().
public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
    if (env.IsEnvironment("Development"))
    {
        // code to be executed in development environment 

    }
    if (env.IsDevelopment())
    {
    // code to be executed in development environment 

    }
}


    

## Starts

https://www.tutorialsteacher.com/core/aspnet-core-program

dotnet new console
dotnet add package System.Collections --version 4.3.0 
  .csproj
    <ItemGroup>
        <PackageReference Include="System.Collections" Version="4.3.0" />
    </ItemGroup>
dotnet build
dotnet add package Microsoft.Extensions.DependencyInjection --version 5.0.1

## logging
https://blog.elmah.io/monitoring-net-scheduled-tasks-tools-and-alternatives/

Logging frameworks: NLog, Serilog, Microsoft.Extensions.Logging. 
It is often a better choice for monitoring the output from these logging frameworks, rather than monitoring the Windows Event Log.
how to send an email on errors logged through NLog
```c#
class Program
{
    static void Main(string[] args)
    {
        var logger = NLog.LogManager.GetCurrentClassLogger();
        try
        {
            // Execute your scheduled task code
            logger.Info("Scheduled task is successful");
        }
        catch (Exception e)
        {
            logger.Error(e, "Error during scheduled task");
        }
        
        NLog.LogManager.Shutdown();
    }
}

NLog.config file:
<target name="Mail" xsi:type="Mail" smtpServer="smpt.myserver.com" smtpPort="587" ... />
```
::::
download.chapter(code/dotnetcore/dotnetcore_on_linux.md)
::::
download.chapter(code/dotnetcore/dotnetcore2.0.md)
::::
download.chapter(code/dotnetcore/dotnetcore3.0.md)

## More

- https://blog.joaograssi.com/posts/2020/asp-net-core-integration-tests-with-docker-compose-github-actions/
- [use ps to call .net framework rom .net core](https://www.c-sharpcorner.com/blogs/using-systemspeech-with-net-core-30)
- https://www.tutorialsteacher.com/core/fundamentals-of-logging-in-dotnet-core
- https://www.tutorialsteacher.com/core/internals-of-builtin-ioc-container-in-aspnet-cohérent
