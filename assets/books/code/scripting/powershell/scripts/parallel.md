
# PARALLELIZE

```bash
1..5 | ForEach-Object -Process {write-output "This is number $_"; sleep 1}

(Measure-Command { 
    1..5 | ForEach-Object -Process {write-output "This is number $_"; sleep 1}
    }).Seconds

(Measure-Command { 
    1..5 | ForEach-Object -Parallel {write-output "This is number $_"; sleep 1}
    }).Seconds    
    
function FetchGitHubRepos {
    $orgs = @(
        'PowerShell',
        'Microsoft',
        'dotnet'
    )

    Measure-Command -Expression {
        foreach($org in $orgs) {
            1..10 | ForEach-Object -ThrottleLimit 3 -Parallel {
                (Invoke-RestMethod "https://api.github.com/orgs/$using:org/repos?page=$_") |
                Select-Object -Property full_name,stargazers_count |
                Export-Csv ./repo_stats.csv -Append
            }
        }
    } | Select-Object -Property Minutes, Seconds
}
FetchGitHubRepos   

Get-Content repo_stats.csv |
    ConvertFrom-Csv |
    Sort-Object { $_.stargazers_count -as [int] } -Descending |
    Select-Object -First 20 
```

- https://hub-binder.mybinder.ovh/user/dotnet-interactive-cb9ukwlm/lab/tree/powershell/Docs/For-EachObject%20parallel.ipynb