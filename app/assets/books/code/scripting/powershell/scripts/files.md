## Where?
Get-Location    returns a PathInfo object (current path + other information)
 (Get-Location).Path
 
## List items
Get-ChildItem *.md | ForEach-Object {
    $content = $_ | Get-Content
    Write-Host $_.Fullname $content 
}

Get-ChildItem -Include *.md,*.txt | ForEach-Object {...  
-Include waits an array

foreach($f in Get-ChildItem) {
  get-content $f.Fullname |  Set-Content -Encoding UTF8 -Path $f.Fullname
}

## Create files

"hello" | out-file -encoding Utf8 "info.txt"

'My name is Joe', 'Welcome' |
Out-File -FilePath $env:TEMP\user.txt

$f='a.md, b.md, c.md'
foreach ($f in $p.split(',')) { '# '+$f | out-File ($f.trim()+'.md') -Append -Encoding UTF8 }
