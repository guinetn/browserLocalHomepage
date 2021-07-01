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





Work on a short-lived feature branch. That tends to keep your pull request smaller so it is more easily comprehensible to reviewers and minimizing your divergence from master reducing the complexity of any conflict resolution.

Master should always have working, production-ready code. That avoids the burden to everyone in having to decide if a particular commit is safe to use as a starting point for a branch, for a demo, etc.

Improve clarity with judicious squashing. Use an interactive rebase to squash trivial commits as well as commits that are not particularly relevant to other developers. Remember, you’re committing for posterity so reduce the noise in the commit history.

Improve clarity with judicious non-squashing. You might decide the path of least resistance is to always squash all commits into one (strategy B). This does have advantages (e.g. less work cleaning up your commit history to make sense, and certainly less complex to do). However, just be aware that it makes your commit history, by necessity, have less detailed messages. Those messages show up in git log and git blame so they then offer less context. This may not be a bad thing, mind you. This particular bullet point really depends on what works for your team.

Do your conflict resolution on your branch so your CI system can provide a safety net to avoid introducing failures to master.

Don’t forget to be a good netizen and cleanup after yourself. Delete your branch on GitHub after your work has been merged. GitHub makes that very easy: as soon as you press the big, green button to confirm the merge, it updates the page with a button to delete your now-unneeded branch. Even if you merge from the command-line, refresh the GitHub page for your PR and it will present you with the same button to delete your unneeded branch.




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


## Git advanced

Development process in Git
Master branch
The Master Branch should always have a copy of the existing code in Production.
No-one — including the tech lead — should be coding directly in the master branch since it is a copy of production code.
The actual code is written in other branches.
Release branch
When the project begins the first thing to do is to create a release branch for the project. The release branch is created from the master branch.
All code pertaining to this project will be in the release branch. The release branch is just a normal branch with the prefix release/.
Let’s call the release branch for this example release/fb.
It’s possible that there are multiple projects running on the same code base. So, for each project, a separate release branch is created. Let’s say there is one more project running in parallel. Then that project can have a separate release branch like release/messenger
The reason to have a release branch is that the same code base can have multiple projects running in parallel — there should be no conflict between the projects.
Feature branch
For every feature that is built in the application a separate feature branch is created. This ensures that the features can be built independently
Feature branch is just like any other branch but with the prefix feature/
Now you, being the tech lead, have asked Alice to build a login screen for Facebook. So she creates a new feature branch for this. Lets call the feature branch feature/login. Alice would write the entire login code only in this feature branch.
The feature branch is generally created from the release branch
Bob has been tasked with building the “Friend” request page. So Bob creates a feature branch called feature/friendrequest
John’s task is to build the news feed. So John creates a feature branch called feature/newsfeed
All of the developers code in their individual feature branches. So far so good 😃
Now, let’s say that Alice finished her task and the login code is ready. She needs to send her code to the release branch release/fb from her feature branch feature/login. This is done through a pull request.
Pull request
First and foremost, a pull request is not to be confused with git pull .
The developer cannot push the code directly into the release branch. The tech lead needs to review the feature code before it goes into the release branch. This is done through a pull request.
Alice can raise the pull request as follows in GitHub — these steps are specifically for GitHub.

Right next to the branch name there is an option called “New pull request”. Clicking on this opens a new screen shown below:

Here:
the compare branch should be Alice’s feature branch feature/login
the base branch should be the release branch release/fb.
Once this is done, Alice needs to enter a title and description for the pull request, and finally click on “Create Pull Request”. Alice also needs to assign a reviewer for this pull request. She enters your name as the reviewer since you are the tech lead.
The tech lead then reviews the code in the pull request, and merges the code from the feature branch into the release branch
So now you have merged the code from the feature/login branch tothe release/fb branch and Alice is pretty happy that her code has been merged. 😃
Code Conflicts 😠
Bob has completed his code as well, and has raised a pull request from feature/friendrequest to release/fb.
Since the release branch already has the login code, code conflicts occur. It is the responsibility of the reviewer to resolve these code conflicts and merge the code. In this case, you as the tech lead need to resolve these code conflicts and merge the code.
Now John has also completed his code and wants to add his code to the release branch. But John is pretty good at handling code conflicts. John takes the Latest code from release/fb branch into his own feature branch feature/newsfeed ( either through git pull or git merge ). John resolves all the conflicts that are present. Now the feature/newsfeed branch has all the code present in release/fb as well.
Finally, John raises a pull request. This time there are no code conflicts in the pull request since John has already resolved them.
So there are two ways to resolve code conflicts:
First method: the reviewer of the pull request needs to resolve the code conflicts.
Second method: the developer ensures that latest code from the release branch is merged into the feature branch and resolves the conflicts themselves.
Master branch again
Once the project is completed, the code from the release branch is merged back into the master branch. The code is then deployed to production. Thus, the code in production and the code in the master branch are always in sync. This also ensures that, for any future project, the up-to-date code is available in master.



