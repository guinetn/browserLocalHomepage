## git reset



code clean-up before doing a commit
permanent undo (no way to retrieve the original copy)
Reset current HEAD to the specified state (~rollback)
Don’t Reset a public History (a pushed to a public repository commit)

      _____
     /     \ 							
    ↓       \
o---o--------x---→ 	reseting

git reset will move the branch pointer back in the chain (typically) to "undo" changes

						 main
						  ↓
9ef9173  ←  7c709f0  ←  b764644
line1       line1 		line1
            line2       line2
            			line3
git log --oneline
b764644 File with three lines
7c709f0 File with two lines
9ef9173 File with one line

git reset 9ef9173     to roll back to a previous commit
git reset current~2   is the same, the results of this operation is:

main
  ↓
9ef9173  ←  7c709f0  ←  b764644
line1       line1 		line1
            line2       line2
            			line3
git log --oneline
9ef9173 File with one line     we'll see just the one commit


git reset					Reset staging area to match most recent commit, but leave the working directory unchanged.
, populate the working directory with the contents of the commit, and reset the staging area; soft to only reset the pointer in the repository; and mixed (the default) to reset the pointer and the staging area.
options: 
* hard 
to reset the commit being pointed to in the repository, populate the working directory with the contents of the commit, and reset the staging area
* soft
to only reset the pointer in the repository
* mixed (the default) 
to reset the pointer and the staging area

git reset --hard			Reset staging (planned next commits) area and working directory to match most recent commit and overwrites all changes in the working directory. It overwrites any uncommitted changes.
git reset `commit`			Move the current branch tip backward to `commit`, reset the staging area to match, but leave the working directory alone.
git reset --hard `commit`	Same as previous, but resets both the staging area & working directory to match. Deletes uncommitted changes, and all commits after `commit`.


git reset `file`
Remove a file from staging 
Unstage the file(s separated by spaces) but preserves its contents. File will not be in next commit
Remove `file` from the staging area, but leave the working directory unchanged. This unstages a file without overwriting any changes.
git reset .
	reset all files of the current directory

git reset --hard
Return to last commited state (no undo) = git reset + git checkout 
THROW AWAY YOUR LOCAL DEVELOPMENTS (updated files, new files...)
Files removed from the staging area and the working directory is taken back to the state of the last commit.

git reset --hard HEAD
	discard all change in your working directory

git reset --hard `commit-hash` 
go back to any commit state. Remember, HEAD is an alias for the last commit-hash of the branch.

git reset HEAD~1 
remove the last commit (if not pushed). HEAD~1 is one commit from the head

git revert HEAD
revert the last commit (create new one)	
If already committed files was a mistake, git revert undo the commits by creating a new commit which has the inverse affect of the commit being reverted.

git revert HEAD...HEAD~2
revert the commits between HEAD and HEAD~2. HEAD~2 is two commits from the head


git log --oneline
723cdc5 updated sass to hopefully fix home page slideshow
2336f9a fixed small JS bug
922d67e completed home page slideshow JS
	↓
commit number you want to revert back
git revert --no-commit 922d67e..HEAD
git add -A 										Add all of the reverted file changes to a commit
git commit -m "reverted to previous commit"		Do a commit with a comment
git push

git checkout
will replace everything in the working directory to the last committed version.

git checkout .
will replace everything in the CURRENT directory to the last committed version.

git checkout -f 		undo changes: check out HEAD
works only with files that are staged for commit or are already part of the repository, but sometimes you want to get rid of new files as well. Using touch, create a file with a name of your choice, then git add it. Verify that running git checkout -f gets rid of it.

git checkout `file`
git checkout src/app.js src2/mm.js
check out the most recent version of `file`
will replace everything in the listed directories to the last committed version.

UNMODIFYING A MODIFIED FILE - restore the file to its previous committed state.
git checkout -- CONTRIBUTING.md 	Don’t want to keep your changes to the CONTRIBUTING.md file?
									revert it back to what it looked like when you last committed

