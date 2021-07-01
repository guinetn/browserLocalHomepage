# Chocolatey - automation on Windows

Free Windows package manager allowing to create a software package and deploying it with the help of the tools you’ve already familiar with. This software management solution works with a wide range of Windows operating systems and cloud environments like Azure, and Amazon AWS.
Chocolatey is empowered by NuGet and PowerShell technology. Created by Microsoft, NuGet is a framework developed for the purposes of bundling code into “packages.” Besides NuGet Chocolatey uses PowerShell (a cross-platform task automation and configuration management framework) to add some functionality that helps to install and update packages.

chocolatey install packages here:
  C:\ProgramData\chocolatey\lib


Install chocolatey: https://chocolatey.org/install
Run PowerShell as admin
Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex

https://chocolatey.org/install
   In Powershell (as admin) 
   * iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
   If not allowed: to run he script: 
   		Get-ExecutionPoliciy   
   		Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
   Upgrade             → choco upgrade chocolatey
http://chocolatey.org/packages
https://en.wikipedia.org/wiki/Chocolatey

a package manager for Windows
Decentralized framework for quickly installing applications and tools needed
Built on the NuGet infrastructure currently using PowerShell as its focus for
delivering packages	from the distros to your door, err computer. It´s a fork of the NuGet gallery

A global PowerShell execution engine using the NuGet packaging infrastructure. Think of it as the
ultimate automation tool for Windows.
A global silent installer for applications and tools. It can also do configuration tasks and anything
that you can do with PowerShell. The power you hold with a tool like Chocolatey is only
limited by your imagination!

You can develop your tools and applications with NuGet, and release them with Chocolatey! But Chocolatey
is not just for .NET tools. It´s for nearly any Windows application/tool!

install packages from?
	By default it installs packages from both chocolatey.org and nuget.org.
	That means you can install packages that don´t appear to exist on chocolatey.org


 http://chocolatey.org/packages
package manager for Windows. Decentralized framework for quickly INSTALLING APPLICATIONS AND TOOLS needed

<CLI_command_line_interface.md>
<PM__Package_Managers.md>
<PM_Chocolatey_WindowsPM.md>


# Difference Chocolatey / NuGet?
	NuGet is for development libraries, Chocolatey is a binary machine package manager.
	"You use NuGet to get 3rd party libraries that you use to build the applications/tools that you host on Chocolatey."

	Many times the way Chocolatey works is to use PowerShell to download the package from the official distribution point,
	this way no distribution rules are broken.

## Microsoft has decided to use Chocolatey´s framework with the upcoming OneGet client: https://github.com/OneGet/oneget


## INSTALL
# To install Chocolatey, execute the following command in your command prompt:
	@powershell -NoProfile -ExecutionPolicy unrestricted -Command "(iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))) >$null 2>&1" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
	or
	@powershell -NoProfile -ExecutionPolicy Unrestricted -Command "iex ((New-Object Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin

## COMMANDS

 choco -?	
 choco list -?
 	-l, --lo, --localonly, --local-only
     LocalOnly - Only search against local machine items.
    ....

 * list - lists remote or local packages
 * search - searches remote or local packages (alias for list)
 * info - retrieves package information. Shorthand for choco search pkgname --exact --verbose
 * install - installs packages from various sources
 * pin - suppress upgrades for a package
 * outdated - retrieves packages that are outdated. Similar to upgrade all --noop
 * upgrade - upgrades packages from various sources
 * uninstall - uninstalls a package
 * pack - packages up a nuspec to a compiled nupkg
 * push - pushes a compiled nupkg
 * new - generates files necessary for a chocolatey package from a template
 * source - view and configure default sources
 * sources - view and configure default sources (alias for source)
 * config - Retrieve and configure config file settings
 * feature - view and configure choco features
 * features - view and configure choco features (alias for feature)
 * apikey - retrieves or saves an apikey for a particular source
 * setapikey - retrieves or saves an apikey for a particular source (alias for apikey)
 * unpackself - have chocolatey set it self up
 * version - [DEPRECATED] will be removed in v1 - use `choco outdated` or `cup <pkg|all> -whatif` instead
 * update - [DEPRECATED] RESERVED for future use (you are looking for upgrade, these are not the droids you are looking for)

