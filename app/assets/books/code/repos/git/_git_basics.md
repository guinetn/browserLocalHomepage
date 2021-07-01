# GIT BASICS

## Clone an existing repository

git clone ssh://you@host.org/project.git
git clone git://host.org/project.git
git clone ..\existing\repo \new_repo

## Create a new local git repository
```vb
git init
git add .
git commit –m "First commit"
git commit --amend                  If you made a mistake in the message for your last commit, you can edit the text (while leaving the changed file(s) untouched)
```

## Github clone
Sign on GitHub
“Create a new” repo button to initialize a repository within your GitHub account
Supply the Repository name field, and click “Create repository”.
git clone git@github.com:githubtrainer/hellogitworld.git 		Mirrors the repo on GitHub
The new local repo is preconfigured with Git remote "bookmark" for synchronizing code between local and GitHub repositories.

## Create a new repository

```vb
mkdir my_repo && cd my_repo
echo "# my project" `` README.md
git init                                                Creates a local hidden .git repository directory in your project. 

git add README.md                                       Add readme.md file in your new local repository. This stages them for the first commit
git commit -m 'First commit'                            Commit the files that you’ve staged in your local repository. 

git add .                                               Add all changes (from root path of the project). Add all the files in your new local repository. This stages them for the first commit
                                                        Track New Files. file go to the stagged area
                                                        Take a snapshot of the contents of all files under the current directory 
	                                                    This snapshot is now stored in a temporary staging area which Git calls the "index". 
	                                                    Used both for new and newly modified files, 
git add -A

git commit -am "Add a README file"                      Permanently store the contents of the index in the repository 
git commit -a 	                                        Commits changes only to files that Git is already tracking and have been modified

git remote add origin YOUR_GITHUB_REPOSITORY_URL        Add the URL for the remote repository where your local repository will be pushed.
git remote add origin https://github.com/guinetn/project1.git
git remote -v 											Check

git push -u origin master                               Push the changes in your local repository to GitHub  
           \___ Set upstream 
                First occurrence of git push included 
                * the “set upstream” option -u
                * the destination origin
                * master
                Once set up, omit all those details and just 'git push'
                Download any changes automatically when we run 'git pull'
				
			origin is the default upstream repository			
			-u push sets GitHub as the upstream repository, which means we’ll be able to download any changes automatically when we run git pull
			The first occurrence of git push included the “set upstream” option -u, the destination origin, and master
			But once these are set up we can omit all those details and just push, like this: git push 		download any changes automatically when we run git pull
```

## Create a new repository 
```vb
echo "# guinetn.github.io" `` README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
        \___ git branch -m master main    Renaming: master → main

        error: refname refs/heads/master not found
        fatal: Branch rename failed
            \___ Fix: git add readme.md + git commit -m "first commit"
git remote add origin https://github.com/guinetn/guinetn.github.io.git
git push -u origin main


gitk 							★★★  git commit viewer
git diff 						difference last commit / unstaged changes (what is changed but not staged)
git diff --staged 				diff of what is staged but not yet committed
git diff master
git difftool --tool-help       	to see what is available on your system.

git log 						show the commit history for the currently active branch
git log -p 						see complete diffs at each step
git log --stat --summary 		overview of the changes is useful to get a feel of each step
git log branchB..branchA 		show the commits on branchA that are not on branchB
git log --follow[file] 			show the commits that changed file, evn accross renames
git show [SHA] 					show any object in Git in human-readable format
```    

## Push an existing repository
git remote add origin https://github.com/guinetn/guinetn.git
git branch -M main		
git push -u origin main
	







cmd.exe
cd c:\temp
mkdir gatsby_try  	
mkdir my_repo && cd my_repo
cd gatsby_try
echo "# test" `` README.md

git clone [url]

git init 		create hidden \.git folder
git add . 		Add all changes (from root path of the project).
				Track New Files. file go to the stagged area
				Take a snapshot of the contents of all files under the current directory 
	            This snapshot is now stored in a temporary staging area which Git calls the "index". 
	            Used both for new and newly modified files, 
git status
git commit      Permanently store the contents of the index in the repository 
git commit -m "first"
git remote add origin https://github.com/guinetn/gatsby_try.git
git push -u origin master -----→ deprecated, see below
								 git branch -m master main    Renaming: master → main
