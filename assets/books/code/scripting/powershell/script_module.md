## SCRIPT MODULE

Container grouping commands, scripts, variables, alias, fonctions
A file containing one or more functions that's saved as a .PSM1 (instead of .PS1)

Find a module
>Get-Module -Name MyScriptModule
Module can be unloaded to remove its functions
>Remove-Module -Name <ModuleName>

MyScriptModule.psm1
```powershell
function Get-MyPSVersion {    # Private Function
    $PSVersionTable           # only accessible by other functions within the module
}

function Get-MyComputerName { # Public Function
    $env:COMPUTERNAME
}

Export-ModuleMember -Function Get-MyComputerName  # only it is available to module's users
```

Available functions:
>Get-Command -Module MyScriptModule

Load the module to avoidthe error "xxxx is not recognized as the name of a cmdlet, function, script file, or operable program":
>Import-Module C:\MyScriptModule.psm1   
>Get-MyComputerName 

***Module autoloading***
From PowerShell version 3
The script module needs to be saved in a folder with the same base name as the .PSM1 file and in a location specified in $env:PSModulePath

***Module Manifests***
All modules should have a module manifest (metadata about it)
.PSD1
Some .PSD1 files are not module manifests, can store environmental portion of a DSC configuration... 
>New-ModuleManifest -Path $env:ProgramFiles\WindowsPowerShell\Modules\MyScriptModule\MyScriptModule.psd1 -RootModule MyScriptModule -Author 'Joe Black' -Description 'MyScriptModule' -CompanyName 'joe.com'
Add Author and Description when planned to be used from a NuGet repository

A module without a manifest has a Version = 0.0
>Update-ModuleManifest if you chzngr the manifest

***Public/Private functions***
Defined either into 
- the .psm1: Export-ModuleMember -Function Get-MyComputerName
- the .psd1: FunctionsToExport = 'Get-MrPSVersion'

### PSModulePath
>$env:PSModulePath.split(';') | sort
    c:\program files\powershell\7\Modules       AllUsers path
    C:\Program Files\PowerShell\Modules         AllUsers path
    C:\Program Files\WindowsPowerShell\Modules
    C:\Users\nguin\AppData\Local\Google\Cloud SDK\google-cloud-sdk\platform\PowerShell
    C:\Users\nguin\Documents\PowerShell\Modules         My current user path
    C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules  Microsoft Only 
    
    if SQL Server Management Studio is installed:
    C:\Program Files (x86)\Microsoft SQL Server\150\Tools\PowerShell\Modules\    
 
### Powershell Gallery
https://www.powershellgallery.com
https://www.powershellgallery.com/api/v2/

Microsoft open source scripts/modules (dsc) NuGet repository 

### PowerShellGet
PowerShell module having commands for from a NuGet repository:
- discovering PowerShell modules
Find-Module -Name MyToolkit       find a module in the PowerShell Gallery
- installing PowerShell modules
Find-Module -Name MrToolkit | Install-Module
- publishing PowerShell modules
- updating PowerShell modules 
 