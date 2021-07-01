## GIT REMOTE REPOSITORY

Remotes are specialized URLs Git can send our code to. 2 types: HTTPS and SSH
Working with remote repositories is one of the primary features of Git, you can push or pull typically via SSH, though a lightweight daemon is also provided

origin		default upstream repository

## REMOTES
Instead to use complex full URLs to specify other repositories as a source or destination for Git commands a shorthand solution called "remotes":
Bookmarks of other repository locations are called remotes.

If a local repository was cloned from another Git source, an “origin” remote will already be present

git remote -v  					View addresses of your configured remotes

git remote add `remote name` `remote address`
git remote add `name` `url` 	Create a new connection to a remote repo. After adding a remote, you can use `name` as a shortcut for `url` in other commands.
git fetch `remote` `branch` 	Fetches a specific `branch`, from the repo. Leave off `branch` to fetch all remote refs.
git pull `remote` 				Fetch the specified remote’s copy of current branch and immediately merge it into the local copy.
git push `remote` `branch` 		Push the branch to `remote`, along with necessary commits and objects. Creates named branch in the remote repo if it doesn’t exist.
git push `remote` --force 		Forces the git push even if it results in a non-fast-forward merge. Do not use the --force flag unless you’re absolutely sure you know what you’re doing.
git push `remote` --all 		Push all of your local branches to the specified remote.
git push `remote` --tags 		Tags aren’t automatically pushed when you push a branch or use the --all flag. The --tags flag sends all of your local tags to the remote repo.

To point your local repository to the remote repository
`git remote add origin [repository url]

To push all the code from the local repository into the remote repository
`git push -u origin master

To pull the latest changes from the remote repository into the local repository
`git pull origin master


## To get a remote

1. create a repository on github.com 

2. add the remote
git remote add origin htttps://github.com/[your username]/[you folder].git

3. list out all of the remotes attached to your repo locally
git remote -v
origin	htttps://github.com/[your username]/studious-gator.git (fetch)
origin	htttps://github.com/[your username]/studious-gator.git (push)
In this case, we have permission for downloading code (fetching) and uploading code (pushing) for our github repository.

4. git push -u origin master
origin: standard common name to give to the primary remote in a repo
master: name of the branch
-u tells Git to create the branch master on origin if it doesn’t exist


download.page(code/repos/git/push.md)
download.page(code/repos/git/pull.md)
download.page(code/repos/git/fetch.md)
download.page(code/repos/git/_git_pull_request.md)


## COLLABORATING

Git’s collaboration model, which gives every developer their own copy of the repository, complete with its own local history and branch structure.
Publish local history by "pushing" branches to other repositories
See what others have contributed by "pulling" branches into your local repository.
Developers need to manually pull upstream commits into their local repository or manually push their local commits back up to the central repository

“git push” 		
“git pull” 		get me all the changes made by other team members and checked into our master repository.

pull       Fetch from and integrate with another repository or a local branch
fetch      Download objects and refs from another repository
push       Show your changes to the world. Update remote refs along with associated objects

REMOTE REPOSITORY
A repository stored on another computer
Hosted versions of your project on the Internet or network somewhere
Allow collaboration on any Git project
'origin' is the standard name to the remote that points to your main offsite repository

Remote repository URLs
Git supports many ways to reference a remote repository
. http://host/path/to/repo.git
. ssh://user@host/path/to/repo.git
	You’ll need a valid SSH account on the host machine
. teammates public repo: http://dev.example.com/john.git

set up two remote repo URLs for one local git repo.
	Sometimes I need to push before I can test, so I may push quite often. I don’t want to have too many tiny git pushes or too many push notifications for everyone. So what I usually do?
	(Warning: this may not be a good practice for some projects, in terms of code security.)
	Set up two remote repos for one local git repo. Keep pushing to one remote repo. Once it’s fully tested, push to the official repo once.

	$ git clone git@github.com:devops/denny-repo.git
	$ git config remote.myremote.url git@bitbucket.org:devops/denny-repo.git
	$ git config remote.origin.url git@github.com:devops/denny-repo.git
	$ cat .git/config
	$ git push origin master # origin points to github
	$ git push bitbucket master # myremote points to bitbucket

REMOTE BRANCHES

pointers to the state of branches in your remote repositories
bookmarks to remind you where the branches on your remote repositories were the last time you connected to them
(remote)/(branch)
origin/master origin/myWork

represent commits from somebody else’s repository. You can check out a remote branch just like a local one,
but this puts you in a detached HEAD state (just like checking out an old commit). You can think of them as
read-only branches.
Remote branches are prefixed by the remote they belong to so that you don’t mix them up with local branches

git branch -r       To view your remote branches

## origin/master
## origin/develop
## origin/some-feature

Are prefixed by the remote they belong to so that you don’t mix them up with local branches

• Inspect these branches with the usual git checkout and git log commands. 
• If you approve the changes a remote branch contains, you can merge it into a local branch with a normal git merge

synchronizing your local repository with a remote repository is actually a two-step process: fetch, then merge. The git pull command is a convenient shortcut for this process.

The 'origin' Remote
origin 
	the standard name to the remote that points to your main offsite repository
	default upstream repository
When you clone a repository with git clone, it automatically creates a remote connection called origin pointing back to the cloned repository. This is useful for developers creating a local copy of a central repository, since it provides an easy way to pull upstream changes or publish local commits. This behavior is also why most Git-based projects call their central repository origin