git checkout $id `file`
checkout the $id version of `file`

git rebase -i HEAD~2  		to squash (écraser) your last few commits

GOING BACK IN TIME TO TRY OUT AN OLDER VERSION OF YOUR PROJECT

In the context of a bug, you want to see how things worked in an older revision.
However, you don't have to maneuver yourself into a detached HEAD state to deal with it. 

Create a (temporary) branch and delete it once you're done.
$ git checkout -b test-branch 56a4e5c08
...do your thing...
$ git checkout master
$ git branch -d test-branch		

AMEND A COMMIT (IF YOU FORGET TO ADD A FILE....)

Fix the last commit (replace it) with staged elements (forget a file...bad commit message)

$ git commit -m 'initial commit'
$ git add `my_forgotten_file`
$ git commit --amend 			Takes your staging area and uses it for the commit
								Overwrites your previous commit msg
$ git commit –a --amend -m “Message Text” 	Adds all changes to the previous commit, overwriting the commit message
											with the new 'Message Text'. Does not include new files
UNDOING LAST COMMIT
git reset HEAD 			Because HEAD points to the last commit

UNSTAGING A STAGED FILE
git reset HEAD `file`				To unstage a file in the staging (git add * done by error..)

git checkout

Switch branches or restore working tree files
Internally it moves HEAD to a different branch and update the working directory to match.
![][img/git/checkout.svg]	



* SOFT RESET - NO FILE IMPACT (working directory unchanged, just unstaging)

When some messy code have been accidentally committed 
Simple unstage.  when you accidentally staged (added) a file i don't want to commit	
A soft reset should be reserved for a genuine mistake whereas a stash can be used to swap code in and out.

git reset `file`
	Remove the file from the staging area. WORKING DIRECTORY UNCHANGED
	This unstages a file without overwriting any changes
	unstages a file without overwriting any changes.
	Remove the specified file from the staging area, but leave the working directory unchanged. 

git reset
	a simple way to undo changes that haven’t been shared with anyone else.
	Reset the staging area to match the most recent commit. WORKING DIRECTORY UNCHANGED
	To re-build the staged snapshot from scratch.
	unstages everything you added for the upcoming commit. It does not change your files.
	unstages all files without overwriting any changes, giving you the opportunity to re-build the staged snapshot from scratch.
	Reset the staging area to match the most recent commit, but leave the working directory unchanged. 

	git checkout hotfix
	git reset HEAD~2  	remove commits from the current branch:	moves the hotfix branch backwards by two commits.

		git reset --soft HEAD  		Undo most recent commit but retain changes in staging area
		git reset --soft HEAD~1     reset the most recent commit
		git reset --soft HEAD~2     reset back more 
					↓
				--soft                reset only HEAD
				
* HARD RESETS - IMPACT FILE (working directory & staging area changed)

alter the staged snapshot and/or the working director

				| --soft                reset HEAD only
				| --mixed               reset HEAD, index
				| --merge               reset HEAD, index, working directory 
				| --hard                reset HEAD, index, working directory 
				| --keep                reset HEAD but keep local changes							  
				|
git reset --hard
	THROW AWAY YOUR LOCAL DEVELOPMENTS (updated files, new files...)
	Reset the staging area AND THE WORKING DIRECTORY to match the most recent commit. In addition to unstaging changes, the --hard flag tells Git to overwrite all changes in the working directory, too. Put another way: this obliterates all uncommitted changes, so make sure you really want to 

	! Undo everything since the last commit. OVERWRITE THE WORKING DIRECTORY
	! Reset the staging area to match the most recent commit					
	handy when an experiment has gone horribly wrong

	$ git reset --hard MyBranch 	# if your
		branch messed up, undo whatever

	git reset --hard HEAD~2     	Decide to scrap the feature and remove the associated commits
									Moves the current branch backward by two commits, effectively
									removing the two snapshots we just created from the project history.

