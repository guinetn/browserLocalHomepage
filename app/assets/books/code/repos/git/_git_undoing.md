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

# GIT MISTAKES

# Spelled last commit message wrong
git commit --amend
This will open up your editor and allow you to make a change to that last commit message. No one needs to know you spelled, “Initial commment” with three “m”s.

# Spelling mistake on branch name
rename this branch in a similar way to how we rename a file with the mv command: by moving it to a new location with the correct name.
git branch -m feature-brunch feature-branch

# If you have already pushed this branch, there are a couple of extra steps required. We need to delete the old branch from the remote and push up the new one:
git push origin --delete feature-brunch
git push origin feature-branch

# Accidentally committed all changes to the master branch
So we can roll back all those changes to a new branch with the following three commands:
Note: Make sure you commit or stash your changes first, or all will be lost!
git branch feature-branch
git reset HEAD~ --hard
git checkout feature-branch
# This creates a new branch, then rolls back the master branch to where it was before you made changes, before finally checking out your new branch with all your previous changes intact.

# Forgot to add a file to that last commit
git add missed-file.txt
git commit --amend

# Added a wrong file in the repo
If all you did was stage the file and you haven’t committed it yet, it’s as simple as resetting that staged file:
git reset /assets/img/misty-and-pepper.jpg
If you have gone as far as committing that change, no need to worry. You just need to run an extra step before:
git reset --soft HEAD~1
git reset /assets/img/misty-and-pepper.jpg
rm /assets/img/misty-and-pepper.jpg
git commit
This will undo the commit, remove the image, then add a new commit in its place.

#  git reflog 
shows you a list of all the things you've done. It then allows you to use Git's magical time-traveling skills to go back to any point in the past. I should note, this is a last resort thing and should not be used lightly. To get this list, type:
git reflog

If you want to go back to any point in the history, run the below command, replacing {index} with that reference, e.g. dfa27a2.
git reset HEAD@{index}





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
