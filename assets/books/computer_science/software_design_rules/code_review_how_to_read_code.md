### How to Read Code

Going into existing codebases is a necessary skill but a common refrain is â€œI hate reading other peopleâ€™s codeâ€ 
The reason is we didnâ€™t write it (weâ€™re the best coders on the planet and no one else can write code like we can): be a passive reader is not so beneficial as the intense thought process that goes into creating code

1. Learn to dig
- git blame   author name, last modified date, commit hash 
- git log to look at the commit history of the overall repo.
  git log | grep someFunction -C 3  (3 lines of context)
- git log -p index.js   file history  

2. Go Back in Time
Reading through issues, pull requests, code reviews
Pay attention to the issues that have generated the largest amount of discussion (pain points)

3. Read the Specs
Specs are the new comments
Unit specs: to figure out what functions and modules are supposed to do, edge cases they handle
Integration specs: to figure out how users are going to interact with your application and what kinds of workflows your application supports.

4. Think of Comments as Hints
Comment is up-to-date ?

5. Find Main
Files, instantiated classes, configuration set

6. Notice Style
Naming conventions, spacing conventions, brace placement, code conventions.

7. Expect to Find Garbage
Find files/functions that are never used, commented-out code that hasnâ€™t been touched in years (git blame). Donâ€™t slow down and spend too much time thinking about it, and donâ€™t be afraid to get rid of this stuff.

8. Donâ€™t Get Lost
Donâ€™t expect it to be a linear process, and donâ€™t expect to understand everything 100%. Pay attention to the important details and know how to dig around to find answers to your questions, and you will find yourself understanding very quickly.
