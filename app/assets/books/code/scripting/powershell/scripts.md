# Scripts

Like UNIX shell scripts and cmd.exe batch files

Packaging your functions in a script module makes them easier to share

### Dot-Sourcing Functions

When a function in a script isn't part of a module, the only way to load it into memory is to dot-source the .PS1 file
Scripts are called by .\xxx.ps1

Stop-ServiceHello.ps1
```bash
function Get-MyPSVersion {
    $PSVersionTable
}
Get-MyPSVersion
```
.\Stop-ServiceHello.ps1

Functions are loaded in the Script scope. When the script completes, that scope is removed and the function is removed with it.
Check if functions are loaded into memory: exist on the Function PSDrive?
>Get-ChildItem -Path Function:\Get-MrPSVersion

download.page(code/scripting/powershell/script_module.md)