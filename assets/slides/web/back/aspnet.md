# aspnet

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