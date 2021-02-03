# Types

***VALUE TYPES***
struct, enum, bool, int, char, float, double, decimal

***REFERENCE TYPES***
class, array, delegate, interface, object, string

***PREDEFINED TYPES = BUILT-IN TYPES***
int, char, float, double, decimal, bool, struct, enum, string, object

using System;
Important types not defined in C#
Contains the most .Net framework types (DateTime...)


int i = 5;
string s = "Hello";
double d = 1.0;
int[] numbers = new int[] {1, 2, 3};
int[] numbers = { 1, 3, 5, 7, 9 };
foreach (var n in numbers) Console.WriteLine(n);
Dictionary<int,Order> orders = new Dictionary<int,Order>();

Range(0, 6).Select(i => ...)

           
::::
download.chapter(dotnet/types/ref/interfaces.md)
::::
download.chapter(dotnet/types/ref/string.md)
::::
download.chapter(dotnet/types/ref/delegates.md)
::::
download.chapter(dotnet/types/ref/class.md)
::::
download.chapter(dotnet/types/ref/span.md)
::::
download.chapter(dotnet/types/ref/dynamic.md)
::::
download.chapter(dotnet/language/covariance.md)
::::
download.chapter(dotnet/types/val/structs.md)
::::