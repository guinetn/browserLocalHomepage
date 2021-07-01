# MSBuild - Microsoft Build Engine 

The build engine for .NET platform and Visual Studio.
Provides an XML schema for a project file that controls how the build platform processes and builds software. 
Visual Studio uses MSBuild
MSBuild can run without Visual Studio (msbuild.exe can orchestrate and build products in environments where Visual Studio isn't installed)

https://docs.microsoft.com/visualstudio/msbuild/msbuild

MS Build documentation
https://docs.microsoft.com/fr-fr/visualstudio/msbuild/msbuild?view=vs-2019

## PS COMPILERS

Start Windows PowerShell
cd 'G:\DotNet\CSharp\CS 2009 Samples\LanguageSamples\__CompilAll'
.\comp.ps1 
gci -path ..\ -recurse -filter *.csproj | foreach { pushd ([System.IO.Path]::GetDirectoryName($_.FullName)); C:\Windows\Microsoft.NET\Framework\v3.5\msbuild $_.fullname; popd; $_; }
 
## C++ 

Project's C++ source files
```c++
#include <iostream>
#include "main.h"
int main()
{
   std::cout << "Hello, from MSBuild!\n";
   return 0;
}
```

***MSBuild Project's file***

myproject.vcxproj
```xml
<Project DefaultTargets="Build" ToolsVersion="16.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
      
  <ItemGroup>
  
    <ProjectConfiguration Include="Debug|Win32">
      <Configuration>Debug</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
  
    <ProjectConfiguration Include="Release|Win32">
      <Configuration>Release</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
  
  </ItemGroup>
  
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.default.props" />
  
  <PropertyGroup>
    <ConfigurationType>Application</ConfigurationType>
    <PlatformToolset>v142</PlatformToolset>
  </PropertyGroup>
  
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.props" />   path to current C++ settings for this project
  
  <ItemGroup>
    <ClCompile Include="main.cpp" />
  </ItemGroup>  
  <ItemGroup>
    <ClInclude Include="main.h" />
  </ItemGroup>
  
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.Targets" />
  
</Project>
```
|   |   |
|---|---|
| ToolsVersion="14.0" | using Visual Studio 2015 | 
| ToolsVersion="15.0" | using Visual Studio 2017 |
| ToolsVersion="16.0" | using Visual Studio 2019 |

***Build the project***
>msbuild myproject.vcxproj /p:configuration=debug
>msbuild myproject.vcxproj /p:configuration=debug /p:platform=win32
>msbuild myproject.vcxproj /p:configuration=release /p:platform=x64
MSBuild creates a folder for the output files, compiles, links your project to generate Myproject.exe

***Customize your project***
 
## build target
 <ClCompile> is a build target and is defined in the default targets folder.
 
 ## More
 
- https://docs.microsoft.com/fr-fr/c++/build/msbuild-visual-cpp?view=msvc-160
- https://docs.microsoft.com/fr-fr/c++/build/walkthrough-using-msbuild-to-create-a-visual-cpp-project?view=msvc-160
