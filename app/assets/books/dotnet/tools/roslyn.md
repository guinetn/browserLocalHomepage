# ROSLYN

Provide 
- C#/VB compilers
- APIs for code analysis and refactoring

Open Source .NET Compiler Platform: 
- https://docs.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/
- https://github.com/dotnet/roslyn
- https://github.com/dotnet/roslyn-sdk

Known distinction between Visual Studio, msbuild, dotnet tool, C# compiler, runtime, SDKs...
 
download.page(code/scripting/powershell/ps_files_recursive_action.md)
 
download.page(code/editors/st3_set_build_system.md)
 
## csc.exe

C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\Roslyn\csc.exe
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\Roslyn\csi.exe

## Using Roslyn C# compiler in .NET 5

.NET 5.0 SDK Roslyn C# compiler: `csc.dll`, there is no `csc.exe` in .NET 5 SDK as Roslyn compiler is cross-platform
So it must be started with `dotnet` command. This way it can be used on Windows, Linux, MacOS…

To invoke the Roslyn compiler directly it is necessary to use the command line driver csc.{exe|dll} and since Roslyn in contrast to the old csc.exe does not reference mscorlib.dll implicitly it is necessary to pass a reference to the required dependencies, i.e. System.Runtime and System.Private.CoreLib libraries and any other required references.

The required dependencies, which are passed to the compiler, are different on different platforms, i.e. on Windows it is enough to pass System.Runtime.dll and System.Console.dll while on Ubuntu 16.04 it is necessary to pass in addition System.Private.CoreLib.dll

>time dotnet /usr/share/dotnet/sdk/2.0.0/Roslyn/csc.exe -r:/usr/share/dotnet/shared/Microsoft.NETCore.App/2.0.0/System.Private.CoreLib.dll -r:/usr/share/dotnet/shared/Microsoft.NETCore.App/2.0.0/System.Console.dll -r:/usr/share/dotnet/shared/Microsoft.NETCore.App/2.0.0/System.Runtime.dll HelloWorld.cs

The Roslyn compiler was designed in a bit different way than the previously used csc.exe and vbc.exe compilers. First of all, Roslyn is written in C# and VB.NET and is a managed .NET application. On Windows it used mainly as a common service running in a server process VBCSCompiler.exe (.dll). However, Roslyn ships with managed command line drivers, csc.exe and vbc.exe (the latest .NET SDK versions ship with csc.dll and vbc.dll) which can be used to compile source files directly from the command line. Anyway, it is exactly what the build system in .NET does, invoking Roslyn via the command line. Running a simple dotnet csc.exe -help command will print usage information which will guide in using the compiler directly from the command line



C:\Program Files\dotnet
- dotnet.exe
C:\Program Files\dotnet\sdk\5.0.102
- dotnet.dll
- dotnet.runtimeconfig.json
```yaml
{
    "runtimeOptions": {
        "tfm": "net5.0",
        "framework": {
        "name": "Microsoft.NETCore.App",
        "version": "5.0.2"
        }
    }
}
```
C:\Program Files\dotnet\sdk\5.0.102\DotnetTools
- dotnet-user-secrets.dll
- dotnet-dev-certs.dll
- dotnet-watch.dll
C:\Program Files\dotnet\sdk\5.0.102\FSharp
- fsc.exe
C:\Program Files\dotnet\sdk\5.0.102\Roslyn\bincore\
- csc.dll
- vbc.dll
- csc.runtimeconfig.json
```yaml
{
    "runtimeOptions": {
        "tfm": "netcoreapp3.1",
        "framework": {
        "name": "Microsoft.NETCore.App",
        "version": "5.0.2"
        },
        "rollForwardOnNoCandidateFx": 2,
        "configProperties": {
        "System.GC.Server": true
        }
    }
}
```

* References are in 
- C:\Program Files\dotnet\shared\Microsoft.NETCore.App\5.0.2
- C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App\5.0.2
- C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App\5.0.2
- mscorlib.dll
- coreclr.dll
- System.Collections.dll
- System.Collections.Concurrent.dll
- System.Collections.Specialized.dll
- System.Configuration.dll
- System.Console.dll
- System.Data.dll
- System.dll
- System.Linq.dll
- System.Runtime.dll
- ...
- createdump.exe
- Microsoft.NETCore.App.deps.json

* C:\Program Files\dotnet\templates\5.0.2
Templates for `dotnet new` zipped in .nupkg

### compile with roslyn

Program.cs
```cs
// Minimalist file using the C#9 'Top-level statements'
CompilerDemo.PrintConsole.Print($"CompilerDemo executed on {(System.Runtime.InteropServices.RuntimeInformation.OSDescription)} with {(System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription)} today :) at: {(System.DateTime.Now.ToLongTimeString())}");
```
  
PrintConsole.cs
```cs
using System;
namespace CompilerDemo
{
    public static class PrintConsole
    {
        public static void Print(string text)
        {
            Console.WriteLine(text);
        }
    }
}
```

