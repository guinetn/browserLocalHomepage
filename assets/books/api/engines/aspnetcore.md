# ASP NET CORE

Can be hosted in
- InProcess
    One web server
    Application hosted in the IIS worker process
    Requests to the application are handled by Asp.net core module
    Asp.net core module forwards requests to 
        IIS HTTP Server: server runnning in-process with IIS
        This results in great perf (bypasses built-in Kesterl web server of asp.net core)
- OutOfProcess
    Two web servers
    Internal: kestrel 
        cross-platform web server included by default in asp.net core project  process used to host the app is dotnet.exe
    External: IIS, Apache, NGinx

System.Diagnostics.Process.GetCurrentProcess().ProcessName
    w3wp/iisexpress (InProcess)
    dotnet/project_name (OutOfProcess)

## Identity

Configure Passwordless Authentication in ASP.NET Core Web App
https://developer.okta.com/blog/2020/12/18/how-to-use-webauthn-csharp-dotnet

https://docs.microsoft.com/en-us/aspnet/identity/

## Startup
ASP.NET Core application must include Startup class. It is like Global.asax
https://www.tutorialsteacher.com/core/aspnet-core-startup
- https://www.tutorialsteacher.com/core/aspnet-core-program

public class Program
{
    public static void Main(string[] args)
    {
        BuildWebHost(args).Run();
    }

    public static IWebHost BuildWebHost(string[] args)
    {
        WebHost.CreateDefaultBuilder(args)
            .UseStartup<Startup>()
            .Build();
    }
}

## Servers

- [Low level ASP.NET Core example web server](https://github.com/benaadams/Ben.Http)
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5

Kestrel
- [KestrelHttpServer](https://github.com/benaadams/KestrelHttpServer)
A development web server for ASP.NET vNext based on libuv

## More

- [Good intro](https://www.youtube.com/watch?v=BfEjDD8mWYg)
- https://www.ezzylearning.net/tutorial/how-to-consume-third-party-web-apis-in-asp-net-core
- https://www.ezzylearning.net/tutorial/introduction-to-asp-net-core-middleware
- https://www.ezzylearning.net/tutorial/a-step-by-step-guide-to-asp-net-core-dependency-injection
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://developer.okta.com/blog/2019/03/21/build-secure-microservices-with-aspnet-core
- https://developer.okta.com/blog/2019/03/11/build-a-crud-app-with-aspnet-mvc-and-entity-framework
- [InProcess hosting model in asp.net core](https://www.youtube.com/watch?v=LxnjX-ZjQ64)
- https://blog.elmah.io/how-to-send-push-notifications-to-a-browser-in-asp-net-core
- https://blog.elmah.io/how-to-secure-asp-net-core-with-oauth-and-json-web-tokens
- https://blog.elmah.io/cookie-authentication-with-social-providers-in-asp-net-core
- https://blog.elmah.io/export-data-to-excel-with-asp-net-core
- https://blog.elmah.io/the-asp-net-core-security-headers-guide
- https://blog.elmah.io/oauth-authentication-with-facebook-and-aspnet-core
- https://github.com/benaadams/practical-aspnetcore
- https://makolyte.com/aspdotnet-how-to-use-a-backgroundservice-for-long-running-and-periodic-tasks/
- https://www.ezzylearning.net/tutorial/13-reasons-to-learn-asp-net-core-in-2021-infographic
- https://www.tutorialsteacher.com/core/aspnet-core-startup
- https://www.tutorialsteacher.com/core/aspnet-core-program
- https://andrewlock.net/avoiding-startup-service-injection-in-asp-net-core-3/
- https://intellitect.com/quickly-configure-asp-net-core-api-to-work-with-vue-cli-3/
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5