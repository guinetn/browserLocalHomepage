## services

Get-Command -Name *service*
Get-Command -Name *service* -CommandType Cmdlet, Function, Alias

Get-Service -Name w32time | Get-Member
    TypeName: System.ServiceProcess.ServiceController

Get-Command -ParameterType ServiceController
Name                         
----                         
Get-Service                  Return a ServiceController object
Remove-Service               
Restart-Service              
Resume-Service               
Set-Service                  
Start-Service                
Stop-Service                 
Suspend-Service              

Get-Service -Name w32time | Select-Object -Property *
Get-Service -Name w32time | Select-Object -Property Status, Name, DisplayName, ServiceType
Get-Service -Name w32time | Select-Object -Property Status, DisplayName, Can*
    CanPauseAndContinue, CanShutdown, and CanStop.
    
Get-Service -Name w32time | Get-Member -MemberType Method    

Stop-Service accepts ServiceController objects via the pipeline by value (by type). This means that when the results of the Get-Service cmdlet are piped to Stop-Service, they bind to the InputObject parameter of Stop-Service.
>Get-Service -Name w32time | Stop-Service

Piping a string to Stop-Service ***binds it by value to the Name*** parameter of Stop-Service
>'w32time' | Stop-Service


Get-Service |
  Where-Object CanPauseAndContinue -eq $true |
    Select-Object -Property *
    
Start-Service -Name w32time -PassThru | Get-Member
-PassThru makes cmdlet produce output so it can be piped without error

'UserService01', 'Windows Time' | Out-File -FilePath $env:TEMP\services.txt
>Stop-Service -DisplayName (Get-Content -Path $env:TEMP\services.txt)