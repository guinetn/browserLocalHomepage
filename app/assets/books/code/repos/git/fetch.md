## git fetch

Fetch downloads the changes from the remote repository into a separate branch named remotes/`remote-name`/`remote-branch-name`. The branch can be accessed using git checkout
A great way to review the changes without affecting your current branch.

To merge the fetched changes into master:
git merge remotes/`remote-name`/`remote-branch-name` master


Imports commits from a remote repository into your local repo
When you want to see what everybody else has been working on
Since fetched content is represented as a remote branch, it has absolutely no effect on your local development work.
Gives you access to the entire branch structure of another repository.
				
Resulting commits are stored as 'remote branches' instead of the normal local branches that we’ve
been working with. This gives you a chance to review changes before integrating them into your copy
of the project.

A safe way to review commits of teammates before integrating them with your local repository. it doesn’t force you to actually merge the changes into your repository.

imports commits from a remote repository into your local repo  as remote branches instead of the normal local branches that we’ve been working with. This gives you a chance to review changes before integrating them into your copy of the project.

git fetch `RemoteName`
	Fetch all of the branches from the repository. This also downloads all of the required commits and files from the other repository.

	Pulls down all the data from that remote project THAT YOU DON’T HAVE YET
	into to your local repository WITHOUT MODIFYING YOUR WORKING DIRECTORY
	It will simply get the data for you and let you merge it yourself
	Gives you references to all the branches from that remote
	Then you can merge in or inspect

	git fetch origin 			Fetches any new work that has been pushed to that server since you cloned					
	# a1e8fb5..45e66a4 master -` origin/master
	# a1e8fb5..9e8ab1c develop -` origin/develop
	# * [new branch] some-feature -` origin/some-feature

git fetch `RemoteName` `branch`
	Same as the above command, but only fetch the specified branch.
	
	To see what commits have been added to the upstream master
	git log --oneline master..origin/master

	To approve the changes and merge them into your local master branch 
	git checkout master
	git log origin/master

	Then we can use git merge origin/master
	git merge origin/master

	The origin/master and master branches now point to the same commit, and you are synchronized with the upstream developments.


	FETCH/PULL: To get data from your remote projects
 	git clone https://github.com/schacon/ticgit
 	cd ticgit
	git remote -v     v to view urls
	git remote add `remote_name` `remote_repo_url`
    git remote add `shortname` `url` 							Add a new remote Git repository as a shortname. 
    git remote add pb https://github.com/paulboone/ticgit 		Now use the string pb on the command line in lieu of the whole URL
    git remote rename pb paul
    git remote rm paul
    git fetch [remote-name] 									Default remote repository is the one under the name “origin”
 	git fetch pb 												Fetch all that Paul has but that you don’t yet have in your repository
 			only downloads the data to your local repository – it doesn’t automatically merge it with any of your work or modify what 
 			you’re currently working on. You have to merge it manually into your work when you’re ready.
	git pull   	to automatically fetch and then merge that remote branch into your current branch.
