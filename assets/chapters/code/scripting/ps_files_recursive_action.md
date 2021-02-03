## Recursive action on files

```sh
gci -path ..\ -recurse -filter *.csproj | foreach { pushd ([System.IO.Path]::GetDirectoryName($_.FullName)); C:\Windows\Microsoft.NET\Framework\v3.5\msbuild $_.fullname; popd; $_; }
 ```