# (CYGWIN)[http://www.cygwin.com/]

* Large collection of GNU and Open Source tools which provide functionality similar to a Linux distribution on Windows.
* a DLL (cygwin1.dll) which provides substantial POSIX API functionality.
* When you're using CygWin, you're not using a Linux distribution. You're using CygWin. 

Cygwin have made it possible to port Unix and Linux tools to Windows, but now with wsl you can run actual Linux binaries without having to dual boot or set up a virtual machine. 

Cygwin where the developers have created a DLL that translates the Linux system calls to Windows. 
With Cygwin, the programs are recompiled into Windows executables.

Windows bash shell emulator (windows tools like Linux = 'Linux feeling on windows')

Get that Linux feeling - on Windows
POSIX for Windows
Cygwin provides a largely POSIX-compliant development and run-time environment for Microsoft Windows.

Cygwin is a compatibility layer, which aims to implement as much as possible of the POSIX and Linux APIs within Windows.
Cygwin is an emulation layer. It allows UNIX code to run on Windows, if you compile it to use the emulation layer. To Windows it looks like any normal DLL and makes OS calls as normal. But when you compile against it, it shows the same functions as UNIX (well, POSIX technically, but UNIX it is). Cygwin is not a Linux emulator, i.e. it doesn't produce or run Linux executables.


* MinGW
	a fork of Cygwin
	provides a less POSIX-compliant development environment and supports compatible C-programmed applications via Msvcrt, Microsoft's old Visual C runtime library.
	posix--

rebuild your linux applications from source if you want it to run on Windows


* WSL
	a layer inside of Windows that allows actual Linux distributions to run against. 
	Microsoft is providing the foundation for Linux distributions to build upon, and keeping their hands out of the tooling itself.

	When you're using CygWin, you're not using a Linux distribution. You're using CygWin. 
	With WSL, you're not using any Linux distributions unless you install them on top of the WSL. 
	Once you do, you're using the tooling provided and build for that Linux distribution.

## Install
choco install cygwin

## Use
# C:\cygwin64>Cygwin.bat
$ pwd
/home/nguin   === C:\cygwin64\home\nguin
$ notepad VR3.txt &
cd . 	go home diretory
cd .. 	prev dir
ls -l 	full, detailed listing





