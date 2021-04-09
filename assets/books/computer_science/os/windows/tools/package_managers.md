# PACKAGE MANAGERS

### winget - Windows Package Manager

https://github.com/microsoft/winget-cli/
https://docs.microsoft.com/fr-fr/windows/package-manager/winget/

 a command-line utility and a set of services for installing applications
 
discover, install, upgrade, remove and configure applications on Windows 10 computers. This tool is the client interface to the Windows Package Manager service.

COMMANDS
hash	Generates the SHA256 hash for the installer.
help	Displays help for the winget tool commands.
install	Installs the specified application.
search	Searches for an application.
show	Displays details for the specified application.
source	Adds, removes, and updates the Windows Package Manager repositories accessed by the winget tool.
validate	Validates a manifest file for submission to the Windows Package Manager repository.

### Chocolatey

https://en.wikipedia.org/wiki/Chocolatey

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
 
 ## Scoop
 https://scoop.sh/
 
 A command-line installer for Windows
 >scoop install curl
 
 ## Ninite
 https://en.wikipedia.org/wiki/Ninite
 
 ## AppGet
 
 ## Npackd 
 https://en.wikipedia.org/wiki/Npackd
 
 ## PowerShell-based OneGet
 https://en.wikipedia.org/wiki/PowerShell
 
 ## MSI
 https://en.wikipedia.org/wiki/.msi
 
 ## nuget
 https://en.wikipedia.org/wiki/NuGet