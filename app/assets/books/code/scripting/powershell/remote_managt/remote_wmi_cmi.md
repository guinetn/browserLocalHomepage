## WMI - Windows Management Instrumentation

Harvest hardware informations 
Command the OS and some Windows applications
To be use locally and on remote

## CMI - Common Information Model

WMI has been used to manage hardware & software on the network but now CIM will replace it. WMI is already using CIM.
CIM = standard

>Get-Command -Noun WMI*
>Get-Command -Module CimCmdlets
  Get-CimAssociatedInstance
  Get-CimClass
  Get-CimInstance
  Get-CimSession
  Invoke-CimMethod
  New-CimInstance
  New-CimSession
  New-CimSessionOption
  Register-CimIndicationEvent
  Remove-CimInstance
  Remove-CimSession
  Set-CimInstance
  
### Query Remote Computers with the CIM cmdlets
  
  https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/07-working-with-wmi?view=powershell-7.1
  
## more
- https://www.editions-eni.fr/open/mediabook.aspx?idR=b674dc457e95f6abdb447eeb153e8128
- https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/07-working-with-wmi?view=powershell-7.1