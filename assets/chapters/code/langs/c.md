# C

### MOST USED HEADER FILES

stdio.h	This is standard input/output header file in which Input/Output
functions are declared
conio.h	This is console input/output header file
string.h	All string related functions are defined in this header file
stdlib.h	This header file contains general functions used in C programs
math.h	All maths related functions are defined in this header file
time.h	This header file contains time and clock related functions
ctype.h	All character handling functions are defined in this header file
stdarg.h	Variable argument functions are declared in this header file
signal.h	Signal handling functions are declared in this file
setjmp.h	This file contains all jump functions
locale.h	This file contains locale functions
errno.h	Error handling functions are given in this file
assert.h	This contains diagnostics functions
https://fresh2refresh.com/c-programming/c-function/c-library-functions/

## DYNAMIC MEMORY ALLOCATION
malloc ()	malloc (number *sizeof(int));
malloc () function is used to allocate space in memory during the execution of the program.
malloc () does not initialize the memory allocated during execution.  It carries garbage value.
malloc () function returns null pointer if it couldn’t able to allocate requested amount of memory.

calloc ()	calloc (number, sizeof(int));
realloc ()	realloc (pointer_name, number * sizeof(int));
free ()	free (pointer_name);

* FUNCTION POINTER

 ```c++
int f() {
   return 3;
}
int g() {
   return 4;
}
#include <iostream>
int main() {
   using namespace std;
   int (*pf)() = f;         // type (*nom)(params)
   cout << pf() << endl;
   pf = g;
   cout << pf() << endl;
}

string (*p)(const string&);      fonction pointer, in: const string&, out: string
string *p(const string&);       fonction, in: const string&, out: string*
 ```

Better with alias:
 ```c++
 int f(int n) {
   return n + 1;
}
int g(int n) {
   return -n;
}
typedef int (*ptr_fct)(int); // alias
#include <iostream>
int main() {
   using namespace std;
   ptr_fct pf = f;
   cout << pf() << endl;
   pf = g;
   cout << pf() << endl;
}
 ```

 ```c++
 int f(int n) {
   return n + 1;
}
int g(int n) {
   return -n;
}
using ptr_fct = int(*)(int);     // c++ 11: using to define a new type
#include <iostream>
int main() {
   using namespace std;   
   ptr_fct pf = f;
   cout << pf() << endl;
   pf = g;
   cout << pf() << endl;
}
 ```

 
- https://fresh2refresh.com/c-programming
- https://www.geeksforgeeks.org/higher-order-functions-in-c
- https://h-deb.clg.qc.ca/Sujets/Divers--c/index.html#general
- https://github.com/signalapp/libsignal-protocol-c/blob/master/src/curve.c
- https://x-engineer.org/graduate-engineering/programming-languages/c/data-types-c-programming-language/
- https://dzone.com/articles/writing-a-linux-daemon-in-c

	systemd
	