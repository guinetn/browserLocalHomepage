# ASP NET CORE

2016, re-design of earlier Windows-only versions of ASP.NET.

Extends the .NET platform with tools and libraries specifically for building many types of web applications, including web pages, REST APIs, microservices, and hubs that push real-time content to connected clients.
- Base framework for web requests processing in C# or F#
- Razor: Web-page templating syntax for building C# dynamic web pages
- Libraries for common web patterns, such as Model View Controller (MVC)
- Authentication system that includes libraries, a database, and template pages for handling logins, including - multi-factor authentication and external authentication with Google, Twitter, and more.
- Editor extensions to provide syntax highlighting, code completion, and other functionality specifically for developing web pages

ASP.NET Core is the open-source and cross-platform version of ASP.NET
You should use ASP.NET Core for all new applications
Windows-only versions of ASP.NET, that existed before ASP.NET Core, is typically just referred to as ASP.NET. The majority of innovation occurs in ASP.NET Core, but other versions continue to receive minor updates and bug-fixes.

- https://github.com/dodyg/practical-aspnetcore ★★★
- https://www.red-gate.com/simple-talk/dotnet/c-programming/build-a-rest-api-in-net-core/
- https://docs.microsoft.com/fr-fr/aspnet/core/tutorials/first-web-api?view=aspnetcore-5.0&tabs=visual-studio-code

## WEB API

1. No HTTPS
HTTPS disabled to make it easier for local development

- https://docs.microsoft.com/fr-fr/learn/modules/build-web-api-aspnet-core/3-exercise-create-web-api

dotnet new webapi --no-https
dotnet new webapi -o api01 --no-https     → http://localhost:5000
dotnet new webapi -o api01                → https://localhost:5001  



  Controllers/	classes with public methods = actions = exposed as HTTP endpoints
  Program.cs	Contient une méthode Main, qui est le point d’entrée managé de l’application.
  Startup.cs	Configure des services et le pipeline des requêtes HTTP de l’application.
  ContosoPizza.csproj	Contient des métadonnées de configuration pour le projet.

  then add models, services: https://docs.microsoft.com/fr-fr/learn/modules/build-web-api-aspnet-core/5-exercise-add-data-store

dotnet build 
dotnet run  
- http://localhost:5000/weatherforecast
- http://localhost:5000/swagger

* Mini API ~ Node like
https://github.com/dodyg/practical-aspnetcore/tree/net5.0/projects/net6/map-4

```cs
using System;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();

string Plaintext() => "Hello, World!";
app.MapGet("/hello", Plaintext);

Greeting Json() => new Greeting("Hello, World!");
app.MapGet("/json", Json);

app.MapGet("/hello/{name}", (string name) => new Greeting($"Hello, {name}!"));

app.Run();

public record Greeting(string Message);
```

* REPL (Read-Eval-Print-Loop) HTTP .NET

>dotnet tool install -g Microsoft.dotnet-httprepl
>httprepl http://localhost:5000                         connect http://localhost:5000
>ls                                                     Explorez les points de terminaison disponibles
>cd WeatherForecast
>get
>get 3
>delete 3
>post -c "{"name":"Hawaii", "isGlutenFree":false}"
>put 3 -c  "{"id": 3, "name":"Hawaiian", "isGlutenFree":false}"
>exit   CTRL+C

swagger origin:
    Startup.cs
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
            services.AddSwaggerGen(c => {
                c.SwaggerDoc("v1", new OpenApiInfo { Title = "api01", Version = "v1" });
            });
        
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment()) {
                app.UseDeveloperExceptionPage();
                app.UseSwagger();
                app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "api01 v1"));
            }

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

* IN-MEMORY DATABASE
download.page(dotnet/tools/entity_framework_in_memory.md)


2. HTTPS
https://docs.microsoft.com/fr-fr/aspnet/core/tutorials/first-web-api?view=aspnetcore-5.0&tabs=visual-studio-code


