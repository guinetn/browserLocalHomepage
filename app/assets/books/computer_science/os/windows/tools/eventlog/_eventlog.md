# EVENTLOG

System.Diagnostics

Event Viewer	
>eventvwr.msc	
Opens the Event Viewer which displays operating system, software, and hardware events


EventLog 	to create and write a message into the eventlog
            SourceExists 		Determines whether an event source is registered on the local computer or not.
            CreateEventSource 	Establishes an application as able to write event information to a particular log on the system.
            WriteEntry 			Writes an entry in the event log, i.e., writes an information type entry, with the given message text, to the event log.
            EventLogEntryType 	Enum. Specifies the event type of an event log entry.

            Source 		What logs the event (application s name...). Gets or sets the source name to register and use when writing to the event log.
                        The event source is the name of the software that logs the event. 
                        It is often the name of the application or the name of a subcomponent of the application if the application is large
            Log		 	Gets or sets the name of the log to read from or write to

            The system uses the Source property to find the appropriate log in which to place your entry
            Three log files exist by default on the server: Application, System, and Security. 
            Applications and services should write to the Application log or a custom log. Device drivers should write to the System log.

                EventLog.CreateEventSource(strLogName, strLogName);
                EventLog SQLEventLog = new System.Diagnostics.EventLog();

                SQLEventLog.Source = strLogName;
                SQLEventLog.Log = strLogName;

                SQLEventLog.Source = strLogName;
                SQLEventLog.WriteEntry("The " + strLogName + " was successfully initialize component.", EventLogEntryType.Information);

            To write directly to the "Application" event log:
                using(EventLog eventLog = new EventLog("Application")) 
                { 
                    eventLog.Source = "Application"; 
                    eventLog.WriteEntry("Log message example", EventLogEntryType.Information, 101, 1); 
                } 

To verify the event log output of your service
In Visual Studio, open Server Explorer (Keyboard: Ctrl+Alt+S), and access the Event Logs node

EventLog.SourceExist -> Security Exception
    it tries to access ALL the event logs (including the Security log) which by default in Vista you will not have permissions for. 
    Another reason can be if the source you are looking for is not found in the event log
    In the eventlog component, set  'Log' property to 'Application' to avoid to write to all logs including security that is forbidden

EventLog.SourceExists
    This method accesses the registry, you must have the appropriate registry permissions on the local computer; otherwise, a SecurityException will be thrown.
    To search for an event source in Windows Vista and later or Windows Server 2003, you must have administrative privileges.
    The reason for this requirement is that all event logs, including security, must be searched to determine whether the event source is unique. Starting with Windows Vista, users do not have permission to access the security log; therefore, a SecurityException is thrown.
    A service that is executing under the LocalSystem account does not have the privileges required to execute this method. 
    The solution is to check whether the event source exists in the ServiceInstaller, and if it does not exist, to create the source in the installer.

Clean an event log with powershell (admin mode)
    remove-eventlog -logname saltShaker
    remove-eventlog -source saltShakerService

```c#
  static public void Write() {
        try
        {
            throw new Exception("Event Log Demo - Your Error Text");
        }
        catch(Exception ex)
        {
            WriteToEventLog(ex.Message + Environment.NewLine + ex.StackTrace);
        }
    }

    static private void WriteToEventLog(string Message)
    {
        string Source = "EventLogsDemo";

        if (!EventLog.SourceExists(Source))
            EventLog.CreateEventSource(Source, "Application");

        EventLog.WriteEntry(Source, Message, EventLogEntryType.Error);
    }
```


## EventLog Notifications: email, exe, messages

Getting notifications when your app writes an error to event logs

Workflow Pre-requisite: this event has been logged at least once in the Event log

![MenuOption](assets/books/computer_science/os/windows/tools/eventlog/MenuOption.png)
![Step1](assets/books/computer_science/os/windows/tools/eventlog/Step1.png)
![Step2](assets/books/computer_science/os/windows/tools/eventlog/Step2.png)
![step3](assets/books/computer_science/os/windows/tools/eventlog/step3.png)
![step5](assets/books/computer_science/os/windows/tools/eventlog/step5.png)
![image001](assets/books/computer_science/os/windows/tools/eventlog/image001.png)

Behind the scenes a task has been added in your Task Scheduler → "Event Viewer Tasks"
![taskscheduler](assets/books/computer_science/os/windows/tools/eventlog/taskscheduler.png)


### More 

- https://www.codeproject.com/Tips/392041/Getting-Notifications-Upon-Your-Application-Writin
- https://4sysops.com/archives/using-the-convert-eventlogrecord-function-instead-of-get-winevent-to-search-the-windows-event-log/