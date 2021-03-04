# SOURCE GENERATORS

Compiler saying “Do you have anything to add to what I have done so far?”
~ C/C++ "#include xxxxx" plugged directly into the normal compiler workflow
A C# generator is just a bit of code runned at compile time producing C# code from its inputs
It could download information from a website (not a good idea). But the three inputs below are the most logical ones as they are part of the project. It is the recommended way to do it.
Program Parse Tree → Additional Files → File Specific Options → C# Code

```cs
public interface ISourceGenerator {
    void Execute(GeneratorExecutionContext context); // To implement. context  is the inputs
    void Initialize(GeneratorInitializationContext context); // rarely used
}
```

Context
- Compilation
parse tree and everything else needed by the compiler (settings, references, etc.)

- AdditionalFiles
additional files for the project
>.csproj
><AdditionalFiles Include="Cars.csv" CsvLoadType="OnDemand" CacheObjects="true" />
><AdditionalFiles Include="Geometry.math" />

Geometry.math
    AreaRectangle(w, h) = w * h
    AreaCircle(r)       = pi * r * r
    
```cs
public void Execute(GeneratorExecutionContext context) {
    context.AddSource("___MathLibrary___.cs", SourceText.From(libraryCode, Encoding.UTF8));
    
    // scans the additional files from the project file and operates on the ones with the extension .math
    foreach (AdditionalText fileName in context.AdditionalFiles) 
    {
        // Parse and gen the formulas functions
        var tokens = Lexer.Tokenize(mathString);
        var code = Parser.Parse(tokens);

        var codeFileName = $@"{fileName}.cs";

        context.AddSource(codeFileName, SourceText.From(code, Encoding.UTF8));
    }
}
```

- .AnalyzerConfigOptions.GetOptions
options for each additional file

## Samples
- https://devblogs.microsoft.com/dotnet/using-c-source-generators-to-create-an-external-dsl/
+
- https://github.com/dotnet/roslyn-sdk/blob/master/samples/CSharp/SourceGenerators/SourceGeneratorSamples/MathsGenerator.cs

## More

- https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/
- https://devblogs.microsoft.com/dotnet/new-c-source-generator-samples/
- https://devblogs.microsoft.com/dotnet/using-c-source-generators-to-create-an-external-dsl/
- https://andrewlock.net/using-source-generators-to-generate-a-nav-component-in-a-blazor-app/