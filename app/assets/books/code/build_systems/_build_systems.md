# BUILD SYSTEMS

A buildsystem describes how to build a project's executables and libraries from its source code using build tools to automate the process. A buildsystem may be a Makefile for use with a command-line make tool or a project file for an Integrated Development Environment (IDE). 

Every programmer needs a build system toa void mistakes while running compîlers by command line
>gcc hello.c sqlite3.dll -o hello.exe     if a dll is needed

C++ compiler and build tools:
- On *NIX platforms it is usually GCC/G++ or Clang compiler and Make or Ninja build tool
- On Windows: Visual Studio IDE or MinGW-w64 compiler
- Native toolchains for Android are provided in the Android NDK
- XCode IDE is used to build software for OSX and iOS platforms

Some code editors like Microsoft Visual Studio have their own built in build tools

- MSBuild: XML not very handy
- PowerShell: lost of unknown
- Fake: new language with a learning curve
- Cake: still scripting

## Java
download.page(code/build_systems/ant.md)
download.page(code/build_systems/maven.md)
download.page(code/build_systems/gradle.md)

# Misc
download.page(code/build_systems/bazel.md)
download.page(code/build_systems/cake.md)
download.page(code/build_systems/cmake.md)
download.page(code/build_systems/fake.md)
download.page(code/build_systems/make.md)
download.page(code/build_systems/ninja.md)
download.page(code/build_systems/rake.md)
download.page(code/build_systems/nuke.md)

## MS
download.page(code/build_systems/visualstudio.md)
download.page(code/build_systems/msbuild.md)
download.page(code/build_systems/nmake.md)
download.page(code/scripting/powershell/_powershell.md)
