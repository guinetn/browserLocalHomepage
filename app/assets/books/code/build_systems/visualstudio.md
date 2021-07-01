# Command Line Build on Windows

Visual C++ provides command-line tools for programmers who prefer to build their applications from the command prompt. If you want to use the command line to build a project created in Visual C++, you can use one of the following:

## CL
Use the compiler (cl.exe) to compile and link source code files.

## Link
Use the linker (link.exe) to link compiled object files.

## MSBuild (Visual C++)
Use MSBuild to build Visual C++ projects and Visual Studio solutions from the command line. Invoking this utility is equivalent to running the Build project or Build Solution command in the Visual Studio integrated development environment.

## DEVENV
Use DEVENV combined with a command line switch, such as /Build or /Clean, to perform certain build commands without displaying the Visual Studio IDE.

## NMake
Use NMake to automate tasks that build Visual C++ projects.



# POST-BUILD EVENT

Solution Properties -> Post-build event command line:

if NOT $(Username) == zuzerTFSBuild (
mkdir $(SolutionDir)MY_APP\$(OutDir)MY_APPPlugins
COPY $(TargetName).* $(SolutionDir)MY_APP\$(OutDir)MY_APPPlugins\)
