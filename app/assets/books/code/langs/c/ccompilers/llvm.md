# LLVM - Low-Level Virtual Machine

https://www.llvm.org/

Collection of compiler or toolchain technologies: it means that we’re not stuck with GCC when we need to compile a program, which enforces a GNU GPL license. 

Clang
C/C++ compiler frontend for LLVM
- Extensive
- Cross-platform (makes it preferable to GCC mostly sticked to *nix platforms like Linux or macOS, and doesn’t normally play well with the Win32 platform without a compatibility layer such as MinGW or Cygwin (and, more recently, the WSL).
- Better debugging experience than that of GCC and, make a short trial run, you’ll see what I mean.

additions to the language and discuss what they provide and take away from the context of a healthy programming language.





## LLVM is a libraries framework

	.front end : translate program languages, such as c/c++ to IR
	.optimizer : faster the speed, IR to IR
	.back end: generate code for machine, from IR to Object files


	when a lot of people talk about LLVM, they actually mean clang, the C and C++ compiler that made a massive impact thanks to Apple (and thanks to pretty useful compiler error messages). Simplified, clang compiles C/C++ to an intermediate representation for LLVM, and LLVM then compiles machine code from that. The advantage is that if you have a new programming language, you only write 1 compiler (Language -> LLVM) and not worry about x86/x64/arm/other platforms since LLVM does that



## The LLVM compiler infrastructure project (formerly Low Level Virtual Machine) is a "collection of modular and reusable compiler and toolchain technologies" used to develop compiler front ends and back ends.

	LLVM is a library that is used to construct, optimize and produce intermediate and/or binary machine code.

## LLVM can be used as a compiler framework, where you provide the "front end" (parser and lexer) and the "back end" (code that converts LLVM's representation to actual machine code).

	LLVM can also act as a JIT compiler - it has support for x86/x86_64 and PPC/PPC64 assembly generation with fast code optimizations aimed for compilation speed.

## If you're interested, you can play with LLVM's machine code that is generated from C or C++ code in their demo page: http://llvm.org/demo/


	The Low Level Virtual Machine (LLVM) is a compiler infrastructure, written in C++, which is designed for compile-time, link-time, run-time, and "idle-time" optimization of programs written in arbitrary programming languages. Originally implemented for C/C++, the language-independent design (and the success) of LLVM has since spawned a wide variety of front-ends, including Objective C, Fortran, Ada, Haskell, Java bytecode, Python, Ruby, ActionScript, GLSL, and others.

	http://en.wikipedia.org/wiki/Low_Level_Virtual_Machine


## LLVM is basically a library used to build compilers and/or language oriented software. The basic gist is although you have gcc which is probably the most common suite of compilers , it is not built to be re-usable ie. it is difficult to take components from gcc and use it to build your own application . LLVM addresses this issue well by building a set of " modular and reusable compiler and toolchain technologies" which anyone could use to build compilers and language oriented software.



	the name LLVM might refer to any of the following:

## The LLVM project/infrastructure: This is an umbrella for several projects that, together, form a complete compiler: frontends, backends, optimizers, assemblers, linkers, libc++, compiler-rt, and a JIT engine. The word "LLVM" has this meaning, for example, in the following sentence: "LLVM is comprised of several projects".

	An LLVM-based compiler: This is a compiler built partially or completely with the LLVM infrastructure. For example, a compiler might use LLVM for the frontend and backend but use GCC and GNU system libraries to perform the final link. LLVM has this meaning in the following sentence, for example: "I used LLVM to compile C programs to a MIPS platform".

## LLVM libraries: This is the reusable code portion of the LLVM infrastructure. For example, LLVM has this meaning in the sentence: "My project uses LLVM to generate code through its Just-in-Time compilation framework".

	LLVM core: The optimizations that happen at the intermediate language level and the backend algorithms form the LLVM core where the project started. LLVM has this meaning in the following sentence: "LLVM and Clang are two different projects".

## The LLVM IR: This is the LLVM compiler intermediate representation. LLVM has this meaning when used in sentences such as "I built a frontend that translates my own language to LLVM"


# Clang 
		compiler front end for the programming languages C, C++, Objective-C, Objective-C++, OpenMP, OpenCL, and CUDA. 
		It uses LLVM as its back end and has been part of the LLVM release cycle since LLVM 2.6. It is designed to be able to replace the full GNU Compiler Collection (GCC).

# LLDB 
		is a next generation, high-performance debugger. It is built as a set of reusable components which highly leverage existing libraries in the larger LLVM Project, such as the Clang expression parser and LLVM disassembler.		

# Emscripten
		is a source-to-source compiler that runs as a back end to the LLVM compiler and produces a subset of JavaScript known as asm.js. This allows applications and libraries originally designed to be run as standard executables to be integrated into client side web applications.		



