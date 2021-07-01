# Rust

- https://www.rust-lang.org
- https://foundation.rust-lang.org/
- https://github.com/microsoft/windows-rs
- https://doc.rust-lang.org/book/title-page.html
- https://cheats.rs/
- https://github.com/microsoft/windows-rs/tree/master/examples

Get the latest version of Rust: rustup update

# RUST SAMPLES
download.slideshow(assets/books/code/langs/rust/code_samples/rust01.md)

```rust
fn main() {
    let v = vec![1,2,3,4,5];    
    let b: Vec<i32> = v.iter().map(|e| e * 2).collect();    
    println!("{:?}", b);
}
```

Rust chaining: a single statement can apply any number of functional operations to a collection
```rust
fn main() {
    let v = vec![1,2,3,4];
    
    let b = v.iter().map(|e| e * 2).filter(|e| e % 6 == 0).fold(0, |acc, x| acc + x);
    
    println!("{:?}", b);
}
```

```c++
#include <iostream>
#include <vector>
#include <algorithm>

int main() {

  std::vector<int> v{1,2,3,4};
  
  std::vector<int> b;
  std::transform(v.begin(), v.end(), std::back_inserter(b), [](int a){return 2 * a;});
  
  for (const auto& e : b) {
    std::cout << e << "\n";
  }
  
  return 0;
}
```

Open-source language; 6,000 contributors
Mozilla (2010, release in 2015) as an alternative to the C/C++
MIT and Apache License 

* Systems programming language 
* Guaranteed memory safety without garbage collection 
* Syntax and performance similar to C++ (but incorporates functional ideas properly). Both Rust and C++ have a first-class function concept. However, Rust lets you express your ideas in a way that’s much closer to pure functional.

Rust: It is a safe, concurrent, practical language. It is a systems programming language that combines strong compile-time correctness guarantees with fast performance. It is most loved programming language as per stackoverflow. The development of web, desktop and mobile apps all are supported in Rust too.

Safer alternative to C++ for low-level Windows programming. Rust is syntactically similar to C++ but has built-in protection against memory bugs that have long plagued developers working with the tricky and complicated C++. Thus Rust is sparking great interest in the .NET community
 
Microsoft's Rust v0.9 provides full consumption support, meaning the language is now capable of calling ANY WINDOWS API. Done with a "LANGUAGE PROJECTION" (developers interact with Windows Runtime (WinRT) APIs in ways natural -- or idiomatic -- to specific languages).   
Language projections:   
- C++/WinRT
- C#/WinRT
- Rust/WinRT ["Rust for Windows"](https://github.com/microsoft/windows-rs)










Welcome to Rust!

This will download and install the official compiler for the Rust
programming language, and its package manager, Cargo.

Rustup metadata and toolchains will be installed into the Rustup
home directory, located at:

  C:\Users\nguin\.rustup

This can be modified with the RUSTUP_HOME environment variable.

The Cargo home directory located at:

  C:\Users\nguin\.cargo

This can be modified with the CARGO_HOME environment variable.

The cargo, rustc, rustup and other commands will be added to
Cargo's bin directory, located at:

  C:\Users\nguin\.cargo\bin

Cargo: the Rust build tool and package manager
When you install Rustup you’ll also get the latest stable version of the Rust build tool and package manager, also known as Cargo. Cargo does lots of things:

build your project with cargo build
run your project with cargo run
test your project with cargo test
build documentation for your project with cargo doc
publish a library to crates.io with cargo publish
To test that you have Rust and Cargo installed, you can run this in your terminal of choice:

cargo --version



 


Start:
1. https://github.com/microsoft/windows-rs
2. cd windows-rs\examples\simple
3. cargo build
4. cargo run


> cargo build      build your project 
> cargo run        run your project 
> cargo test       test your project 
> cargo doc        build documentation for your project 
> cargo publish    publish a library to crates.io 
>cargo --version   test that you have Rust and Cargo installed



“most-loved programming language”
For systems that emphasize parallelism, speed, memory safety
Designed with safety in mind
Good at running concurrent code
Users of C++ will find it very familiar.

built from scratch to incorporate multiple design elements from other mature systems programming languages

Applications
IoT: from operating systems, gaming engines, file systems, web browser components, and new simulation engines for virtual reality.
Rust directly interacts with the memory and hardware, it is an ideal language for embedded systems and bare-metal development. 
Rust can write extremely low machine-level code, making it ideal for working with microcontroller applications or OS kernels. Machine code is the language that is as close as possible to what the server’s CPU can run. 

## Rust Ecosystem
- Standardized compiler 
- built-in package manager and builder
- a testing system
- a documentation generator


### Cargo
Rust package manager
Can auto-generate documentation, run tests, and upload packages to a repository. 
It also downloads and installs multiple third-party packages with ease.
https://crates.io/

CRATES
Rust community’s crate registry
https://crates.io/
https://crates.io/crates/hyper    A fast and correct HTTP implementation for Rust.
       https://hyper.rs/
       
```rust       
use std::{convert::Infallible, net::SocketAddr};
use hyper::{Body, Request, Response, Server};
use hyper::service::{make_service_fn, service_fn};

async fn handle(_: Request<Body>) -> Result<Response<Body>, Infallible> {
Ok(Response::new("Hello, World!".into()))
}

#[tokio::main]
async fn main() {
let addr = SocketAddr::from(([127, 0, 0, 1], 3000));

let make_svc = make_service_fn(|_conn| async {
       Ok::<_, Infallible>(service_fn(handle))
});

let server = Server::bind(&addr).serve(make_svc);

if let Err(e) = server.await {
       eprintln!("server error: {}", e);
}
}
```

## Install

Linux: curl https://sh.rustup.rs -sSf | sh 
       /usr/local/lib/rustlib/uninstall.sh
Windows: https://win.rustup.rs/x86_64 or Scoop/Chocolatey 

IDE
- Visual Studio Code
- IntelliJ’s rust-analyzer: https://www.jetbrains.com/idea/
- https://intellij-rust.github.io/


## web applications
[Crates:  Rust community’s crate registry](https://crates.io/)

[Rocket](https://rocket.rs/)
[Actix](https://crates.io/crates/actix-web)
[Nickel](https://crates.io/crates/nickel)

[warp](https://crates.io/crates/warp)
[gotham](https://crates.io/crates/gotham)


## Microservices
- https://genekuo.medium.com/coding-a-simple-microservices-with-rust-3fbde8e32adc
- https://medium.com/tenable-techblog/building-a-microservice-with-rust-23a4de6e5e14

## More

- https://www.liquidweb.com/kb/how-to-install-and-configure-the-rust-programming-language
- https://www.youtube.com/embed/LajquCjHXK4

- https://github.com/saschagrunert/webapp.rs
- https://medium.com/@saschagrunert/lessons-learned-on-writing-web-applications-completely-in-rust-2080d0990287