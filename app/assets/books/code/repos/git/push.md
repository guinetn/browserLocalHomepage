## git push

Transfer commits from your local repository to a remote repo.
Exports commits to remote branches


A typical Git workflow would be to perform multiple small commits as you complete a task and push to a remote at relevant points, such as when the task is complete, to ensure synchronisation of the code within the team.

To connect your local repository to your distant repo, you will need to set a remote for your repository and push your commits to it.
git remote add origin https://github.com/username/Hello-World.git   # Creates a remote named "origin" pointing at your GitHub repository
git push origin master												# Sends your commits in the 'master' branch on origin

When everything you have done has been in your local repository you can transfer commits from your local repository to a remote repo. 
Exports commits to remote branches (can overwrite changes)


git push -u origin master 		This will push your local repository to your remote repository. 
								This command only needs to be written like this when you do it for the first time.
git push     					This is what you will use to push your code to GitHub after your initial push.
git pull 						Pull the latest version from the remote repository and update your local version so you can work with the latest updates as their changes enter the codebase.


git push 	Push to default remote

git push `RemoteName` `branch_to_push`
	Push the specified branch to `remote`, along with all of the necessary commits and internal objects. This creates a local branch in the destination repository.

	git push origin master		# Sends your commits in the 'master' branch on origin

git push `remotename` --force
	Same as the above command, but force the push even if it results in a non-fast-forward merge. Do not use the --force flag unless you’re absolutely sure you know what you’re doing.

git push `remotename` --all
	Push all of your local branches to the specified remote.

git push `remotename` --tags
	Tags are not automatically pushed when you push a branch or use the --all option. The --tags flag sends all of your local tags to the remote repository.

git push --set-upstream origin master
git push -u origin master
	Pushes local repository changes to a remote master branch in a linked repository (GitHub). Syncs remote with local.
	-u push sets GitHub as the upstream repository, which means we’ll be able to download any changes automatically when we run git pull
	Counting objects: 6, done.
	Delta compression using up to 4 threads.
	Compressing objects: 100% (4/4), done.
	Writing objects: 100% (6/6), 607 bytes | 0 bytes/s, done.
	Total 6 (delta 1), reused 0 (delta 0)
	remote: Resolving deltas: 100% (1/1), done.
	Branch master set up to track remote branch master from origin.
	To https://github.com/guinetn/tstgit
		* [new branch]      master -` master



PUSH - Pushing to Your Remotes
Update local cloned repo by fetching from the server
git pull origin master
git checkout ...
git commit -m "..."
git push -u `remote_name` `local_branch_name`    
-u option to git push sets GitHub as the upstream repository, which means we’ll be able to download any changes automatically when we run git pull
git push [remote-name] [branch-name] [tagname]
git push origin master
git push origin v1.5 			By default, the git push command doesn’t transfer tags to remote servers.
git push origin --tags 			Transfer all of your tags to the remote server that are not already there.


