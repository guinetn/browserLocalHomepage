# Services

https://makolyte.com/run-a-windows-service-as-a-console-app/

Get-Service | Get-Member TypeName: System.Service.ServiceController#StartupType

PS>Get-Service -Name WinDefend | Get-Member
PS>Get-Service -Name WinDefend | Format-List
Name                : WinDefend
DisplayName         : Windows Defender Service
Status              : Stopped
DependentServices   : {}
ServicesDependedOn  : {RpcSs}
CanPauseAndContinue : False
CanShutdown         : False
CanStop             : False
ServiceType         : Win32OwnProcess
