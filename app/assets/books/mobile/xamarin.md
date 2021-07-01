# XAMARIN - cross-platform-mobile-development

https://docs.microsoft.com/fr-fr/xamarin/get-started/what-is-xamarin

Official distributions of .NET will be available for Linux and OS X
Cross-platform developers are now welcome to use the .NET framework on a platform of their choice. Web, desktop, cloud or mobile development on almost any platform can now be targeted with the .NET framework. You can build native ASP.NET web applications on a Mac. 
You can build native iOS or Android applications using C#, along with Windows counterparts. And you can build Hybrid single-codebase cross-platform mobile apps using plain HTML/CSS/JS and the Apache Cordova open source framework. This is a huge and welcome change and can potentially spread the use of .NET to non-Microsoft developers
2021: Goodbye Xamarin.Forms, Hello .NET MAUI !


# FIRST CROSS PLATFORM APP USING XAMARIN FORMS
cross platform app
	VS New C# → cross platform → Cross platform (Xamarin.Forms or Native) → Blank app (Xamarin + PCL)
	Choose target (Nexus 5...)
	Build
	Android emulator launched

Build cross-platform apps with .NET and C#. No more Java and Objective-C or Swift. Everything you can do with these languages and platforms, can be done with Xamarin in C#. This is possible because of the Mono project (Linux variant of the .NET framework)

# Create native iOS, Android, Mac and Windows apps in C#
Base: Mono
	  Use natives api
	  Xamarin Forms: 1 seul interface C# or xaml
	  Compatible universal Apps
	  100% API .net, Android, iOS


Xamarin is a free Microsoft tool that allows developers to write fully native Android and iOS apps using C# and programming models already familiar to .NET developers. With Xamarin, you can build native Android and iOS apps without needing to know Java or Objective-C and best of all it is included with all editions of Visual Studio 2015. For Android development, Visual Studio has one of the most performant Android emulators built in so you can test your Xamarin.Android apps from your Windows development environment. For iOS development, Xamarin provides a remote iOS simulator for Visual Studio to test your applications without having to switch to a Mac. It even supports touch and multi-touch; something that is missing from testing iOS apps on the iOS simulator on a Mac. You will still need to connect to a physical Mac in order to build the application, but the entire development process is completely done in Visual Studio, including editing storyboards.

Apps built using Xamarin compile to native code on their respective platforms. Xamarin wraps low level native APIs so you are able to access sensors and other platform specific features. Xamarin.iOS projects compile to .app files that can be deployed to Apple mobile devices. Xamarin.Android projects compile to .apk files, the application package used for deploying to Android devices.


http://xamarin.com
http://xamarin.com/getting-started/android
http://www.journaldunet.com/developpeur/technos-net/visual-studio-pour-ios-et-android-avec-xamarin.shtml
http://www.microsoftvirtualacademy.com/training-courses/developper-une-application-cross-plateformes-avec-xamarin?CR_CC=200412513
https://blogs.windows.com/buildingapps/2016/09/23/background-audio-and-cross-platform-development-with-xamarin-app-dev-on-xbox-series/#0SHiWd8AZjm0egId.97

		iOS App 					Android App 			Windows App
 Objective-C, Swift, Xcode 		   Java, Eclipse 			C#, Visual Studio

# Get Started
Editor: Xamarin Studio or Visual Studio

Sample app  
good cross-platform architectural design including
. data access
. business logic
. native-UI element


# Xamarin.Forms

cross-platform development framework that allows writing  mobile applications in C# or F# and runs on any mobile platform.
share UI for all mobile platforms (iOS, Android, UWP) using XAML-based pages.
Xamarin project is open-source
Xamarin.Forms allows using common UI control libraries that are mapped to native UI controls of iOS, Android, UWP. You can write one business code library and can share with iOS, Android, UWP Xamarin applications.
Xamarin.Forms allows you to write the UI code that can be compiled for the Android, iOS, and UWP platforms.

C# code you write with Xamarin.Forms is converted to the target platform (Android, iOS, WP) at compile time. During this conversion, your code is optimized by the Compiler, and because it removes some basic faults, it is often more efficient than code written in the native environment.

Mac requirement: To develop an application for iOS on Windows you must have a mac. You can use Xamarin Mac Agent on Visual Studio to compilation and debugging, but also you need a mac on remote.

2011	Xamarin.Native (Xamarin.Android, Xamarin.iOS), done using the Mono-Project
2014  	Xamarin.Forms

Development Environment (IDE): Visual Studio and Xamarin Studio 
Rich Components Library on github
Rich platform support (including Windows Phone, Windows Desktop, Hololens etc.)

**Xamarin Android Runtime**
Xamarin on Android takes the advantages of Just In Time (JIT) compilation on the Android devices and applications  run natively. 
Access to device specific features is provided by .net APIs of Mono CLR. You cannot access to device-specific features directly because they are part of the Android SDK. Because of this reason, Mono CLR uses Android binding libraries to access.

**Xamarin iOS Runtime**
Xamarin on iOS does full Ahead Of Time (AOT) compilation to produce an ARM binary and runs natively on device.
Xamarin provides a large ecosystem of tools, other than Xamarin.Forms they also provide Xamarin.iOS and Xamarin.Android.
For the cross-platform mobile development with maximum code sharing, Xamarin.Forms is the best option.



