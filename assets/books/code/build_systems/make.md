# Make
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