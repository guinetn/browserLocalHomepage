## CLR - Common Language Runtime

CLR = The .NET runtime

A program written with any of the .NET languages that respect the CLS (Common Language Specification) can be compiled into bytecode that the .Net rutime can interpret using 
the Just-In-Time compiler. It also has additional responsibilities like memory management (GC), security...


runtime: collection of external services that are required to execute a given compiled unit of code
- application using MFC requires the MFC runtime library (mfc42.dll)
- VB6 codes are ties to a runtime module or two such as msvbvm60.dll
- Java codes are tied to the Java Virtual Machine (JVM)
- .NET runtime provides a single well-defined runtime layer that is shared by all languages and platforms that are .NET-aware.

* mscoree.dll (the Common Object Runtime Execution Engine)
Crux of the CLR 
When an assembly is referenced for use, mscoree.dll is loaded automatically, which in turn loads the required assembly into memory. The runtime engine is responsible for a number of tasks. 
- First in charge of resolving the location of an assembly and finding the requested type within the binary by reading the contained metadata. 
- Then CLR lays out the type in memory, compiles the associated CIL into platform-specific instructions, performs any necessary security checks, and then executes the code.

* mscorlib.dll
In addition to loading our custom assemblies and creating custom types, the CLR will also interact with the types contained within the .NET base class libraries when required. Although the entire base class library has been broken into a number of discrete assemblies, the key assembly is mscorlib.dll. It contains a large number of core types that encapsulate a wide variety of common programming tasks as well as the core data types used by all .NET languages. When we build .NET solution, we automatically have access to this particular assembly.