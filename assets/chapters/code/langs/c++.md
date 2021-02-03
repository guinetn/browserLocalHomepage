# C++

<div class="slideShowContainer">

 <!-- Full-width slides/quotes -->
<div class="slideShowSlide">
```c++
#include <iostream>
void main()
{
    std::cout << "Hello World";    
}
```
g++ cpp01.cpp && ./a.out  
g++ cpp01.cpp -o cpp01.exe && ./cpp01.exe  
</div>

<div class="slideShowSlide">
1. Define a container element 
```js
#include <iostream>
std::string name;
int main() {
std::cout << i << std::endl;
return 0;
}

#include <iostream>
using namespace std;
int main() {
cout <<  "Hello World" << endl;
return 0;
}

```
</div>

<div class="slideShowSlide">
```js
     Mingwin tools, in path for cmd, not for ps             ($env:path.split(';')) | where {$_ -like '*mingw*'} | ls
        ↑                                                                        \____  Directory: C:\MinGW\mingw-w64\x86_64-8.1.0-win32-seh-rt_v6-rev0\mingw64\bin
  cmd> gcc hello.c -o hello.exe     
       g++ hello.c -o hello.exe
       gcc hello.c sqlite3.dll -o hello.exe     if a dll is needed
       g++ -std=c++17 -O2 -Wall -pedantic -pthread hello.cpp && ./a.out
               ↓        \   ---------------
            Standard     \      \___ Warnings
            c++98         \
            c++11          \___ optimization level -O0  None
            c++14                                  -O1  Moderate  
            c++17                                  -O2  Full 
                                                   -O3  Max  

   ps> gcc hello.c -o hello.exe     
       g++ not found

       C:\MinGW\mingw-w64\x86_64-8.1.0-win32-seh-rt_v6-rev0\mingw64\bin
        make.cmd
        ld.exe
        g++.exe
        gcc.exe
        gdb.exe
        cpp.exe
```
</div>

</div>

 * C++11 INHERITANCE

 ```c++
class GameObject
{
    public:
        virtual ~GameObject() {}
        virtual void update() {}
        virtual void draw() {}
        virtual void collide(Object objects[]) {}
};

class Visible : public GameObject
{
    public:
        virtual void draw() override { /* draw model at position of this object */ };
    private:
        Model* model;
};

class Solid : public GameObject
{
    public:
        virtual void collide(GameObject objects[]) override { /* check and react to collisions with objects */ };
};

class Movable : public GameObject
{
    public:
        virtual void update() override { /* update position */ };
};
 ```
