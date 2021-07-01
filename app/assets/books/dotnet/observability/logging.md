## logging

give you the root cause of the problem
In distributed world ensure log records have in-depth information to debug that can be queried  from a central place. Each log record needs to have a correlation id, so they’re tracked in a single transaction to get the big picture. Generating a correlation ID at the start of a transaction and then logging it in each message related to that transaction makes it easier to search for all related messages from the centralized logging systems.

# LOGGERS


## Log4net

When .NET Core 1.0 launched, log4net had not been ported to support .NET Core (it has since). Their long delay in support for .NET Core is just one example of where log4net has been slow to keep up with new trends and features in logging frameworks. It may be the most popular framework, but NLog and Serilog are on the leading edge.
Be sure to check out our tips and best practices guide on log4net. https://stackify.com/log4net-guide-dotnet-logging/


## NLog

NLog has quickly become the second most popular framework for .NET logging. They had support for .NET Core when v1.0 came out and continue to rapidly add new features. NLog even works across Xamarin, Mono, and other runtimes. NLog is a safe bet if you are thinking about selecting a new logging framework for ASP.NET Core.
Be sure to check out our tips and best practices guide on NLog. https://stackify.com/nlog-guide-dotnet-logging/


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

## Serilog

Serilog was created to bring more structure to logging variables and objects. It has become very popular and continues to grow. It supports all the common logging features you would support, like configurable output targets and is much more modern than log4net.
Serilog: La différence majeure par rapport aux autres bibliothèques de log est qu’elle propose un mécanisme permettant d’avoir des méta données sur les événements survenus. Cela permet d’exploiter plus facilement ces logs que des logs en texte brut.


```c#
using System;
using System.IO;

using log4net;
using log4net.Core;
[assembly: log4net.Config.XmlConfigurator( ConfigFile = "Log4Net.config", Watch = true )]

namespace Hello
{
	private static readonly log4net.ILog log = log4net.LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

        /// <summary>
        ///   The main entry point for the application
        /// </summary>
        [STAThread]
        public static void Main(string[] args)
        {
            log.Info("Application [ConsoleApp] Start");

            Console.WriteLine(…);
            Console.WriteLine(…);

 			log.Info("Application [ConsoleApp] End");
        }
    }
}
```

log4net.dll

log4net.xml

***Log4Net.config***
```xml
<?xml version="1.0" encoding="utf-8" ?>
<log4net>
    <!-- A1 is set to be a ConsoleAppender -->
    <appender name="ConsoleAppender" type="log4net.Appender.ConsoleAppender">

        <!-- A1 uses PatternLayout -->
        <layout type="log4net.Layout.PatternLayout">
            <conversionPattern value="%-4timestamp [%thread] %-5level %logger %ndc - %message%newline" />
        </layout>
    </appender>

    <root>
        <appender-ref ref="ConsoleAppender" />
    </root>
</log4net>
```

## More


- https://docs.microsoft.com//aspnet/core/fundamentals/logging
- https://blog.elmah.io/monitoring-net-scheduled-tasks-tools-and-alternatives/
- https://michaelscodingspot.com/logging-in-dotnet/
- https://dzone.com/articles/5-good-reasons-to-use-a-log-server

- https://intellitect.com/net-core-dependency-injection/
- https://github.com/IntelliTect-Samples/2016.04.01-EssentialNetLoggingWithNetCore
- https://intellitect.com/implementing-a-custom-ilogger-with-exception-handling-for-net-core/
- https://michaelscodingspot.com/logging-in-dotnet/
- https://www.ezzylearning.net/tutorial/logging-in-asp-net-core-5-using-serilog