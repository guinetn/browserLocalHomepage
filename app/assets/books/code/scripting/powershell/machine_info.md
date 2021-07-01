# Machine Info

### paths
$env:Path
$env:PSModulePath
$PSVersionTable

### Disks
Get-PSDrive
Get-PSProvider


### security
Get-ExecutionPolicy

gin = Get-ComputerInfo
gci =  Get-ChildItem

### Process & Services
Get-Process -Name PowerShell
Get-Process -Name *goo*

Get-Service -Name *goo*

### bios
Get-CimInstance -Query 'Select * from Win32_BIOS'

### Network
ipconfig /all