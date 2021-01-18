# Scheduling

## Windows Task Scheduler (built-in)
>task scheduler
To monitor tasks EVERY time they are supposed to have run, you can enable "Enable All Tasks History" → log messages to the Windows Event Log 

Event Viewer: overview of all executed tasks. 
Event Viewer (local) > Applications and Services Logs > Microsoft > Windows > TaskScheduler > Operational:


## MONITORING SYSTEMS

### Logging  
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


### Heartbeat Monitoring

A heartbeat is simply a ping from your application which is validated by the chosen service. You typically set up an expected schedule and let Heartbeat Monitoring send you a notification if a ping is not received in time.
https://blog.elmah.io/introducing-heartbeats/


elmah.io
https://elmah.io/features/heartbeats/

class Program
{
    // Install-Package Elmah.Io.Client
    static void Main(string[] args)
    {
        var logId = new Guid("LOG_ID");
        var api = ElmahioAPI.Create("API_KEY");
        try
        {
            // Execute your scheduled task code
            api.Heartbeats.Healthy(logId, "HEARTBEAT_ID");
        }
        catch (Exception e)
        {
            api.Heartbeats.Unhealthy(logId, "HEARTBEAT_ID");
        }
    }
}

### Hangfire

Implementing background processes in .NET
Implement everything from fire-and-forget type of jobs to scheduled tasks.

Once set up, scheduling a recurring job:
```C#
RecurringJob.AddOrUpdate(() =>
{
    // ...
}, Cron.Hourly);
```

### Azure Functions

Azure Functions can run in a serverless mode, which means that you only pay for the virtual machine executing the scheduled task as long as it is running. Azure Functions is a great and cheap way to implement scheduled tasks if you are already on Azure.

```C#
// Azure Function scheduled to run hourly
public class MyScheduledFunction
{
    [FunctionName("MyScheduledFunction")]
    public async Task Run([TimerTrigger("0 0 * * * *")]TimerInfo myTimer)
    {
        // Add your scheduled code here
        
        return Task.CompletedTask;
    }
}
```

### Hosted services in .NET Core

A hosted service is sort of like a Windows Service but hosted inside a .NET process (like a console application). Using a simple Timer you can create scheduled tasks using hosted services:

```C#
public class MyService : IHostedService
{
    private Timer timer;

    public Task StartAsync(CancellationToken cancellationToken)
    {
        timer = new Timer(Execute, null, TimeSpan.Zero, TimeSpan.FromHours(1));
        return Task.CompletedTask;
    }

    private void Execute(object state)
    {
        // Run your hourly code
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        // ...
        return Task.CompletedTask;
    }
}

// Adding the service is easy from either a console app or ASP.NET Core:
services.AddHostedService<MyService>();
```

### Quartz.NET

A scheduling framework   
Like hosted services it let you define jobs/services:

```C#
public class MyJob : IJob
{
    public Task Execute(JobExecutionContext context)
    {
        // ...
        return Task.CompletedTask;
    }
}
Jobs can then be scheduled:

var job = JobBuilder.Create<MyJob>().Build();
var trigger = TriggerBuilder.Create()
    .StartNow()
    .WithSimpleSchedule(x => x
        .WithIntervalInHours(1)
        .RepeatForever())            
    .Build();
await scheduler.scheduleJob(job, trigger);
```

Quartz.NET support a couple of integrations with other frameworks like ASP.NET Core and even hosted services, which make it a good alternative to simple timers.

### Background workers in ASP.NET

alternatives for scheduled tasks
ASP.NET supports long-running tasks through the HostingEnvironment.QueueBackgroundWorkItem method.   
The idea behind QueueBackgroundWorkItem is to have the webserver execute a long-running task in an async way that let a controller action return a response to the client before finishing the task. QueueBackgroundWorkItem is not suited for scheduling tasks.