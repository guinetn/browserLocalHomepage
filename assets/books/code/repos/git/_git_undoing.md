## GIT UNDOING

FIX MISTAKES: amending commits & rebasing

git rebase -i HEAD~1  		Remove last commit
git rm --cached -r .        Remove every file from Git's index

git revert `commit`    	Create new commit that undoes all of the changes made in `commit`, then apply it to the current branch.

git log -p 				Display the full diff of each commit.

git reset 			 	Reset staging area to match most recent commit, but leave the working directory unchanged.
git reset --hard        Rewrite the Git index to pick up all the new line endings.
                        Reset staging area and working directory to match most recent commit and overwrites all changes in the working directory.
git reset `commit`      Move the current branch tip backward to `commit`, reset the staging area to match, but leave the working directory alone.
git reset --hard `commit`  Same as previous, but resets both the staging area & working directory to match. Deletes uncommitted changes, and all commits after `commit`.



https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826

* Change the commit message (when you realized that last commit message you entered is actually not clear)
git commit --amend -m “New commit message”

* You commit only 5 of the 6th files needed...
## Dont need to create a new commit and add the 6th file to that commit: add this file to your previous commit itself
git add file6
git commit --amend --no-edit
				   --no-edit means that the commit message does not change



download.page(code/repos/git/clean.md)
download.page(code/repos/git/revert.md)
download.page(code/repos/git/reset.md)


## UNDOING CHANGES

The motivation behind creating new commits is that re-writing history in Git is an anti-pattern. If you have pushed your commits then you should create new commits to undo the changes as other people might have made commits in the meantime.

Rewriting Git History

	git commit --amend 		Replace the last commit with the staged changes and last commit combined. 
	 						Use with nothing staged to edit the last commit’s message.
	git rebase `base`		Rebase the current branch onto `base`. `base` can be a commit ID, a branch name, a tag, or a relative reference to HEAD.
	git reflog 				Show a log of changes to the local repository’s HEAD. Add --relative-date flag to show date info or --all to show all refs.



## REWRITING HISTORY

overwriting committed snapshots
using history-rewriting commands may result in lost content

git commit --amend 

	To fix up the most recent commit (REPLACES PREVIOUS COMMIT) because of 'premature commits' or to reformat commit message  
	It lets you combine staged changes with the previous commit instead of committing it as an entirely new snapshot. 
	It can also be used to simply edit the previous commit message without changing its snapshot.

	Never reset commits that have been shared with other developers. 
	The same goes for amending: never amend commits that have been pushed to a public repository.

	git commit --amend         to just change the commit message (but REPLACE the last commit)

	# Edit hello.py and main.py
	git add hello.py
	git commit
	# Realize you forgot to add the changes from main.py
	git add main.py
	git commit --amend --no-edit
							\_____ make the amendment to your commit without changing its commit message
git merge
	Join two or more development histories together
	The most common way to combine branches is git merge, but there’s a second method called git rebase

download.page(code/repos/git/squash.md)

How do you find a list of files that has changed in a particular commit?
git diff-tree -r {hash}
list all the files that were changed or added in that commit. The -r flag makes the command list individual files, rather than collapsing them into root directory names only.
git diff-tree --no-commit-id --name-only -r {hash}        supress the commit hashes from appearing in the output
