# NuGet

C:\Users\[you]\AppData\Roaming\NuGet\NuGet.Config
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />    
    <!-- Fix: Échec de l'installation de 'Microsoft.Extensions.DependencyInjection.Abstractions'.
    Impossible de charger l'index de service pour la source https://dotnet.myget.org/F/roslyn-analyzers/api/v3/index.json -->
    <!--  <add key="Package source" value="https://dotnet.myget.org/F/roslyn-analyzers/api/v3/index.json" /> -->
    <add key="Microsoft Visual Studio Offline Packages" value="C:\Program Files (x86)\Microsoft SDKs\NuGetPackages\" />  
  </packageSources>
  <packageRestore>
    <add key="enabled" value="True" />
    <add key="automatic" value="True" />
  </packageRestore>
  <bindingRedirects>
    <add key="skip" value="False" />
  </bindingRedirects>
  <packageManagement>
    <add key="format" value="0" />
    <add key="disabled" value="False" />
  </packageManagement>
</configuration>
