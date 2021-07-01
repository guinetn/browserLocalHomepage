# WinRT - Windows Runtime

[Browse the Winrt api: namesapces, Classes, Structs, Interfaces
Enums, Delegates…](https://docs.microsoft.com/en-us/uwp/api/)
These are in WinRT...Build 10240, Build 10586, Build 14383, Build 15063, Build 16299, Build 17134, Build 17763, Build 18362, Build 19041…


The Windows Runtime is the foundational infrastructure used by Windows to expose its APIs. It is intended to be the successor to the flat, C-based Win32 API (although you can use the Windows Runtime and the Windows API side by side).

The Windows Runtime is based on Component Object Model (COM) APIs, and it's designed to be accessed through language projections. A projection hides the COM details, and provides a more natural programming experience for a given language.


The Windows Runtime is exposed using a modernized version of COM. Components can be consumed and authored by a wide variety of languages. Components encode their public interfaces using [ECMA-335](https://www.ecma-international.org/publications/standards/Ecma-335.htm) conforming metadata (.winmd files). The technology itself does not rely on .NET or the CLR.

## WINRT Users
Several new technologies were published using the (then new) Windows Runtime as a delivery channel. The most obvious one being the new UI framework. To my knowledge, it still doesn't have a name. It used to go by the names "Metro", "Modern UI", "Fluent Design", "WPF". It's rendered using Direct2D, and commonly authored using XAML.

While often conflated with the Windows Runtime, WPF is merely a client of the technology. It is not part of the Windows Runtime itself.

Another important point is, that the Windows Runtime does not mandate use of any particular UI library or framework. It works equally well in a classic desktop app (written in straight Win32, MFC, WTL, wxWidgets, ...) or a .NET application (Windows Forms, WPF) as it does in an application with a XAML/WPF UI.


download.page(computer_science/os/windows/winrt/c++winrt.md)
download.page(computer_science/os/windows/winrt/crt.md)
download.page(computer_science/os/windows/winrt/ucrt.md)
download.page(computer_science/os/windows/winrt/uwp.md)
download.page(computer_science/os/windows/winrt/win_ui.md)
download.page(computer_science/os/windows/winrt/com.md)

## Windows Runtime components

a component that's callable from a Universal Windows app built using any Windows Runtime language (C#, Visual Basic, C++, or Javascript).

A self-contained software module that you can author, reference, and use with any Windows Runtime language (including C#, C++/WinRT, Visual Basic, JavaScript, and C++/CX). You can use Visual Studio to create a Windows Runtime component that can be used in your Universal Windows Platform (UWP) app.
For C++ developers recommend use of C++/WinRT for new applications.


There are several reasons for building a Windows Runtime component in C++.
- To get the performance advantage of C++ in complex or computationally intensive operations.
- To reuse code that's already written and tested.

Samples: https://docs.microsoft.com/en-us/windows/uwp/winrt-components/
https://docs.microsoft.com/en-us/visualstudio/extensibility/walkthrough-creating-an-sdk-using-csharp-or-visual-basic?view=vs-2019

 

Windows Runtime Library (WRL, replaced by c++Winrt), and C++/WinRT all do basically the same thing: Provide a mechanism for calling "Windows Runtime" style APIs & types from C++ and for authoring "Windows Runtime" style APIs & types.

Windows Runtime APIs?

Original Win32 API was designed for a native code world, and most programs were written in C or C++. 

COM (Component Object Model)
was created as a way to handle runtime versioning (+ other features) using the same basic Application Binary Interface (ABI). C++ is a more natural way to use COM, but you can still technically use C through various macros and what not.

.NET + other managed languages came along later, and use a different calling mechanism. You can use native interop to get to Win32 or COM APIs, but they generally don't work in a very "C# friendly" way. Various 'wrapper assemblies' have been created provide a more C# natural way to access fundamentally C/C++ APIs & types.

With the growth of the Internet and in particular the Worldwide Web, another class of applications are written using HTML5+JavaScript. They don't have any specific access to Win32 or COM APIs so special modules & libraries are written to cover the functionality gaps.

SO given all three of these major approaches, "Windows Runtime" style is an approach which combines the features of COM with the reflection-rich metadata of .NET. The idea being that an API could be written once and be usable by C++, C#, HTML5+JavaScript.

Of course there are a lot of issues with using an API beside just being able to call the ABI, and each of those language paradigms are quite different, but from systems programming view that's the point of it all.

There is also a "Universal Windows Platform" that uses Windows Runtime APIs which itself has three basic 'appmodels': XAML, DirectX, XAML+DirectX. These are the kinds of applications that can make heavy use of C++/WinRT if they are written in C++, but you can also use Windows Runtime APIs from Win32 desktop apps.


- https://docs.microsoft.com/en-us/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt