# CMake

- https://cmake.org/
- https://medium.com/swlh/c-project-structure-for-cmake-67d60135f6f5
- https://www.bogotobogo.com/cplusplus/make.php

CMake is a tool to manage building of source code.
CMake is a generator of build systems that can produce Makefiles for Unix like systems, Visual Studio Solutions for Windows and XCode projects for Mac OS.

open-source, cross-platform family of tools designed to build, test and package software. CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice. The suite of CMake tools were created by Kitware in response to the need for a powerful, cross-platform build environment for open-source projects such as ITK and VTK.

open-source, cross-platform tools to build, test, package software

Control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice. 

A build system generator
CMake is a generator: it generates native build systems files (Makefile, IDE project files, ...), so it does not compile (i.e. build) the sources, the underlying build tool (make, XCode, Code::Blocks...) does.
CMake scripting language is used to describe the build
The developer edit CMakeLists.txt invoke CMake but should never edit the generated files
CMake may be (automatically) re-invoked by the build system





how C++ project structure should look
how to make cross-platform builds

{library_name}
 ├── include                        PUBLIC header files (.h files).
 │   └── {library_domain}
 ├── src                            PRIVATE source files (.h and .m files).
 ├── test                           tests files if you write tests (indefinitely you should).
 └── libs                           third party or your own libraries you depend on.
 
 
The building blocks of CMake are CMakeLists.txt files. 
You basically write those CMakeLists files and they define what should be included into generated build system. 

## install
configure: 
>cmake
C:\Program Files\CMake\bin\cmake.exe
C:\Program Files\CMake\bin\cmake-gui.exe

## generators
cmake --help     list generators available (kind of buildsystem to generate)

## 
mkdir build ; cd build
cmake ../src                 source tree must contain a CMakeLists.txt

cmake .                     

After generating a buildsystem one may use the corresponding native build tool to build the project. For example, after using the Unix Makefiles generator one may run make directly:

$ make
$ make install
Alternatively, one may use cmake to Build a Project by automatically choosing and invoking the appropriate native build tool.


## Basic project 

an executable built from source code files  
For simple projects, a three line CMakeLists.txt file is all that is required

CMakeLists.txt
```makefile
cmake_minimum_required(VERSION 3.20.4)
# set the project name
project(Tutorial)
# add the executable
add_executable(Tutorial tutorial.cxx)
```

# Visualization Toolkit (VTK)
http://www.vtk.org/

open source 3D graphics and visualization system.



# SAMPLE 01

~/Work/bogo/bogo.c
bogo.c
```c
#include <stdio.h>

int main()
{
    printf("bogo CMake test\n");
}
```

~/Work/bogo/CMakeLists.txt
CMakeLists.txt
```makefile
cmake_minimum_required(VERSION 2.8.12)
project(bogoCMake)
add_executable(bogoCMake bogo.c)
```

Make a build directory. ~/Work/bogo/build. Everything will be built under this directory.
$ ls        ~/Work/bogo 
bogo.c  build  CMakeLists.txt

>cd build
>cmake ..
-- The C compiler identification is GNU 4.7.2
-- The CXX compiler identification is GNU 4.7.2
   ...
-- Configuring done
-- Generating done
-- Build files have been written to: /home/Work/bogo/build
   
If we look into the build directory, we can see what's been done by the CMake.
$ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile
  
We can finish the process by issuing make
$ make
Scanning dependencies of target bogoCMake
[100%] Building C object CMakeFiles/bogoCMake.dir/bogo.o
Linking C executable bogoCMake
[100%] Built target bogoCMake
  
Let's look into the directory to see what's been newly added:
$ ls
bogoCMake  CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile  
  
Since our executable has been made (bogoCMake), we can run it.
$ ./bogoCMake
bogo CMake test










https://cmake.org/
https://cmake.org/cmake-tutorial/
https://frankie-yanfeng.github.io/2019/11/12/CMake-2019/


	open-source, cross-platform family of tools designed to build, test and package software. 
	Control compilation using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice. The suite of CMake tools were created by Kitware in response to the need for a powerful, cross-platform build environment for open-source projects such as ITK and VTK.

Ex:

	https://github.com/hachibu/note.sh
	https://github.com/hachibu/note.sh/blob/main/Makefile

	MAKE
		current_dir = $(shell pwd)
		install:
			ln -s $(current_dir)/src/note.sh /usr/local/bin/note.sh
		uninstall:
			unlink /usr/local/bin/note.sh

	note.sh
		#!/usr/bin/env bash
		set -euo pipefail

		if [ -z ${NOTE_DIR+x} ]; then
		  echo "Error: Please configure and export NOTE_DIR environment variable."
		  exit 1
		fi

		function usage() {
		  echo "Usage: note.sh [action]"
		  echo
		  echo "  actions:"
		  echo "    grep [pattern]"
		}

		mkdir -p "$NOTE_DIR"

		if [ $# -eq 0 ]; then
		    $EDITOR "$NOTE_DIR/$(date +'%Y-%m-%d').md"
		else
		  case $1 in
		    grep)
		      grep -i -r --color "$2" "$NOTE_DIR"
		      ;;
		    *)
		      usage
		      ;;
		  esac
		fi

# Ex: http://asciidoc.org/INSTALL.html

	asciidoc - converts an AsciiDoc text file to HTML or DocBook

	Installing asciidoc for all users
	Create configure using autoconf(1); use configure to create the Makefile; run make(1); build the man pages; install:
	$ autoconf
	$ ./configure
	$ make
	$ sudo make install

	To uninstall:
	$ sudo make uninstall

# Distribution tarball installation
	$ tar -xzf asciidoc-8.6.9.tar.gz
	$ cd asciidoc-8.6.9
	$ ./configure
	$ sudo make install
	To install the documentation:

	$ sudo make docs
	To uninstall AsciiDoc:

	$ sudo make uninstall


>cmake /?
>cmake --system-information [file]  = Dump information about this system.
...
# CMAKE_DL_LIBS == ""
# CMAKE_LIBRARY_PATH_FLAG == "-LIBPATH:"
# CMAKE_LINK_LIBRARY_FLAG == ""
# CMAKE_SKIP_RPATH == "NO"
# CMAKE_SYSTEM_INFO_FILE == "Platform/Windows"
# CMAKE_SYSTEM_NAME == "Windows"
# CMAKE_SYSTEM == "Windows-10.0.17134"
# CMAKE_CXX_COMPILER == "C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.15.26726/bin/Hostx86/x86/cl.exe"    ← cl.exe
# CMAKE_C_COMPILER == "C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.15.26726/bin/Hostx86/x86/cl.exe"
# CMAKE_COMPILER_IS_GNUCC == ""
# CMAKE_COMPILER_IS_GNUCXX == ""
...

# Unix-like 
# Makefiles originated in Unix like systems and is still the primary software build mechanism.

# Microsoft Windows
# Windows supports a variation of makefiles with its nmake utility. Standard Unix like makefiles can be executed in Windows in a Cygwin environment.

# There are some better builder than GNU Make, like Omake http://omake.metaprl.org/index.html


# CMake is designed to be used in conjunction with the native build environment. 
# Simple configuration files placed in each source directory (called CMakeLists.txt files) are used to generate standard build files 
• makefiles on Unix
• projects/workspaces in Windows MSVC

# CMakeLists.txt 

# In CMake, this is a comment

# To run our code, we will use these steps:
#  - mkdir build && cd build
#  - cmake ..
#  - make
# 
# With those steps, we will follow the best practice to compile into a subdir
# and the second line will request to CMake to generate a new OS-dependent
# Makefile. Finally, run the native Make command.

#------------------------------------------------------------------------------
# Basic
#------------------------------------------------------------------------------
#
# The CMake file MUST be named as "CMakeLists.txt".

# Setup the minimum version required of CMake to generate the Makefile
cmake_minimum_required (VERSION 2.8)

# Raises a FATAL_ERROR if version < 2.8
cmake_minimum_required (VERSION 2.8 FATAL_ERROR)

# We setup the name for our project. After we do that, this will change some
# directories naming convention generated by CMake. We can send the LANG of
# code as second param
project (learncmake C)

# Set the project source dir (just convention)
set( LEARN_CMAKE_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR} )
set( LEARN_CMAKE_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR} )

# It's useful to setup the current version of our code in the build system
# using a `semver` style
set (LEARN_CMAKE_VERSION_MAJOR 1)
set (LEARN_CMAKE_VERSION_MINOR 0)
set (LEARN_CMAKE_VERSION_PATCH 0)

# Send the variables (version number) to source code header
configure_file (
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
    "${PROJECT_BINARY_DIR}/TutorialConfig.h"
)

# Include Directories
# In GCC, this will invoke the "-I" command
include_directories( include )

# Where are the additional libraries installed? Note: provide includes
# path here, subsequent checks will resolve everything else
set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMake/modules/" )

# Conditions
if ( CONDITION )
    # Output!

    # Incidental information
    message(STATUS "My message")

    # CMake Warning, continue processing
    message(WARNING "My message")

    # CMake Warning (dev), continue processing
    message(AUTHOR_WARNING "My message")

    # CMake Error, continue processing, but skip generation
    message(SEND_ERROR "My message")

    # CMake Error, stop processing and generation
    message(FATAL_ERROR "My message")
endif()

if( CONDITION )

elseif( CONDITION )

else( CONDITION )

endif( CONDITION )

# Loops
foreach(loop_var arg1 arg2 ...)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
endforeach(loop_var)

foreach(loop_var RANGE total)
foreach(loop_var RANGE start stop [step])

foreach(loop_var IN [LISTS [list1 [...]]]
                    [ITEMS [item1 [...]]])

while(condition)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
endwhile(condition)


# Logic Operations
if(FALSE AND (FALSE OR TRUE))
    message("Don't display!")
endif()

# Set a normal, cache, or environment variable to a given value.
# If the PARENT_SCOPE option is given the variable will be set in the scope
# above the current scope.
# `set(<variable> <value>... [PARENT_SCOPE])`

# How to reference variables inside quoted and unquoted arguments
# A variable reference is replaced by the value of the variable, or by the
# empty string if the variable is not set
${variable_name}

# Lists
# Setup the list of source files
set( LEARN_CMAKE_SOURCES 
    src/main.c
    src/imagem.c
    src/pather.c
)

# Calls the compiler
#
# ${PROJECT_NAME} refers to Learn_CMake 
add_executable( ${PROJECT_NAME} ${LEARN_CMAKE_SOURCES} )

# Link the libraries
target_link_libraries( ${PROJECT_NAME} ${LIBS} m )

# Where are the additional libraries installed? Note: provide includes
# path here, subsequent checks will resolve everything else
set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMake/modules/" )

# Compiler Condition (gcc ; g++)
if ( "${CMAKE_C_COMPILER_ID}" STREQUAL "GNU" )
    message( STATUS "Setting the flags for ${CMAKE_C_COMPILER_ID} compiler" )
    add_definitions( --std=c99 )
endif()

# Check for OS
if( UNIX )
    set( LEARN_CMAKE_DEFINITIONS
        "${LEARN_CMAKE_DEFINITIONS} -Wall -Wextra -Werror -Wno-deprecated-declarations -Wno-unused-parameter -Wno-comment" )
endif()



