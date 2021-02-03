## logging
https://blog.elmah.io/monitoring-net-scheduled-tasks-tools-and-alternatives/

Logging frameworks: NLog, Serilog, Microsoft.Extensions.Logging. 
It is often a better choice for monitoring the output from these logging frameworks, rather than monitoring the Windows Event Log.
how to send an email on errors logged through NLog

```cs
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

## More

- https://intellitect.com/net-core-dependency-injection/
- https://github.com/IntelliTect-Samples/2016.04.01-EssentialNetLoggingWithNetCore
- https://intellitect.com/implementing-a-custom-ilogger-with-exception-handling-for-net-core/