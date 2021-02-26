# DotNet cli

dotnet CLI tooling comes with several built-in cmds such as build, run, test... but it turns out it’s possible to add your own verb to that list.

[Commands](https://docs.microsoft.com/en-us/dotnet/core/tools/index)

Your application can then be packaged up (using dotnet pack) and distributed through NuGet.
dotnet new [template] -t C#
dotnet new console -o myApp
dotnet new console -l F#
cd ...
code .
dotnet add [package]
dotnet restore
dotnet build
dotnet run
dotnet test
dotnet pack
dotnet publish

## CLI
dotnet [commande] --help
dotnet watch --help

dotnet --info
dotnet --list-sdks
3.1.405 [C:\Program Files\dotnet\sdk]
5.0.102 [C:\Program Files\dotnet\sdk]
dotnet  --list-runtimes
Microsoft.AspNetCore.All 2.1.24 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.All]
Microsoft.AspNetCore.App 2.1.24 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]
Microsoft.AspNetCore.App 3.0.3 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]
Microsoft.AspNetCore.App 3.1.11 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]
Microsoft.AspNetCore.App 5.0.2 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]
Microsoft.NETCore.App 2.0.0 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 2.1.24 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 3.0.3 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 3.1.11 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 5.0.2 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.WindowsDesktop.App 3.0.3 [C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App]
Microsoft.WindowsDesktop.App 3.1.11 [C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App]
Microsoft.WindowsDesktop.App 5.0.2 [C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App]

***dotnet [runtime-options] [path-to-application] [arguments]***
***dotnet [sdk-options] [command] [command-options] [arguments]***

### Exécutez une application .NET

***runtime-options***
  --additionalprobingpath <path>   Chemin contenant la stratégie de collecte et les assemblys à collecter.
  --additional-deps <path>         Chemin du fichier deps.json supplémentaire.
  --depsfile                       Chemin du fichier <application>.deps.json.
  --fx-version <version>           Version du framework partagé installé à utiliser pour exécuter l'application.
  --roll-forward <setting>         Restaurer par progression la version du framework (LatestPatch, Minor, LatestMinor, Major, LatestMajor, Disable).
  --runtimeconfig                  Chemin du fichier <application>.runtimeconfig.json.

***path-to-application***
  Chemin d'un fichier .dll d'application à exécuter.

### Exécutez une commande du kit SDK .NET

***sdk-options***
  -d|--diagnostics  Activez la sortie des diagnostics.
  -h|--help         Affichez l'aide de la ligne de commande.
  --info            Affichez les informations sur .NET.
  --list-runtimes   Affichez les runtimes installés.
  --list-sdks       Affichez les SDK installés.
  --version         Affichez la version utilisée du kit SDK .NET.

***Commandes du SDK***
add               Ajoutez un package ou une référence à un projet .NET.
build             Générez un projet .NET.
  	• Builds a .NET Core application
	• Compiles all dependencies to produce a binary executable
	• dotnet restore must have been run prior
	• Outputs binaries in child Bin folder
	Options:
	• -o/–output [Dir] | Target directory to put compiled binaries
	• -f/–framework [Framework] | Compile for a specific framework defined in project.json file
build-server      Interagissez avec les serveurs démarrés par une build.
clean             Nettoyez les sorties de build d'un projet .NET.
help              Affichez l'aide de la ligne de commande.
list              Listez les références de projet d'un projet .NET.
msbuild           Exécutez des commandes MSBuild (Microsoft Build Engine).
new               Créez un fichier ou projet .NET.

    Initializes a .NET Core application project
    • Bootstraps project with bare essential files	
    • -l/–lang | Choose preferred language | Valid choices – ‘C##/F##’
    • -t/–type | Choose preferred app type | Valid choice now – ‘console’ | May be expanded in future
    Ingredients are 
    - program.cs file with executable code
    - project.json file with all dependencies
    - NuGet.config that points to the NuGet source to resolve dependencies.	

    dotnet new [arguments] [options]
    
    * ARGUMENTS
    template  The template to instantiate.

    * OPTIONS
    -h, --help          Displays help for this command.
    -l, --list          Lists templates containing the specified name. If no name is specified, lists all templates.
    -n, --name          The name for the output being created. If no name is specified, the name of the current directory is used.
    -o, --output        Location to place the generated output.
    -i, --install       Installs a source or a template pack.
    -u, --uninstall     Uninstalls a source or a template pack.
    --interactive       Allows internal dotnet restore cmd to stop and wait for user input/action (complete authentication..)
    --nuget-source      Specifies a NuGet source to use during install.
    --type              Filters templates based on available types. Predefined values are "project", "item" or "other".
    --dry-run           Summary of happen if the given command line were run if it would result in a template creation.
    --force             Forces content to be generated even if it would change existing files.
    -lang, --language   Filters templates based on language and specifies the language of the template to create.
    --update-check      Check the currently installed template packs for updates.
    --update-apply      Check the currently installed template packs for update, and install the updates.
        
    dotnet new -all 		        list available templates
    dotnet new console -n myapp    
    dotnet new mvc -h 	    		display available options of a template
    dotnet new console -o hwapp
    cd hwapp
        
