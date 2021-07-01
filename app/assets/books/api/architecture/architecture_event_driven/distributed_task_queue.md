# DISTRIBUTED TASK QUEUE


ability to execute tasks in the background while the application continues to resolve other tasks.

Task queues manage background work that must be executed outside the usual HTTP request-response cycle.

allows you offload work to another process, to be handled asynchronously (once you push the work onto the queue, you don't wait) and in parallel (you can use other cores to process the work).

Instead of handling a command or event, synchronously and in-process, work can be dispatched to a distributed task queue to be handled asynchronously and out-of-process. The trade-off here is between the cost of distribution against performance.

Tasks are handled asynchronously either because they are not initiated by an HTTP request or because they are long-running jobs that would dramatically reduce the performance of an HTTP response.

## Use Cases of Task Queues
The most basic and understandable example would be sending emails after the user is registered. In this case, you don’t know how much time is it going to get to send the email to the user, it can be 1ms but it can be more, or sometimes even not sent at all, because, in these case scenarios, you are not responsible or simply said you’re not aware of the task is going to be successfully done, because it’s another provider who is going to do that for you.
So now that you got a simple idea of how you can benefit from the task queues, identifying such tasks is as simple as checking to see if they belong to one of the following categories:

***Third-party tasks***
The web app must serve users quickly without waiting for other actions to complete while the page loads, e.g., sending an email or notification or propagating updates to internal tools (such as gathering data for A/B testing or system logging).

***Long-running jobs***
Jobs that are expensive in resources, where users need to wait while they compute their results, e.g., complex workflow execution (DAG workflows), graph generation, Map-Reduce like tasks, and serving of media content (video, audio).

***Periodic tasks***PeriodicJobs that you will schedule to run at a specific time or after an interval, e.g., monthly report generation or a web scraper that runs twice a day.

### more

- https://paramore.readthedocs.io/en/latest/ImplementingDistributedTaskQueue.html
- https://www.fullstackpython.com/task-queues.html
- https://awesomeopensource.com/projects/task-queue