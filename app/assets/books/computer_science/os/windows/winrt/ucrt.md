## UCRT - Universal CRT

- Windows 10 component
- ISO C99 standard
- Standard C Library, POSIX extensions, Microsoft-specific functions, macros, global variables 
- UCRT library files+headers are now part of the Windows SDK

C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt
- assert.h
- conio.h
- ...

The UCRT static libraries and dynamic link stub libraries are found under 
Windows Kits\10\Lib\sdk-version\ucrt\architecture, where architecture is ARM, x86, X64. 

C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\
- x64\ucrt.lib
- x86
- arm
- arm64

UCRT library files and headers are now part of the Windows software development kit (SDK). When you install Visual Studio, the parts of the Windows SDK required to use the UCRT are also installed. The Visual Studio installer adds the locations of the UCRT headers, libraries and DLL files to the default paths used by the Visual Studio project build system

