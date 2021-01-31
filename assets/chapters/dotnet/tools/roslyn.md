# ROSLYN

open-source C# and Visual Basic compiler with code analysis APIs for Microsoft's development stack

Open Source: https://roslyn.codeplex.com/SourceControl/latest
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
    .AddReferences(references: new[]
    { MetadataReference.CreateFromAssembly(typeof(object).Assembly) })
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
