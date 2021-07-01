# WSL

Execute a GNU/Linux environment on Windows
Tools: grep, sed, awk,  vim, emacs, tmux
Langages : NodeJS, Javascript, Python, Ruby, C/C++, C# & F#, Rust, Go, etc.
Services : SSHD, MySQL, Apache, lighttpd, MongoDB, PostgreSQL.
Interop Linux/Windows: https://docs.microsoft.com/fr-fr/windows/wsl/interop

WSL 2: faster, file system
>wsl --list --verbose
>wsl --set-default-version 2
>sudo apt-get update

Add wget (to retrieve content from web servers) and ca-certificates (to allow SSL-based applications to check for the authenticity of SSL connections)
>sudo apt-get install wget ca-certificates

- [Chhose a GNU/Linux distribution to install](https://aka.ms/wslstore)
- https://docs.microsoft.com/fr-fr/windows/wsl/about
- [★★ VSCOde <---> Linux <---> WSL <---> Docker](https://www.youtube.com/watch?v=A0eqZujVfYU)
- [Editing your code and files on Windows Subsystem for Linux on Windows 10](https://www.youtube.com/watch?v=XfRo63afjtM)
- https://docs.microsoft.com/fr-fr/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

## Developing on WSL 2 using the new Windows Terminal
host a static website using Apache Server on Ubuntu Environment from a Windows System using the Windows Subsystem for Linux and the new Windows Terminal. 

Start WSL then
>sudo apt intall apache
>cd /var/www/htl
>sudo apt
>git clone ...sime .html site
>ls -l
>sudo service apache2 restart
http://localhost/my_page....
>sudo chown -R me .
>code .

## Install VS Code +  WSL extension
https://docs.microsoft.com/fr-fr/windows/wsl/tutorials/wsl-vscode
To open a project from your WSL distribution: code .
CTRL+SHIFT+P → Remote-WSL → list of the VS Code Remote options available