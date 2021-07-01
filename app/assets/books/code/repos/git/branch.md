## git branch

“Your branch distance from main is equal to your level of insanity” - anonymous

Common branches:
Feature  To add new features to the code base
Release  Code planned for next release
Master   Default branch that all code eventually gets merged to
Develop  Active development branch, where code is being work on for next release(s)
Hotfix   Change to fix a specific blocking bug or service disruption
Service Pack: Collection of hotfixes (+ features) for previous release

Branches are just names for commits

Whenever you start a new feature, a new experiment, a new bugfix, create a new branch

git branch 						List all of the branches in your repo 
git branch newbranch 			Starts a new feature (creates a new branch) called "mybranch". Only create a new branch – IT DIDN’T SWITCH TO THAT BRANCH.
git branch newbranch frombranch

git checkout newbranch          Checking out, or switching to, a branch
git checkout -b `new-branch`	Create the branch and check out `new-branch`
git checkout `commit-branch-tag` 
git branch -d `branch` 			Delete the specified branch
git branch -m `branch` 			Rename the current branch to `branch`

git branch -a 			List all local and remote branches
git branch -v 			details
git branch -r 			List all remote branches
git branch --merged   	filter this list to branches that you have merged into the branch you’re currently on
git branch ---no-merged  	filter this list to branches that you have not yet merged into the branch you’re currently on
git merge `branch` 			Merge `branch` into the current branch.


## Default branch name
master' → 'main' 	From the 01/10/2020 in Github & GitLab
git branch -M main
        \___ git branch -m master main    Renaming: master → main
git branch
	
List, create, or delete local branches in the current repository	

git branch
	List all of the branches in your repository.

									a revision number (or the first 6 characters of such) or an appropriate tag
										↑
	git branch [options][`BranchName`][`StartPoint`]
					↓
			-a 	List all local and remote branches
			-r 	List all remote branches

git branch `BranchName`
	Create a new branch called `BranchName` in the current repository 				
	This doesn't check out the new branch.				

	git branch mybranch 			# Creates a new branch called "mybranch". Only create a new branch – IT DIDN’T SWITCH TO THAT BRANCH.
	git checkout mybranch 			# Makes "mybranch" the active branch
	git checkout -b mybranch 		# Creates a new branch called "mybranch" and makes it the active branch				
	git log --oneline --decorate 	# git log shows where the branch pointers (master, Head) are pointing. This option is called --decorate.

git branch -d `branch`
	Delete the specified branch. 
	Cannot delete if it has unmerged changes.

git branch -D `branch`
	Force delete the specified branch, even if it has unmerged changes. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development.

git branch -m `branch`
	Rename the current branch to `branch`

SAMPLE
git branch crazy-experiment
git branch -d crazy-experiment
git branch -D crazy-experiment

git branch 				List all local branches
							* prefixes master branch: indicates the branch that you currently have checked out (HEAD points to)
git branch -r 			List all remote branches
git branch -a 			List all local and remote branches
git branch -v 			details
git branch --merged   	filter this list to branches that you have merged into the branch you’re currently on
git branch ---no-merged  	filter this list to branches that you have not yet merged into the branch you’re currently on
git branch -d hotfix 		delete the 'hotfix' branch			
