# MinGW[http://www.mingw.org/] (Minimalistic GNU for Windows)

* Collection d’outils permettant de faire de la programmation, parmi ces outils sont présents des portages de gcc, gdb, make…
* Ne nécessite pas la présence de DLL intermédiaires (comme Cygwin, ou Visual Studio 2005). 
* Un autre de ses autres avantages est la présence d’un portage de l’API Windows sous forme de headers et librairies.
* MinGW se décompose en plusieurs packages remplissant chacun une fonction (compilation, debuggage, API, …).
* GNU toolsets that allow one to produce native Windows programs that do not rely on any 3rd-party C runtime DLLs
* Dosesn't provide a POSIX runtime environment for POSIX application deployment on MS-Windows. If you want POSIX application deployment on this platform, please consider Cygwin instead.

# Minimalist development environment (Open Source programming tool) for the development of native MS-Windows applications which do not depend on any 3rd-party C-Runtime DLLs. (It does depend on a number of DLLs provided by Microsoft themselves, as components of the operating system; most notable among these is MSVCRT.DLL, the Microsoft C runtime library. Additionally, threaded applications must ship with a freely distributable thread support DLL, provided as part of MinGW itself).

# MinGW compilers provide access to the functionality of the Microsoft C runtime and some language-specific runtimes. MinGW, being Minimalist, does not, and never will, attempt to provide a POSIX runtime environment for POSIX application deployment on MS-Windows. If you want POSIX application deployment on this platform, please consider Cygwin instead.

# Collection of freely available and freely distributable Windows specific header files and import libraries combined with GNU toolsets that allow one to produce native Windows programs that do not rely on any 3rd-party C runtime DLLs. Gambit Scheme system, compiler and interpreter

# MinGW, a fork of Cygwin, provides a less POSIX-compliant development environment and supports compatible C-programmed applications via Msvcrt, Microsoft's old Visual C runtime library.

# POSIX
* IEEE defined standards APIs (interface between an application and the os) for software compatibility between operating systems
* Enable an application written for a POSIX conformant operating system to be compiled for another POSIX conformant operating system

# CYGWIN
provides a largely POSIX-compliant development and run-time environment for Microsoft Windows.
# MinGW, a fork of Cygwin, provides a less POSIX-compliant development environment and supports compatible C-programmed applications via Msvcrt, Microsoft's old Visual C runtime library.
* a large collection of GNU and Open Source tools which provide functionality similar to a Linux distribution on Windows.
* a DLL (cygwin1.dll) which provides substantial POSIX API functionality.
* rebuild your linux applications from source if you want it to run on Windows


choco install mingw

// hello.c
// cmd
// > gcc hello.c -o hello.exe  !! can generate a "false positive" with some antivirus
// > hello
#include <stdio.h>
int main(int argc, char *argv[])
{
  printf("Hello World\n");
}

# On Unix, for historical reasons, the default name of an executable is a.out. For MinGW, the default name is a.exe



# MinGW includes
.A port of the GNU Compiler Collection (GCC), including C, C++, ADA and Fortran compilers;
.GNU Binutils for Windows (assembler, linker, archive manager)
.A command-line installer, with optional GUI front-end, (mingw-get) for MinGW and MSYS deployment on MS-Windows
.A GUI first-time setup tool (mingw-get-setup), to get you up and running with mingw-get.


gcc-core : Le compilateur c
gcc-g++ : Le compilateur c++
binutils : Les outils de linkage, assemblage, gestion des ressources, …
mingw-runtime : Les headers et librairies permettant d’utiliser les fonctions de base du standard C/C++
w32api : Les headers et librairires permettant d’utiliser les fonctions de l’API Windows
gmp, mpc, mpfr : des librairies de calcul mathématique avancé utilisées par gcc
# De plus si vous souhaitez utiliser MinGW avec CDT dans Eclipse, les packages suivants sont indispensables :
gdb : Le portage du debuggeur GNU gdb
mingw32-make : Le portage de l’outil make
expat : Librairie utilisée par gdb

# Ajout de la commande ‘make’
pour appeller make, il faut écrire : « mingw32-make ». C’est pourquoi je recommande d’ajouter la commande « make » en suivant les étapes ci-dessous :
# Créer un nouveau fichier avec le Bloc-Notes Windows contenant les lignes suivantes :
@echo off
mingw32-make %*

# PS : la dernière ligne blanche ne doit pas être oubliée !
# Enregistrer ce fichier dans le dossier bin de l’installation de MinGW (ex : « C:\MinGW\bin ») en l’appellant : « make.cmd » (Attention à ce qu’il ne soit pas nommé « make.cmd.txt »)
# Après cela, lorsque vous tapperez « make » dans l’invite de commandes, tout se passera comme si c’était « mingw32-make » qui aura été écrit (avec les arguments transmis biensûr)


# Librairies standard pour le C++
# Ceux d’entre vous qui tenteront d’utiliser g++ auront d’étranges surprises. En effet, un programme codé en C++ utilise presque systématiquement les librairies standard C++. Jusque là pas d’inquiétude, sauf que depuis les versions récentes de g++ (4.4 et 4.5) ces librairies sont linkées (reliées au programme principal) de façon dynamique alors que dans les vieilles version c’était statique. L’impact c’est qu’il est donc nécessaire d’avoir ces librairies (standard C et standard C++) accessibles sous forme de dll (libgcc_s_dw2.dll et libstdc++-6.dll) distribuées avec le programme principal, sinon il ne fonctionnera pas. Ces DLL sont téléchargeables sur le site SourceForge de MinGW.
# Il existe aussi une alternative à devoir se trimbaler ces DLL avec son exécutable. C’est de forcer le linkage statique. C’est possible en ajoutant les options de linkage suivantes (sur gcc ou ld) : -static-libgcc -static-libstdc++
# Cela va rendre l’exécutable plus gros (car il inclura une partie du code présent dans les dll précédentes), mais les dépendances DLL sont supprimées, ce qui rend la distribution du programme plus simple.


# MSYS (Minimal SYStem)
# Bourne Shell command line interpreter system
# Offered as an alternative to Microsoft's cmd.exe
# Provides a general purpose command line environment, which is particularly suited to use with MinGW, for porting of many Open Source applications to the MS-Windows platform; a light-weight fork of Cygwin-1.3, it includes a small selection of Unix tools, chosen to facilitate that objective.

#CODE::BLOCKS
# Code::Blocks and MINGW, A Free C and C++ Compiler, on Windows
http://www.codeblocks.org/
http://www.cprogramming.com/code_blocks/
a free, open-source, cross-platform C, C++ and Fortran IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.
# Finally, an IDE with all the features you need, having a consistent look, feel and operation across platforms.