```sh
dotnet "C:\Program Files\dotnet\sdk\5.0.100-rc.1.20452.10\Roslyn\bincore\csc.dll" 
-r:"C:\Program Files\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Private.CoreLib.dll" 
-r:"C:\Program Files\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Console.dll" 
-r:"C:\Program Files\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Runtime.dll" 
-r:"C:\Program Files\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Runtime.InteropServices.RuntimeInformation.dll" *.cs -out:CompilerDemo.dll
```
I get CompilerDemo.dll assembly which is runtime dependent .NET console application
I need `dotnet` command to start it
>dotnet CompilerDemo.dll
But wait, when I execute my app I get:
>dotnet Jenx.CscDemo.dll
Cannot use file stream for [C:\....\demo\CompilerDemo.deps.json]: No such file or directory
A fatal error was encountered. The library 'hostpolicy.dll' required to execute the application was not found
Failed to run as a self-contained app.
- The application was run as a self-contained app because 'C:\...\CompilerDemo.runtimeconfig.json' was not found.
- If this should be a framework-dependent app, add the 'C:\...CompilerDemo.runtimeconfig.json' file and specify the appropriate framework.

To run the resulting executable with dotnet HelloWorld.exe a corresponding HelloWorld.runtimeconfig.json has to be created, containing the targeting .NET Core runtime version
 
Therefore, create new file named CompilerDemo.runtimeconfig.json with following content:
This is basically runtime info telling which framework is my app targeting. Now everything works as expected:
{
  "runtimeOptions": {
    "tfm": "net5.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "5.0.0-rc.1.20451.14"
    }
  }
}

>dotnet CompilerDemo.dll

### Compile

```cs
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Test {
    
	public class Program {

    	public static void Main() {
    	}
   }
}
```

dotnet C:\Progra~1\dotnet\sdk\5.0.102\Roslyn\bincore\csc.dll test.cs
	test.cs(1,7): error CS0246: Le nom de type ou d'espace de noms 'System' est introuvable (manque using ou une référence d'assembly?)
	test.cs(13,15): error CS0518: Le type prédéfini 'System.Object' n'est pas défini ou importé
	test.cs(15,20): error CS0518: Le type prédéfini 'System.Void' n'est pas défini ou importé

dotnet C:\Progra~1\dotnet\sdk\5.0.102\Roslyn\bincore\csc.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Private.CoreLib.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Runtime.dll test.cs

error CS0234: Le nom de type ou d'espace de noms 'Linq' n'existe pas dans l'espace de noms 'System' (vous manque-t-il une référence d'assembly ?)
Fix:
-r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Linq.dll

dotnet C:\Progra~1\dotnet\sdk\5.0.102\Roslyn\bincore\csc.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Private.CoreLib.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Runtime.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Linq.dll test.cs

error CS0103: Le nom 'Console' n'existe pas dans le contexte actuel
Fix:
-r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Console.dll test.cs

dotnet C:\Progra~1\dotnet\sdk\5.0.102\Roslyn\bincore\csc.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Private.CoreLib.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Runtime.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Linq.dll -r:C:\Progra~1\dotnet\shared\Microsoft.NETCore.App\5.0.2\System.Console.dll test.cs

>dotnet test.exe
Cannot use file stream for [I:\_langs\c#\test.deps.json]: No such file or directory
A fatal error was encountered. The library 'hostpolicy.dll' required to execute the application was not found in 'I:\_langs\c#\'.
Failed to run as a self-contained app.
  - The application was run as a self-contained app because 'I:\_langs\c#\test.runtimeconfig.json' was not found.
  - If this should be a framework-dependent app, add the 'I:\_langs\c#\test.runtimeconfig.json' file and specify the appropriate framework.

Fix: create a file test.runtimeconfig.json
This is basically runtime info telling which framework is my app targeting. Now everything works as expected:

test.runtimeconfig.json
{
  "runtimeOptions": {
    "tfm": "net5.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "5.0.2"
    }
  }
}
>dotnet test.exe


##

/Src/Roslyn.sln → Build → Binaries → csc.exe…
C:\Users\<you>\Documents\Visual Studio 2015\Projects\roslyn\Binaries\Debug>csc.exe
Visual Studio: View -> Other Windows -> Roslyn Syntax Visualizer

```c#
public static void Main(string[] args)
{
    SyntaxTree tree = CSharpSyntaxTree.ParseText(
    @"using System;
    using System.Collections.Generic;
    using System.Text;
    namespace HelloWorld
    {
    class Program
    {
    static void Main(string[] args)
    {
    Console.WriteLine(""Hello, TDN!"");
    }
    }
    }");
    var root = (CompilationUnitSyntax)tree.GetRoot();
    var compilation = CSharpCompilation.Create("HelloTDN")
    .AddReferences(references: new[] { MetadataReference.CreateFromAssembly(typeof(object).Assembly) })
    .AddSyntaxTrees(tree);
}

SemanticModels

var model = compilation.GetSemanticModel(tree);
var nameInfo = model.GetSymbolInfo(root.Usings[0].Name);
var systemSymbol = (INamespaceSymbol)nameInfo.Symbol;
foreach (var ns in systemSymbol.GetNamespaceMembers())
{
    Console.WriteLine(ns.Name);

```

## More

- [Use Roslyn to Write a Live Code Analyzer for Your API](msdn.com/magazine/dn879356)
- [Adding a Code Fix to Your Roslyn Analyzer](msdn.com/magazine/dn904670)
- [Maximize Your Model-View-ViewModel Experience with Roslyn](msdn.com/magazine/mt703435)
- [ How Microsoft rewrote its C# compiler in C# and made it open source](https://medium.com/microsoft-open-source-stories/how-microsoft-rewrote-its-c-compiler-in-c-and-made-it-open-source-4ebed5646f98)
- [ps compiler](https://github.com/IntelliTect/EssentialCSharp/tree/v8.0)
- https://stackoverflow.com/questions/46065777/is-it-possible-to-compile-a-single-c-sharp-code-file-with-the-net-core-roslyn-c