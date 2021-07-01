Concurrent    When program can handle multiple tasks at once  
Parallelism   when program can execute multiple tasks at once using multiple processors  

In other words, concurrency is a property of a program that allows you to have multiple tasks in progress at the same time but not necessarily executing at the same time. 

## parallelism 

Parallelism is a runtime property where two or more tasks are executed at the same time.
Parallelism can therefore be a means to achieve the property of concurrency, but it is just one of many means available to you.
The key tools for concurrency in Golang are goroutines and channels. Goroutines are concurrent lightweight threads, while channels allow goroutines to communicate with each other during execution.