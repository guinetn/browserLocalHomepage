## git remote

git remote 						List of your remote repositories that have been associated with your project
git remote -v  					View addresses of your configured remotes
git remote add `remote name` `remote address`
git remote add `name` `url` 	Create a new connection to a remote repo. After adding a remote, you can use `name` as a shortcut for `url` in other commands.
git fetch `remote` `branch` 	Fetches a specific `branch`, from the repo. Leave off `branch` to fetch all remote refs.
git pull `remote` 				Fetch the specified remote’s copy of current branch and immediately merge it into the local copy.
git push `remote` `branch` 		Push the branch to `remote`, along with necessary commits and objects. Creates named branch in the remote repo if it doesn’t exist.
git push `remote` --force 		Forces the git push even if it results in a non-fast-forward merge. Do not use the --force flag unless you’re absolutely sure you know what you’re doing.
git push `remote` --all 		Push all of your local branches to the specified remote.
git push `remote` --tags 		Tags aren’t automatically pushed when you push a branch or use the --all flag. The --tags flag sends all of your local tags to the remote repo.



To connect your local repository to your distant repo, you will need to set a remote for your repository and push your commits to it.
git remote add origin https://github.com/username/Hello-World.git   # Creates a remote named "origin" pointing at your GitHub repository
git push origin master												# Sends your commits in the "master" branch to GitHub

To create, view, and delete connections to other repositories. Remote connections are more like bookmarks rather than direct links into other repositories. 

SHOWING YOUR REMOTES

	git remote 			List defined remotes connections you have to other repositories. 
						Return 'origin' for cloned repository (the default name Git gives to the server you cloned from)
						You can have more than one remote for working with several collaborators

	git remote -v 		idem 'git remote' but include the URL of each connection.
	origin	https://github.com/schacon/ticgit (fetch)
	origin	https://github.com/schacon/ticgit (push)

	git remote show `RemoteName` 		Informations about a particular remote

ADDING REMOTE REPOSITORIES

	git remote add `name` `RemoteURL`
	Create a new connection to a remote repository. After adding a remote, you’ll be able to use `name` as a convenient shortcut for `RemoteURL` in other Git commands.

	git remote add origin https://github.com/joeblack				
	git remote add john http://dev.example.com/john.git
	git remote add origin https://github.com/userName/project.git
	This adds the location of your remote repository. Everything up until now has been on your local repository on your computer. You will need to go to your GitHub account and create a new remote repository where you will be able to push your local repository. After you created your remote repository you will be provided with a link and that link is the location you will want to use in the above command.

	git remote add origin `RemoteURL`
	Introduces local Git to remote repository (typically GitHub). Adds hooks for pull/push for syncing with remote source.

	git remote add `RemoteName` `RemoteURL` 		# Add the specified remote repo to your git config file
	git remote add origin https://github.com/guinetn/pook

	git remote add origin https://github.com/username/Hello-World.git  # Creates a remote named "origin" pointing at your GitHub repository
	git remote add upstream https://github.com/octocat/Spoon-Knife.git

REMOVING AND RENAMING REMOTES
	
	git remote rm `name`
		Remove the connection to the remote repository called `name`.

	git remote rename `old-name` `new-name`