git push -u origin main   -----→ 'main' from the 01/10/2020 in Github & GitLab
		  \    \      \___ master: name of the target branch 
		   \    \___ origin: standard common name to give to the PRIMARY remote in a repo
		    \
		     \__ Set upstream 
			 	 First occurrence of git push included 
			 	 	* the “set upstream” option -u
			 	 	* the destination origin
			 	 	* master
			 	 Once these are set up we can omit all those details and just push with 'git push'
			 	 Download any changes automatically when we run git pull
		         
		         create the branch master on origin if it doesn’t exist
				 sets GitHub as the upstream repository: means you can download any changes automatically (git pull)
	
git status                by itself commits changes only to files Git is already tracking and have been modified
git add .                 .....so add . `- 
git commit -m "my second commit"    
git push

git commit -am "Add a README file"   = ???

git log -n 2

gitk    						git commit viewer ***
git diff 						difference last commit / unstaged changes (what is changed but not staged)
git diff --staged 				diff of what is staged but not yet committed
git diff master
git difftool --tool-help       	to see what is available on your system.

git log 						Viewing the current branch’s all commits history: author and message
git log --pretty=oneline 		One line per commit
git log -p 						Display the full diff of each commit.
git log -p -2 					shows the difference introduced in each commit at level 2...
git log --stat
git log --pretty=format:"%h %an %ar - %s"
git log --pretty=format:"%h %s" --graph
git log --since=2.weeks

git log branchB..branchA 		show the commits on branchA that are not on branchB
git log --follow [file] 		show the commits that changed file, even across renames
git diff branchB...branchA 		show the diff of what is in branchA that is not in branchB
git show [SHA] 					show any object in Git in human-readable format

git branch experimental
git branch   				

git rm --cached -r .           Remove every file from Git's index.
git reset [file]               Unstage a file while retaining the changes in working directory

git revert `commit`    	Create new commit that undoes all of the changes made in `commit`, then apply it 
	                    to the current branch.
git reset 			 	Reset staging area to match most recent commit, but leave the working directory unchanged.
						ONLY THE STAGING (previous changes you plan to push) ! Not current modified files !
git reset --hard 		Reset staging area and working directory to match most recent commit and 
						overwrites all changes in the working directory.
 						Rewrite the Git index. (if a commit is not pushed, use the syntax --hard `commit`)
git reset `commit`      Move the current branch tip backward to `commit`, reset the staging area to match, 
	                    but leave the working directory alone.
git reset --hard `commit`  Same as previous, but resets both the staging area & working directory to match. 
	                       Deletes uncommitted changes, and all commits after `commit`.
git tag -l
git tag v1.4-lightweight-tag
git tag -a v1.4-annotated-tag -m "my annotation message"
git tag -a v1.2 9fceb02			Tagging later	

git show TagName 					Print information about a specific tag to the console window

To impact working directory
	
	git reset --hard `commit`
	git checkout `file` 			to discard changes in working directory
	git checkout -f 				checkout head ?

	  	git checkout ... 	Check out a particular branch or a tagged version of the code to hack on
	  						git checkout -f 		undo changes: check out HEAD
	  						works only with files that are staged for commit or are already part of the repository, but sometimes you want to get rid of new files as well. 
	  						Using touch, create a file with a name of your choice, then git add it. 
	  						Verify that running git checkout -f gets rid of it.

Tags are not pushed by defaut, explicitly push tags
git push origin v1.4            
git push --tags 				  push tags to a remote repository
git push origin --tags            transfer all of your tags to the remote server that are not already there

git checkout v2.0.0 				Checking out Tags = detached HEAD
									Any new commit won’t belong to any branch and will be unreachable, except by the exact commit hash.
git checkout -b version2 v2.0.0   To make changes(say you’re fixing a bug on an older version)


## CONTRIBUTING

git checkout -b my-work origin/master

Then do the required changes
git add --all 			stage them for commit
git status 				show which changes will be committed
git commit 				commit those changes


https://github.com/jupyter/notebook/issues/2379

I just submitted a PR that should fix this for both French and German keyboards. 
Since I have an English keyboard, I can't test myself, so I need someone here to help test.

git fetch jupyter pull/2535/head:pr/2535
git checkout pr/2535
npm run build










## If you’re starting to track an existing project in Git, you need to go to the project’s directory and type:

```sh
$ git init
```
## This creates a new subdirectory named .git that contains all of your necessary repository files — a Git repository skeleton. At this point, nothing in your project is tracked yet.

## To start version-controlling existing files you should start by tracking those files and do an initial commit. To accomplish that you should start with a few  `$ git add` that specifies the files you want to track followed by a commit.

```sh
$ git add `file`
$ git add README
$ git commit -m 'Initial project version'
```
#### Checking the status of your files

## The main tool you use to determine which files are in which state is the `$ git status` command. If you run this command directly after a clone, you should see something like this:

```sh
$ git status
## On branch master
nothing to commit (working directory clean)
```

## If you add a new file to your project, and the file didn't exist before, when you run a `$ git status` you should see your untracked file like this:

```sh
$ git status
## On branch master
## Untracked files:
##   (use "git add `file`..." to include in what will be committed)
#
##   README
nothing added to commit but untracked files present (use "git add" to track)
```

#### Staging files

## After initializing a git repository in the chosen directory, all files will now be tracked. Any changes made to any file will be shown after a `$ git status` as changes not staged for commit.

## To stage changes for commit you need to add the file(s) - or in other words, stage file(s).

```sh
## Adding a file
$ git add filename

