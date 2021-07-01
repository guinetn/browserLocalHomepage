## Environment Variable

Debug tab --> Environment Variables

IHostingEnvironment service includes EnvironmentName property which contains the value of ASPNETCORE_ENVIRONMENT variable. ASP.NET Core also includes extension methods to check the environment such as IsDevelopment(), IsStating(), IsEnvironment() and IsProduction()

```cs
public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
    if (env.IsEnvironment("Development"))
    {
        // code to be executed in development environment 

    }
    if (env.IsDevelopment())
    {
    // code to be executed in development environment 

    }
}
```
