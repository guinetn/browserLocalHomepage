# .Net 6.0

Final .NET unification plan started with .NET 5 

## Minimal API -  C# 10
Great for building small services
Making http://ASP.NET to be like NodeJS
https://github.com/davidfowl/CommunityStandUpMinimalAPI

1.
var app = WebApplication.Create(args);
if (Environment.GetEnvironmentVariable("APP_ENV") == "dev") {
    app.UseDebugExceptionPage();
}
app.Get("/", () => "Hello World");
...
app.Post("/echo", (JsonObject todo) => Response.Ok(todo));
app.Run();

2. 
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
if (app.Environment .IsDevelopment())
{
app.UseDevelLoperExceptionPage() ;
}
app.MapGet("/", () => "Hello World!");
app.MapGet("/hello/{name}", (string name) => $"Hello {name}");
app.MapGet("/json", () => new { Name = "Jonh Doe", Age = 23 });
app.MapGet("/json-advanced", () => Results.Json(new { Name = "Jonh Doe", Age = 23 }, statusCode: 201));
app.MapGet("/nocontent", () => Results.NoContent());
app.MapGet("/notfound", () => Results.NotFound());
app.MapGet("/problem", () => Results.Problem("This is the problem details", statusCode: 400));
app.MapPost("/json-echo", (JsonObject todo) => Results.Ok(todo));
app.Run();


##### Articles

- https://devblogs.microsoft.com/dotnet/announcing-net-6-preview-1/
- https://www.i-programmer.info/news/89/14371.html
- [Build an Android app with .NET 6](https://nicksnettravels.builttoroam.com/android-net-6/)