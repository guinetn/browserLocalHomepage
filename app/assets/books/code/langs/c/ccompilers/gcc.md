# GCC - GNU Compiler Collection

https://gcc.gnu.org/
https://www.gnu.org/software/gcc/
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system. It contains compilers for the following languages: C, C++, Objective-C, Fortran, Java...

Written in C and accepts options + file names


>man gcc
```bash
gcc [-c|-S|-E] [-std=standard]
        [-g] [-pg] [-Olevel]
        [-Wwarn...] [-Wpedantic]
        [-Idir...] [-Ldir...]
        [-Dmacro[=defn]...] [-Umacro]
        [-foption...] [-mmachine-option...]
        [-o outfile] [@file] infile...
```


|Flags|||
|---|---|---|
|--version||||
|--help option|||
|             |--help=| gcc --help=f|
|             |optimizers|Display optimization options supported|
|             |warnings|Display options controlling warning messages|
|             |target|Display target-specific options|
|             |params|Display the values recognized by --param option|
|             |language|Display the options supported for language|
| -E | Preprocess only (don't compile) and send to output||
| -S | Compile only, don't assemble |.s (assembler code file)|
| -c | Compile + assemble, don't link |.o|
| -o myfile | Place output in file 'myfile'| a.out is default|
| -v | Display the programs invoked by the compiler||
|-wrapper|Invoke all subcommands under a wrapper|gcc -c t.c -wrapper gdb,--args|
| -std= | Determine the language standard | c89 c90 c11|
| -shared | Create a shared library||
| -B <directory>| Add <directory> to the compiler's search paths ||
| -time | Time the execution of each subprocess ||

-wall       enables all the warnings 
-pedantic   Issue all the warnings demanded by strict ISO C/C++; reject all programs that use forbidden extensions. Valid ISO C and ISO C++ programs should compile properly with or without this option (though a rare few require -ansi or a -std option specifying the required version of ISO C). However, without this option, certain GNU extensions and traditional C and C++ features are supported as well. With this option, they are rejected.
-werror     Make all warnings into errors.

gcc hello.c -o hello.exe     
g++ hello.c -o hello.exe
gcc hello.c sqlite3.dll -o hello.exe     if a dll is needed


https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html
Overall Options
C Language Options
C++ Language Options
Diagnostic Message Formatting Options
Warning Options
Static Analyzer Options
Debugging Options
  -g 
Optimization Options
  -O  -O0  -O1  -O2  -O3  -Os  -Ofast  -Og
Program Instrumentation Options
Preprocessor Options
  -C  -CC  
Linker Options  
Directory Options
Developer Options
x86 Windows Options


```c
#include <stdio.h>
int main(void)
{
    printf("Hello World!\n");
    return (0);
}
```

* Preprocessing
- gcc -E main.c  will output the processing step
- 1. it removes all the comments
- 2. it includes code from header and source file
cc looks for lines with '#': 
#include <stdio.h>
#include "set.h"
takes the contents of a file (interpreted by the CPP program, a tool for substituting text when it really comes down to it.)
- 3. it replaces macros 
#define PI 3.14

* Compilation
>gcc -S main.c  
-S option stops the compiler after the compiler step, this creates a 'main.s' which contains the assembly code

preprocessor output is passed into the compiler and the compiler generates assembly code.
The assembly code generated is particular to the instruction set of the processor inside your computer. The most common of which are ARM and x86. The ability to utilize different assemblers enables gcc to turn C source code into machine code that can work on a plurality of computer architectures. Assembly code is the least human readable form of code before it becomes machine language, which is virtually impossible to read and interpret.
https://en.wikipedia.org/wiki/ARM_architecture
https://en.wikipedia.org/wiki/X86
https://www.tutorialspoint.com/assembly_programming/

>cat main.s
        .file   "main.c"
        .section        .rodata
.LC0:
        .string "Hello World!"
        .text
        .globl  main
        .type   main, @function
main:
.LFB0:
        .cfi_startproc
        pushq   %rbp
        .cfi_def_cfa_offset 16
        .cfi_offset 6, -16
        movq    %rsp, %rbp
        .cfi_def_cfa_register 6
        movl    $.LC0, %edi
        call    puts
        movl    $0, %eax
        popq    %rbp
        .cfi_def_cfa 7, 8
        ret
        .cfi_endproc
.LFE0:
        .size   main, .-main
        .ident  "GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609"
        .section        .note.GNU-stack,"",@progbits
        
        
* Assembly        
Convert assembly code into binary code (base2), instructions for the CPU

* Linking
linker accepts the main.o as input and it also accepts any pre-compiled libraries that were imported with the #include preprocessor directive. Next, it merges the unique (non duplicated parts) to make what is called a standalone executable binary



>gcc -w main.c
>./out.a

>