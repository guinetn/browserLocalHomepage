# Cmake

- https://cmake.org
- https://medium.com/swlh/c-project-structure-for-cmake-67d60135f6f5

open-source, cross-platform tools to build, test, package software

Control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice. 


how C++ project structure should look
how to make cross-platform builds

{library_name}
 ├── include                        PUBLIC header files (.h files).
 │   └── {library_domain}
 ├── src                            PRIVATE source files (.h and .m files).
 ├── test                           tests files if you write tests (indefinitely you should).
 └── libs                           third party or your own libraries you depend on.
 
 
The building blocks of CMake are CMakeLists.txt files. You basically write those CMakeLists files and they define what should be included into generated build system. 