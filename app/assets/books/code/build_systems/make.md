# Make

## install

build executable programs and libraries from source code.

make is a GNU command so the only way you can get it on Windows is installing a Windows version like the one provided by GNUWin32. Anyway, there are several options for getting that:
The most simple choice is using Chocolatey. First you need to install this package manager. Once installed you simlpy need to install make (you may need to run it in an elevated/admin command prompt) :
>choco install make

Other recommended option is installing a Windows Subsystem for Linux (WSL/WSL2), so you'll have a Linux distribution of your choice embedded in Windows 10 where you'll be able to install make, gccand all the tools you need to build C programs.

## make vs cmake

They take a bunch of C/C++ files and turn them into a binary.

https://stackoverflow.com/questions/25789644/difference-between-using-makefile-and-cmake-to-compile-the-code
Make (or rather a Makefile) is a buildsystem - it drives the compiler and other build tools to build your code.

CMake is a generator of buildsystems. It can produce Makefiles, it can produce Ninja build files, it can produce KDEvelop or Xcode projects, it can produce Visual Studio solutions. From the same starting point, the same CMakeLists.txt file. So if you have a platform-independent project, CMake is a way to make it buildsystem-independent as well.



Make is invoked with a list of target file names to build as command-line arguments:
>make TARGET [TARGET ...]
Without arguments, make builds the first target that appears in its makefile, traditionally named 'all'



rules + dependencies

targets: prerequisites (dependencies)
   command
   command
   command

```make
hello:
    echo "hello world"
```

```make
blah: blah.o
    cc blah.o -o blah # Runs third

blah.o: blah.c
    cc -c blah.c -o blah.o # Runs second

blah.c:
    echo "int main() { return 0; }" > blah.c # Runs first
```



makefile                         ← describe how your program should be built
```make

CC=gcc                          ← use variables to specify things that you will change in the futur

all: hello                      ← default 'make' command

hello:helloc.c                   ← rule 'hello', depend on hello.c
    $(CC) hello.c -o hello           how to built

test.o:test.c
    $(CC) -c test.c -o test.o

clean:                         ← clean generated files  'make clean'       
    rm hello test
```
>make hello

hello.c
```c
#include <stdio.h>

void main(void) {
    printf("Hi world\n");
}
```

## More 

- https://makefiletutorial.com/
- https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html
- http://perso.univ-lyon1.fr/jean-claude.iehl/Public/educ/Makefile.html