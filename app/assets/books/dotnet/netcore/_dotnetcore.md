# .Net Core

https://github.com/dotnet/core
https://docs.microsoft.com/en-us/dotnet/core/tools

||||
|---|---|---|
|.Net 6.0 		| 2021          | |
|.Net 5.0 SDK	| 2020 November | ***There is No More .NET Core, it’s .NET 5*** |
|.NET Core 4.0  |               |❌ Team omit 4.x and go straight to .NET 5.0 to avoid confusion with .NET Framework 4.x|
|.NET Core 3.1	| 2019 December | |
|.NET Core 3.0	| 2019 September| |
|.NET Core 2.2	| 2018 December | | 
|.NET Core 2.1	| 2018 May      | |
|.NET Core 2.0	| 2017 August   | |
|.NET Core 1.1	| 2016 November | |
|.NET Core 1.0  | 2016 June     | |

[.NET Supported OS](https://github.com/dotnet/core/blob/master/os-lifecycle-policy.md)

- Set of runtime, library and compiler component*
- Open source GitHub sous la licence MIT
- Cross-platform
- Releases:  
> major releases (highly stable), supported for three years after it ships, or 12 months after the next major release ships
> minor releases (faster rate of change and innovation)
> servicing updates (patches)
2 Support perspective:
>Current releases: supported for a period of 3 months after the next major or minor release ships.
>Long Term Support (LTS releases): supported for a minimum of 3 years, or 1 year after the next LTS release ships (whichever is longer).

Component*:  
Set of files or features included with a Microsoft product. May be shipped with it or updated/released later


***.NET Core Platform is made up of several components:***
|||
---|---
|CoreFX   | .NET Core foundational libraries: https://github.com/dotnet/corefx |
|CoreCLR  | .NET Core runtime |
|CLI      | .NET Core command-line tools |
|Roslyn   | .NET Compiler Platform |

.NET Core is the modular, open source and cross-platform set of tools that allows you to build next-generation .NET applications, which run on Windows, Linux and macOS (microsoft.com/net/core/platform). It can also be installed on the Windows 10 for IoT distribution, and it runs on devices such as the Raspberry PI. .NET Core is a powerful platform that includes the runtime, libraries, and compilers, with full support for languages such as C#, F#, and Visual Basic. This means you can code in C# not only on Windows, but also on different OSes because the .NET Compiler Platform (github.com/dotnet/roslyn), also referred to as “Project Roslyn,” provides open source, cross-platform compilers with rich code analysis APIs. As an important implication, you can leverage the Roslyn APIs to perform many code-related operations on different OSes, such as code analysis, code generation and compilation. This article walks through the necessary steps to set up a C# project on .NET Core to use the Roslyn APIs and explains some interesting code-generation and compilation scenarios. It also discusses some basic Reflection techniques to invoke and run code compiled with Roslyn on .NET Core. 

::::
download.page(dotnet/netcore/dotnet_cli.md)
::::
download.page(dotnet/netcore/project.json.md)
download.page(dotnet/netcore/env_vars.md)
::::
download.page(dotnet/netcore/depency_injection_ioc.md)
::::
download.page(dotnet/netcore/configuration.md)
::::
download.page(dotnet/netcore/logging.md)
::::
download.page(dotnet/netcore/dotnetcore_on_linux.md)
::::
download.page(dotnet/netcore/dotnetcore2.0.md)
::::
download.page(dotnet/netcore/dotnetcore3.0.md)


## PORTING A NET FRAMEWORK LIBRARY TO NET CORE

https://www.codeproject.com/Articles/1190475/Porting-a-NET-Framework-library-to-NET-Core
https://docs.microsoft.com/en-us/dotnet/core/porting/index

You can browse the currently available .NET core libraries at the Awesome .NET Core project. 
https://github.com/thangchung/awesome-dotnet-core/

Porting existing code to .NET Core used to be quite hard because the available API set was very small. In .NET Core 2.0, we already made this much easier, thanks to .NET Standard 2.0. Today, we’re happy to announce that we made it even easier with the Windows Compatibility Pack, which provides access to an additional 20,000 APIs via a single NuGet package. NET Core is optimized for building highly scalable web applications, running on Windows, macOS or Linux. If you’re building Windows desktop applications, then the .NET Framework is the best choice for you.

API Portability Analyzer tool 
	https://github.com/Microsoft/dotnet-apiport/
	identifying APIs that:
	Are not portable to specific platforms
	Have breaking changes between 4.x versions

The first goal of these tools are to help identify APIs that are not portable among the various .NET Platforms. Some APIs may be removed on certain platforms (such as AppDomains, File I/O, etc.), or refactored into other types (such as some Reflection APIs).

	Analyzing a directory and show breaking changes
		ApiPort.exe analyze -f C:\git\Application\bin\Debug -b

	Analyzing a directory and show any non-portable APIs
		ApiPort.exe analyze -f C:\git\Application\bin\Debug -p
    
    
## More
- https://blog.joaograssi.com/posts/2020/asp-net-core-integration-tests-with-docker-compose-github-actions/
- [use ps to call .net framework rom .net core](https://www.c-sharpcorner.com/blogs/using-systemspeech-with-net-core-30)
- https://www.tutorialsteacher.com/core/fundamentals-of-logging-in-dotnet-core
- https://www.tutorialsteacher.com/core/internals-of-builtin-ioc-container-in-aspnet-cohérent
- https://intellitect.com/ildasm-with-net-core/    
- https://contextly.com/redirect/?id=Sk2Hb09xcy:33102:3307:18:RVM=::previous:6018f9e42c6bd6-56853379
- https://medium.com/swlh/deploy-your-net-core-3-1-application-to-heroku-with-docker-eb8c96948d32