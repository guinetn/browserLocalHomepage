## C++/WinRT 

A language projection for Windows Runtime (WinRT) APIs. 

[winrt namespace (C++/WinRT)](https://docs.microsoft.com/en-us/uwp/cpp-ref-for-winrt/winrt)

C++/WinRT (like any other language projection) translates the COM-based Windows Runtime interfaces to natural, idiomatic language patterns, C++ in case of C++/WinRT. Most notably it does 3 things:
- Automates resource management of COM objects by binding the reference counting to object lifetimes of smart pointers.
- Translates between COM's error reporting (based on HRESULT return values) and C++ error reporting based on C++ exceptions.
- Maps the Windows Runtime's asynchronous patterns based on IAsyncInfo to C++20 coroutines
>- https://en.cppreference.com/w/cpp/language/coroutines  
>- https://medium.com/pranayaggarwal25/coroutines-in-cpp-15afdf88e17e

C++/WinRT is an entirely standard modern C++17 language projection for Windows Runtime (WinRT) APIs, implemented as a header-file-based library, and designed to provide you with first-class access to the modern Windows API. With C++/WinRT, you can author and consume Windows Runtime APIs using any standards-compliant C++17 compiler. The Windows SDK includes C++/WinRT; it was introduced in version 10.0.17134.0 (Windows 10, version 1803).

Replacement for the C++/CX language projection and the Windows Runtime C++ Template Library (WRL). 


    - [cpp-with-winrt](https://docs.microsoft.com/en-us/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt)