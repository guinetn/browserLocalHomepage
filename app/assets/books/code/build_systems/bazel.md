# Bazel

https://bazel.build/
https://docs.bazel.build/versions/master/tutorial/cpp.html

Google open source tool (from blaze) 
Automation of building and testing of software

Similar to build tools like Make, Apache Ant, or Apache Maven
Bazel builds software applications from source code using a set of rules. 
    Rules and macros are created in the Skylark language, a subset of Python
    There are built-in rules for building software written in the programming languages of Java, C, C++, Python, Objective-C and Bourne shell scripts
Bazel can produce software application packages suitable for deployment for the Android and iOS operating systems.[6]


open-source build and test tool similar to Make, Maven, and Gradle. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms.

build a single target residing in a single package

cpp-tutorial/stage1

	  WORKSPACE (file)
	 	
	 	lives at the root of the project’s directory structure
	 	identifies the directory that holds your project’s source files and Bazel’s build outputs as a Bazel workspace 

>cd cpp-tutorial/stage1
>bazel build //main:hello-world		
			   \         \
				\         \___hello-world is what we named that target in the BUILD file
				 \
				  \___ //main:  is the location of our BUILD file relative to the root of the workspace

cpp-tutorial/stage1/main

BUILD (one or ++ files)
Tell Bazel how to build different parts of the project. (A directory within the workspace that contains a BUILD file is a package.
Instructions for Bazel
Build rule: Tells Bazel how to build the desired outputs (exec, libs)
            Each instance of a build rule in the BUILD file is called a target and points to a specific set of source files and dependencies. A target can also point to other targets.
```
cc_binary(
    name = "hello-world",                 ← Target name. Instantiates Bazel’s built-in 'cc_binary' rule. 
    srcs = ["hello-world.cc"],            The rule tells Bazel to build a self-contained exe binary from hello-world.cc  with no dependencies. 
)
```

hello-world.cc
```c
#include <ctime>
#include <string>
#include <iostream>

std::string get_greet(const std::string& who) {
    return "Hello " + who;
}

void print_localtime() {
    std::time_t result = std::time(nullptr);
    std::cout << std::asctime(std::localtime(&result));
}

int main(int argc, char** argv) {
    std::string who = "world";
    if (argc > 1) {
    who = argv[1];
    }
    std::cout << get_greet(who) << std::endl;
    print_localtime();
    return 0;
}
```




In designing Bazel, emphasis has been placed on build speed, correctness, and reproducibility. The tools uses parallelization to speed up parts of the build process.
It includes a Bazel Query language that can be used to analyze build dependencies in complex build graphs

	>y
	choco install bazel

	a build tool which coordinates builds and run tests. It works with source files written in any language, with native support for Java, C, C++ and Python. Bazel produces builds and runs tests for multiple platforms.

	WORKSPACE  		reference external dependencies 
	BUILD 			targets can be built (describe with Bazel's build language ~ python)

	genrule(
	  name = "hello",
	  outs = ["hello_world.txt"],
	  cmd = "echo Hello World > $@",
	)

	genrule(
	  name = "double",
	  srcs = [":hello"],
	  outs = ["double_hello.txt"],
	  cmd = "cat $< $< > $@",
	)

	$ bazel build :hello
	.
	INFO: Found 1 target...
	Target //:hello up-to-date:
	  bazel-genfiles/hello_world.txt
	INFO: Elapsed time: 2.255s, Critical Path: 0.07s


