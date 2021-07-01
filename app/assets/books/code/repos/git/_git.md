# GIT - Social Coding 

Version control system in both local and distributed environments tracing changes occurring in a project's files. They can be recalled or reviewed later. 
Git was born out of the Linux Kernel Community’s frustrations with available VCSs. Linus Torvald’s original authorship.

Git works local, commit-often, publish-when-you-can methodology. No requirement for a server, retains full history on the user’s machine, and can quickly
be setup to publish and act as a Distributed Version Control System

At the core of Open Source  

Git: a collection of files grouped in units called 'commits' (Snapshots of altered files, NOT DIFFERENCES)
The collection origin can be a remote folder (on a server) or a local folder
You can create parallel commits (branches). 
HEAD is a pointer to the current branch

* Git store snapshots of files in a local database, it doesn't store differences
* Integrity of snapshots is check thankfully hash when pushing 
* You can work offline by accumulating your commits in local repo: Git doesn’t force you to interact with the central repository until you’re ready
* Git is not for large files (media, images): use dropbox, youtube... see GIT LFS (Large File Storage)

* Git is not diff-based, it is object-based.
* Git does not apply diffs to show you a version of your project
* Git does traverse object trees to show you a version of your project
* Git does use diffs to minimize disk space for its objects


Git stores files content in objects called 'blobs"
Folders turn into objects calles 'trees' containing other 'trees' (subfolders) and 'blobs'
A commit is a type of object containing a 'tree'. Once created objects cannot change

Git is a free and open source DVCS (DISTRIBUTED VERSION CONTROL SYSTEM)	started in 2005
Written in C which means there is a unique distribution for each supported platform.
	
A tool for storing the history of a collection of files 
Miniature filesystem like (every commit takes a picture of what ALL your files). A stream of snapshots
Everything in Git is check-summed before it is stored and is then referred to by that checksum (SHA-1, a 40 hexadecimal chars string), and not by file name

Git stores a series of snapshots (Git is a mini filesystem) AND NOT A SERIES OF CHANGESETS OR DIFFERENCES.
Other systems (CVS, Subversion, Perforce) store changes made to each file over time.
Git store data as a stream of snapshots
Commit / Save your project --`  Takes a picture of what ALL your files look like and stores a reference to that snapshot.
								FILE NOT CHANGED ? --` GIT DOESN’T STORE THE FILE AGAIN—JUST A LINK TO THE PREVIOUS IDENTICAL FILE IT HAS ALREADY STORED
								Other CVS systems tend to store data as changes to a base version of each file.

Nearly Every Operation Is Local
	you have the entire history of the project right there on your local disk, most operations seem almost instantaneous
	There is very little you can’t do if you’re offline or off VPN.
	You can commit happily until you get to a network connection to upload.  In many other systems, doing so is either impossible or painful.
	in Subversion and CVS, you can edit files, but you can’t commit changes to your database (because your database is offline).

Git Has Integrity
	At low level. Everything in Git is check-summed (SHA-1 hash: a 40 chars hexa string calculated based on the contents of a file or directory)
	You can’t lose information in transit or get file corruption without Git being able to detect it.
	Git stores everything not by file name but by hash value
													↓
													SHA-1 check summed (a 40-hexadecimal characters string) calculated based on the contents of a file or directory structure in Git
													24b9da6552252987aa493b52f8696cd6d3b00373

## COMMIT HASHES & SHORTHAND

Commits are marked with a SHA–1 hash that is unique to the user committing the changes, the folders containing changed files, and the modified files comprising the changeset.
This allows commits to be made independent of any central coordinating server(rather than a sequential revision ID)

A full SHA–1 hash is 40 hex characters: 64de179becc3ed324daab72f7238df1404723672

Navigate the history of hashes

- any unique sub-portion of the hash can be used (in most cases, 4–5 characters are sufficient)
- using symbolic shorthand notation
HEAD Last commit
HEAD^ One commit ago
HEAD^^ Two commits ago
HEAD~1 One commit ago
HEAD~3 Three commits ago

git diff HEAD~2
git checkout HEAD^^ 
git merge RELEASE–2.1

## TERMS