nuget             Fournit des commandes NuGet supplémentaires.
pack              Créez un package NuGet.
  	• Creates a NuGet package of your code
	• Build nupkg packages with source and debug symbols
	• NuGet dependencies of the project being packed are added to the nuspec file for resolution
	• Builds the project as first step before packaging
	Options:
	• [Path] | Specifies path to project to be packed | Defaults to the current	directory if omitted
	• -o/–output [Dir] | Directory in which built packages are placed
publish           Publiez un projet .NET à des fins de déploiement.
  	• Publishes a .NET application in a bundled container
	• Packs application and all dependencies into single folder for publishing
	• Packaging includes application’s Intermediate Language (IL) code and
	dependencies for portable applications
	• For self-contained applications, packaging includes IL, dependencies and
	runtime of the targeted platform
	Options:
	• [Path] | Specifies path to project.json of project to be published
	• -o/–output [Dir] | Directory in which the built packages are placed
	• -f/–framework [Framework] | Publish the application for a given
	framework as defined in project.json
	• -r/–runtime [Runtime] | Publish the application for a given runtime
remove            Supprimez un package ou une référence d'un projet .NET.
restore           Restaurez les dépendances spécifiées dans un projet .NET.
    • Restores the dependencies for a given project from NuGet using Project.JSon file
    • The NuGet feed source is configured in the NuGet.config file
    • By default, looks first for packages in the NuGet package cache
    Options:
    • -s/–source | Override NuGet.config source of NuGet packages
    • –packages [Dir] | Specifies the target directory for restored packages
    The first time you run dotnet restore on a fresh machine, all .NET Core basic
    dependencies will be pulled down from NuGet servers—about 100 packages.
    NuGet packages that are pulled down are cached for subsequent usage in a global
    NuGet cache, which, by default, is .nuget/packages in the user’s home directory, as
    seen below. Subsequent restoration of the same dependencies is very quick.
    C:\Users\[user]\.nuget\packages
run               Générez et exécutez une sortie de projet .NET.
  	• Runs application from source code ‘in place’
	• Combines compile, build binaries and launch into one step
	• Depends on dotnet build
	Options:
	• -f/–framework [Framework] | Runs the app for a given framework identifier
	• -p/–project [Path] | Specifies which project to run | Path points to project.json
	in the project directory
sln               Modifiez les fichiers solution Visual Studio.
store             Stockez les assemblys spécifiés dans le magasin de packages de runtime.
test              Exécutez des tests unitaires à l'aide du programme Test Runner spécifié dans un projet .NET.
  	• Executes unit tests for given project and gives you guilt if you don’t unit test
	• Uses configured test runner in project.json
	• Resolves dependencies on NUnit/XUnit and bootstraps tests as class libraries
	• Defaults to running tests in Console mode
	Options:
	• [Path] | Specifies the path to test project | Defaults to the current directory if
	omitted
	• -o/–output [Dir] | Directory in which to find binaries to run
tool              Installez ou gérez les outils qui étendent l'expérience .NET.
vstest            Exécutez des commandes VSTest (Microsoft Test Engine).

***Commandes supplémentaires d'outils groupés***
dev-certs         Créez et gérez des certificats de développement.
fsi               Démarrer F# Interactive / exécuter les scripts F#.
sql-cache         Outils en ligne de commande du cache SQL Server.
user-secrets      Gérez les secrets d'utilisateur de développement.
watch             Démarrez un observateur de fichier qui exécute une commande quand les fichiers changent
    dotnet watch run
    dotnet watch test
 
## Templates

