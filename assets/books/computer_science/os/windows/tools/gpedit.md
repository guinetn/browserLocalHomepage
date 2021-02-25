## gpedit

éditeur de stratégie de groupe local
gpedit.msc

* Not present in Windows 10 family. Cependant, il est possible d'activer gpedit.msc afin de pouvoir autoriser ou désactiver certains fonctionnalités de Windows 10.

Dans Windows on peut configurer des restrictions administrateurs.
Cela se fait souvent en entreprise pour bloquer l'accès à certains composants.
Cela permet d'éviter que les utilisateurs modifient ou accèdent à certains fonctions.

On peut les configurer que dans certains éditions de Windows 10.
Ainsi la version home ou famille ne possède pas ces restrictions

INSTALL GPEDIT
    https://forums.commentcamarche.net/forum/affich-34991466-installer-gpedit-msc-sur-la-version-familiale-de-windows

    xxx.bat (admin exec)
    @echo off
    pushd "%~dp0"

    dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt
    dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt

    for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"C:\Windows\servicing\Packages\%%i"
    pause