# SAMPLE
	Install Notepad++:   choco install notepadplusplus   or
							cinst notepadplusplus

	cinst scriptcs

	choco install pdfcreator
	choco install sublimetext3
	choco install sysinternals
	choco install procexp
	choco install skype
	choco install ruby
	choco install curl
	choco install wget
	choco install console2
	choco install phantomjs
	choco install youtube-dl
	choco install make
	choco install cygwin
	choco install mingw
		MinGW ("Minimalistic GNU for Windows") is a collection of freely available and freely distributable Windows specific header files and import libraries combined with GNU toolsets that allow one to produce native Windows programs that do not rely on any 3rd-party C runtime DLLs. Gambit Scheme system, compiler and interpreter
	choco install scriptcs
	choco upgrade scriptcs
	choco install audacity
	

	With Chocolatey, keeping scriptcs updated is just as easy:
	cinst notepadplusplus
	cup notepadplusplus

# Staying up-to-date
	With Chocolatey, keeping scriptcs updated is just as easy:
	choco upgrade scriptcs

# How does chocolatey work?
	When a package has an exe file, chocolatey will create a link "shortcut" to the file so that you can run that tool anywhere on the machine.
	When a package has a chocolateyInstall.ps1, it will run the script. The instructions in the file can be anything. This is limited only by the .NET framework and powershell.
	Most of the chocolatey packages that take advantage of the powershell download an application installer and execute it silently.

## SOME INSTALLS

Chocolatey v0.10.3
android-sdk 24.4.1.3
audacity 2.1.2.20161210
autohotkey.portable 1.1.24.04
azcopy 3.1.0
bower 1.8.0
ccleaner 5.26.5937
chocolatey 0.10.3
chocolatey-core.extension 1.0.5
codeblocks 16.1.0.20161209
Compass 1.0.1
ConEmu 17.1.18.0
curl 7.28.1
docker 17.05.0
dropbox 16.4.30
electron 1.4.15
filezilla 3.23.0.2
Firefox 51.0.1
git 2.11.0.3
git.install 2.11.0.3
googledrive 1.32.4066.7445
googleearth 7.1.7.2602
InkScape 0.92.0
iTunes 12.5.5
jdk8 8.0.121
libjpeg-turbo 1.2.1.201304081
linqpad4 4.57.02
linqpad4.install 4.57.02
mongodb 3.2.10
mongodb.install 3.2.10
mysql.workbench 6.3.8
nodejs.install 7.4.0
OptiPNG 0.7.5.20141004
paint.net 4.0.6
PhantomJS 2.1.1
python 3.6.0
python3 3.6.0
ruby 2.3.1
scriptcs 0.16.1
sourcetree 1.9.10.0
SQLite 3.16.2
vcredist2013 12.0.30501.20150616
wget 1.18.0.20161210
yarn 0.19.1
Yeoman 1.1.2





choco -?

 * list - lists remote or local packages
 * find - searches remote or local packages (alias for search)
 * search - searches remote or local packages (alias for list)
 * info - retrieves package information. Shorthand for choco search pkgname --exact --verbose
 * install - installs packages from various sources
 * pin - suppress upgrades for a package
 * outdated - retrieves packages that are outdated. Similar to upgrade all --noop
 * upgrade - upgrades packages from various sources
 * uninstall - uninstalls a package
 * pack - packages up a nuspec to a compiled nupkg
 * push - pushes a compiled nupkg
 * new - generates files necessary for a chocolatey package from a template
 * sources - view and configure default sources (alias for source)
 * source - view and configure default sources
 * config - Retrieve and configure config file settings
 * feature - view and configure choco features
 * features - view and configure choco features (alias for feature)
 * setapikey - retrieves, saves or deletes an apikey for a particular source (alias for apikey)
 * apikey - retrieves, saves or deletes an apikey for a particular source
 * unpackself - have chocolatey set itself up
 * version - [DEPRECATED] will be removed in v1 - use `choco outdated` or `cup <pkg|all> -whatif` instead
 * update - [DEPRECATED] RESERVED for future use (you are looking for upgrade, these are not the droids you are looking for)
 