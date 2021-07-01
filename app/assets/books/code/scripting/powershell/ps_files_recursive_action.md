## Recursive action on files

```sh
gci -path ..\ -recurse -filter *.csproj | foreach { pushd ([System.IO.Path]::GetDirectoryName($_.FullName)); C:\Windows\Microsoft.NET\Framework\v3.5\msbuild $_.fullname; popd; $_; }


# CREATE FILES FROM A LIST
$filesToCreate = 'a,b,c'
foreach ($f in $filesToCreate.split(',')) { '# '+$f | out-File ($f.trim()+'.md') -Append }    # !! UTF-16 created
gci *.md | Rename-Item -NewName {$_.name -replace ' ' , '_' }

# CHANGE ENCODING
cd ...    
foreach($f in Get-ChildItem) {
    Write-Host $f.Fullname 
}

foreach($f in Get-ChildItem) {
    get-content $f.Fullname
}

# RENAME

gci *.md |  rni -New {$_.FullName.ToLower()}
gci *.md | Rename-Item -NewName {$_.name -replace ' ' , '_' }
Get-Childitem "I:\notebooks\_md" -recurse -filter "Cloud_*" | Rename-Item -NewName {$_.name -replace 'Cloud_','Architecture_Cloud_' }

gci . -recurse -force | ?{!$_.PSIsContainer} | rni -New {$_.Name.replace("aaa","bbb")} 


# BULK WAY POWERSHELL

get-content C:\Temp\repolist.txt | ForEach-Object { Invoke-WebRequest -Uri https://api.github.com/repos/$_ -Method “DELETE” -Headers @{"Authorization"="token bb0aef1450d3cb25cb4587864f"} }


# REPLACE ALL MD images by their base64 equivalent
....
![volumes](volumes.jpg)
....


$convtob64 = {  param($match)
    $img = $match.Groups[1].Value
    $dst = Join-Path -Path $PSScriptRoot -ChildPath $img    
    $ImageBits = [Convert]::ToBase64String((Get-Content $dst -Encoding Byte))
    return "<img src=data:image/png;base64,$($ImageBits) alt='$img'/>"     
}

gci *2.html | % { 
    $content = $_ | Get-Content -Raw
    $regex = [regex] '(?m)!\[\w*\]\((?<imgpath>[^\)]*)\)'      
    $newContent = $regex.Replace($content, $convtob64  )  
    #write-host $newContent 
    Set-Content -PassThru $_ $newContent -Encoding UTF8 -Force
}  


```