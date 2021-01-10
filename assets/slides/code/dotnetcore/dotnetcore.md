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
download.md(assets/slides/code/dotnetcore/dotnetcore_on_linux.md)
::::
download.md(assets/slides/code/dotnetcore/dotnetcore2.0.md)
::::
download.md(assets/slides/code/dotnetcore/dotnetcore3.0.md)

## More
- https://blog.joaograssi.com/posts/2020/asp-net-core-integration-tests-with-docker-compose-github-actions/