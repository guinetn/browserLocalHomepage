## GIT HOOKS

https://www.atlassian.com/git/tutorials/git-hooks

scripts that run automatically every time a particular event occurs in a Git repository
• customize Git’s internal behavior
• trigger customizable actions at key points in the development life cycle.

. encouraging a commit policy
. altering the project environment depending on the state of the repository
. continuous integration workflows

To alter internal behavior and receive notifications when certain events occur in a repository.
Hooks are ordinary scripts that reside in the .git/hooks repository which makes them very easy to install and customize.

## Perform customizable actions at every stage in the commit creation process, as well as the git push process.

Hooks reside in either local or server-side repositories and they are only executed in response to actions in that repository. Hooks reside in the .git/hooks directory of every Git repository. Git automatically populates this directory with example scripts when you initialize a repository. 

Samples are in `user_repo`\.git\hooks
To “install” a hook, all you have to do is remove the .sample extension

prepare-commit-msg
-------------------------------------------------------------
#!/bin/sh                                                  shebang line: how your file should be interpreted
echo "# Please include a useful commit message!" ` $1
-------------------------------------------------------------

chmod +x prepare-commit-msg 		# Hooks need to be executable

in python:

#!/usr/bin/env python
import sys, os
commit_msg_filepath = sys.argv[1]
with open(commit_msg_filepath, 'w') as f:
f.write("# Please include a useful commit message!")

* LOCAL HOOKS

* SERVER-SIDE HOOKS