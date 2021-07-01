# In & Out

## Customize console
$host.UI.RawUI.ForegroundColor = [System.ConsoleColor]::Blue

## Clear console
Clear-Host = cls

## Write to console

Write-Host "hi"
Write-Host "Something to think about ..." -ForegroundColor Blue -BackgroundColor Gray
Write-Host "Hello " -NoNewline -ForegroundColor Red
Write-Host "World!" -ForegroundColor Blue

Out-Host            
writes directly to the PowerShell host, but it doesn't produce object-based output for the pipeline. So it can't be piped to Get-Member.
Get-ChildItem | Out-Host -Paging     output page-by-page display

Write-Warning "Warning"
Write-Verbose "Verbose" -Verbose
Write-Debug "Debug" -Debug

## Prompt
Write-Verbose "Ask for name" -Verbose
$name = Read-Host -Prompt "What's your name? "
Write-Host "Greetings, $name!" -ForegroundColor DarkBlue

Read-Host -Prompt "token? " -AsSecureString
token? : ········
System.Security.SecureString

Mandatory parameter prompts
Write-Output | ForEach-Object { "I received '$_'" }

$number = Get-Random -Minimum 1 -Maximum 10
do {
  $guess = Read-Host -Prompt "What's your guess?"
  if ($guess -lt $number) {
    Write-Output 'Too low!'
  }
  elseif ($guess -gt $number) {
    Write-Output 'Too high!'
  }
}
until ($guess -eq $number)


## PROGRESSBAR

Display at top of the host

For ($i=0; $i -le 100; $i++) {
    Write-Progress -Id 1 -Activity "Parent work progress" -Status "Current Count: $i" -PercentComplete $i -CurrentOperation "Counting ..."
 
    For ($j=0; $j -le 10; $j++) {
        Start-Sleep -Milliseconds 5
        Write-Progress -Parent 1 -Id 2 -Activity "Child work progress" -Status "Current Count: $j" -PercentComplete ($j*10) -CurrentOperation "Working ..."
    }
    
    if ($i -eq 50) {
        Write-Verbose "working hard!!!" -Verbose
        "Something to output"
    }
}
                            
## Misc

Multi-selection when running commands:
Get-Command nonExist -ErrorAction Inquire