Repository/repo 
	is a collection of all the changes made to your project over time and will build a history of these changes)
	a place for storing things. With Git, this means your code folder

Branch 		Branche
Commit 		Valider
Merge 		Fusionner
Stash 		Remiser
Discard 	Rejeter
Fetch 		Rapatrier
Pull 		Récupérer
Tag 		Etiquette
Push 		Envoyer

Fork
	Creating a fork is producing a personal copy of someone else's project. 
	Forks act as a sort of bridge between the original repository and your personal copy. You can submit Pull Requests to help make other people's projects better by offering your changes up to the original project. 
	Forking is at the core of social coding at GitHub.

COMMIT: "snapshot of your code" 
			An action to save the current state — such that one can revisit this state if needed

BRANCH 	Parallel commits
	A branch in Git is a lightweight movable pointer to one of these commits. 
	The default branch name in Git is master.
			
	- Master (main) branch
	- Develop branch
	- Feature branch (topic branch)
	- Hot fix branch
	- Release branch

	master : default development branch		
	HEAD : current branch (Pointer to the current branch)
	HEAD^ : parent of HEAD
	HEAD~2 : the grandparent of HEAD
	HEAD~4 : the great-great grandparent of HEAD

REMOTE	
	A repository that isn’t local. Can be in another folder or in the cloud (for example: Github): helps other people to easily collaborate
	origin : default upstream repository


download.page(code/repos/git/_git_install.md)
download.page(code/repos/git/_git_configuration.md)
download.page(code/repos/git/_git_security.md)

download.page(code/repos/git/_git_repo.md)

download.page(code/repos/git/_git_basics.md)

download.page(code/repos/git/_git_branches.md)
download.page(code/repos/git/_git_remotes.md)

download.page(code/repos/git/_git_workflow.md)

download.page(code/repos/git/_git_repo.md)

download.page(code/repos/git/_git_commands.md)

download.page(code/repos/git/archive.md)

download.page(code/repos/git/_git_best_practices.md)
download.page(code/repos/git/_git_github.md)
download.page(code/repos/git/_git_gitlab.md)
download.page(code/repos/git/_git_bash.md)
download.page(code/repos/git/_git_hooks.md)
download.page(code/repos/git/_git_submodules.md)
download.page(code/repos/git/_git_lfs.md)

download.page(code/repos/git/_git_internals.md)
download.page(code/repos/git/_git_ops_.md)

## TOOLS