## Adding all files
$ git add -A

## Adding all files changes in a directory
$ git add .

## Choosing what changes to add (this will got through all your changes and you can 'Y' or 'N' the changes)
$ git add -p
```

#### Stashing files

## Git stash is a very useful command, where git will 'hide' the changes on a dirty directory - but no worries you can re-apply them later. The command will save your local changes away and revert the working directory to match the HEAD commit.

```sh
## Stash local changes
$ git stash

## Stash local changes with a custom message
$ git stash save "this is your custom message"

## Re-apply the changes you saved in your latest stash
$ git stash apply

## Re-apply the changes you saved in a given stash number
$ git stash apply stash@{stash_number}

## Drops any stash by its number
$ git stash drop stash@{0}

## Apply the stash and then immediately drop it from your stack
$ git stash pop

## 'Release' a particular stash from your list of stashes
$ git stash pop stash@{stash_number}

## List all stashes
$ git stash list

## Show the latest stash changes
$ git stash show

## See diff details of a given stash number
$ git diff stash@{0}
```

#### Committing files

## After adding/staging a file, the next step is to commit staged file(s)

```sh
## Commit staged file(s)
$ git commit -m 'commit message'

## Add file and commit
$ git commit filename -m 'commit message'

## Add file and commit staged file
$ git commit -am 'insert commit message'

## Amending a commit
$ git commit --amend 'new commit message' or no message to maintain previous message

## Squashing commits together
$ git rebase -i
## This will give you an interface on your core editor:
## Commands:
##  p, pick = use commit
##  r, reword = use commit, but edit the commit message
##  e, edit = use commit, but stop for amending
##  s, squash = use commit, but meld into previous commit
##  f, fixup = like "squash", but discard this commit's log message
##  x, exec = run command (the rest of the line) using shell

## Squashing commits together using reset --soft
$ git reset --soft HEAD~number_of_commits
$ git commit
** WARNING: this will require force pushing commits, which is OK if this is on a branch before you push to master or create a Pull Request.
```

#### Branching and merging

```sh
## Creating a local branch
$ git checkout -b branchname

## Switching between 2 branches (in fact, this would work on terminal as well to switch between 2 directories - $ cd -)
$ git checkout -

## Pushing local branch to remote
$ git push -u origin branchname

## Deleting a local branch - this won't let you delete a branch that hasn't been merged yet
$ git branch -d branchname

## Deleting a local branch - this WILL delete a branch even if it hasn't been merged yet!
$ git branch -D branchname

## Remove any remote refs you have locally that have been removed from your remote (you can substitute `origin` to any remote branch)
$ git remote prune origin

## Viewing all branches, including local and remote branches
$ git branch -a

## Viewing all branches that have been merged into your current branch, including local and remote
$ git branch -a --merged

## Viewing all branches that haven't been merged into your current branch, including local and remote
$ git branch -a --no-merged

## Viewing local branches
$ git branch

## Viewing remote branches
$ git branch -r

## Rebase master branch into local branch
$ git rebase origin/master

## Pushing local branch after rebasing master into local branch
$ git push origin +branchname
```

#### Fetching and checking out remote branches

```sh
## This will fetch all the remote branches for you.
$ git fetch origin

