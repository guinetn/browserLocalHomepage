# MSBuild - Microsoft Build Engine 

The build engine for .NET platform and Visual Studio.
Provides an XML schema for a project file that controls how the build platform processes and builds software. 
Visual Studio uses MSBuild
MSBuild can run without Visual Studio (msbuild.exe can orchestrate and build products in environments where Visual Studio isn't installed)

https://docs.microsoft.com/visualstudio/msbuild/msbuild


## PS COMPILERS

Start Windows PowerShell
cd 'G:\DotNet\CSharp\CS 2009 Samples\LanguageSamples\__CompilAll'
.\comp.ps1 
gci -path ..\ -recurse -filter *.csproj | foreach { pushd ([System.IO.Path]::GetDirectoryName($_.FullName)); C:\Windows\Microsoft.NET\Framework\v3.5\msbuild $_.fullname; popd; $_; }
 