# C


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

 
- https://www.geeksforgeeks.org/higher-order-functions-in-c
- https://h-deb.clg.qc.ca/Sujets/Divers--c/index.html#general
- https://github.com/signalapp/libsignal-protocol-c/blob/master/src/curve.c