## With the remote branches in hand, you now need to check out the branch you are interested in, giving you a local working copy:
$ git checkout -b test origin/test

## Deleting a remote branch
$ git branch -rd origin/branchname
$ git push origin --delete branchname  or  $ git push origin:branchname
```

#### Merging branch to trunk/master

```sh
## First checkout trunk/master
$ git checkout trunk/master

## Now merge branch to trunk/master
$ git merge branchname

## To cancel a merge
$ git merge --abort
```

#### Updating a local repository with changes from a Github repository

```sh
$ git pull origin master
```

#### Tracking existing branch

```sh
$ git branch --set-upstream-to=origin/foo foo
```

#### Resetting

```sh
## Mixes your head with a give sha
## This lets you do things like split a commit
$ git reset --mixed [sha]

## Upstream master
$ git reset HEAD origin/master -- filename

## The version from the most recent commit
$ git reset HEAD -- filename

## The version before the most recent commit
$ git reset HEAD^ -- filename

## Move head to specific commit
$ git reset --hard sha

## Reset the staging area and the working directory to match the most recent commit. In addition to unstaging changes, the --hard flag tells Git to overwrite all changes in the working directory, too.
$ git reset --hard
```

#### Git remote

```sh
## Show where 'origin' is pointing to and also tracked branches
$ git remote show origin

## Show where 'origin' is pointing to
$ git remote -v

## Change the 'origin' remote's URL
$ git remote set-url origin https://github.com/user/repo.git

## Add a new 'origin'
## Usually use to 'rebase' from forks
$ git remote add [NAME] https://github.com/user/fork-repo.git
```

#### Git grep

```sh
## 'Searches' for parts of strings in a directory
$ git grep 'something'

## 'Searches' for parts of strings in a directory and the -n prints out the line numbers where git has found matches
$ git grep -n 'something'

## 'Searches' for parts of string in a context (some lines before and some after the grepped term)
$ git grep -C`number of lines` 'something'

## 'Searches' for parts of string and also shows lines BEFORE the grepped term
$ git grep -B`number of lines` 'something'

## 'Searches' for parts of string and also shows lines AFTER the grepped term
$ git grep -A`number of lines` 'something'
```

#### Git blame

```sh
## Show alteration history of a file with the name of the author
$ git blame [filename]

## Show alteration history of a file with the name of the author && SHA
$ git blame [filename] -l
```

#### Git log

```sh
## Show a list of all commits in a repository. This command shows everything about a commit, such as commit ID, author, date and commit message.
$ git log

## List of commits showing commit messages and changes
$ git log -p

## List of commits with the particular expression you are looking for
$ git log -S 'something'

## List of commits by author
$ git log --author 'Author Name'

## Show a list of commits in a repository in a more summarised way. This shows a shorter version of the commit ID and the commit message.
$ git log --oneline

## Show a list of commits in a repository since yesterday
$ git log --since=yesterday

## Shows log by author and searching for specific term inside the commit message
$ git log --grep "term" --author "name"
```

#### Checking what you are committing

```sh
## See all (non-staged) changes done to a local repo
$ git diff

## See all (staged) changes done to a local repo
$ git diff --cached

## Check what the changes between the files you've committed and the live repo
$ git diff --stat origin/master
```

#### Useful commands

```sh
## Check if a sha is in production
$ git tag --contains [sha]

## Number of commits by author
$ git shortlog -s --author 'Author Name'

## List of authors and commits to a repository sorted alphabetically
$ git shortlog -s -n

## List of commit comments by author
$ git shortlog -n --author 'Author Name'
## This also shows the total number of commits by the author

## Number of commits by contributors
$ git shortlog -s -n

## Undo local changes to a File
$ git checkout -- filename

## Shows more detailed info about a commit
$ git cat-file sha -p

