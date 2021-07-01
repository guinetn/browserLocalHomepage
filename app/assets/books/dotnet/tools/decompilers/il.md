## IL

any .NET language isn’t compiled to machine code but to MS Intermediate Language or IL (Microsoft Common Intermediate Language or CIL)

IL key features:
- a stack oriented language
- object oriented
- strongly typed
- It makes heavy use of the .NET Framework classes

https://www.i-programmer.info/programming/other-languages/933-getting-started-with-il.html

.NET Framework
\Windows\Microsoft.NET\Framework\vx.y.z
ILasm.exe
included with the Mono .NET download for a range of platforms including Windows, Mac OSX, Linux etc.

### Assembler directives (begin with a dot)
.assembly extern mscorlib {}    informs the assembler that we are going to be using objects and methods within the  mscorlib assembly, i.e. the console class and its WriteLine method.


### Hello World in IL
Hello.IL
```c
.assembly extern mscorlib {}          directive: will use mscorlib assembly
.assembly Hello {}                    we are creating an assembly (means that it can be run)
.module Hello.exe                     and module name

.class Hello.Program                  declares a class and states that it inherits from Object
extends [mscorlib]System.Object
{
 .method static void Main(string[] args)   define a CIL managed static method
 cil managed
 {
  .entrypoint                              where the program should be started
  ldstr "Hello World"                      IL instructions:loads string “Hello World” onto the stack
  call void [mscorlib]System.Console::     calls the WriteLine method of the static Console class
  WriteLine(string)
  ret
 }
}
```
>ILasm Hello   → assemble this to an "Hello.exe "

download.page(dotnet/tools/decompilers/ildasm.md)

download.page(dotnet/tools/decompilers/ilspy.md)

download.page(dotnet/tools/decompilers/_decompilers.md)