Approuvez le certificat de développement HTTPS en exécutant la commande suivante :
>dotnet dev-certs https --trust
https://docs.microsoft.com/fr-fr/aspnet/core/security/enforcing-ssl?view=aspnetcore-5.0#trust-the-aspnet-core-https-development-certificate-on-windows-and-macos


## WEB APP (not api, no controller)
>dotnet new webApp -o myWebApp --no-https
    webApp  = template to use when creating your app
    -o = creates a directory named myWebApp where your app is stored.
    --no-https specifies not to enable HTTPS.

    \myWebApp
        Startup.cs          app startup code and middleware configuration
        Pages               application web pages 
            Index.cshtml
                @page                            @ = .net 'mode', razor syntax
                @model IndexModel
                @{
                    ViewData["Title"] = "Home page";
                }

                <div class="text-center">        ← classic html
                    <h1>Hello, world!</h1>
                    <p>The time on the server is @DateTime.Now</p>
                </div>
        myWebApp.csproj     libraries are referenced
>cd myWebApp
>dotnet watch run           build and start the app + rebuild/restart the app whenever you make code changes

>yo aspnet   wizard for generating a new ASP.NET Core app  
>yo aspnet [projecttype [applicationname] [uiframework]]
https://github.com/OmniSharp/generator-aspnet

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



## ASP.NET Core data-protection system 

It encrypts and decrypts sensitive data such as the authentication cookie.
Symmetric-key encryption to protect data. A key containing random data is used to encrypt the data, and the same key is used to decrypt the data.
It assumes that it will be the same app or application decrypting the data as encrypted it. That implies it has access to the same key, and knows the parameters used to encrypt the data.
The data-protection keys are designed to expire and be rotated
https://andrewlock.net/an-introduction-to-the-data-protection-system-in-asp-net-core/

## Startup

ASP.NET Core application must include Startup class. It is like Global.asax
- https://www.tutorialsteacher.com/core/aspnet-core-startup
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

- https://docs.microsoft.com/fr-fr/learn/modules/build-web-api-aspnet-core/?WT.mc_id=docs-dotnet-learn
>dotnet new webapi --no-https

- [Low level ASP.NET Core example web server](https://github.com/benaadams/Ben.Http)
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5

download.page(web/back/servers/kestrel.md)

## Enable CORS in ASP.NET Core Web API

By default, browser security doesn’t allow a web page to make requests to a different domain other than the one from where the web page is served. This restriction is called the same-origin policy.

```c#
public void ConfigureServices(IServiceCollection services)
{
    services.AddCors(policy =>
    {
        policy.AddPolicy("CorsPolicy", opt => opt
            .AllowAnyOrigin()
            .AllowAnyHeader()
            .AllowAnyMethod());
    });
 
    services.AddControllers();
}

// Also add the following line in the Configure method of Startup.cs file
app.UseCors("CorsPolicy");
```

## Logging

https://www.ezzylearning.net/tutorial/logging-in-asp-net-core-5-using-serilog

## Tutorial

https://www.youtube.com/watch?v=BfEjDD8mWYg
https://www.youtube.com/watch?v=C5cnZ-gZy2I&t=217s

download.page(api/engines/aspnetcore/identity.md)
download.page(api/engines/aspnetcore/razor.md)

## More

- [Good intro](https://www.youtube.com/watch?v=BfEjDD8mWYg)
- https://www.ezzylearning.net/tutorial/a-step-by-step-guide-to-bundling-and-minification-in-asp-net-core
- https://www.ezzylearning.net/tutorial/creating-custom-tag-helpers-in-asp-net-core

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
- https://medium.com/swlh/consuming-wsdl-services-using-asp-net-core-141fbc77924f
- https://www.ezzylearning.net/tutorial/display-live-sports-updates-using-asp-net-core-signalr
- https://www.ezzylearning.net/tutorial/implementing-crud-operations-in-blazor-server-apps