[Scan your repos for secrets with GitGuardian](https://dashboard.gitguardian.com)

gitk    git commit viewer. diagram visualization of the project’s commit history and branching

worktree	
	https://git-scm.com/docs/git-worktree
	Manage multiple working trees attached to the same repository.
	A git repository can support multiple working trees, allowing you to check out more than one branch at a time.
	allows you to have multiple branches of the same local repository to be checked out in different directories
	
	rm -rf public
	git worktree add -B gh-pages public upstream/gh-pages
	`More on https://gohugo.io/hosting-and-deployment/hosting-on-github`


## ESLINT issue

	Expected linebreaks to be 'LF' but found 'CRLF'  linebreak-style
	https://help.github.com/articles/dealing-with-line-endings/
	http://stackoverflow.com/questions/1967370/git-replacing-lf-with-crlf

	:: git error :: fatal: CRLF will be replaced by LF in `some file in the repo`
	SublimeText: select View`Line Endings`Unix
	https://github.com/titoBouzout/LineEndings    LineEndings for Sublime Text repo

	git config core.autocrlf command is used to change how Git handles line endings
	# that command will print "true" or "false" or "input"

	git config --global core.autocrlf true
	# Configure Git on Windows to properly handle line endings

	    -  autocrlf = true    if you have unix-style lf in one of your files (= RARELY),
	    -  autocrlf = input   if you have win-style crlf in one of your files (= almost ALWAYS),
	    -  autocrlf = false   - NEVER!

	Windows    "\r\n" for (CRLF)
	Linux      "\n" (for LF) 

	linebreak-style rule configure as below either in your .eslintrc or in source code:
	/*eslint linebreak-style: ["error", "unix"]*/
	Since you're working on Windows, you may want to use this rule instead:
	/*eslint linebreak-style: ["error", "windows"]*/


## MORE

- https://git-scm.com                download git
- https://git-scm.com/blog
- https://git-scm.com/doc
- https://github.com/
- [Merge vs rebase](https://www.youtube.com/watch?v=CRlGDDprdOQ)
- http://blog.nodejitsu.com/package-dependencies-done-right/		
- http://channel9.msdn.com/Series/NET-Framework/Git-Training-for-the-NET-Team
- http://cheat.errtheblog.com/s/git
- http://dundalek.com/interactive-git-cheat-sheet/
- http://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- http://git-scm.com/downloads
- http://gitexplorer.com/
- http://gitimmersion.com/
- http://kushagragour.in/blog/2014/01/build-git-learn-git/
- http://marklodato.github.io/visual-git-guide/index-en.html
- http://mherman.org/blog/2013/10/11/basic-git-commands/#.Vpqt-xXhCHs
- http://nbviewer.jupyter.org/github/demotu/BMC/blob/master/notebooks/VersionControlGitGitHub.ipynb
- http://nbviewer.jupyter.org/github/demotu/BMC/blob/master/notebooks/VersionControlGitGitHub.ipynb
- http://nvie.com/posts/a-successful-git-branching-model/
- http://ohshitgit.com/
- http://socketnodeci.azurewebsites.net/
- http://visualstudiomagazine.com/articles/2014/04/01/source-code-control-with-git-and-mercurial.aspx
- http://www.mikestreety.co.uk/blog/ignoring-libraries-in-git
- https://alm.developpez.com/faq/git/ 
- https://atom.io 		The github editor
- https://backlogtool.com/git-guide/en/stepup/stepup2_6.html
- https://dev.to/codetraveling/how-to-manage-multiple-github-accounts-on-your-local-machine-3gj0
- https://dev.to/gcdcoder/git-tricks-285p
- https://dzone.com/articles/8-useful-but-not-well-known-git-concepts?edition=374212
- https://dzone.com/articles/reset-checkout-and-revert
- https://github.com/30-seconds/30-seconds-of-code
- https://github.com/explore/Book progit-en.1084.pdf
- https://github.com/fer/dotfiles/wiki/git
- https://github.com/integrations
- https://github.com/mmorejon/gitignore   A collection of useful .gitignore templates
- https://github.com/mrdoob/three.js/wiki/A-Contributor's-Guide-to-the-Git-Galaxy
- https://github.com/taniarascia/dotfiles/blob/master/.gitconfig
- https://github.com/taniarascia/git
- https://help.github.com/articles/generating-ssh-keys
- https://medium.com/@gohberg/the-biggest-misconception-about-git-b2f87d97ed52
- https://medium.com/pragmatic-programmers/managing-files-with-git-5272e699b9cf
- https://medium.freecodecamp.org/a-developers-introduction-to-github-1034fa55c0db
- https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826
- https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369
- https://ndpsoftware.com/git-cheatsheet.html#loc=index;
- https://ohmygit.org/
- https://the-awesome-git-cheat-sheet.com/
- https://try.github.io/levels/1/challenges/1 					Got 15 minutes and want to learn Git?
- https://www.atlassian.com/git/tutorial/git-basics
- https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud
- https://www.atlassian.com/git/tutorials/undoing-changes/git-clean
- https://www.git-tower.com/blog/git-cheat-sheet/
- https://www.kernel.org/pub/software/scm/git/docs/user-manual.html#repositories-and-branches
- https://www.quora.com/What-is-the-best-Git-cheat-sheet
- https://www.red-gate.com/simple-talk/sysadmin/devops/git-anatomy/
- https://www.slideshare.net/slideshow/embed_code/39694335#
- https://dzone.com/articles/reset-checkout-and-revert
- https://www.mattjennings.net/git/revert-previous-commit-locally
- https://medium.com/free-code-camp/how-to-use-git-efficiently-54320a236369
- https://www.techwatching.dev/gitcheatsheet   to add

## SUBVERSION ←→ GIT

git svn clone --stdlayout `svn-repo-url`   convert to a Git repository a local working copy of a Subversion repository that uses the traditional structure (trunk, tags, branches)