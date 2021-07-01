# STRUCTURED LOGGING

Using structured logging, you can add serialized objects to the logs that are efficiently queryable by log monitoring systems. For e.g., you can query the entire transaction log based on a customerID or a transactionID. In ASP.NET Core apps, you can use Serilog, which provides structured logging. 


- https://stackify.com/what-is-structured-logging-and-why-developers-need-it/
- https://dzone.com/articles/what-is-structured-logging

The problem with log files is they are unstructured text data. This makes it hard to query them for any sort of useful information. As a developer, it would be nice to be able to filter all logs by a certain customer # or transaction #. The goal of structured logging is to solve these sorts of problems and allow additional analytics.

For log files to be machine-readable more advanced functionality, they need to be written in a structured format that can be easily parsed. This could be XML, JSON, or other formats. But since virtually everything these days is JSON, you are most likely to see JSON as the standard format for structured logging.

## Structured logging can be used for a couple different use cases:

* Process log files for analytics or business intelligence – A good example of this would be processing web server access logs and doing some basic summarization and aggregates across the data.
* Searching log files – Being able to search and correlate log messages is very valuable to development teams during the development process and for troubleshooting production problems.

Diagnostics
    What caused this stack trace?
    What was the sequence of events that led up to this request failing unexpectedly?
Analytics
    Who is using our service?
    What does usage look like over time?
    What are our customers using our system to do?
Monitoring
    How long is it taking to process a request?
    How much available memory is there?

