# WSL

Execute a GNU/Linux environment on Windows
Tools: grep, sed, awk,  vim, emacs, tmux
Langages : NodeJS, Javascript, Python, Ruby, C/C++, C# & F#, Rust, Go, etc.
Services : SSHD, MySQL, Apache, lighttpd, MongoDB, PostgreSQL.
Interop Linux/Windows: https://docs.microsoft.com/fr-fr/windows/wsl/interop

WSL 2: faster, file system

- [Chhose a GNU/Linux distribution](https://aka.ms/wslstore)
- https://docs.microsoft.com/fr-fr/windows/wsl/about
- [★★ VSCOde <---> Linux <---> WSL <---> Docker](https://www.youtube.com/watch?v=A0eqZujVfYU)


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