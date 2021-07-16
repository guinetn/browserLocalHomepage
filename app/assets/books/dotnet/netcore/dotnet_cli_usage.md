## CLI usage


## C# REPL

1. C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\Roslyn\csi.exe
2. interactive window: View > Other Windows > C# Interactive 
3. https://dotnetfiddle.net/

C# scripting language, traditionally saved into a CSX file
for testing out your C# and .NET snippets without the effort of creating multiple unit testing or console projects.
  
#reset 32 - switches to .NET Framework 32-bit process
#reset 64 - switches to .NET Framework 64-bit process
#reset core - switches to .NET Core 64-bit process

## dotnet-script
https://github.com/filipw/dotnet-script
https://www.cs-script.net/
https://www.linqpad.net/




dotnet new webapi --no-https
dotnet new webapi -o api01 --no-https     → http://localhost:5000
dotnet new webapi -o api01                → https://localhost:5001  
dotnet add package Microsoft.EntityFrameworkCore.InMemory

dotnet new sln
dotnet new webapi --no-https
dotnet sln add .


## Scaffolding a .NET Core Application in C# (Hello world)

* program.cs
```cs
using System;
namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```
* project.json : dependencies

* nuget.config : NuGet sources to resolve dependencies

* project.csproj
```xml
<ItemGroup>
    <PackageReference Include="System.Collections" Version="4.3.0" />
</ItemGroup>
``` 
dotnet new console
dotnet add package System.Collections --version 4.3.0         
code .
dotnet build
dotnet add package Microsoft.Extensions.DependencyInjection --version 5.0.1
dotnet run       run the actual sample

https://andrewlock.net/adding-authentication-to-a-blazor-server-app-using-auth0
dotnet user-secrets init
dotnet user-secrets set "Auth0:Domain" "some-domain.eu.auth0.com"
dotnet user-secrets set "Auth0:ClientId" "ABC123someClientId"
dotnet user-secrets set "Auth0:ClientSecret" "some_random_string_of_letters"


dotnet new page -o Pages/Account -n Login -np
dotnet new page -o Pages/Account -n Logout -np
dotnet new page -o Pages/Account -n AccessDenied -np
dotnet new razorcomponent -o Shared -n LoginDisplay