# Dotnet - Powershell


Lancez Windows PowerShell
cd 'G:\DotNet\CSharp\CS 2009 Samples\LanguageSamples\__CompilAll'
.\comp.ps1 
gci -path ..\ -recurse -filter *.csproj | foreach { pushd ([System.IO.Path]::GetDirectoryName($_.FullName)); C:\Windows\Microsoft.NET\Framework\v3.5\msbuild $_.fullname; popd; $_; }


## :: Static member operator
Call the static properties operator and methods of a .NET Framework class.
```powershell
[datetime] | gm -static     Find the static properties and methods of an object (gm = alias Get-Member)
[datetime]::now
[datetime]::Utcnow
```
## Get Members
$array = @(1,'hello')
$array | Get-Member
Get-Member -InputObject $array

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