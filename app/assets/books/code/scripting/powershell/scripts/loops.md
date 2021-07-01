# Loops

$_ = $PSItem = is the current object

### for
for ($i = 1; $i -lt 5; $i++) {
  Write-Output "$i. Done"
  Start-Sleep -Seconds $i
}

### foreach
$files = 'f1.txt', 'f2.txt'
foreach ($file in $files) {
  Write-Host $file
}

### do until - do while
$number = Get-Random -Minimum 1 -Maximum 10
$i = 0
do {
  $i += 1
}
until ($i -eq $number)

do {
  $i += 1 
}
while ($i -ne $number)

### While

$date = Get-Date -Date 'February 22'
while ($date.DayOfWeek -ne 'Thursday') {
  $date = $date.AddDays(1)
}
Write-Output $date

### Break, Continue, and Return

for ($i = 1; $i -lt 5; $i++) {
  Write-Output "Sleeping for $i seconds"
  break
}

while ($i -lt 10) {
  $i += 1
  if ($i -eq 5) {
    continue
  }
  Write-Output $i
}

'ActiveDirectory', 'SQLServer' |
   ForEach-Object {Get-Command -Module $_} |
     Group-Object -Property ModuleName -NoElement |
         Sort-Object -Property Count -Descending