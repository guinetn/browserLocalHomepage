### FUNCTIONS

Whenever possible, I prefer to write functions because they are more tool oriented. I can put the functions in a script module, put that module in the $env:PSModulePath, and call the functions without needing to physically locate where they're saved. Using the PowerShellGet module, it's easy to share those modules in a NuGet repository. 

PowerShell functions 
- Pascal case name
- <ApprovedVerb>-<Prefix><SingularNoun>

***Verbs***
The module generates a warning message at load time if you choose an unapproved verb

Get-Verb | Sort-Object -Property Verb
Verb        Group: idea of how these verbs are used
----        -----
Add         Common
Approve     Lifecycle
Assert      Lifecycle
Backup      Data
Block       Security
Checkpoint  Data
Clear       Common
Close       Common
Compare     Data
...

### Function

* At command-line scope
* At scrit scope
Functions are loaded in the Script scope. When the script completes, that scope is removed and the function is removed with it.

```bash
function Get-PSVersion {
    # Call bt 'Get-Version'
    # PS is the prefix (avoid conflicts). 
    $PSVersionTable.PSVersion
}
```

Check for conflicts
>Get-ChildItem -Path Function:\Get-*Version
Remove these functions from your current session
>Get-ChildItem -Path Function:\Get-*Version | Remove-Item
Module can be unloaded to remove its functions
>Remove-Module -Name <ModuleName>

Check if functions are loaded into memory: exist on the Function PSDrive?
>Get-ChildItem -Path Function:\Get-MrPSVersion

### Parameters

https://www.sqlservercentral.com/articles/powershell-day-by-day-customizing-scripts-with-parameters

```bash
function Test-MyParameter {
    param ($ComputerName)
    Write-Output $ComputerName
}
```
```bash
function Get-MyParameterCount {
    param ( [string[]]$ParameterName )
    foreach ($Parameter in $ParameterName) {
        $Results = Get-Command -ParameterName $Parameter -ErrorAction SilentlyContinue
        [pscustomobject]@{
            ParameterName = $Parameter
            NumberOfCmdlets = $Results.Count
        }
    }
}
```
Get-MyParameterCount -ParameterName ComputerName, Computer, ServerName, Host, Machine

```bash
# https://hub-binder.mybinder.ovh/user/dotnet-interactive-cb9ukwlm/lab/tree/powershell/Docs/For-EachObject%20parallel.ipynb

function FetchGitHubRepos {
    $orgs = @(
        'PowerShell',
        'Microsoft',
        'dotnet'
    )

    Measure-Command -Expression {
        foreach($org in $orgs) {
            1..10 | ForEach-Object -ThrottleLimit 3 -Parallel {
                (Invoke-RestMethod "https://api.github.com/orgs/$using:org/repos?page=$_") |
                Select-Object -Property full_name,stargazers_count |
                Export-Csv ./repo_stats.csv -Append
            }
        }
    } | Select-Object -Property Minutes, Seconds
}
FetchGitHubRepos    

```

```bash
```

* The Simple Way To Use Parameters - $args[]

$args[0] - first parameter passed in
$args[1] - second parameter passed in
$args[2] - second parameter passed in
...

$i = $args[3]
if ($i.Length -eq 0) {write-host("Missing parameter") }
else {write-host("Fourth parameter: $i")}
$i = $args[3]
if ($i -eq $null) {write-host("Missing parameter") }
else {write-host("Fourth parameter: $i")}

$filetype = $args[0]
$prefix = $args[1]
$a = Get-ChildItem .
foreach ($i in $a) {
 if ($i.extension -eq $filetype) {
   $newname = $prefix + $i.Name
   Rename-Item $i $newname
 }
}

* Named Parameters

param([Parameter(Mandatory)]$extension, $prefix )
if ($extension -eq $null) {
    write-host("Missing extension parameter") 
  }
  else {
    write-host("Extension Parameter: $extension")
  }
if ($prefix -eq $null) {
    write-host("Missing prefix parameter") 
  }
  else {
    write-host("Prefix Parameter: $prefix")
  }

* Default Values for Parameters

param( $FileExtension="csv"
     , [Parameter(Mandatory)]$ArchivePrefix )
if ($FileExtension.substring(1,1) -ne ".") {
  $FileExtension = "." + $FileExtension
}
$a = Get-ChildItem .
foreach ($i in $a) {
 if ($i.extension -eq $FileExtension) {
   $newname = $ArchivePrefix + $i.Name
   Rename-Item $i $newname
 }
}

* Adding Help

<#
.PARAMETER FileExtension
    The extension of the files to be checked. This can include or exclude the period. The default here is CSV.
.PARAMETER ArchivePrefix
    A string value that is prepended to files matching the extension parameter.
.EXAMPLE
    .\prefix_filenames.ps1 -ArchivePrefix "202106_" 
    This will add 202106_ to each file with the default csv extension.
#>
param( $FileExtension="csv"
     , [Parameter(Mandatory)]$ArchivePrefix )
if ($FileExtension.substring(1,1) -ne ".") {
  $FileExtension = "." + $FileExtension
}
$a = Get-ChildItem .
foreach ($i in $a) {
 if ($i.extension -eq $FileExtension) {
   $newname = $ArchivePrefix + $i.Name
   Rename-Item $i $newname
 }
}

## more

- https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/09-functions?view=powershell-7.1