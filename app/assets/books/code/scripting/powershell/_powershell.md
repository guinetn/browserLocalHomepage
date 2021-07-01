# Dotnet - Powershell
 
Cross-platform task automation and configuration management framework

https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1
https://www.educba.com/powershell-string-replace/?source=leftnav

## install

$PSHOME     stores the installation directory for PowerShell
$Home       current user's home directory

https://github.com/PowerShell/PowerShell/releases
- Prerequisites: C Runtime Library, WMF
- ARM-based version of PowerShell on computers like the Microsoft Surface Pro X.
- HKLM\Software\Microsoft\PowerShellCore\InstalledVersions\
- >pwsh.exe

PowerShell 1.0	Nov-2006 -  Initially, Windows PowerShell was built on the .NET Framework and only worked on Windows systems
...
PowerShell 6.0	Jan-2018 - First built on .NET Core 2.1. Installable on Windows, Linux, macOS
PowerShell 7.1  Nov-2020 - Built on .NET Core 5.0 

## PowerShell Core vs Windows PowerShell
Microsoft ciblera désormais .NET Core et PowerShell Core. Windows PowerShell et le Framework .NET restent bien évidemment supportés, mais ces deux composants majeurs de l’écosystème Microsoft n’évolueront plus. Il n’y aura plus de nouvelles fonctionnalités, seulement des correctifs de sécurité. La version 5.1 sera donc la dernière version de Windows PowerShell. L’avenir est donc à chercher du côté du monde plus ouvert avec PowerShell Core (version 6). 
No snap-in in PowerShell Core


## EXTENSIBLE COMMANDS
Create your own cmdlet and function modules using compiled code or scripts.

Cross-platform: Windows 8.1, 10, Windows Server, Ubuntu, Debian, CentOS , Arch
Task automation/configuration management framework
- a command-line shell
- a scripting language

Game changer: 
1. ***Output is object-based = do reflection = access type/properties/methods***

***Get-Member***: Discovering objects, properties, methods

Discovering types: 
***'w32time' | Get-Member***      TypeName: System.String: view all its properties/methods

Discovering properties
Get-Location  returns a PathInfo object (current path + other information)
Get-Location | Get-Member -MemberType Property
(Get-Location).Path  Access property with (). 

Discovering methods
Get-Location | Get-Member -MemberType Method
(Get-Service -Name w32time).Stop()
 
2. 
Get-Command -Noun string
Get-Command -Name *service* -CommandType Cmdlet, Function, Alias

An object is structured information that is more than just the string of characters
- In & out are .NET objects (unlike most shells accept and return text)
- Built on top of the .NET Common Language Runtime (CLR):
- PowerShell commands are cmdlets, designed to deal with objects. Ex: Get-Help cmdlet 
- Output Command always carries extra information you can use if you need it.
- Handles console input and output is formatted 

Create your own cmdlet or function modules using compiled code or scripts
Modules can add cmdlets and providers to the shell. 


C:\Program Files\WindowsPowerShell\Modules
C:\Program Files\WindowsPowerShell\Configuration
C:\Program Files\WindowsPowerShell\Scripts

>$PSHOME   # All is here
C:\Program Files\PowerShell\7
C:\Program Files\PowerShell\7\System.Linq.dll
C:\Program Files\PowerShell\7\System.Net.HttpListener.dll
C:\Program Files\PowerShell\7\System.Management.Automation.dll  → "Microsoft Windows PowerShell Engine Core Assembly". Use "justDecompil" (Telerik tool): Drag & Drop C:\windows\assembly\GAC_MSIL\System.Management.Automation then Search → "BuildRedirectionPipeline" for ex.

  
    
download.page(code/scripting/powershell/machine_info.md)

download.page(code/scripting/powershell/help.md)

download.page(code/scripting/powershell/providers.md)

download.page(code/scripting/powershell/aliasing.md)

download.page(code/scripting/powershell/pipeline_objects.md)

download.page(code/scripting/powershell/scripts.md)

download.page(code/scripting/powershell/scripts/_scripts.md)

download.page(code/scripting/powershell/security.md)

download.page(code/scripting/powershell/remote_managt/_remote_managt.md)


## Get-Member: reflection on objects, properties, methods

PROPERTIES: 
    Get-Service -Name w32time

