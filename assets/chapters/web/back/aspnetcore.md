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

- https://developer.okta.com/blog/2019/03/21/build-secure-microservices-with-aspnet-core
- https://developer.okta.com/blog/2019/03/11/build-a-crud-app-with-aspnet-mvc-and-entity-framework
- [InProcess hosting model in asp.net core](https://www.youtube.com/watch?v=LxnjX-ZjQ64)
- https://blog.elmah.io/how-to-send-push-notifications-to-a-browser-in-asp-net-core
- https://blog.elmah.io/how-to-secure-asp-net-core-with-oauth-and-json-web-tokens
- https://blog.elmah.io/cookie-authentication-with-social-providers-in-asp-net-core
- https://blog.elmah.io/export-data-to-excel-with-asp-net-core
- https://blog.elmah.io/the-asp-net-core-security-headers-guide
- https://blog.elmah.io/oauth-authentication-with-facebook-and-aspnet-core
