# asp.net

Extends the .NET platform with tools and libraries specifically for building many types of web applications, including web pages, REST APIs, microservices, and hubs that push real-time content to connected clients.
- Base framework for web requests processing in C# or F#
- Razor: Web-page templating syntax for building C# dynamic web pages
- Libraries for common web patterns, such as Model View Controller (MVC)
- Authentication system that includes libraries, a database, and template pages for handling logins, including - multi-factor authentication and external authentication with Google, Twitter, and more.
- Editor extensions to provide syntax highlighting, code completion, and other functionality specifically for developing web pages

ASP.NET Core is the open-source and cross-platform version of ASP.NET
You should use ASP.NET Core for all new applications
Windows-only versions of ASP.NET, that existed before ASP.NET Core, is typically just referred to as ASP.NET. The majority of innovation occurs in ASP.NET Core, but other versions continue to receive minor updates and bug-fixes.

## Encrypt App.settings

web.config
```xml
    <configSections>
    <section name="secureAppSettings" type="System.Configuration.NameValueSectionHandler, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
    </configSections
    ...
    <AppSettings>
     <add key="..." value="XXXXX"/>
     <add key="..." value="XXXXX"/>
    </AppSettings>
    <secureAppSettings>
     <add key="Password" value="XXXXXXXX"/>
    </secureAppSettings>
```
    
cd C:\Windows\Microsoft.NET\Framework\v4.0.30319
aspnet_regiis.exe -pef "secureAppSettings" "your application web config path" -prov "DataProtectionConfigurationProvider"    

Accessing appsettings encrypted key value from .NET code

```cs
using System.Collections.Specialized;
var passwordValue = "";
var section = System.Web.Configuration.WebConfigurationManager.GetSection("secureAppSettings") as NameValueCollection;
if (section != null && section["Password"] != null)
{
passwordValue = section["Password"];
}
```
## More
- https://www.c-sharpcorner.com/blogs/how-to-encrypt-a-appsettings-key-in-webconfig