MEMBERS:   
    Get-Service -Name w32time | Select-Object -Property Status, DisplayName, Can*
    
    Get-Service -Name w32time | Get-Member
    TypeName: System.ServiceProcess.ServiceController    
        \____ TypeName tells you what type of object was returned
    Name                      MemberType    Definition
    ----                      ----------    ----------
    Name                      AliasProperty Name = ServiceName
    RequiredServices          AliasProperty RequiredServices = ServicesDependedOn
    Disposed                  Event         System.EventHandler Disposed(System.Object, Sy...
    Close                     Method        void Close()

    Find commands THAT ACCEPT THAT TYPE OF OBJECT AS INPUT
    Get-Command -ParameterType ServiceController
        Get-Service                                        
        Start-Service                                      
        Stop-Service                                        
        Resume-Service                                     
        Restart-Service                                    

METHODS:  action that can be taken
    Get-Service -Name w32time | Get-Member -MemberType Method
        TypeName: System.ServiceProcess.ServiceController
        Start     void Start(), void Start(string[] args)
        Stop      void Stop()

    (Get-Service -Name w32time).Stop()


## Array
$array = @(1,2,3,5,7,11)
$array[2] = 13
foreach($item in $array)
{
    Write-Output $item
}
Write-Output $array[3]

## Hashtable
$ageList = @{}
$key = 'Kevin'
$value = 36
$ageList.add( $key, $value )
$ageList.add( 'Alex', 9 )

Hashtables with values
$ageList = @{
    Kevin = 36
    Alex  = 9
}

$ageList = @{}
$ageList.Kevin = 35
$ageList.Alex = 9

By default, hashtables aren't ordered (or sorted). We can
$person = [ordered]@{
    name = 'Kevin'
    age  = 36
}

$person.remove('age')
$person = @{} or $person.clear()

if( $person.age ){...}
if( $person.age -ne $null ){...}
if( $person.ContainsKey('age') ){...}
if( $person.ContainsValue('age') ){...}

## lookup table
$environments = @{
    Prod = 'SrvProd05'
    QA   = 'SrvQA02'
    Dev  = 'SrvDev12'
}
$server = $environments[$env]

Multiselection: an array of keys to get multiple values.
$environments[@('QA','DEV')]
$environments[('QA','DEV')]
$environments['QA','DEV']



$ageList.count
$ageList.values 
$ageList.keys 
$ageList | Measure-Object
$ageList.values | Measure-Object -Average
Count   : 2
Average : 22.5
$ageList.keys | ForEach-Object{
    $message = '{0} is {1} years old!' -f $_, $ageList[$_]
    Write-Output $message
}

foreach($key in $ageList.keys)
{
    $message = '{0} is {1} years old' -f $key, $ageList[$key]
    Write-Output $message
}

https://docs.microsoft.com/fr-fr/powershell/scripting/learn/deep-dives/everything-about-arrays?view=powershell-7.1

https://docs.microsoft.com/fr-fr/powershell/scripting/learn/deep-dives/everything-about-hashtable?view=powershell-7.1


System administration tasks: managing the registry to WMI (Windows Management Instrumentation) — are exposed via PowerShell cmdlets

($env:path.split(';')) | where {$_ -like '*mingw*'} | ls

$array = @(1,'hello')
$array | Get-Member
Get-Member -InputObject $array
Name           MemberType            Definition
----           ----------            ----------
Add            Method                int IList.Add(System.Object value)

Get-Member -InputObject $array | ForEach-Object { $_.Name }
Get-Member -InputObject $array | ForEach-Object { $_.MemberType }
Get-Member -InputObject $array  | where {$_.MemberType -like '*Method*'} 
Get-Member -InputObject $array  | where {$_.MemberType -like '*Property*'} 


## PowerShell "Profile" concept

Create a profile to 
- customize your environment: add commands, aliases, functions, variables, snap-ins, modules, PowerShell drives
- add session-specific elements to every PowerShell session that you start

https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-7.1#the-profile-variable

Scripts that run when a new instance of PowerShell is started. Inside of a profile, you can put any PowerShell script you'd like.
>$profile   # To see the location of the profile

On startup, PowerShell will run `any .ps1 files it finds in` the "My Documents/PowerShell"
Typically a xxxx_profile.ps1
$profile is an automatic variable that points at your user profile for all PowerShell hosts
C:\Users\nguin\Documents\PowerShell\Microsoft.PowerShell_profile.ps1   
!! The file is listed but can not really exists, it's the default!
For me I just have a 'profile.ps1" 

### basic profiles
$PSHOME     installation directory for PowerShell
$Home       current user's home directory
            %USERPROFILE% 'C:\Users\nguin'
            $Home         'C:\Users\nguin'

All Users, All Hosts	$PSHOME\Profile.ps1
All Users, Current Host	$PSHOME\Microsoft.PowerShell_profile.ps1
Current User, All Hosts	$Home\[My ]Documents\PowerShell\Profile.ps1
Current user, Current Host	$Home\[My ]Documents\PowerShell\
Microsoft.PowerShell_profile.ps1


|$PROFILE Property Name	| Description|
|---|---|
|$PROFILE.CurrentUserCurrentHost |	The current user for the current host|
|$PROFILE.AllUsersCurrentHost  |	All users for the current host|
|$PROFILE.CurrentUserAllHosts  |	The current user for all hosts|
|$PROFILE.AllUsersAllHost	   | All users for all hosts|

$PROFILE is the same as $PROFILE.CurrentUserCurrentHost

In addition, other programs that host PowerShell can support their own profiles. For example, Visual Studio Code supports the following host-specific profiles.
All users       Current Host	$PSHOME\Microsoft.VSCode_profile.ps1
Current user    Current Host	$Home\[My ]Documents\PowerShell\
Microsoft.VSCode_profile.ps1

### Examples
* Custom prompt
https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_prompts?view=powershell-7.1
function Prompt
{
  $env:COMPUTERNAME + "\" + (Get-Location) + "> "
}

* Output foreground/background colors 
$host.UI.RawUI.ForegroundColor = [System.ConsoleColor]::Blue

* Add a global variable to our profile:
>$global:SET_IN_PROFILE = $true' >> $PROFILE
From a PS session:
>$global:SET_IN_PROFILE

## Host
 Refers to a PowerShell Host application or a "PSHost". These are ***applications that host a PowerShell runtime***:

- ConsoleHost (used by pwsh.exe/pwsh)
- PowerShell Editor Services Host (used by the PowerShell extension for Visual Studio Code's PowerShell Integrated Console)
- .NET Interactive Host (used by this experience in .NET Interactive)
- VSCode
- ...
## Windows PATH environment variable 
*  is where applications look for executables -- meaning it can make or break a system or utility installation
Admins can use PowerShell to manage the PATH variable -- a process that entails string manipulation.
$env:Path
Path strings that refer to a directory are technically correct with or without a trailing slash -- '\' -- and, either way, that path will resolve correctly. 

Modify user/system environment variables permanently (i.e. will be persistent across shell restarts)
    Permanent modify a system environment variable
    [Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)
    Permanent modify a user environment variable
    [Environment]::SetEnvironmentVariable("INCLUDE", $env:INCLUDE, [System.EnvironmentVariableTarget]::User)
        
$addPath = 'C:\TopSecret\Bin'
// Iterate through all existing paths and check if the new path is already included with or without a '\' on the end
Set-PathVariable {
    param (
        [string]$AddPath,
        [string]$RemovePath
    )
    $regexPaths = @()
    if ($PSBoundParameters.Keys -contains 'AddPath'){
        $regexPaths += [regex]::Escape($AddPath)
    }

    if ($PSBoundParameters.Keys -contains 'RemovePath'){
        $regexPaths += [regex]::Escape($RemovePath)
    }
    
    $arrPath = $env:Path -split ';'
    foreach ($path in $regexPaths) {
        $arrPath = $arrPath | Where-Object {$_ -notMatch "^$path\\?"}
    }
    $env:Path = ($arrPath + $addPath) -join ';'
}
    
To remove all " from paths in the PATH environment variable for your session: 
$($Env:PATH).Split(';') | %{ $str += "$($_.Trim('"'));" }; $Env:PATH=$str
    
download.page(code/scripting/powershell/ps_files_recursive_action.md)


## :: Static member operator
Call the static properties operator and methods of a .NET Framework class.
```bash
[datetime] | gm -static     Find the static properties and methods of an object (gm = alias Get-Member)
[datetime]::now
[datetime]::Utcnow
```
## Get Members
$array = @(1,'hello')
$array | Get-Member
$array | gm
Get-Member -InputObject $array

[system.appdomain] | Get-Member -static
[System.Threading.Tasks.Task] | Get-Member -static

$a=${}
$a.GetType()
$a.GetType().GetMethods().Name|Sort
$array = [int[]]::new(5)
for ($index = 0; $index -lt 5; $index++) {
    $array[$index] = $index * 2
}

[System.Collections.Generic.List[int]]$list = @()
foreach ($value in 1..5) {    
    $list.Add($value)
}
gm -InputObject $list




$List = [System.Collections.Generic.List[object]]@(1..5)
$List.AddRange(5..10)
$List = [System.Collections.Generic.List[int]]@(1..5)
$List.AddRange([int[]](5..10))

$File = Get-Item c:\test\textFile.txt
$File.PSObject.Properties | Where-Object isSettable | Select-Object -Property Name

Name
----
PSPath
PSParentPath
PSChildName
PSDrive
PSProvider
PSIsContainer
IsReadOnly
CreationTime
CreationTimeUtc
LastAccessTime
LastAccessTimeUtc
LastWriteTime
LastWriteTimeUtc
Attributes

### Pester 

C:\Program Files\WindowsPowerShell\Modules\Pester\3.4.0

provides a framework for **running unit tests to execute and validate PowerShell commands from within PowerShell**. Pester consists of a simple set of functions that expose a testing domain-specific language (DSL) for isolating, running, evaluating and reporting the results of PowerShell commands.

Pester tests can execute any command or script that is accessible to a Pester test file. This can include functions, cmdlets, modules and scripts. Pester can be run in *ad-hoc* style in a console or **it can be integrated into the build scripts of a continuous integration (CI) system**.

**Pester also contains a powerful set of mocking functions** in which tests mimic any command functionality within the tested PowerShell code.
https://mikefrobbins.com/2015/10/22/using-pester-to-test-powershell-code-with-other-cultures/

## More

- https://intellitect.com/how-i-installed-software-on-a-server/
- https://searchwindowsserver.techtarget.com/tutorial/Implement-simple-server-monitoring-with-PowerShell
- https://searchitoperations.techtarget.com/answer/Manage-the-Windows-PATH-environment-variable-with-PowerShell
- https://searchitoperations.techtarget.com/answer/Perform-a-Windows-event-log-search-with-PowerShell
- https://www.editions-eni.fr/open/mediabook.aspx?idR=a7f2e460904c752894541fa3034d27a5