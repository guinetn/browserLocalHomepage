# HIGH PERFORMANCE C# 

Lots of effort goes into reducing allocation, not because the act of allocating is itself particularly expensive, but because of the follow-on costs in cleaning up after those allocations via the garbage collector (GC). No matter how much work goes into reducing allocations, however, the vast majority of workloads will incur them, and thus it’s important to continually push the boundaries of what the GC is able to accomplish, and how quickly.

- Visual Studio 16 "allocation profiler" new tool (Alt+F2) 
To optimize your .NET code: Help the .NET GC out by avoiding it when you can

- Rider & resharper has dynamic program analysis (DPA) which will warn you at build time itself about unwanted and avoidable allocations

download.page(dotnet/high_perf/benchmarking.md)

download.page(dotnet/high_perf/memory_allocation.md)
download.page(dotnet/high_perf/frugal_object.md)
download.page(dotnet/high_perf/pooling.md)
download.page(dotnet/high_perf/zero_copy.md)
download.page(dotnet/high_perf/struct_of_arrays.md)
download.page(dotnet/high_perf/stack_based_data.md)
download.page(dotnet/high_perf/buffered_builder.md)

download.page(dotnet/high_perf/io.pipelines.md)

See also IValueTaskSource

- https://adamsitnik.com/
- https://adamsitnik.com/Array-Pool/
- https://www.youtube.com/watch?v=3r6gbZFRDHs&t=2255s
- Slides: https://prodotnetmemory.com/slides/PerformancePatterns/#1
- https://prodotnetmemory.com
- https://blogs.msdn.microsoft.com/dotnet/2018/04/18/performance-improvements-in-net-core-2-1/
- https://www.youtube.com/watch?v=nK54s84xRRs
	



- https://levelup.gitconnected.com/5-ways-to-improve-the-performance-of-c-code-for-free-c89188eba5da