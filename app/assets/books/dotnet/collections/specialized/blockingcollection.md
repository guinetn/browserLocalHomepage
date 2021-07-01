## BlockingCollection

.NET 4 
Solve the producer-consumer problem. It allows to produce and handle jobs from multiple threads. It supports a maximum capacity of items. It also allows to block when we have no items to handle or when we reached its full capacity. It’s completely thread-safe. The default implementation acts as a Queue. This makes BlockingCollection perfect to act as the buffer between our pipeline steps. Here’s the basic implementation plan:


https://docs.microsoft.com/en-us/dotnet/standard/collections/thread-safe/blockingcollection-overview
https://michaelscodingspot.com/pipeline-pattern-implementations-csharp/