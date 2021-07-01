# clang

- https://clang.llvm.org/
- https://llvm.org/
- https://releases.llvm.org/10.0.0/tools/clang/docs/UsersManual.html#introduction
- https://releases.llvm.org/10.0.0/tools/clang/docs/ReleaseNotes.html

open-source compiler for the C family of programming languages:
- C Language: K&R C, ANSI C89, ISO C90, ISO C94 (C89+AMD1), ISO C99 (+TC1, TC2, TC3).
- Objective-C Language: ObjC 1, ObjC 2, ObjC 2.1, plus variants depending on base language.
- C++ Language
- Objective C++ Language
- OpenCL C Language: v1.0, v1.1, v1.2, v2.0.

an "LLVM native" C/C++/Objective-C compiler
a front end for the LLVM compiler back end [llvm.org](https://www.llvm.org)
 
$ cat t.c
#include <stdio.h>
int main(int argc, char **argv) { printf("hello world\n"); }
$ clang t.c
$ ./a.out
hello world