# Remote Management

CIM/WMI allowed to do some actions on remote machines.
There are other ways to control machine remotely = F(security, OS):
- RPC Protocol (dynamic ports, firewall issue?)
- WinRM (Since PS 2.0, use WS-Man implémentation)
- SSH (To replace WinRM. SSH since PowerShell 6: manage Linux/Mac OS very easily thanks to SSH)

download.page(code/scripting/powershell/remote_managt/remote_wmi_cmi.md)
download.page(code/scripting/powershell/remote_managt/remote_rpc.md)
download.page(code/scripting/powershell/remote_managt/remote_ssh.md)
download.page(code/scripting/powershell/remote_managt/remote_winrm.md)

### Ways to run commands against remote computers

* Remotely query WMI using the CIM cmdlets
- https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/07-working-with-wmi?view=powershell-7.1

* cmdlets with built-in 'ComputerName' parameter:

>Get-Command -ParameterName ComputerName
Stop-Computer
Get-HotFix
Invoke-Command
...

Not the long-term way Microsoft is heading for running commands against remote computers. 
Command with a 'ComputerName' parameter need to specify a 'Credential' parameter that doesn't exists. And from elevated account, a firewall between you and the remote computer can block the request.

* PS Session
- Enter-PSSession
- Get-PSSession
- Remove-PSSession

1. Enable PowerShell remoting on the remote computer
>Enable-PSRemoting   
WinRM has been updated to receive requests.
WinRM service type changed successfully.
WinRM service started.
WinRM has been updated for remote management.
WinRM firewall exception enabled.

2. One-To-One Remoting: Interactive remote session 

Store your domain admin credentials in $Cred
>$Cred = Get-Credential 
Create a one-to-one PowerShell remoting session to the domain controller named dc01.
>Enter-PSSession -ComputerName dc01 -Credential $Cred
> Get-Process | Get-Member
>Exit-PSSession

3. One-To-Many Remoting: Interactive remote session 
To perform a task on multiple remote computers at the same time
>Invoke-Command -ComputerName dc01, sql02, web01 {Get-Service -Name W32time} -Credential $Cred
>Invoke-Command -ComputerName dc01, sql02, web01 {Get-Service -Name W32time} -Credential $Cred | Get-Member