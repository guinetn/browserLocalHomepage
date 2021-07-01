## Compil c++ file

## Online Compilers 

[Compiler explorer - godbolt.org](https://godbolt.org/)
[cppinsights](https://cppinsights.io/)



```html
#include <iostream>
void main()
{
    std::cout << "Hello World";    
}
```
>g++ cpp01.cpp && ./a.out   
>g++ cpp01.cpp -o cpp01.exe && ./c++01.exe  

* On Linux
```c
$ wget http://git.zx2c4.com/CVE-2012-0056/plain/mempodipper.c
$ gcc mempodipper.c -o mempodipper
$ ./mempodipper
```

## Compil c++ library

## Compilers
    
On windows you have to compile GCC using cygwin, mingwin or visual c++ runtime
        
* MS C++ build tool
https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16
open developer command prompt for VS 2019, then type this command: msbuild [Your Project Name].vcxproj
https://docs.microsoft.com/en-us/c++/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?view=vs-2019

* MinGW (Minimalist GNU for windows)
Download http://sourceforge.net/projects/mingw-w64/files/latest/download
Add to environment variables: path = C:/Mingw/bin (contains GNU compilers gcc, g++...)
From command prompt: use gcc/g++...
Executable will be a.exe (windows) instead of than a.out (Linux based Operating systems)
    
($env:path.split(';')) | where {$_ -like '*mingw*'} | ls
* C:\MinGW\mingw-w64\x86_64-8.1.0-win32-seh-rt_v6-rev0\mingw64\bin
    cpp.exe
    g++.exe   → GNU c++ compiler 
    gcc.exe   → GNU c compiler 
    ld.exe
    gdb.exe
    make.cmd          

```c
gcc hello.c -o hello.exe     
g++ hello.c -o hello.exe
gcc hello.c sqlite3.dll -o hello.exe     if a dll is needed
g++ -std=c++17 -O2 -Wall -pedantic -pthread hello.cpp && ./a.out
        ↓        \ ---------------
    Standard      \      \___ Warnings
    c++98         \
    c++11          \___ -Ox: Optimization level 
    c++14                   -O0  None           Optimizations disabled
                                                Reduce compilation time and make debugging produce the expected results. This is the default.
    c++17                   -O1  Moderate  
                            -O2  Full 
                            -O3  Max  
                            -O   reduce code size and execution time   without performing any optimizations             
```
    
https://www.gnu.org/software/gcc/
https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html

The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system.

* VSCODE
https://medium.com/swlh/simple-vscode-setup-to-develop-c-7830182ee4d8