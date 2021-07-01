## C LIBRARIES

#include <stdio.h>    // printf(), scanf() 

### C static libraries

Collection of object code files created at compilation
For code reusability: contains function modules
Speeds up the program’s creation 

Also known as "archives"

/usr/lib/


lib_xxxx.a, ex: libc.a
ar -t <archive> to inspect the library (creates, modifies, extracts)
-t flag displays a table listing the contents of the archive.

#include <stdio.h> 
- a header file has the declaration of the function (prototype)
- a library contains the definition of the function

download.page(code/langs/c/c_libs/sll.md)
download.page(code/langs/c/c_libs/dll.md)