## Strings

Get-Command -Noun string

'w32time' | Get-Member      TypeName: System.String: view all its properties/methods

$p='a,b,c'
$p = $p + ',d'
$p.split(',')
$env:Path.split(';') | sort
$env:PSModulePath -split ';'
$p.trim()

'PowerShell' -replace 'Shell'  → Power
'John doe - Mary Jane' -Replace 'doe','Doe'
'John doe - Mary Jane'.Replace('doe','Doe')

Out-String
Join-String
Select-String