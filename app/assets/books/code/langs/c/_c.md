# C

Low-level programming language (high-level compared to assembly) which lets you have total control over MCUs and memory, leading to need for manual memory management.  
As it resides at the lowest level of abstraction C is largely used to code 
- device firmware
- device drivers
- kernel
Procedural language  
C is not a type-safe language  
Developed by Dennis Ritchie  

# C SAMPLES
download.slideshow(assets/books/code/langs/c/code_samples/c01.md)

***Keypoints***  

Compiled languages: PREPROCESSED → COMPILED → ASSEMBLED → LINKED

- Variable Declarations
- Definitions and Scope
- Data Types
- Storage Classes
- I/O Operations
- Operators
- Preprocessor
- Enums
- Structs
- Functions
- Pointers

## C Tokens
smallest individual units in a program  
- identifiers: user defined names 
- keywords: language instructions
- constants: values wich don't change
- strings: sequence of characters
- operators
   math. + - * / ++ --
   logical  && || !
   relational   == >= <=
- special symbols: preprocessor directive (#)



add: - [Hash Table in C](https://www.yo utube.com/watch?v=2Ti5yvumFTU&t=1040s)

download.page(code/langs/c/c_libs/_c_libs.md)
download.page(code/langs/c/ccompilers/_ccompilers.md)


### MOST USED HEADER FILES

| stdio.h | Standard input/output header file in which Input/Output functions are declared|
|---|---|
| conio.h | This is console input/output header file |
| string.h | All string related functions are defined in this header file |
| stdlib.h | This header file contains general functions used in C programs |
| math.h | All maths related functions are defined in this header file |
| time.h | This header file contains time and clock related functions |
| ctype.h | All character handling functions are defined in this header file |
| stdarg.h | Variable argument functions are declared in this header file |
| signal.h | Signal handling functions are declared in this file |
| setjmp.h | This file contains all jump functions |
| locale.h | This file contains locale functions |
| errno.h | Error handling functions are given in this file |
| assert.h | This contains diagnostics functions |

https://fresh2refresh.com/c-programming/c-function/c-library-functions/


## User input/Output
printf(), scanf(=
getchar(), putchar()
gets(), puts()

Format strings
Abrev. | Data type
---|---
%d | integer
%f | floating point
%c | character
%s | string

## DATA TYPES

* Primitive Types
void 
int
bool
char
floating point
double

* Derived Types
Array
References
Pointer

* Used defined Types
Struct
Union
Enum

## MEMORY

C/C++ interact with your memory in a low-level way with stdlib (malloc, calloc, free). Sometimes this creates a lot of problems you didn’t get before: segfaults. 

- Malloc (memory allocation) 
requests the system for the amount of memory that was asked for, and returns a pointer to the starting address. 
- Free 
tells the system that the memory we asked for is no longer needed and can be used for other tasks.

```c
#include <stdio.h>
#include <stdlib.h>

// static memory allocation for the life of the program
int my_variable = 70;

int main(int argc, char *argv[])
{
  	printf("Malloc - Calloc - Realloc - Free\n");

	// Dynamic memory allocation: when you need more memory


	// Malloc: ask for a pointer to a block of memory of a certain size. 
	//         return null if not enough memory available (you can't have memory)
	int *x = malloc(sizeof(int));  			// give me space for 1 'int' 
	int *arr = malloc(sizeof(int)*100);  	// give me space for 100 'int'
	*x = 120;

	// R/W to the memory	
	arr[90] = 0xFEEF8EEF;
	arr[101] = 8;  // Out of bounds: This is bad

	free(arr);	  // We don't need this memory anymore
	arr = NULL; 	// Good practice to set the pointer to NULL after free()	



	// Calloc = malloc + number of elements to allocate as argument + Set block elemnets to 0			
	double *darr; 
	darr = calloc(sizeof(double), 100); // same as malloc(sizeof(double)*100)


	// Realloc: resize up/down an allocated block. pointer can change if not enough continuous memory (and elements are copied)
	darr = realloc(darr, sizeof(double)*500); 
}

```
accessing memory that has already been freed (released with free or memory that your program has automatically released, for example from the stack) will cause `segfault`

***Memory Leak***
is memory that was requested by the user that was never freed — when the program ended or pointers to its locations were lost. This makes the program use much more memory than what it was supposed to. To avoid this, every time we don’t need an heap allocated element anymore, we free it.

after the memory is freed, accessing it or using it might cause you a segfault.

Memory is divided in multiple segments
![](assets/books/code/langs/c/memory_division.jpg)

***STACK***
Is an ordered insertion place 
It’s where some of your processor’s registers information gets saved. 
This memory is also managed by the program and not by the developer.
LIFO (Last-In-First-Out) data structure: push/pop
`Stack Pointer` is a processor register that keep track of the current memory place
Every local variable and every function you call goes there. Every time you need to save something — like a variable or the return address from a function — it pushes and moves the stack pointer up. Every time you exit from a function, it pops everything from the stack pointer until the saved return address from the function.

***HEAP***
is all random — you allocate memory wherever you can
used to allocate big amounts of memory that are supposed to exist as long as the developer wants.
Developer’s job to control the usage of the memory on the heap.
When building complex programs, you often need to allocate big chunks of memory, and that’s where you use the heap. We call this Dynamic Memory.
You’re placing things on the heap every time you use malloc to allocate memory for something. Any other call that goes like int i; is stack memory.


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

download.page(computer_science/os/windows/winrt/crt.md)

## More 
- [J. Sorber Progress Bars]-https://www.youtube.com/watch?v=t_vM_8TLjFE)
- https://fresh2refresh.com/c-programming
- https://www.geeksforgeeks.org/higher-order-functions-in-c
- https://h-deb.clg.qc.ca/Sujets/Divers--c/index.html#general
- https://github.com/signalapp/libsignal-protocol-c/blob/master/src/curve.c
- https://x-engineer.org/graduate-engineering/programming-languages/c/data-types-c-programming-language/
- https://dzone.com/articles/writing-a-linux-daemon-in-c
- [Hash Table in C]https://www.youtube.com/watch?v=2Ti5yvumFTU&t=1040s


- https://opensource.com/article/21/2/linux-software-libraries
- https://opensource.com/article/20/6/linux-libraries

- [networking in C](https://www.youtube.com/watch?v=daA-KBKfJ_o)
- [Pipe System Call](https://www.youtube.com/watch?v=8AXEHrQTf3I)
- []()
- []()
- []()
- []()
- []()