|Templates                                      | Short Name            | Language         | Tags |
|--------------------------------------------   | -------------------   | ------------     | ---------------------- |
|Console Application                            | console               | [C#], F#, VB     | Common/Console |
|Class library                                  | classlib              | [C#], F#, VB     | Common/Library |
|WPF Application                                | wpf                   | [C#], VB         | Common/WPF |
|WPF Class library                              | wpflib                | [C#], VB         | Common/WPF |
|WPF Custom Control Library                     | wpfcustomcontrollib   | [C#], VB         | Common/WPF |
|WPF User Control Library                       | wpfusercontrollib     | [C#], VB         | Common/WPF |
|Windows Forms App                              | winforms              | [C#], VB         | Common/WinForms |
|Windows Forms Control Library                  | winformscontrollib    | [C#], VB         | Common/WinForms |
|Windows Forms Class Library                    | winformslib           | [C#], VB         | Common/WinForms |
|Worker Service                                 | worker                | [C#], F#         | Common/Worker/Web |
|Unit Test Project                              | mstest                | [C#], F#, VB     | Test/MSTest |
|NUnit 3 Test Project                           | nunit                 | [C#], F#, VB     | Test/NUnit |
|NUnit 3 Test Item                              | nunit-test            | [C#], F#, VB     | Test/NUnit |
|xUnit Test Project                             | xunit                 | [C#], F#, VB     | Test/xUnit |
|Razor Component                                | razorcomponent        | [C#]             | Web/ASP.NET |
|Razor Page                                     | page                  | [C#]             | Web/ASP.NET |
|MVC ViewImports                                | viewimports           | [C#]             | Web/ASP.NET |
|MVC ViewStart                                  | viewstart             | [C#]             | Web/ASP.NET |
|Blazor Server App                              | blazorserver          | [C#]             | Web/Blazor |
|Blazor WebAssembly App                         | blazorwasm            | [C#]             | Web/Blazor/WebAssembly |
|ASP.NET Core Empty                             | web                   | [C#], F#         | Web/Empty |
|ASP.NET Core Web App (Model-View-Controller)   | mvc                   | [C#], F#         | Web/MVC |
|ASP.NET Core Web App                           | webapp                | [C#]             | Web/MVC/Razor Pages |
|ASP.NET Core with Angular                      | angular               | [C#]             | Web/MVC/SPA |
|ASP.NET Core with React.js                     | react                 | [C#]             | Web/MVC/SPA |
|ASP.NET Core with React.js and Redux           | reactredux            | [C#]             | Web/MVC/SPA |
|Razor Class Library                            | razorclasslib         | [C#]             | Web/Razor/Library |
|ASP.NET Core Web API                           | webapi                | [C#], F#         | Web/WebAPI |
|ASP.NET Core gRPC Service                      | grpc                  | [C#]             | Web/gRPC |
|dotnet gitignore file                          | gitignore             |                  | Config |
|global.json file                               | globaljson            |                  | Config |
|NuGet Config                                   | nugetconfig           |                  | Config |
|Dotnet local tool manifest file                | tool-manifest         |                  | Config |
|Web Config                                     | webconfig             |                  | Config |
|Solution File                                  | sln                   |                  | Solution |
|Protocol Buffer File                           | proto                 |                  | Web/gRPC |


download.page(dotnet/dotnetcore/cli_usage.md)
   
   
## Extending the .NET CLI

### Add verb to `dotnet` command 

- https://mattwarren.org/2016/10/03/Adding-a-verb-to-the-dotnet-CLI-tooling/
- https://intellitect.com/ildasm-with-net-core/

Any executable found in the PATH named in this way, that is as dotnet-{command}, will be invoked by the dotnet driver.
When you run `dotnet build`, the driver will run the `dotnet-build` executable. 
All of the arguments following the command are passed to the command being invoked. 

###  
1. NuGet Packages on per-project basis
create a portable console application that runs on top of .NET Core.
Your application can then be packaged up (using dotnet pack) and distributed through NuGet. 
To consume, you simply need to make a reference to the tooling in project.json. 
The custom tooling is only available in the context of the project that references/restores the NuGet package.
Your project needs to follow the .NET CLI driver-command nomenclature of dotnet-[command]

To consume, you simply need to add a Tools section in projects’ project.json, like so:

“tools”: {
“dotnet-domything”: {
“version”: “1.0.0”,
“imports”: [“dnxcore50”]
}
}
Once dotnet restore is run on the project, the NuGet tool and all of its dependencies are resolved. 
You can then happily use the command dotnet-domything, but only in context of your project

2. System Path on per-machine basis
to build custom .NET CLI tooling that can be used across multiple projects, but only on the given machine. The one drawback is portability to another machine requires deploying the tool elsewhere

The dotnet driver can invoke any command that follows the dotnet-[command] convention. The default resolution logic will first probe several locations in the context of the project and finally fall back to the system PATH. If the requested command exists in the system PATH and is a binary that can be invoked, the dotnet driver can invoke it.

The custom binary tool can be pretty much anything that the operating system can execute. On Unix or OSX systems, this means any command script saved as dotnet-domything that has the execute bit set via chmod +x. On Windows, it means anything that Windows knows how to run.


   
## More
- https://www.tutorialsteacher.com/core/aspnet-core-program
- [Welcome to .NET Core (.Net CLI)](https://dotnet.github.io)
- [.NET Core - Cross-Platform Code Generation with Roslyn and .NET Core][https://msdn.microsoft.com/en-us/magazine/mt808499]
- [.NET API Browser](https://docs.microsoft.com/en-us/dotnet/api)
- https://github.com/hgupta9/awesome-dotnet-core
- https://github.com/quozd/awesome-dotnet#graphics
- https://github.com/auth0-blog/dotnet-core-auth
- https://intellitect.com/ildasm-with-net-core/
- https://mattwarren.org/2016/10/03/Adding-a-verb-to-the-dotnet-CLI-tooling/
