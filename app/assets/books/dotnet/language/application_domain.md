## Application Domain

To run an external assembly
Applications avoid problems of security issues/inefficient resource usage such (printers/file system) from external assemblies

![](assets/books/dotnet/assets/appdomain.gif)

Application domain 
- is a logical location in memory where a process runs. 
When .NET CLR execute .NET assembly it creates the main application process and then .NET developers create more small application domains to run external .NET assemblies separately then the main application process.
- Keeps assemblies separated within a single process
 isolate .NET assemblies for security reasons but also improve reliability and efficiency of .NET applications.
 
```cs
// Creating Application Domain
AppDomain domain = AppDomain.CreateDomain("MyDomain");
 
// Loading Assembly in Application Domain
domain.ExecuteAssembly("../../TestAssembly.exe");
 
// Unload Application Domain
AppDomain.Unload(domain);
```