git pull
				
Fetch + Merge upstream changes into your local repository 
an easy way to synchronize your local repository with upstream changes

git pull `RemoteName`
	= git fetch `remote` + git merge origin/`current-branch`
	Fetch the specified remote’s copy of the current branch and immediately merge it into the local copy

	git pull origin master
		Pulls down a master/named branch from a linked remote repository to a local working directory. Syncs local with remote.

git pull --rebase `RemoteName`
	Perform a git fetch followed by a git rebase
	Same as the above command, but instead of using git merge to integrate the remote branch with the local one, use git rebase.

	4 WAYS TO AVOID MERGE COMMITS IN GIT 

	https://stackoverflow.com/questions/18529206/when-do-i-need-to-do-git-pull-before-or-after-git-add-git-commit

	avoid "Merge branch 'master' of github.com:xxx/ProjectYYY"

	git pull --rebase What’s happening here? Git will rewind (undo) all of your local commits, pull down the remote commits then replay your local commits on top of the newly pulled remote commits. If any conflicts arise that git can’t handle you’ll be given the opportunity to manually merge the commits then simply run git rebase --continue to carry on replaying your local commits.

	Tell git to always rebase when pulling, to do this on a project level add this to your .git/config file:
	[branch “master”]
		rebase = true
	Or do it all on the command line with git config branch.master.rebase true

	Add a global config option to always rebase when pulling
	[branch]
		autosetuprebase = always
	Or again do it all on the command line with git config --global branch.autosetuprebase always

	And the final way, which is what I personally use, in ~/.gitconfig
	[alias]
		pl = pull —rebase



HOW TO SYNCHRONIZE WITH THE CENTRAL REPOSITORY'S MASTER BRANCH
git checkout master
git pull --rebase origin
This moves your local changes onto the top of what everybody else has already contributed.

PULLING VIA REBASE
The --rebase option can be used to ensure a linear history by preventing unnecessary merge commits. Many developers prefer rebasing over merging, since it’s like saying, "I want to put my changes on top of what everybody else has done." 

git config --global branch.autosetuprebase always
All git pull commands will integrate via git rebase instead of git merge
