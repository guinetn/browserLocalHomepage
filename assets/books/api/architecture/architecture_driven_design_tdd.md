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


