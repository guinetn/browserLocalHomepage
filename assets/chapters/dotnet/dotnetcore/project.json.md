## project.json

App portable or self-contained application using type property of Microsoft.NETCore.App dependency in project.json.
For the self-contained application, remove type-platform from the dependency. This makes it a self-contained application which means .NET Core will be included when you build and publish an application.

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp2.0</TargetFramework>
    <TargetFrameworks>netcoreapp2.0;net45;net46</TargetFrameworks>  <--- To target multiple frameworks
  </PropertyGroup>

  <ItemGroup Condition=" '$(TargetFramework)' == 'net40' ">
    <Reference Include="System.Net" />
  </ItemGroup>
  <ItemGroup Condition=" '$(TargetFramework)' == 'net45' ">
    <Reference Include="System.Net" />
  </ItemGroup>

</Project>
```

```cs
using System;

namespace MultiFrameworkConsole
{
    public class Program
    {
        public static void Main(string[] args)
        {
                    
        #if NET40
                Console.WriteLine("Target framework: .NET Framework 4.0");
        #elif NET45
                Console.WriteLine("Target framework: .NET Framework 4.5");
        #else
                Console.WriteLine("Target framework: .NET Core 2.0");
        #endif
                Console.ReadKey();
        }
    }
}
```
