# NuGet

Open platform for sharing finished code packages with .NET developers around the world.
From DLLs to other content needed in the projects that consume these packages, the Microsoft-supported mechanism for sharing code is NuGet, which defines how packages for .NET are created, hosted, and consumed, and provides the tools for each of those roles.

Chocolatey is empowered by NuGet and PowerShell technology. Created by Microsoft, NuGet is a framework developed for the purposes of bundling code into “packages.” Besides NuGet Chocolatey uses PowerShell (a cross-platform task automation and configuration management framework) to add some functionality that helps to install and update packages.

to include dev development libraries in apps. Chocolatey is a binary machine package manager.

vs studio: Right-click solution → Manage Nuget packages

C:\Users\[you]\AppData\Roaming\NuGet\NuGet.Config

```xml

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

```

## more

- https://www.ctrl-alt-suppr.dev/2021/03/31/tips-tricks-creer-un-package-nuget/
- https://channel9.msdn.com/Series/NET-Core-101/NET-Using-a-Nuget-Package




## NuGet: A way of adding/updating assemblies references to a project

	http://www.nuget.org
	http://nugetmusthaves.com 		Best NuGet Packages
	https://neelbhatt.com/2018/06/23/guide-to-create-and-publish-nuget-packages-using-net-core-cli-net-core-cli-part-ii/
	http://nuget.codeplex.com/wikipage?title=Package%20Manager%20Console%20Command%20Reference%20(v1.3)

## The package manager for the Microsoft development platform including .NET.

	The NuGet client tools provide the ability to
		produce
			You can develop your own package and share it via the NuGet Gallery
		consume packages
			The NuGet Gallery is the central package repository used by all package authors and consumers.

## When you use NuGet to

		.install a package, it copies the library files to your solution and automatically updates
		your project (add references, change config files, etc.).

		. remove a package, NuGet reverses whatever changes it made so that no clutter is left.

	Develop your own package
		You can share it via the NuGet Gallery.
		Read the documentation for more details on how to create and publish a package.
		http://docs.nuget.org/docs/creating-packages/creating-and-publishing-a-package
		If you don´t plan on submitting a package, there´s no need to register.


# .nuspec file 

	serves as the "blueprint" for your NuGet package (.nupkg). 
    A .nuspec file describes the contents of your NuGet package.

## A .nuspec file is an XML manifest that contains package metadata. This manifest is used both to build the package and to provide information to consumers. The manifest is always included in a package.

    coders.nuspec
    <?xml version="1.0" encoding="utf-8"?>
    <package xmlns="http://schemas.microsoft.com/packaging/2012/06/nuspec.xsd">
      <metadata>
        <id>Decoders_Package</id>
        <version>1.0.0-Iteration1-Release</version>
        <authors>ZN5573</authors>
        <owners>ZN5573</owners>
        <licenseUrl>http://example.com</licenseUrl>
        <projectUrl>http://example.com</projectUrl>
        <requireLicenseAcceptance>false</requireLicenseAcceptance>
        <description>Package of the coders</description>    
        <releaseNotes>Bug fixes and performance improvements</releaseNotes>
        <copyright>Copyright 2017</copyright>
        <tags>OctopusDeploy</tags>       
      </metadata>
       <files>
         <file src="..\..\bin\common\coders\*.dll" target="coders" />
        </files>
    </package>

    $currentScriptDir = Split-Path -parent $PSCommandPath
    $nugetSource = "HeadendPackages"
    $nugetPath = [System.IO.Path]::Combine($currentScriptDir, "..\..\tools\NuGet\nuget.exe")

    build.ps1
    # Decoders are packed and pushed to octopus library
    &$nugetPath pack [System.IO.Path]::Combine($currentScriptDir, "decoders.nuspec")
    &$nugetPath push [System.IO.Path]::Combine($currentScriptDir, "Decoders_Package.5.0.0-Iteration1-Release.nupkg") -ApiKey API-AWF5H45KMKVIHQPN27OW75YG-Source http://dev-a-build-03:8080/nuget/packages?replace=true



