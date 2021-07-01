## git checkout 

To navigate between the branches and select the line of development you’re working on
Switch branches or restore working tree files
Internally it moves HEAD to a different branch and update the working directory to match.
Checking out a branch updates the files in the working directory to match the version stored in that branch, and it tells Git to record all new commits on that branch
.can checking out files 		lets you see an old version of a file, leaving the rest of your working directory untouched.
.can checking out commits 		entire working directory match that commit
.can checking out branches

⚠️ SWITCHING BRANCHES CHANGES FILES IN YOUR WORKING DIRECTORY (adds, removes, modifies files): it updates the working directory to match.	
1. MOVES THE HEAD POINTER (pointer to a commit)
2. REVERTED THE FILES IN YOUR WORKING DIRECTORY back to the snapshot that 'BranchName' points to

⚠️ WORKS ONLY IF YOUR WORKING DIRECTORY IS CLEAN (no more changes are present in the current branch your on). 
This does not necessarily mean you alway have to commit everything to be able to change branches. 
You can also use `git stash` which is a very important tool used in git
Tip: When you switch between branches, the files that you work on (the "working copy") ARE UPDATED to reflect the changes in the new branch. 
If you have changes you have not committed, git will ensure you do not lose them.

git checkout `existing-branch-commit-tab` 		Checking out/switching from the current branch to an existing branch (making it the current branch)									
git checkout master					Makes "master" the active branch
git checkout mybranch 				Makes "mybranch" the active branch
								
git checkout -b `new-branch`	Create the branch and check out `new-branch`
git checkout `file` 

## CHECKING OUT BRANCHES

git checkout -b `new-branch`	Create the branch and check out `new-branch`
								-b means "git branch `new-branch`" 

git checkout -b `new-branch` `existing-branch`	Same as the above but base the new branch off of `existing-branch` instead of the current branch.

## CHECKING OUT COMMITS

git checkout `commit`
Update all files in the working directory to match the specified commit. You can use either a commit hash or a tag as the `commit` argument. 
This will put you in a detached HEAD state ! See `https://www.atlassian.com/git/tutorials/undoing-changes`
Re-commit the old version in a new snapshot as you would any other file. So, in effect, this usage of git checkout serves as a way to revert back to an old version of an individual file.
This makes your working directory match the exact state of the a1e8fb5 commit. YOU CAN LOOK AT FILES, COMPILE THE PROJECT, RUN TESTS, AND EVEN EDIT FILES WITHOUT WORRYING ABOUT LOSING THE CURRENT STATE OF THE PROJECT. NOTHING YOU DO IN HERE WILL BE SAVED IN YOUR REPOSITORY.
To continue developing, you need to get back to the “current” state of your project: git checkout master

	During the normal course of development, the HEAD usually points to master or some other local branch, but when you check out a previous commit, HEAD no longer points
	to a branch—it points directly to a commit. This is called a “detached HEAD” state,
												↑
git checkout `commit` 			put you in a detached HEAD state
				↓ 					Update all files in the working directory to match the specified commit.
	commit hash or a tag 		A read-only operation. It’s impossible to harm your repository while viewing an old revision
								You can look at files, compile the project, run tests, and even edit files without worrying
								about losing the current state of the project.
								Nothing you do in here will be saved in your repository.
								When back in the master branch, you can use either git revert or git reset to undo any undesired changes.

								git log --oneline
								b7119f2 Continue doing crazy things
								872fa7e Try something crazy
								a1e8fb5 Make some important changes to hello.py
								435b61d Create hello.py
								9773e52 Initial import

								git checkout a1e8fb5

## CHECKING OUT FILES

git checkout `file`		Check out an old file, AFFECT THE CURRENT STATE OF YOUR REPOSITORY
						Check out a previous version of a file, overwrite the working directory and adds it to the staging area
						A way to revert back to an old version of a file
						If you don’t want to keep the old version, you can check out the most recent
						version with the following: git checkout HEAD `file`

Check out a previous version of a file. This turns the `file` that resides in the working directory into an exact copy of the one from `commit` and adds it to the staging area.

git checkout a1e8fb5 hello.py
Remember, unlike checking out a commit (see below), THIS DOES AFFECT THE CURRENT STATE OF YOUR PROJECT. The old file revision will show up as a “Change to be committed,” giving you the opportunity to revert back to the previous version of the file. If you decide you don’t want to keep the old version, you can check out the most recent version with the following:
git checkout HEAD hello.py

git checkout HEAD `file`
check out the most recent version of `file`


