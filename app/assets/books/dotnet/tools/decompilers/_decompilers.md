# .Net Decompilers

https://www.nuget.org/packages/runtime.ubuntu.18.04-x64.Microsoft.NETCore.ILAsm/

## FREE

- Online decompiler: https://www.decompiler.com/

- JustDecompile
https://www.telerik.com/products/decompiler.aspx
C:\Program Files (x86)\Progress

- https://github.com/TomSmartBishop/facile-api

- https://devextras.com/decompiler/

- dotPeek
http://www.jetbrains.com/decompiler/
Decompiling .NET 1.0-4.5 assemblies to C#
Support for .dll, .exe, .zip, .vsix, .nupkg, and .winmd files
Quick jump to a type, assembly, symbol, or type member
Effortless navigation to symbol declarations, implementations, derived and base symbols, and more
Accurate search for symbol usage with advanced presentation of search results
Overview of inheritance chains
Support for downloading code from source servers
Syntax highlighting
Complete keyboard support
dotPeek is free!


- dotnet-ildasm
    
https://www.nuget.org/packages/dotnet-ildasm/
    
install .net core runtime if required
> sudo apt-get update; \
> sudo apt-get install -y apt-transport-https && \
> sudo apt-get update && \
> sudo apt-get install -y dotnet-runtime-3.0

find required tool
>dotnet tool search ildasm
    output:
    Package ID         Latest Version      Authors      Downloads      Verified
    ---------------------------------------------------------------------------
    dotnet-ildasm      0.12.2              pjbgf        100154                 
    dotasm             1.0.1               DotAsm       434 

Install tool
>dotnet tool install -g dotnet-ildasm

Output IL to file:
Go to project folder
> cd ../project/bin/Debug/netx.x
> dotnet ildasm program.dll -o program.il

## F# snippet

```c#
open System.Reflection

[<EntryPoint>]
let main argv =
  let asm =
    argv
    |> Array.tryHead
    |> Option.map Assembly.LoadFrom
    |> Option.defaultWith (Assembly.GetExecutingAssembly)

  printfn "%s" asm.FullName

  for t in asm.GetTypes () do
    printfn " * %s" t.FullName
```



## NOT FREE

- Reflector (Not free)
https://www.red-gate.com/products/dotnet-development/reflector/

### Example


By default, in Windows PowerShell output in UTF-16
echo hello > hi.txt, then open it in notepad/vscode: format ends up in UTF-16

echo hello | out-file -encoding utf8 hi.txt

To have utf-8 default whith redirection operator? Not possible
https://superuser.com/questions/327492/default-powershell-to-emitting-utf-8-instead-of-utf-16
Using a .NET decompiler on the System.Management.Automation assembly (a.k.a. the "Microsoft Windows PowerShell Engine Core Assembly") reveals this code fragment:

Open justDecompil (Telerik, free)
Drag & Drop C:\windows\assembly\GAC_MSIL\System.Management.Automation
Search → BuildRedirectionPipeline

// class: System.Management.Automation.RedirectionNode
private PipelineProcessor BuildRedirectionPipeline(string path, ExecutionContext context)
{
    CommandProcessorBase commandProcessorBase = context.CreateCommand("out-file");
    commandProcessorBase.AddParameter("-encoding", "unicode");
    if (this.Appending)
    {
        commandProcessorBase.AddParameter("-append", true);
    }
    commandProcessorBase.AddParameter("-filepath", path);
    ...
So, it looks pretty hardcoded to me.

