# WASM - Web Assembly

A language specification for a virtual machine that runs in the browser (or out the browser: wasi). Web Assembly is based on LLVM  (Low Level Virtual Machine), a stack based virtual machine that compilers can target

Runtime, with multi-language support, that provides near-native execution speeds within the browser,

JavaScript complement (not a replacement) to run bytecode on the web
Runs on
- all major web browsers
- V8 runtimes (Node.js)
- Independent Wasm runtimes: standalone runtime for WebAssembly
>[Wasmtime](https://wasmtime.dev/)
- https://github.com/bytecodealliance/wasmtime/
WebAssembly runtime. It runs WebAssembly outside of the browser, in a fast, portable, secure, and scalable way.
> Lucet
> Wasmer
> WebAssembly Micro-Runtime (WAMR)
WAMR is an interpreter based WebAssembly runtime, optimized for embedded and resource-constrained devices.


Let’s use already existing useful code that has been written for other environments.  
Performance benefits over JavaScript.

- https://wasmweekly.news/
- https://github.com/diekmann/wasm-fizzbuzz : WebAssembly from Scratch: From FizzBuzz to DooM

# WASI - WebAssembly System Interface

a specification, led by the [Bytecode Alliance](https://bytecodealliance.org/), that is adding various out-of-browser capabilities.
The Wasi interface, initiated by Mozilla is an extension of WebAssembly based upon the idea of running WebAssembly programs outside of a browser. 

# WABT
https://github.com/WebAssembly/wabt

## Langs for wasm
https://docs.wasmtime.dev/lang.html

- C/C++
- C#/.NET
- Python
- Java
- Go
- Rust
- Elixir
- Bash
- https://www.assemblyscript.org/

## Sample

- Setup  

```bash
git clone https://github.com/emscripten-core/emsdk.git
cd emsdk
git pull
./emsdk install latest
./emsdk activate latest
```

***Set some environment variables:***

On Windows 10 run
>emsdk_env.bat

For the other operating systems run
>source emsdk_env.sh

Using Visual Studio Code:
```c++
#include 
int main(int argc, char**argv) 
{
     printf("Hello World!\n");
    return 0;
}
```

Compile the code:
>emcc hello.cpp -o hello.html

After the compiler runs you will have three new files.
- hello.wasm – the compiled version of your program
- hello.html – an HTML page for hosting your web assembly
- hello.js – JavaScript for loading your web assembly into the page

the html page will have to be served through an HTTP server. 
>npm install  http-server -g

Start the server from the directory with your hello.html
>http-server . -p 81

Open a browser and navigate to http://localhost:81/hello.html. 

Web Assembly Explorer
>https://mbebenita.github.io/WasmExplorer/  
Online tool for compiling C++ into Web Assembly and is an option if you don’t have the tools installed.

## https://bytecodealliance.org/

 open source community dedicated to creating secure new software foundations, building on standards such as WebAssembly and WebAssembly System Interface (WASI).

## webassembly
https://webassembly.org/

## Wasi - WebAssembly System Interface 
https://wasi.dev/

https://github.com/bytecodealliance/wasmtime/blob/main/docs/WASI-tutorial.md


### wasmtime

https://wasmtime.dev/

a WebAssembly runtime 
Run WebAssembly outside the web (browser), in a fast, portable, secure, and scalable way
Used both as 
- a command-line utility 
- a library embedded in a larger application.

Written in Rust, but bindings are available through a C API for a number of other languages too:

Rust
C
Python
.NET
Go
Bash


### Lucet 
https://github.com/bytecodealliance/lucet

AOT compiler utilizing Cranelift. It is meant specifically for low-latency, high-concurrency server-based applications of WebAssembly.

### More
- https://wasmbyexample.dev
- https://github.com/torch2424
- https://blog.j2i.net/2020/12/20/introduction-to-web-assembly-with-c-c-part-1/