## Show number of lines added and removed from a repository by an author since some time in the past.
$ git log --author="Author name" --pretty=tformat: --numstat --since=month | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'
```

#### Useful alias
## To add an alias simply open your .gitconfig file on your home directory and include the alias code

```sh
## Shows the log in a more consisted way with the graph for branching and merging
lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)`%an`%Creset' --abbrev-commit
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push -u origin my-new-feature`
5. Submit a pull request - cheers!


## Project Sample

git init .
	
git status
	On branch master
	Initial commit
	nothing to commit (create/copy files and use "git add" to track)

npm init
	npm questions....	

git status
	On branch master
	Initial commit
	Untracked files:
	(use "git add <file>..." to include in what will be committed)
	package.json
	nothing added to commit but untracked files present (use "git add" to track)		

git add package.json	
git status		
	On branch master
	Initial commit
	Changes to be committed:
		(use "git rm --cached <file>..." to unstage)
		new file:   package.json

Make a change in package.json   ... the change is not stagged 
									= will not be into the next commit until i do 'git add package.json' again)
git status		
	On branch master
	Initial commit
	Changes to be committed:
		(use "git rm --cached <file>..." to unstage)
		new file:   package.json
	Changes not staged for commit:
		(use "git add <file>..." to update what will be committed)
		(use "git checkout -- <file>..." to discard changes in working directory)
		modified:   package.json

git commit -m "initial project version"
	[master (root-commit) e35ec42] initial project version
		1 file changed, 11 insertions(+)
		create mode 100644 package.json
git status
	On branch master
	Changes not staged for commit:
		(use "git add <file>..." to update what will be committed)
		(use "git checkout -- <file>..." to discard changes in working directory)
			modified:   package.json
	no changes added to commit (use "git add" and/or "git commit -a")

git tag v1.0.0
git add . 								Add all changes (from root path of the project)git add .
git status
	On branch master
	Changes to be committed:
	(use "git reset HEAD <file>..." to unstage)
		modified:   package.json

git commit -m "package.json has new author"
git status
	On branch master
	nothing to commit, working tree clean

git log 	print out all the commits which have been done up until now.    (to see the commit history)
	commit e57fe50266581f45877530d7e67e2b72a4b5b941
	Author: NGI5\nguin <me@me.com>
	Date:   Thu May 18 09:46:49 2017 +0200
		package.json has new author

	commit e35ec42d48807d0666646ba4cbf65febbaf103ac
	Author: NGI5\nguin <me@me.com>
	Date:   Thu May 18 09:36:57 2017 +0200
		initial project version

git log -p -2 	show diff.
	commit e57fe50266581f45877530d7e67e2b72a4b5b941
	Author: NGI5\nguin <me@me.com>
	Date:   Thu May 18 09:46:49 2017 +0200
		package.json has new author
	diff --git a/package.json b/package.json
	-  "author": "",
	+  "author": "ng",		
	...

	Bad idea...
	git checkout e35ec42d48807d0666646ba4cbf65febbaf103ac    go back in time and checkout your app from a previous commit
		Note: checking out 'e35ec42d48807d0666646ba4cbf65febbaf103ac'.

		You are in 'detached HEAD' state. You can look around, make experimental changes and commit them, and you can discard any commits you make in this state without impacting any branches by performing another checkout.If you want to create a new branch to retain commits you create, you may	do so (now or later) by using -b with the checkout command again. 
		
		git checkout -b <new-branch-name>
		HEAD is now at e35ec42... initial project version
		git checkout master 	to solve

Create a repo on github.com
	https://github.com/guinetn/tstgit.git

git remote add origin https://github.com/guinetn/tstgit    
git config -l
	...
	remote.origin.url=https://github.com/guinetn/tstgit
	remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
git remote -v
	origin  https://github.com/guinetn/tstgit2 (fetch)
	origin  https://github.com/guinetn/tstgit2 (push)

git push -u origin master    
-u push sets GitHub as the upstream repository, which means we’ll be able to download any changes automatically when we run git pull


	

echo 'My Project' > README
echo 'V 1.0.0-SNAPSHOT' >> README
git add README
git add . 						Add all changes (from root path of the project)
								Track New Files. file go to the stagged area

cat .gitignore  				Copy standard input to standard output.	
*.[oa] 							tells Git to ignore any files ending in “.o” or “.a”
*~ 								tells Git to ignore all files whose names end with a tilde (~), 

git diff 						difference between the last commit and unstaged changes
git diff master
git difftool --tool-help       	to see what is available on your system.

git log 						Viewing the commit history: author and message,
git log -p -2 					shows the difference introduced in each commit at level 2...
git log --stat
git log --pretty=format:"%h %an %ar - %s"
git log --pretty=format:"%h %s" --graph
git log --pretty=oneline
git log --since=2.weeks

