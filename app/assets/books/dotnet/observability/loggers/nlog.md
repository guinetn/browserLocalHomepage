## NLog

NLog has quickly become the second most popular framework for .NET logging. They had support for .NET Core when v1.0 came out and continue to rapidly add new features. NLog even works across Xamarin, Mono, and other runtimes. NLog is a safe bet if you are thinking about selecting a new logging framework for ASP.NET Core.
Be sure to check out our tips and best practices guide on NLog. https://stackify.com/nlog-guide-dotnet-logging/


Logging frameworks: NLog, Serilog, Microsoft.Extensions.Logging. 
It is often a better choice for monitoring the output from these logging frameworks, rather than monitoring the Windows Event Log.
how to send an email on errors logged through NLog

> dotnet add package NLog.Web.AspNetCore

```c#
using NLog;

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


using NLog.Web;
Host.CreateDefaultBuilder(args)
  .ConfigureWebHostDefaults(webBuilder =>
  {
    webBuilder.UseStartup<Startup>();
  })
  .UseNLog();

// appsettings.json:
"Logging": {
  "LogLevel": {
    "Default": "Information",
    "Microsoft": "None",
    "Microsoft.AspNetCore": "Error",
    "Microsoft.Hosting.Lifetime": "Information"
  }
}
```

NLog.config file

```xml
<target name="Mail" xsi:type="Mail" smtpServer="smpt.myserver.com" smtpPort="587" ... />


<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      throwExceptions="false"
      throwConfigExceptions="false"
      autoReload="true"
      internalLogLevel="Warn"
      internalLogFile=
           "C:\temp\BuildRestApiNetCore\RestApi-internal-nlog.txt">
 
  <extensions>
    <add assembly="NLog.Web.AspNetCore"/>
  </extensions>
 
  <targets async="true">
    <target xsi:type="File"
            name="ownFile-web"
            fileName=
              "C:\temp\BuildRestApiNetCore\RestApi-${shortdate}.log">
 
      <layout xsi:type="JsonLayout">
        <attribute name="Timestamp" layout="${longdate}" />
        <attribute name="Level" layout="${uppercase:${level}}" />
        <attribute name="Logger" layout="${logger}" />
        <attribute name="Action" layout="${aspnet-mvc-action}" />
        <attribute name="Message" layout="${message}" />
        <attribute 
           name="Exception" layout="${exception:format=tostring}" />
      </layout>
    </target>
  </targets>
 
  <rules>
    <logger name="Microsoft.*" maxlevel="Info" final="true" /> 
                
    <logger name="*" minlevel="Info" writeTo="ownFile-web" />
  </rules>
</nlog>
```

