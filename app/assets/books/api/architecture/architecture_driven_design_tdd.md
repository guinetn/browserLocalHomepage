### TDD - TEST DRIVEN DEVELOPMENT

Test-driven design/unit-testing

Development model in wich we are writing unit tests before the real code 

2 groups in TDD: 

* les fondamentalistes qui exigent qu’aucune ligne de code ne doive être écrite sans un test, 
* les renieurs, ceux qui se refusent carrément à utiliser le TDD 

Projets = succès, avec et sans TDD


fluent_assertions.md to add

## React sample

Par exemple avec React :
Create projet: create-react-app
Push it on Github
connecte on Netlify
Create End To End (E2E) test called by Github Actions (checked at each push): check app works globally
(Can add Jest for unit testing, complement to E2E)
Create a new feature
E2E + unit tests OK + feature ok → push on master/main
This open a PR (pull request) + run test from Github Actions
Test pass → validate PR, validate merge, delete feature branch
Automatic deploy to netlify



# F# TEST
Example of a password strength validator. Requirements are “a password must be at least 8 characters long to be valid”. 

```f#
namespace FSharpTests

open Xunit
open CSharpCode

module ``Password validator tests`` =

[<Fact>]
let ``length above 8 should be valid`` () =
let password = "12345678"
let validator = Validator ()
# Assert.True(validator.IsValid(password))
… and in the CSharpCode project, I would then write the dumbest minimal implementation that could passes that requirement, that is:

public class Validator
{
public bool IsValid(string password)
{
return true;
}
}
```

Next, I would write a second test, to verify the obvious negative:

```f#
namespace FSharpTests

open Xunit
open CSharpCode

module ``Password validator tests`` =

[<Fact>]
let ``length above 8 should be valid`` () =
let password = "12345678"
let validator = Validator ()
# Assert.True(validator.IsValid(password))

[<Fact>]
let ``length under 8 should not be valid`` () =
let password = "1234567"
let validator = Validator ()
# Assert.False(validator.IsValid(password))
# This fails, producing the following output in Visual Studio:
# … which forces to fix implementation:

public class Validator
{
public bool IsValid(string password)
{
if (password.Length < 8)
{
return false;
}

return true;
}
}
```






