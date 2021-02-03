# Unix

 UNIX was designed to be built in separate pieces that could be piped together. 
 
 Proprietary Unix operating systems (and Unix-like variants) run on a wide variety of digital architectures, and are commonly used on web servers, mainframes, and supercomputers. In recent years, smartphones, tablets, and personal computers running versions or variants of Unix have become increasingly popular.
 Linux is just the kernel. Unix is a complete package of Operating system.
 
Operating system developed at Bell laboratory in the year 1970
by Dennis Ritchie, Ken Thompson, Brian Kernighan, Joe Ossanna and Douglas Mcllroy  
Allow multiple users to work on it simultaneously by cultivating the principles of interoperability like POSIX and following the philosophies like single-purpose execution, standard interface operating only on text, core kernel coiling the Unix systems thereby allowing the systems and other processes and interoperable to a large extent.
 
 https://www.educba.com/what-is-unix/
 
 Unix os is written in C language
 UNIX can also be called as an operating system that has its utilization in both work stations and servers.
 
 ## UNIX Philosophy

* Small is beautiful
* Make each program do one thing well
* Build a prototype as soon as possible
* Choose portability over efficiency
* Store data in flat text files
* Use software leverage to your advantage
* Use shell scripts to increase leverage and portability
* Avoid captive user interfaces
* Make every program a filter

## ERIC RAYMOND’S 17 UNIX RULES
https://en.wikipedia.org/wiki/Unix_philosophy
. Rule of Modularity
. Developers should build a program out of simple parts connected by well defined interfaces, so problems are local, and parts of the program can be replaced in future versions to support new features. This rule aims to save time on debugging code that is complex, long, and unreadable.
. Rule of Clarity
. Developers should write programs as if the most important communication is to the developer, including themselves, who will read and maintain the program rather than the computer. This rule aims to make code readable and comprehensible for whoever works on the code in future.
. Rule of Composition
. Developers should write programs that can communicate easily with other programs. This rule aims to allow developers to break down projects into small, simple programs rather than overly complex monolithic programs.
. Rule of Separation
. Developers should separate the mechanisms of the programs from the policies of the programs; one method is to divide a program into a front-end interface and a back-end engine with which that interface communicates. This rule aims to prevent bug introduction by allowing policies to be changed with minimum likelihood of destabilizing operational mechanisms.
. Rule of Simplicity
. Developers should design for simplicity by looking for ways to break up program systems into small, straightforward cooperating pieces. This rule aims to discourage developers’ affection for writing “intricate and beautiful complexities” that are in reality bug prone programs.
. Rule of Parsimony
. Developers should avoid writing big programs. This rule aims to prevent overinvestment of development time in failed or suboptimal approaches caused by the owners of the program’s reluctance to throw away visibly large pieces of work. Smaller programs are not only easier to optimize and maintain; they are easier to delete when deprecated.
. Rule of Transparency
. Developers should design for visibility and discoverability by writing in a way that their thought process can lucidly be seen by future developers working on the project and using input and output formats that make it easy to identify valid input and correct output. This rule aims to reduce debugging time and extend the lifespan of programs.
. Rule of Robustness
. Developers should design robust programs by designing for transparency and discoverability, because code that is easy to understand is easier to stress test for unexpected conditions that may not be foreseeable in complex programs. This rule aims to help developers build robust, reliable products.
. Rule of Representation
. Developers should choose to make data more complicated rather than the procedural logic of the program when faced with the choice, because it is easier for humans to understand complex data compared with complex logic. This rule aims to make programs more readable for any developer working on the project, which allows the program to be maintained.[19]
. Rule of Least Surprise
. Developers should design programs that build on top of the potential users' expected knowledge; for example, ‘+’ in a calculator program should always mean 'addition'. This rule aims to encourage developers to build intuitive products that are easy to use.
. Rule of Silence
. Developers should design programs so that they do not print unnecessary output. This rule aims to allow other programs and developers to pick out the information they need from a program's output without having to parse verbosity.
. Rule of Repair
. Developers should design programs that fail in a manner that is easy to localize and diagnose or in other words “fail noisily”. This rule aims to prevent incorrect output from a program from becoming an input and corrupting the output of other code undetected.
. Rule of Economy
. Developers should value developer time over machine time, because machine cycles today are relatively inexpensive compared to prices in the 1970s. This rule aims to reduce development costs of projects.
. Rule of Generation
. Developers should avoid writing code by hand and instead write abstract high-level programs that generate code. This rule aims to reduce human errors and save time.
. Rule of Optimization
. Developers should prototype software before polishing it. This rule aims to prevent developers from spending too much time for marginal gains.
. Rule of Diversity
. Developers should design their programs to be flexible and open. This rule aims to make programs flexible, allowing them to be used in ways other than those their developers intended.
. Rule of Extensibility
. Developers should design for the future by making their protocols extensible, allowing for easy plugins without modification to the program's architecture by other developers, noting the version of the program, and more. This rule aims to extend the lifespan and enhance the utility of the code the developer writes.

## Unix Architecture

- Kernel
deals with all the hardware connections
manages the connections related to hardware, applications and commands.

- Hardware

- Shell
bridge between the user, user commands and predefined UNIX commands.
Various tasks which shell ask the kernel to do are
File opening.
File writing.
Executing programs.
Obtaining detailed information about the program.
Termination of the process.
Getting information about time and date.

- Files and directories
files and directories which are called Unix programs mostly and can be considered as commands in Unix

## File
a collection of information or data which is stored in the disk.
Files that contain data, text and program instructions. 
>ls
-rw-r–r–    1 root root     3028 Apr  4  2018 Sample.conf
drwxr-xr-x  3 root root     4096 Apr  4  2018 Test.txt
             \    \    \      \        \      \___  pathname/filename
              \    \    \      \        \___  Date details
               \    \    \      \___  bytes in the file
                \    \    \___ File group name  
                 \    \___ Owner of the file 
                  \___ Links in the file
                   
Mode and access details associated with the file
group 1: d
group 2: rwx
group 3: r-x
group 4: r-x
r: Permission only to read
w: Permission only to write
x: Permission to execute
–: No permission

