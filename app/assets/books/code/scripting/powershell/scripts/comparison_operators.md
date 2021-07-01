## COMPARISON OPERATORS

To compare/find values values that match certain patterns

| Operator     |  Definition |
|---|----|
| -cxxxxx      |  Use case-sensitive |
| -eq          |  Equal to |
| -ne          |  Not equal to |
| -gt          |  Greater than |
| -ge          |  Greater than or equal to |
| -lt          |  Less than |
| -le          |  Less than or equal to |
| -Like        |  Match using the * wildcard character |
| -NotLike     |  Does not match using the * wildcard character |
| -Match       |  Matches the specified regular expression |
| -NotMatch    |  Does not match the specified regular expression |
| -Contains    |  Determines if a collection contains a specified value |
| -NotContains |  Determines if a collection does not contain a specific value |
| -In          |  Determines if a specified value is in a collection |
| -NotIn       |  Determines if a specified value is not in a collection |
| -Replace     |  Replaces the specified value |

PowerShell' -eq 'powershell'    True
'PowerShell' -ceq 'powershell'   False. use case-sensitive
'PowerShell' -ne 'powershell'
'PowerShell' -like '*shell'
'PowerShell' -match '^*.shell$'  Use regex
'PowerShell' -replace 'Shell'

5 -gt 5

$Numbers = 1..10
$Numbers -contains 7
$Numbers -notcontains 2
15 -in $Numbers