git reset --hard HEAD
	Reset HEAD pointer to a previous commit and discard all change in your working directory

	'git reset' will resets the current branch to the commit you specify (--hard means to discard both index and working directory  changes)
		reset --hard HEAD^ resets the current branch one commit backward
		reset --hard HEAD just discards all local changes.

		reset --hard HEAD~1		erases definitively your last commit
	
git reset `commit`
	Reset HEAD pointer to a previous commit and keep all changes as unstaged changes
	Move the current branch tip backward to `commit`, reset the staging area to match, but leave the working directory alone. All changes made since `commit` will reside in the working directory, which lets you re-commit the project history using cleaner, more atomic snapshots.

	! Move the current branch to `commit`, reset staging area to match
	Leave the working directory alone. All changes made since `commit` will reside in the working directory, which lets you re-commit the project history using cleaner, more atomic snapshots.

git reset --keep `commit`
	Reset HEAD pointer to a previous commit and preserve uncommited local changes

git reset --hard `commit`
	Move the current branch tip backward to `commit` and reset both the staging area and the working directory to match. This obliterates not only the uncommitted changes, but all commits after `commit`, as well..
	! Move the current branch to `commit`, reset staging area & working directory to match.
	! This obliterates not only the uncommitted changes, but all commits after `commit`



## REWRITING HISTORY

overwriting committed snapshots
using history-rewriting commands may result in lost content

How do you revert a commit that has just been made but not commited?
git reset --hard HEAD~1

How do you revert a commit that has just been made?
git revert HEAD~2..HEAD
revert creates a new commit with patches that cancel out the changes introduced in specific commits.
Alternatively, one can always checkout the state of a particular commit from the past, and commit it anew.

How do you squash last N commits into a single commit?
git rebase -i HEAD~{N}

commits are being combined into one ("squashed" in Git slang)

You may have several local git commits. Now run “git push,” and it will generate several git commit histories. 
To consolidate them as one, we can use the “git squash” technique.
## get local 3 latest commits
$ git rebase -i HEAD~3
## In editor, change "pick" to "squash". Keep the first one as "pick"
$ git rebase --continue
$ git push origin $branch_name


How do you find a list of files that has changed in a particular commit?
git diff-tree -r {hash}
list all the files that were changed or added in that commit. The -r flag makes the command list individual files, rather than collapsing them into root directory names only.
git diff-tree --no-commit-id --name-only -r {hash}        supress the commit hashes from appearing in the output


http://ohshitgit.com/
Oh shit, I committed and immediately realized I need to make one small change!
## make your change
git add .
git commit --amend
## follow prompts to change or keep the commit message
## now your last commit contains that change!
This usually happens to me if I merge to master, then run tests/linters... and FML, I didn't put a space after the equals sign. You could also make the change as a new commit and then do rebase -i in order to squash them both together, but this is about a million times faster.

Oh shit, I need to change the message on my last commit!
git commit --amend
## follow prompts to change the commit message
Stupid commit message formatting requirements.

Oh shit, I accidentally committed something to master that should have been on a brand new branch!
## create a new branch from the current state of master
git checkout -b some-new-branch-name
## remove the commit from the master branch
git checkout master
git reset HEAD~ --hard
git checkout some-new-branch-name
## your commit lives in this branch now :)
Note: this doesn't work if you've already pushed to origin, and if you tried other things first, you might need to git reset HEAD@{number}. Infinite sadness.

Oh shit, I accidentally committed to the wrong branch!
## undo the last commit, but leave the changes available
git reset HEAD~ --soft
git add .
git stash
## move to the correct branch
git checkout name-of-the-correct-branch
git stash pop
git add .
git commit -m "your message here"
## now your changes are on the correct branch

Oh shit, I tried to run a diff but nothing happened?!
git diff --staged
Bizarrely, git won't do a dif of files that have been add-ed to your staging area without this flag. File under ¯\_(ツ)_/¯

Fuck this noise, I give up.
cd ..
sudo rm -r fucking-git-repo-dir
git clone https://some.github.url/fucking-git-repo-dir.git

