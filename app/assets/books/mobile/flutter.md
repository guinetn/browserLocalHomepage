# Flutter

# Quick
>flutter create app01    Your application code is in app01\lib\main.dart
>cd app01
>flutter run 			 Have your phone connected
Launching lib\main.dart on SM A105FN in debug mode...
Running Gradle task 'assembleDebug'... Done                       211,3s
√  Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app.apk...

View on 
- phone
- Flutter dev tools
	http://127.0.0.1:9101?uri=http%3A%2F%2F127.0.0.1%3A56486%2FOJgOrCe-DB0%3D%2F

Syncing files to device SM A105FN...                               577ms

Flutter run key commands.
r Hot reload.
R Hot restart.
h Repeat this help message.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

 Running with sound null safety

An Observatory debugger and profiler on SM A105FN is available at: http://127.0.0.1:56486/OJgOrCe-DB0=/
Lost connection to device





Compiles to machine code while coming with its own render engine. This promises a consistent cross-platform user experience as well as good performance. Neither Ionic nor React Native can compete with this.
Flutter projects are written in Dart, a language more or less unique to Flutter development. Dart is a pretty modern language, too, and it fits mobile development quite well.

the best part about Flutter is 
- user interface 
- user experience 
Flutter is very strong with Material Design and there are ready-to-use Material widgets to help create a good user experience with minimal effort. It’s all customizable with your fonts, colors, spacings, and a lot more, of course.
https://material.io/
https://flutter.dev/docs/development/ui/widgets/material
https://flutterstudio.app/

Native iOS development is done using Swift  
Native Android development strongly suggest using Kotlin

course to read: 0/0 https://zaiste.net/courses/flutter-in-practice/

https://flutter.dev/docs/get-started/install/windows

Open plugin preferences (File > Settings > Plugins).
Select Marketplace, select the Flutter plugin and click Install.

>flutter create myapp
main.dart ← main file = widgets 
everything is widget. Make you own: class myApp extends StatelessWidget {...}
>flutter --version
>where flutter dart
>flutter doctor
>flutter devices

flutter doctor
Doctor summary (to see all details, run flutter doctor -v):
[√] Flutter (Channel stable, 2.2.0, on Windows, locale fr-FR)
[√] Android toolchain - develop for Android devices (Android SDK version 30.0.3)
[√] Chrome - develop for the web
[√] Android Studio
[√] VS Code, 64-bit edition (version 1.56.2)
[√] Connected device (2 available)


ISSUES
if: Android Studio (not installed)...
fix: flutter config --android-studio-dir="C:\Program Files\Android\Android Studio"

flutter doctor --android-licenses                         

