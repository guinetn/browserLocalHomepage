# Configuration

Many configuration providers easily extensible with a custom provider
configuration API supports configuration providers for in-memory .NET objects, INI files, JSON files, XML files, command-line arguments, environment variables, an encrypted user store, and any custom provider you create

Each provider is located in its own NuGet package where the NuGet package name corresponds to the provider: 
***Configuration Providers***
- InMemoryConfigurationProvider
- JsonFileConfigurationProvider for Config.json,Config.Production.json
- EnvironmentVariableConfigurationProvider
- CommandLineConfigurationProvider

All configuration keys (names) are case-insensitive
Although configurations can be updated they are not persisted back into the original store

## IConfigurationProvider 

Each type of configuration mechanism has a corresponding configuration provider class that implements IConfigurationProvider

In the majority of built-in provider implementations, the implementation is jump-started by deriving from ConfigurationBuilder rather than using custom implementations for all of the interface methods. Perhaps surprisingly, there’s no direct reference to any of the providers in Figure 1. This is because instead of manually instantiating each provider and registering it with the ConfigurationBuilder class’s Add method, each provider’s NuGet pacakge includes a static extension class with IConfigurationBuilder extension methods. (The name of the extension class is generally identified by the suffix ConfigurationExtensions.) With the extension classes, you can start accessing the configuration data directly from ConfigurationBuilder (which implements IConfigurationBuilder) and directly call the extension method associated with your provider. For example, the JSonConfigurationExtensions class adds AddJsonFile extension methods to IConfigurationBuilder so that you can add the JSON configuration with a call to Configuration­Builder.AddJsonFile(fileName, optional).Build();.

![](assets/books/dotnet/assets/configuration.png) 

## NuGet packages
Microsoft.Extensions.Configuration
Microsoft.Extensions.Configuration.EnvironmentVariables. optionally allows for a key prefix, will load only those environment variables with the specified prefix
Microsoft.Extensions.Configuration.Ini
Microsoft.Extensions.Configuration.Json to leverage JSON files for your configuration
Microsoft.Extensions.Configuration.Xml
Microsoft.Extensions.Configuration.CommandLine 
Microsoft.Exten­sions.Configuration.Binder 
Microsoft.Extensions.Configuration.Abstractions to create you're own by implementing these interfaces
Microsoft.Extensions.Configuration.User­Secrets
 

 
## Configuration
Microsoft.Extensions.Configuration
→ ConfigurationBuilder to access the configuration
Providers use IConfigurationBuilder extension methods, ex: AddInMemoryCollection() takes a Dictionary<string,string> instance of the configuration name-value pairs, which it uses to initialize the configuration provider before adding it to the ConfigurationBuilder instance. 
Once the configuration builder is "configured" you invoke its Build() method to retrieve the configuration.

A configuration is simply a hierarchical list of name-value pairs in which the nodes are separated by a colon
SampleApp:Users:Inigo­Montoya:MaximizeMainWindow
SampleApp:AllUsers:Default:MaximizeMainWindow
Any stored value maps to a string, and there’s built-in binding support that allows you to deserialize settings into a custom POCO object.

Console.WriteLine($"Hello {Configuration["Profile:UserName"]}");
Configuration.Get<int>("AppConfiguration:MainWindow:ScreenBufferSize", 80);
Optional argument following the key, for which you can specify a default value to return when the key doesn’t exist. (Without the default value, the return will be assigned default(T), rather than throw an exception as you might expect.)
 
InMemoryConfigurationProvider 
```cs
public class Program
{
  static public string DefaultConnectionString { get; } =
    @"Server=(localdb)\\mssqllocaldb;Database=SampleData-0B3B0919-C8B3-481C-9833-
    36C21776A565;Trusted_Connection=True;MultipleActiveResultSets=true";
  static IReadOnlyDictionary<string, string> DefaultConfigurationStrings{get;} = new Dictionary<string, string>() {
      ["Profile:UserName"] = Environment.UserName,
      [$"AppConfiguration:ConnectionString"] = DefaultConnectionString,
      [$"AppConfiguration:MainWindow:Height"] = "400",
      [$"AppConfiguration:MainWindow:Width"] = "600",
      [$"AppConfiguration:MainWindow:Top"] = "0",
      [$"AppConfiguration:MainWindow:Left"] = "0",
    };
  static public IConfiguration Configuration { get; set; }
  public static void Main(string[] args = null)
  {
    ConfigurationBuilder configurationBuilder = new ConfigurationBuilder();
      // 1. initialize the configuration provider
      configurationBuilder.AddInMemoryCollection(DefaultConfigurationStrings);
      Configuration = configurationBuilder.Build(); // invoke Build() to retrieve the configuration
      // Retrieving strings
      Console.WriteLine($"Hello {Configuration["Profile:UserName"]}");
      // Retrieve values via the ConfigurationBinder’s Get<T> extension methods
      ConsoleWindow consoleWindow = Configuration.Get<ConsoleWindow>("AppConfiguration:MainWindow");
      ConsoleWindow.SetConsoleWindow(consoleWindow);
  }
}
```

Adding Multiple Configuration Providers—the Last One Specified Takes Precedence
```cs
public static void Main(string[] args = null)
{
  ConfigurationBuilder configurationBuilder = new ConfigurationBuilder();
  configurationBuilder.AddInMemoryCollection(DefaultConfigurationStrings)
                      .AddJsonFile("Config.json", true) // Bool indicates file is optional "EssentialDotNetConfiguartion" is an optional prefix for all environment configuration keys, but once used, only environment variables with that prefix will be found        
                    .AddEnvironmentVariables("EssentialDotNetConfiguration")
                    .AddCommandLine( args, GetSwitchMappings(DefaultConfigurationStrings));
                
  Console.WriteLine($"Hello {Configuration["Profile:UserName"]}");
  AppConfiguration appConfiguration = Configuration.Get<AppConfiguration>(nameof(AppConfiguration));
}

static public Dictionary<string,string> GetSwitchMappings(IReadOnlyDictionary<string, string> configurationStrings) {
  return configurationStrings.Select(item =>
    new KeyValuePair<string, string>( "-" + item.Key.Substring(item.Key.LastIndexOf(':')+1), item.Key))
      .ToDictionary( item => item.Key, item=>item.Value);
}
```

Config.json
```js
{
  "AppConfiguration": {
    "MainWindow": {
      "Height": "400",
      "Width": "600",
      "Top": "0",
      "Left": "0"
    },
    "ConnectionString":
      "Server=(localdb)\\\\mssqllocaldb;Database=Database-0B3B0919-C8B3-481C-9833-
      36C21776A565;Trusted_Connection=True;MultipleActiveResultSets=true"
  }
}
```

## User­Secrets

Microsoft.Extensions.Configuration system has built-in support for reading encrypted values
Microsoft.Extensions.Configuration.User­Secrets to access the secure store by using IConfigurationBuilder.AddUserSecrets() extension method
>user-secret set <secretName> <value> [--project <projectPath>]


## More
- https://intellitect.com/essential-net-configuration-in-net-core-msdn/