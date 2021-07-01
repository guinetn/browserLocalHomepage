# C++

C++ is not just C with Classes, needs way more effort to be competent compared with C  
The “engine of everything”

***Keypoints***  
- Object Oriented Programming: Classes, Inheritance, Encapsulation, Abstraction
- STL and common Containers
- Modern C++ Features (11...)
- Boost Library

## Precision of Language
C++ programmer has to manually take care of memory management and has to specify every part of a program meticulously. Fast in games because it works precisely with the hardware of the computer.

## Additions to the language 

***Extensive set of features***  
C++ language has a set of standards that are set by the International Organization for Standardization (ISO). These standards are introduced every three years, according to a release cadence specified in 2011, and each release adds more and more to the language.

Ex: "concepts" feature was added with C++20 that expands on what templates initially sought out to do, which was to enable the support for generic programming practices.


download.page(code/langs/c/c_libs/dll.md)

download.page(code/langs/c++/c++_compilers.md)

# C++ SAMPLES
download.slideshow(assets/books/code/langs/c++/code_samples/c++01.md)

download.page(code/langs/c++/c++_98.md)
download.page(code/langs/c++/c++_11.md)
download.page(code/langs/c++/c++_14.md)
download.page(code/langs/c++/c++_17.md)
download.page(code/langs/c++/c++_20.md)


# C++ GUI 
download.page(code/langs/c++/c++_gui.md)


download.page(code/langs/c++/allocator.md)


download.page(code/langs/c++/stl.md)



## Libraries
###
 Boost

Portable C++ source libraries:
JSON, LEAF, PFR. Updated Libraries: Asio, Atomic, Beast, Container, Endian, Filesystem, GIL, Histogram, Interprocess, Intrusive, Log, Move, Mp11, Optional, Outcome, Polygon, Preprocessor, Rational, Signal2, System, uBLAS, VMD, Wave...

https://www.boost.org/
```c++
#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>

int main()
{
    using namespace boost::lambda;
    typedef std::istream_iterator<int> in;

    std::for_each(
        in(std::cin), in(), std::cout << (_1 * 3) << " " );
}
```

## Web Application in C++

- https://github.com/artyom-beilis/cppcms
- http://cppcms.com/wikipp/en/page/main

- https://www.webtoolkit.eu/wt/  📌  
Quickly develop highly interactive web app with a GUI library (widgets)  
Handles all request handling and page rendering for you, so you can focus on functionality 

At the heart, the library takes charge of two tasks within a single session: (1) rendering this widget tree as HTML/JavaScript in the web browser, and tracking changes as incremental updates, and (2) synchronizing user input and relaying events from the browser to these widgets.




A pointer is a general concept for a variable that contains an address in memory. This address refers to, or “points at,” some other data.
Most lower-level languages have pointers in some way, shape, or form and they’re often used in conjunction with other features of the individual language.
Smart pointers, on the other hand, are data structures that not only act as a pointer but also have additional metadata and capabilities.
C++ has types like std::shared_ptr and std::unique_ptr that act as pointers with special features.

## More

- https://docs.microsoft.com/fr-fr/c++/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-160
- https://www.codeproject.com/Articles/5278932/Synchronization-with-Visual-Cplusplus-and-the-Wind
- https://learn.saylor.org/course/resources.php?id=65

- https://www.bogotobogo.com/cplusplus/cpptut.php
- https://www.bogotobogo.com/cplusplus/C11/9_C11_DeadLock.php