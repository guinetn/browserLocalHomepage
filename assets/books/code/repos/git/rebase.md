## git rebase

GIT FIX MISTAKES: amending commits & rebasing

- [Merge vs rebase](https://www.youtube.com/watch?v=CRlGDDprdOQ)

main 				m1  →  m2  → m3
						   ↓
feature 			       m2  →  f1  → f2

way 1
git merge feature 		will merge all changes + all commits of the feature branch (not a pb as git track how the project elvolve)

way 2
git merge --squash feature 		will merge all changes + all commitsof the feature branch (not a pb as git track how the project elvolve)
                                --squash allow to summarize all "feature" branch commits in one commit message:
git commit -m "feature and master merged"      must be added
main combined      m1  →  m2  → m3 → "feature and master merged"

way 3: rebase
git rebase master  			(done from feature branch)
First, rewiding head to replay your work on top of it...
Applying it...
git log
feature 			m1  →  m2  →  m3  →  f1  →  f2

1. git check last commit in the 2 branches

* Manage history: rebasing

https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826
Good practise: keep your local repository code up-to-date with the code in the remote repository. This avoids a lot of merge conflicts later when you raise a pull request
Every time you pull the code from the remote repository to the local repository a new merge commit is created in your local repository. This means that your local commit history is going to have a lot of merge commits which can make things look confusing to the reviewer.

to ensure the Feature branch gets the latest code from the Release branch.
Rebasing tries to add each commit, one by one, and checks for conflicts. 

Use rebase when you are updating your local code repository with the latest code from the remote repository. 
Use merge when you are dealing with pull requests to merge the Feature branch back with the Release or Master branch.
Rebase when the commit history is a mess
git checkout feature
git rebase release      this get the commits from the Release branch into your Feature branch

git rebase `source branch name`
git rebase `source branch name` `destination branch name`

Rebasing is the rewinding of existing commits on a branch with the intent of moving the branch start point forward, then replaying the rewound
commits. This allows developers to test their branch changes safely in isolation on their private branch just as if they were made on top of the
mainline code, including any recent mainline bug fixes.



git rebase -i `base`   		Interactively rebase current branch onto `base`. Launches editor to enter commands for how each commit will be transferred to the new base.
git pull --rebase `remote` 	Fetch the remote’s copy of current branch and rebases it into the local copy. Uses git rebase instead of merge to integrate the branches.

git rebase -i HEAD~1  		to remove last commit

git rebase 

	Reapply commits on top of another base tip. If you don’t care about your git commit history, you can skip “git rebase,” but if you would prefer a clean, linear history free of unnecessary merge commits, you should reach for git rebase instead of git merge when integrating changes from another branch.

	You should only rebase commits that have not been shared with other people via push. Rebasing commits causes their commit-ids to change which can result in losing future commits.

	The merge commit messages can be useful to indicate synchronisation points but they can also produce a lot of noise. For example if you're working against local branches and haven't pushed then this additional information is meaningless, and confusing, to other developers looking at the repository.
	To solve this you can use git rebase instead of git merge. A rebase will unwind the changes you've made and replay the changes in the branch, applying your changes as if they happened all on the same branch. The result is a clean history and graph for the merge.
	Important As rebase will replay the changes instead of merging, each commit will have a new hash id. If you, or other developers, have pushed/pulled the repository then changing the history can git to lose commits. As such you shouldn't rebase commits that have been made public, for example pushing commits then rebasing in older commits from a different branch. The result will be previously public commits having different hash ids. More details can be found at The Perils of Rebasing.


	Rebasing is the rewinding of existing commits on a branch with the intent of moving the “branch start point” forward, then replaying the rewound commits.

	Rebasing = MOVING A BRANCH from one commit to another (apply changes from one branch onto another)
	Can be used to permanently delete files from your codebase.
	TAKE ALL THE CHANGES THAT WERE COMMITTED ON ONE BRANCH AND REPLAY THEM ON ANOTHER ONE

	Internally git creates new commits and apply them to the specified base—it’s (literally rewriting project history)
	The branch looks the same but it’s composed of entirely new commits
	mechanism that allows you to apply your local commits on top of the arriving commits, rather than to have two strings in parallel that need to be merged
	
	To maintain a linear project history
	A common way to integrate upstream changes into your local repository. Pulling in upstream changes with git merge results in a superfluous merge commit every time you want to see how the project has progressed. On the other hand, rebasing is like saying, “I want to base my changes on what everybody has already done.”
	To test their branch changes safely in isolation on their private branch just as if they were made on top of the mainline code, including
	any recent mainline bug fixes.
	
	git-rebase 	Reapply commits on top of another base tip
	git rebase [-i | --interactive] [options] [--exec `cmd`] [--onto `newbase`]	[`upstream` [`branch`]]
	git rebase [-i | --interactive] [options] [--exec `cmd`] [--onto `newbase`]	--root [`branch`]
	git rebase --continue | --skip | --abort | --quit | --edit-todo

	Assume the following history exists

					A---B---C 	topic   ← HEAD (current branch is "topic")
					/
			D---E---F---G 		master

		From this point, the result of either of the following commands:
		git rebase master
		git rebase master topic  	(short-hand of git checkout topic + git rebase master)
		would be:
							A'--B'--C' 	topic
							/
			D---E---F---G 				master

		

	Rebasing interactively 

		Re-writing the repositories history is done using git rebase -interactive. By putting rebase into interactive mode you have more control over the changes you want to make. After launching into interactive mode you are given six commands to perform on each commit in the repository. By using the editor which opens, by default Vim, you define which actions you want to perform on each commit.
		Commands:
			* p 	pick	 use commit
			* r 	reword	 use commit, but edit the commit message
			* e 	edit	 use commit, but stop for amending
			* s 	squash	 use commit, but meld (fusion) into previous commit
			* f 	fixup	 like "squash", but discard this commit's log message
			* x 	exec	 run command (the rest of the line) using shell

		
		git rebase --interactive --root 			enter Interactive Rebase mode
		i 											insert mode                  
		pick a096aaf Initial comit of the list  	
			↑	                  \_____ Error: a 'm' is missing
		.... to change 'comit' to 'commit', change 'pick' to 'reword', esc, :wq...
			↓
		reword a096aaf Initial comit of the list  	
		pick 542fde3 New Item
		pick 51f5b2f Final Item

		A faster alternative to change the last commit message is using git commit --amend					
		git rebase --interactive HEAD~8 			 we want to modify the previous 8 commits using 
													use squash instead of 'pick'



		git rebase -i `after-this-commit`
					\___ interactively
							Means that you have a chance to edit the commits which are rebased
							You can reorder the commits, and you can remove them 

		git rebase -i HEAD~5
		reorder the last 5 commits, such that HEAD~4 becomes the new HEAD

		Re-order Commits
			git rebase --interactive HEAD~2    in vim, use dd(delete a line) p(paste a line)

		Split Commit
			git rebase --interactive HEAD~1 			define commit to split
			Splitting Commits
			After defining we want to edit the commit we are now in a state that allows us to change the history.
			As we want to split an existing commit we first we need to remove it using git reset HEAD^.
			The commit has been removed but the files still exist. We can now perform the commits as we previously desire, as two separate actions.
			Execute the commands:

			git add file3.txt
			git commit -m "File 3"
			git add file4.txt
			git commit -m "File 4"

			git rebase --continue
			You can see the output and the two new commits using git log --oneline

git rebase `base`
	Rebase the current branch onto `base`, which can be any kind of commit reference (an ID, a branch name, a tag, or a relative reference to HEAD).

Rebase to combine all of those commits into a single, concise commit.
	git rebase -i HEAD~4
	open a vim window
		pick 130deo9 oldest commit message
		pick 4209fei second oldest commit message
		pick 4390gne third oldest commit message
		pick bmo0dne newest commit message
	To combine these, we need to change the “pick” option to “fixup”
	Merge all of your commits into the commit with the message “oldest commit message”.
		pick 130deo9 oldest commit message
		fixup 4209fei second oldest commit message
		fixup 4390gne third oldest commit message
		fixup bmo0dne newest commit message
		:wq

git reset --hard commit-id 	remove the entire commit
git rebase -i 				default text editor will open with your list of commits (-i = interactive)
git rebase -i HEAD~1  		to remove last commit
git rebase -i HEAD~2  		to squash (écraser) your last few commits
git rebase -i --root 		prevents your branch from being limited by requiring an upstream branch.
When you save the file, Git will open your commit message to edit. Exit with :q!

# Start a new feature
git checkout -b new-feature master
# Edit files
git commit -a -m "Start developing a feature"
# Fix a security hole:
# Create a hotfix branch based off of master
git checkout -b hotfix master
# Edit files
git commit -a -m "Fix security hole"
# Merge back into master
git checkout master
git merge hotfix
git branch -d hotfix

After merging the hotfix into master, WE HAVE A FORKED PROJECT HISTORY. 
Instead of a plain git merge, we’ll integrate the feature branch with a rebase to maintain a linear history:

git checkout new-feature
git rebase master			
This moves new-feature to the tip of master, which lets us do a standard fast-forward merge from master:

git checkout master
git merge new-feature

How do you revert a commit that has just been made?
git revert HEAD~2..HEAD
revert creates a new commit with patches that cancel out the changes introduced in specific commits.
Alternatively, one can always checkout the state of a particular commit from the past, and commit it anew.

How do you squash last N commits into a single commit?
git rebase -i HEAD~{N}

commits are being combined into one ("squashed" in Git slang)

You may have several local git commits. Now run “git push,” and it will generate several git commit histories. 
To consolidate them as one, we can use the “git squash” technique.
# get local 3 latest commits
$ git rebase -i HEAD~3
# In editor, change "pick" to "squash". Keep the first one as "pick"
$ git rebase --continue
$ git push origin $branch_name


How do you find a list of files that has changed in a particular commit?
git diff-tree -r {hash}
list all the files that were changed or added in that commit. The -r flag makes the command list individual files, rather than collapsing them into root directory names only.
git diff-tree --no-commit-id --name-only -r {hash}        supress the commit hashes from appearing in the output


http://ohshitgit.com/
Oh shit, I committed and immediately realized I need to make one small change!
# make your change
git add .
git commit --amend
# follow prompts to change or keep the commit message
# now your last commit contains that change!
This usually happens to me if I merge to master, then run tests/linters... and FML, I didn't put a space after the equals sign. You could also make the change as a new commit and then do rebase -i in order to squash them both together, but this is about a million times faster.


## Tips: Using remote branches so much easier than rebasing (no need to get the local base branch up to date)

git fetch
git rebase origin/master

vs

git checkout master
git pull
git checkout mybranch
git rebase master

https://opensource.com/article/18/6/git-reset-revert-rebase-commands