# GIT BRANCHES

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

What is a trunk in software?
In the world of software development, "trunk" means main development branch under a version control system. It’s the base of a project, where all improvements are being merged together.

What is code branching and merging?
Branches are created from the base project, in order to develop a new feature, fix a bug, or simply do some refactoring. They prevent software developers from disturbing each other and enable them to work in parallel. Once a change is finished and tested, the branch is merged back to the trunk.

What is a branch in version control?
A branch in a version control system is a duplicate of the base project. It’s created so that changes can happen in parallel across other branches. It essentially solves the problem of working on the same files at the same time.

Feature branch
The feature branch has a clear and highly-focused purpose—to add specific functionality to a project. It shouldn’t contain any other changes that fix bugs, introduce other features, or are part of a refactoring.

## Création d’une branche par Feature / Bug

master		default development branch
master 		for production ---→ deprecated, see below
main 		for production ---→ 'main' from the 01/10/2020 in Github & GitLab 
release 	branche de version
develop 	for development
feature 	pour new functionality	
exerimental
fix 		correctif	
hotfix 		correctif urgent


## Master branch
should always have a copy of the existing code in Production.

No-one?—?including the tech lead?—?should be coding directly in the master branch since it is a copy of production code.
The actual code is written in other branches.

## Release branch
When the project begins the first thing to do is to create a release branch for the project. The release branch is created from the master branch.
All code pertaining to this project will be in the release branch. The release branch is just a normal branch with the prefix release/.
Let’s call the release branch for this example release/fb.
It’s possible that there are multiple projects running on the same code base. So, for each project, a separate release branch is created. Let’s say there is one more project running in parallel. Then that project can have a separate release branch like release/messenger
The reason to have a release branch is that the same code base can have multiple projects running in parallel?—?there should be no conflict between the projects.

## Feature branch
For every feature that is built in the application a separate feature branch is created. This ensures that the features can be built independently
Feature branch is just like any other branch but with the prefix feature/
Now you, being the tech lead, have asked Alice to build a login screen for Facebook. So she creates a new feature branch for this. Lets call the feature branch feature/login. Alice would write the entire login code only in this feature branch.
The feature branch is generally created from the release branch
Bob has been tasked with building the “Friend” request page. So Bob creates a feature branch called feature/friendrequest
John’s task is to build the news feed. So John creates a feature branch called feature/newsfeed
All of the developers code in their individual feature branches. So far so good ??
Now, let’s say that Alice finished her task and the login code is ready. She needs to send her code to the release branch release/fb from her feature branch feature/login. This is done through a pull request.
Once the project is completed, the code from the release branch is merged back into the master branch. The code is then deployed to production. Thus, the code in production and the code in the master branch are always in sync. This also ensures that, for any future project, the up-to-date code is available in master.




EXPERIMENTS USING BRANCHES
	
	A branch = an independent line of development (encapsulate your changes in a specific context)
	To build new features or test out ideas without putting your main project at risk.
	The default branch in Git is called 'master'
	When you switch a branch, Git changes the contents of the working directory.
	As additional branches work in the same way as master they are ideal for prototyping and experiments as any changes can be merged to master if required.
	
	git branch `new branch name` `starting branch` 
	takes an existing branch and creates a separate branch to work in. At this point both branches are identical.
	
	git branch -va
	List all the branches with their last commit message 


	A branch represents the tip of a series of commits—it's not a container for commits. 
	New commits are recorded in the history for the current branch, which results in a fork in the history of the project.
	This makes sure that unstable code is never committed to the main code base, and it gives you the chance to clean up your feature’s history before merging it into the main branch

Having a dedicated branch for each new feature is a dramatic shift from the traditional SVN workflow. It makes it ridiculously easy to try new experiments without the fear of destroying existing functionality, and it makes it possible to work on many unrelated features at the same time. In addition, branches also facilitate several collaborative workflows.

		foo..bar 	from branch 'foo' to branch 'bar'
		'master' is the default branch
		
download.page(code/repos/git/branch.md)
download.page(code/repos/git/_git_branches_head.md)
download.page(code/repos/git/checkout.md)
download.page(code/repos/git/tag.md)