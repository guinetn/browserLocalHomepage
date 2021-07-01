# INSTALL GIT

Official Git Home Page
Installers, release notes, and documentation pages: http://git-scm.org

Linux
    $ sudo apt-get update
    $ sudo apt-get install git

Windows (msysGit)	
    http://git-scm.com/download/win
    http://windows.github.com/ 		Git Shell (powershell) - GitHub
    
>git --version         
2.31   06/2021  
If you see -bash: git: command not found as a response, you either do not have Git installed, or your CLI is unaware of the installation

>git config -l

>which git   # determine the location of git installation
>echo 'export PATH=/PATH/TO/GIT/bin:$PATH' &lt;&lt; ~/.profile

- C:\Program Files\Git
- C:\Program Files\Git\bin    these commands are actually the Cygwin Win32 ports of most of Linux’s commands

## Git Bash
Provides a UNIX-based environment on Windows OS machines when we install Git.