# Hosting your own NuGet feeds
[Lightweight standalone NuGet server](https://www.nuget.org/packages/NuGet.Server/)
https://docs.microsoft.com/en-us/nuget/hosting-packages/overview


# PACKAGES SAMPLES

	EntityFramework
	Json.NET
	jQuery
	BootStrap
	NInject
	Log4Net
	NUnit
	Caliburn.Micro
	ELMAH (Error Logging Modules and Handlers)

	PM>install-packageMvcScaffold
	PM>Add-MvcView Empty
	Added file 'Views\Empty.aspx'

# MANAGING NUGET PACKAGES FROM VS

## INSTALLL A PACKAGE

	 	Tools → Library Package Manager → Manage NuGet Packages
	 	or
		Solution Explorer → "References" right-click → click "Manage NuGet Packages"

		Select "online" then "Install"
		A new folder named "packages" is created in your solution folder
		If your app.config or web.config file required changes, those have been applied.

		If the package you are installing is dependent on other packages, NuGet installs them also if they are not already installed.
		If the package requires license acceptance, you will not be prompted in a dialog box.
		Instead, a message states that your use of the library constitutes license acceptance.

			When installing a package from nuget.org, files go through the following flow:

				nupkg file is downloaded from nuget.org and saved in a cache (max of 100 packages cached) here:
				%LocalAppData%\NuGet\Cache
				 
				nupkg file is copied into the solution packages folder:
				D:\git\jeffhandley\MyAwesomeSolution\packages
				 
				When the project is built, binaries from the package are copied into the project’s bin folder:
				D:\git\jeffhandley\MyAwesomeSolution\CoolProject\bin
				The 3rd party is of course standard build behavior that is not specific to NuGet.

	REMOVE/UPDATE A PACKAGE
		Open the Manage NuGet Packages dialog and make sure the Installed Packages tab is selected to display
		the list of installed packages.


## PACKAGE VISUALIZER

 			In VS ultimate!	Tools → Library Package Manager → Package Visualizer



# PACKAGE MANAGER CONSOLE

 	VS menu → Tools → Library Package Manager → Package Manager Console

 	The Package Manager Console is a PowerShell console within Visual Studio used to interact with NuGet and automate Visual Studio.
 	Commands Ref: http://docs.nuget.org/docs/Reference/Package-Manager-Console-PowerShell-Reference

 	Help
 			get-help xxx
 			get-help Install-Package

 	Find
 			Find-Package markdown

 	Install
 			Install-Package xxx
 			Install-Package EntityFramework

 			Uninstall-Package xxx
 			Uninstall-Package EntityFramework

 	Update packages
 	 		Get-Package				List installed packages
 	 		Get-Package -updates 	Check if there are newer versions available for any installed packages
			Update-Package xxx
			Update-Package jQuery


http://nuget.codeplex.com/wikipage?title=Package%20Manager%20Console%20Command%20Reference%20(v1.3)


# CREATING A NUGET PACKAGE #1

	http://ebooks.syncfusion.com/downloads/azure-devops-succinctly/azure-devops-succinctly.pdf

	Open Visual Studio
	Create a new Class Library (.NET Standard) project. 
	Name it "SuccinctlyPackage"
	Enter a property in the default Class1 (for example, a Name property). 
	Also make sure the class is public. This will be our package.

	namespace SuccinctlyPackage
	{
		public class Class1
		{
			public string Name { get; set; }
		}
	}
	
	Open the project file 
	Add a GeneratePackageOnBuild element to the	PropertyGroup. 
	The entire .csproj file should look as follows.
	
	<Project Sdk="Microsoft.NET.Sdk">
	  <PropertyGroup>
		<TargetFramework>netstandard2.0</TargetFramework>
		<GeneratePackageOnBuild>true</GeneratePackageOnBuild>
  	  </PropertyGroup>
	</Project>

	Build
	 when you build the project
	 a .nupkg file is created in your bin\Debug folder 
	 							  (or bin\Release when you make a release build)

	Publish it to our feed
		dotnet nuget push

# CREATING A NUGET PACKAGE #2

	http://www.hanselman.com/blog/CreatingANuGetPackageIn7EasyStepsPlusUsingNuGetToIntegrateASPNETMVC3IntoExistingWebFormsApplications.aspx

	1. Get (NuGet.exe)[http://nuget.codeplex.com/releases] command line and put it in your PATH

	2. Create a New Folder for your package
	   nuget.exe spec  → Package.nuspec

	<?xml version="1.0"?>
	<package xmlns="http://schemas.microsoft.com/packaging/2010/07/nuspec.xsd">
	  <metadata>
	    <id>Package</id>
	    <version>1.0</version>
	    <authors>Author here</authors>
	    <owners>Owner here</owners>
	    <licenseUrl>http://LICENSE_URL_HERE_OR_DELETE_THIS_LINE</licenseUrl>
	    <projectUrl>http://PROJECT_URL_HERE_OR_DELETE_THIS_LINE</projectUrl>
	    <iconUrl>http://ICON_URL_HERE_OR_DELETE_THIS_LINE</iconUrl>
	    <requireLicenseAcceptance>false</requireLicenseAcceptance>
	    <description>Package description</description>
	    <tags>Tag1 Tag2</tags>
	    <dependencies>
	      <dependency id="SampleDependency" version="1.0" />
	    </dependencies>
	  </metadata>
	</package>
	
	3. CREATE A 'CONTENT' FOLDER, ADD THINGS (Files…) INSIDE

	4. TO MODIFY/TRANSFORM A FILE DURING INSTALLATION

### A. CONFIGURATION FILE TRANSFORMATIONS

			web.config.transform

			<configuration>
			    <system.webServer>
			        <modules>
			            <add name="MyNuModule" type="Sample.MyNuModule" />   ← This line will added in the project´s 'web.config' file
			        </modules>
			    <system.webServer>
			</configuration>

			More items:

			<configuration>
			    <system.web>
			        <httpModules>
			            <add name="ErrorLog" type="Elmah.ErrorLogModule, Elmah" />
			        </httpModules>
			        <httpHandlers>
			            <add verb="POST,GET,HEAD" path="elmah.axd"
			              type="Elmah.ErrorLogPageFactory, Elmah" />
			        </httpHandlers>
			    </system.web>
			    <system.webServer>
			        <validation validateIntegratedModeConfiguration="false" />
			        <modules>
			            <add name="ErrorLog" type="Elmah.ErrorLogModule, Elmah" />
			        </modules>
			        <handlers>
			            <add name="Elmah" verb="POST,GET,HEAD" path="elmah.axd"
			              type="Elmah.ErrorLogPageFactory, Elmah" />
			        </handlers>
			    </system.webServer>
			</configuration>

			Support for XML-Document-Transform (XDT)
			Xdt is a powerful xml syntax for manipulating the structure of an XML DOM
			http://msdn.microsoft.com/en-us/library/dd465326.aspx

			web.config.install.xdt
			…	
			<add name="MyNuModule" type="Sample.MyNuModule" xdt:Transform="Insert" />  	
			<add name="MyNuModule" xdt:Transform="Remove" xdt:Locator="Match(name)" />

### B. SOURCE CODE TRANSFORMATIONS

			Pre-process the source to use current´s project context (names, namespaces…) by including Visual 
			Studio project properties ($……) in the code
		 	 				  ↓
						RootNamespace, LocalPath, FileName, AssemblyName... 
						http://msdn.microsoft.com/en-us/library/vslangproj.projectproperties_properties(VS.80).aspx

			Add .pp extension to files to transform automatically by NuGet: HomeController.cs  →  HomeController.cs.pp
			In the .pp files, add tokens to be replaced (at install-time) by the project´s context for that package
			NuGet transforms the files, removes the .pp extension, and adds them to the target project’s directory

		 				 project’s root namespace
		 					↓
			namespace $rootnamespace$.Models {
			    public struct CategoryInfo {
			        public string categoryid;
			        public string description;
			        public string htmlUrl;
			        public string rssUrl;
			        public string title;
			    }
			}
		
	5. ADD POWERSHELL SCRIPT 

		If needed, especially for adding references
		Most package wont need much PowerShell, but some do. 
		You can have an install.ps1 and an uninstall.ps1 and do lots of things. 
		These go in a folder called Tools that is next to Content (not inside.)

		install.ps1
		param($installPath, $toolsPath, $package, $project) 
		if ($host.Version.Major -eq 1 -and $host.Version.Minor -lt 1) 
		{ 
		    "NOTICE: This package only works with NuGet 1.1 or above. Please update your NuGet install at http://nuget.codeplex.com. Sorry, but you're now in a weird state. Please 'uninstall-package AddMvc3ToWebForms' now."
		}
		else
		{
		    $project.Object.References.Add("Microsoft.CSharp"); 
		    $project.Object.References.Add("System.Web.Mvc"); 
		    $project.Object.References.Add("Microsoft.Web.Infrastructure"); 
		    $project.Object.References.Add("System.Web.WebPages"); 
		    $project.Object.References.Add("System.Web.Razor"); 
		    $project.Object.References.Add("System.ComponentModel.DataAnnotations"); 
		}

	4. PACK & SUBMIT YOUR PACKAGE

		nuget.exe pack	  → ….nupkg

### Login to the (NuGet Gallery)[http://www.nuget.org/] and Contribute Your Package...






## Update-Package -reinstall       Reinstall a Package

    https://docs.microsoft.com/en-us/nuget/what-is-nuget
    flow of packages between creators, hosts, and consumers

    https://docs.microsoft.com/en-us/nuget/tools/nuget-exe-cli-reference
    Consumption config, help, install, list, locals, restore, setapikey, sources, update
    Creation    config, help, init, pack, spec
    Publishing  add, config, delete, help, list, push, setapikey, sources

    sources
        https://suezsmartsolutions.pkgs.visualstudio.com/_packaging/HeadendPackages/nuget/v3/index.json
        https://api.nuget.org/v3/index.json

    My nuget_token (on vsts, "add" a Personal access tokens)
        dbzh7obrdsitmwc5djks4dlcgi4jhg24ivgkctpy4iu3xgz26tva

## VS → Tools → Nuget → package manager parameters

    nuget sources remove -name "HeadendPackages"
    nuget sources add -name "HeadendPackages" -source "https://suezsmartsolutions.pkgs.visualstudio.com/_packaging/HeadendPackages/nuget/v3/index.json" -username <Your user name here> -password <Your access token here>

    nuget sources add -name "HeadendPackages" -source "https://suezsmartsolutions.pkgs.visualstudio.com/_packaging/HeadendPackages/nuget/v3/index.json" -username nicolas.guinet.ext@suezenvironnement.com -password dbzh7obrdsitmwc5djks4dlcgi4jhg24ivgkctpy4iu3xgz26tva

    nuget list

    use the Newtonsoft.Json API in the app
    https://docs.microsoft.com/en-us/nuget/quickstart/use-a-package


# SOME NUGET PACKAGES

[Humanizer: humanize text](https://www.youtube.com/watch?v=bLKXqJwRNSY&t=1s)
"car".Pluralize()
3501.ToWords()