# Rust

https://www.rust-lang.org
https://foundation.rust-lang.org/
https://github.com/microsoft/windows-rs
https://doc.rust-lang.org/book/title-page.html
https://cheats.rs/

Open-source language; 6,000 contributors
Mozilla (2010, release in 2015) as an alternative to the C/C++
MIT and Apache License 

* Systems programming language 
* Syntax and performance similar to C++ 
* Guaranteed memory safety without garbage collection 

Rust: It is a safe, concurrent, practical language. It is a systems programming language that combines strong compile-time correctness guarantees with fast performance. It is most loved programming language as per stackoverflow. The development of web, desktop and mobile apps all are supported in Rust too.

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
## ## More

- https://www.liquidweb.com/kb/how-to-install-and-configure-the-rust-programming-language
- https://www.youtube.com/embed/LajquCjHXK4
