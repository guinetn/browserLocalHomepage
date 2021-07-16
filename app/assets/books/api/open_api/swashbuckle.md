# swashbuckle

https://www.nuget.org/packages/Swashbuckle.AspNetCore/

Swagger tools for documenting API's built on ASP.NET Core

The most popular OpenAPI-generating package for ASP.NET Core
Used not only by the Swagger Codegen project, but also by the ASP.NET Core 5 Web API templates (catch the HTTP APIs session from .NET Conf where we highlight these updates to the Web API template). Swashbuckle emits Swagger/OpenAPI 2.0, 3.0, and 3.0 YAML, and can output the Swagger UI test page to make testing and documenting your APIs easy.


- https://github.com/davidfowl/Swashbuckle.AspNetCore
- https://github.com/dodyg/practical-aspnetcore/tree/net5.0/projects/net6/map-4


- https://github.com/beautifulcoder/BuildRestApiNetCore

>dotnet add package Swashbuckle.AspNetCore

```c#
// ConfigureServices:
services.AddSwaggerGen(c => c.SwaggerDoc("v1", new OpenApiInfo
{
  Title = "Products",
  Description = "The ultimate e-commerce store for all your needs",
  Version = "v1"
}));

// enable this in Configure:
app.UseSwagger();
app.UseSwaggerUI(opt => opt.SwaggerEndpoint("/swagger/v1/swagger.json", "Products v1"));

// http://localhost:5000/swagger
```
