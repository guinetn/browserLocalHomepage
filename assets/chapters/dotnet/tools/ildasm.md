# Ildasm - Intermediate Language Disassembler

CIL code Diassembler Tool that convert CIL code into text: to view the assembly content of all classes and methods available in .NET application.
Available in Visual Studio and .NET SDK.

C# compiler converts C# code to CIL code (common intermediate language) and not to machine code
The processor can directly understand machine code, but CIL code needs to be converted before the processor can execute it.

### use ildasm with a .NET Core project

mkdir HelloWorld; cd HelloWorld
dotnet new console
Add a package reference to the project for dotnet-ildasm (the latest version)
dotnet add package dotnet-ildasm -v "*"
In HelloWorld.csproj, replace 'PackageReference' node with 'DotNetCliToolReference'
(type .\HelloWorld.csproj) -replace '<PackageReference Include="dotnet-ildasm"','<DotNetCliToolReference Include="dotnet-ildasm"' | Set-Content -Path .\HelloWorld.csproj
dotnet restore         Will download the package
At this point, dotnet should have a new verb `ildasm`, that you can use to extract the CIL from your assembly as text

>dotnet ildasm .\bin\Debug\netcoreapp2.0\HelloWorld.dll -t
 
 
### 
 
class Class1
{
    Protected override void Finalize()
    {
        try{..}
        finally { base.Finalize();}
    }
}

method family hide bysig virtual instance void
Finalize() cil managed
{
    // Code size 10 (0xa)
    .maxstack 1
    .try
    {
      IL_0000: leave.s IL_0009
    } // end .try
    finally
    {
        IL_0002: ldarg.0
        IL_0003: call instance void [mscorlib]System.Object::Finalize()
        IL_0008: endfinally
    } // end handler
    IL_0009: ret
} // end of method Class1::Finalize




## more