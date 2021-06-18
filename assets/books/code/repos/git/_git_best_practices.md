## GIT BEST PRACTICES

* Commit early and commit often

* Every repository must include 
- README
- LICENSE
- .gitignore

* Keep your local repository code up-to-date with the code in the remote repository. 
This avoids a lot of merge conflicts later when you raise a pull request
Every time you pull the code from the remote repository to the local repository a new merge commit is created in your local repository. This means that your local commit history is going to have a lot of merge commits which can make things look confusing to the reviewer.

* Whenever you start a new feature, a new experiment, a new bugfix, create a new branch

* Have relevant commit names 
e.g. “Bugfix for #444 login page - fix flicker due to missing $scope function”.

Feature branches provide an isolated environment for every change to your codebase. When a developer wants to start working on something—no matter how big or small—they create a new branch. This ensures that the master branch always contains production-quality code.

Delete branches after the corresponding pull request has been merged onto master. Orphaned branches only cause confusion.

Fork a project, branch off and make a pull request sooner rather than later. This announces your intent to work on something to the rest of the collaborators. A pull request does not have to wait until all the work has been finalized before merging it onto master.

Don’t keep working for too long on your own local branch. Things can get out of sync quickly if you do so.

GitHub does not magically solve merge conflicts between branches. Diff tools are your friend. 

Projects on GitHub do not automatically become open source. GitHub repositories need to pick a valid license before they are truly considered open-source software—make your pick as you’re setting up your repository.

Please play nice with others and have meaningful ReadMe files and descriptive commit messages. Emojis are more than welcome


## HOTFIX SAMPLE

Switch to your production branch.
Create a branch to add the hotfix.
After it’s tested, merge the hotfix branch, and push to production.
Switch back to your original story and continue working.
Merge hotfix into master branch

					master
					↓
	C0 	←  	C1	←	C2

HEY, A BUG !
1. SAVE YOUR CURRENT WORK

		git checkout -b myWork

						master
						↓
		C0 	←  	C1	←	C2
						↑
						myWork

	vim index.html
	git commit -a -m 'added a new footer [issue 05]'

						master
						↓
		C0 	←  	C1	←	C2	← 	C3 
								↑
								myWork

2. FIX THE BUG FROM master, not the current version we are working on

git checkout master
git checkout -b hotfix
vim index.html
git commit -a -m 'fixed the broken email address'

					master 	hotfix
					↓		↓
					↓	← 	C4
	C0 	←  	C1	←	C2
						← 	C3
							↑
							myWork

Test, then merge it back into your master branch to deploy to production.
git checkout master
git merge hotfix
							master
							↓
							hotfix
							↓
						← 	C4
	C0 	←  	C1	←	C2
						← 	C3
							↑
							myWork

	Switch back to the work you were doing before you were interrupted.
	Delete the hotfix branch, because you no longer need it
	git branch -d hotfix
	git checkout myWork

	The work you did in your hotfix branch is not contained in the files in your myWork branch.
	If you need to pull it in, you can merge your master branch into your myWork branch by running
	'git merge master', or you can wait to integrate those changes until you decide to pull the myWork
	branch back into master later.


https://opensource.com/article/21/4/context-switching-git