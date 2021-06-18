## INSPECTING (DEBUG/SEARCH) A REPOSITORY

https://spin.atomicobject.com/2017/06/01/how-to-read-code
A necessary skill
“I hate reading other people’s code” is a common refrain
Reason we hate reading other people’s code is because we didn’t write it ourselves: you are the best coders on the planet
Because there’s an intense thought process that goes into creating code, and a passive reader doesn’t get the benefit of experiencing that firsthand.

git log 								to look at the commit history of the overall repo
git log | grep someFunction -C 3
git log -p index.js 					history of a single file
git blame `file`						to get an author name, last modified date, and commit hash for every single line
git grep author                         Print lines matching a pattern. 
git bisect								Binary search algorithm to find the commit that introduced a bug

download.page(code/repos/git/log.md)
download.page(code/repos/git/reflog.md)
download.page(code/repos/git/git_whatchanged.md)
download.page(code/repos/git/diff.md)
download.page(code/repos/git/blame.md)
download.page(code/repos/git/status.md)
download.page(code/repos/git/bisect.md)
download.page(code/repos/git/grep.md)
