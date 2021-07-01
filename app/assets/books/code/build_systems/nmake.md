# nmake

looks for makefile in the current directory
>nmake 
>nmake -f myfile option

cl.exe does the compiling 
link.exe does the linking

nmake           Without a target nmake will look for the first available target in the makefile and build it
nmake clean     We can run nmake without a target or we can specify a target

makefile
```makefile
myHOME = C:\Testing
INCS=$(myHOME)\include
LIBS=$(myHOME)\lib

mybuild: main.obj foo.obj
	cl /o myTest.exe main.obj foo.obj /link  \
		/LIBPATH:$(LIBS) myLib.lib /NODEFAULTLIB:libcmt.lib 
main.obj: main.cpp
	cl /c /EHsc main.cpp -I $(INCS)
foo.obj: foo.cpp
	cl /c /EHsc foo.cpp -I $(INCS)
 
all:mybuild

clean:
   del *.exe *.obj
```

make does the following:

make runs the rule for first target mybuild and figures its dependencies on main.obj and foo.obj.
make next checks if any of the two object files are listed as targets. If yes, as in the example, it runs the rule for first prerequisite, that is, main.obj, to find its dependencies.
make checks whether the prerequisites of main.obj have further dependencies. If no, as in the example, it checks if main.obj is up to date. If not, it runs the command for main.obj by compiling main.cpp to get the object file.
make looks at the targets foo.obj and compiles these object files in a similar fashion.
make returns to first target mybuild. As it now has all up-to-date object files for the rule, it executes the command to build mybuild.
make removes (deletes) mybuild and all object files at make clean.


main.cpp
```
#include <iostream>
#include "foo.h"
using namespace std;

int main(void)
{
    cout << "main: This is test!" << endl;
    foo();
    return 0;
}
```

C:\Testing\foo.cpp
```
#include <iostream>
#include "d.h "
using namespace std;

void foo()
{
  	cout << "foo(): This is from foo!" << endl;
	HelloWorld();
}
```

C:\Testing\include\foo.h
```
void foo();
```

C:\Testing\include\d.h
```
#pragma once  
void HelloWorld();
```

C:\Testing\lib\myLib.lib
This library has a function "HelloWorld(), and it just prints out "Hello world!"
d.h
```h
#pragma once  
void HelloWorld();
```


```c++
#include <stdio.h> 
// For the printf() function
#include "d.h"

void HelloWorld() 
{    
	printf("Hello world!");
}
```

- https://www.bogotobogo.com/cplusplus/make.php