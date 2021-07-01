## Pipelines = flow of work
The most valuable concept used in command-line interfaces
Any command that produces object-based output can be piped 
>Get-ChildItem | Out-Host -Paging
>Get-Location | Get-Member



Stop-Service accepts ServiceController objects via the pipeline by value (by type). This means that when the results of the Get-Service cmdlet are piped to Stop-Service, they bind to the InputObject parameter of Stop-Service.
>Get-Service -Name w32time | Stop-Service

Piping a string to Stop-Service ***binds it by value to the Name*** parameter of Stop-Service
>'w32time' | Stop-Service

$CustomObject = [pscustomobject]@{  Service = 'w32time'}
$CustomObject | Stop-Service : Error, it doesn't produce a ServiceController or String object, and it doesn't have a property named Name.
$CustomObject |
  Select-Object -Property @{name='Name';expression={$_.Service}} |
    Stop-Service

### Filtering

Get-Service |
  Where-Object CanPauseAndContinue -eq $true |
    Select-Object -Property *
 
Get-Service |
  Where-Object CanPauseAndContinue |
    Select-Object -Property DisplayName, Status    