if: Flutter SDK is not found in the specified location.
The path to the SDK should be to the main Flutter folder (e.g. C:\src\flutter and not to the bin folder as set in the Environment Variable Path.


# C:\tools\flutter

one code for cross-platform (Android and iOS) mobile development 
by Google that makes it easy to build cross-platform iOS and Android apps with one programming language (Dart)


[Flutter in 100 seconds](https://www.youtube.com/watch?v=lHhRhPV--G0)
https://www.youtube.com/watch?v=NWbkKH-2xcQ
https://www.youtube.com/watch?v=wUSkeTaBonA&t=1079s
https://www.youtube.com/watch?v=7edR32QVp_A

Flutter is your ticket to fast, secure and scalable cross-platform mobile apps. This bundle takes you hands on with the game-changing SDK, showing how it’s easier than ever to build high-performance apps for iOS and Android.
https://www.manning.com/books/flutter-in-action

Google’s open-source toolkit 
To build iOS & Android apps with just one codebase
Flutter apps are written in the Dart language and compile to native code (performance)

Flutter is a great cross-platform framework from Google that can be used to build applications for mobile, desktop, and web platforms. Officially released in December of 2018, it took barely a year to gain more popularity than React Native on both GitHub and Stack Overflow


# Fuchsia 
https://medium.com/swlh/flutter-and-fuchsia-the-death-of-react-android-a34f6d12bb82

# ADVANTAGES OF FLUTTER

	underlying language and SDK to address common issues and shortcomings of other technologies. Here’s a simple breakdown of a few reasons why you should choose Flutter for your next project, 
	
	1. The Dart Language
		designed from the ground-up to be an excellent tool for building client applications, and has been tuned up and optimized for developing UI.
		Dart has a clean and incredibly powerful syntax that not only facilitates but encourages strong application architecture and design, 
	 It’s similar to other popular languages such as C#, Java, and TypeScript, meaning it’s easy for those with some experience to adopt and begin using right away.
	2. Widespread Developer Adoption
		In one short year, Flutter has become more popular than React Native (which was the most popular framework of it’s time) on both GitHub and Stack Overflow. 
	3. It’s Extremely Fast
		Flutter apps compile down into native binaries that rely on graphics and rendering engines built in C/C++ 
	4. It’s Easy to Learn (relatively)
		excellent documentation available and large number of high-quality examples for reference. 
	5. It’s Well-Designed
		Flutter was designed from the ground up on top of an excellent language (Dart) and a fast high-performance rendering engine (Skia).

    "I think Flutter is the way to go these days. It’s saved me a lot of time in my development. I got my start in the mobile world with Android development using Java. Learning Flutter helped me bridge into the iOS ecosystem. Now I can have one codebase for both apps. The Flutter documentation and community is amazing!"

# FLUTTER VS KOTLIN

	Depends on what it's aiming for, these two are pretty different things:  
	* Flutter 
		is a framework for cross-platform (Android and iOS) mobile development which uses Dart programming language 
		Flutter solves a specific problem, it’s a UI framework. 
	* Kotlin 
		is a programming language that compiles to JVM, JavaScript and native code
		Kotlin is a general purpose programming language. Based on that, learning Kotlin will give you more benefits.

	You can design and develop Native Looking Apps using Flutter SDK using Dart Programming language.
	You can develop server side apps in Kotlin also.
	Kotlin team is also working on iOS app development using Kotlin/Native.

	To develop mobile apps: 
		Learn Flutter + Dart (programming language Flutter is written in)
		Kotlin is officially supported for Android development, but iOS development in Kotlin would be complicated. 
		Anyway, I’d use Flutter even for Android, it’s such a nice framework to work with. :)

	To develop desktop applications
		Kotlin + some framework (JavaFX for instance) is much better option. There’s some preliminary support for desktop apps in Flutter, but not production-ready and Linux-only AFAIR.

	For web applications 
		Flutter is unapplicable at all, so Kotlin is the only choice among these two. 

https://flutter.io/
https://flutter.io/get-started/install/
https://flutter.io/get-started/editor/ 		configre editor (android studio)

https://material.io/components/

https://academind.com/learn/flutter/
https://www.youtube.com/watch?v=XHsrxgoESz8&t=609s
https://levelup.gitconnected.com/why-choose-flutter-in-2020-22d87e60200a
https://morioh.com/p/d94ec1c92875   Flutter Tutorial for Beginners 2020 - Build App with Flutter

# install

	https://flutter.dev/docs/get-started/install/windows
	* Extract the zip Flutter SDK in, for example, C:\src\flutter (do not install in C:\Program Files\ that requires elevated privileges)
	* Set your Flutter Path environment variable, preferably permanently.
		For Windows, you can enter the following command 	setx path "%path%;c:\flutter\bin\"
		For MacOS and Linux, you will want to open or create $HOME/.bash_profile and add this line export PATH=/usr/local/flutter/bin:$PATH

# You are now ready to run Flutter commands in the Flutter Console!




flutter doctor
flutter doctor --android-licenses
flutter devices
	1 connected device:
	ASUS X00HD • HAAXB7699526H6E • android-arm64 • Android 7.1.1 (API 25)
flutter run


flutter doctor -v
[√] Flutter (Channel stable, v1.9.1+hotfix.6, on Windows, locale fr-FR)
    • Flutter version 1.9.1+hotfix.6 at C:\tools\flutter
    • Framework revision 68587a0916 (2 months ago), 2019-09-13 19:46:58 -0700
    • Engine revision b863200c37
    • Dart version 2.5.0

[!] Android toolchain - develop for Android devices (Android SDK version 29.0.2)
    • Android SDK at H:\android\sdk-win
    • Android NDK location not configured (optional; useful for native profiling support)
    • Platform android-29, build-tools 29.0.2
    • ANDROID_HOME = H:\android\sdk-win
    • Java binary at: C:\Program Files\Android\Android Studio\jre\bin\java
    • Java version OpenJDK Runtime Environment (build 1.8.0_202-release-1483-b03)
    X Android license status unknown.
      Try re-installing or updating your Android SDK Manager.
      See https://developer.android.com/studio/#downloads or visit https://flutter.dev/setup/#android-setup for
      detailed instructions.

[√] Android Studio (version 3.5)
    • Android Studio at C:\Program Files\Android\Android Studio
    • Flutter plugin version 41.1.2
    • Dart plugin version 191.8593
    • Java version OpenJDK Runtime Environment (build 1.8.0_202-release-1483-b03)

[√] VS Code, 64-bit edition (version 1.40.1)
    • VS Code at C:\Program Files\Microsoft VS Code
    • Flutter extension version 3.6.0

[√] Connected device (1 available)
    • SM A105FN • R58M87GWE0V • android-arm • Android 9 (API 28)

! Doctor found issues in 1 category.

#issues
	...android\gradlew.bat exited abnormally



# Samples

https://buildflutter.com/getting-started-flutter/
vscode 	→ + extension "Flutter (+dart)"
		→ palette : flutter: new project
		go to lib/main.dart. This is your main app code.

		Make sure you have a device or emulator running. 
			On Mac you will need Xcode if you want the iOS simulators. 
			On WIndows or Mac if you want the Android emulators you will need Android Studio. 
		You can start an Android Emulator via the AVD Manager.

		→ Debug > Start Debugging to start running your app.

- [Lab: Write your first Flutter app](https://flutter.dev/docs/get-started/codelab)

- https://www.youtube.com/watch?v=7JdcGBSWo50

- https://github.com/Elvis10ten/FlutterCryptocurrencyListApp
- https://www.codeproject.com/Articles/1251117/Flutter-Getting-Started-Tutorial-1-Basics


# EVERYTHING IS A WIDGET

# C INTEROP

	https://dart.dev/guides/libraries/c-interop
	https://medium.com/flutter-community/build-and-deploy-native-c-libraries-with-flutter-cc7531d590b5

	hello.c

		#include <stdio.h>
		#include "hello.h"

		int main()
		{
		    hello_world();
		    return 0;
		}

		// Note:
		// ---only on Windows---
		// Every function needs to be exported to be able to access the functions by dart.
		// Refer: https://stackoverflow.com/q/225432/8608146
		void hello_world()
		{
		    printf("Hello World\n");
		}


## PLUGINS

* INSTALL THE FLUTTER AND DART PLUGINS

Start Android Studio
Preferences > Plugins
Select the Flutter plugin, click Install
Click Yes when prompted to install the Dart plugin
Click Restart when prompted.

Open pubspec.yaml
Add the url_launcher dependency: ...
shared_preferences: 2.0.5
>flutter pub get


* shared_preferences
	persistent storage on ios, android, macos...
	https://pub.dev/packages/shared_preferences
	https://pub.dev/packages/shared_preferences/example

	Android: shared Prefs
	Web: Local Storage
	Mac: Who cares
	Windows: IDK
	IOS: NSUserDefaults

	>flutter pub add shared_preferences
	This will add a line like this to your package's pubspec.yaml and run an implicit dart pub get
	dependencies:
	shared_preferences: ^2.0.6




## MORE

- https://www.didierboelens.com/
- https://levelup.gitconnected.com/writing-a-flutter-starter-application-for-beginners-f3e2ce591e3e
- https://raphaelstaebler.medium.com/from-zero-to-mvp-in-3-months-with-flutter-d6adcc1db9a7
- with REST APIs, retrofit is a great package that generates a lot of the code you would otherwise have to write yourself: https://pub.dev/packages/retrofit
- https://insights.dice.com/2021/06/02/flutter-what-you-need-to-know-about-cross-platform-development/
- https://levelup.gitconnected.com/writing-a-flutter-starter-application-for-beginners-f3e2ce591e3e
- https://raphaelstaebler.medium.com/from-zero-to-mvp-in-3-months-with-flutter-d6adcc1db9a7
- with REST APIs, retrofit is a great package that generates a lot of the code you would otherwise have to write yourself: https://pub.dev/packages/retrofit
- https://insights.dice.com/2021/06/02/flutter-what-you-need-to-know-about-cross-platform-development/
- [Dashboard](https://www.youtube.com/watch?v=_uOgXpEHNbc&t=205s)
- [Flutter way](https://www.youtube.com/channel/UCJm7i4g4z7ZGcJA_HKHLCVw)
- [firebase+Flutter](https://www.youtube.com/watch?v=niJ4wNee_Eo)
