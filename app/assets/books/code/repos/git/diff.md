## git diff

Show changes between commits, commit and working tree, etc
Useful to find bugs

## View merge conflicts

git diff
	Show unstaged changes between your working directory and the index
	Compare WORKING directory and last commit
	by default just shows the difference between the last commit and unstaged changes in the current project
	compare changes in the working directory against a previously committed version. 
	By default the command compares the working directory and the HEAD commit.
	Shows files differences not yet staged. 

git diff --base $file 		against base file
git diff --ours $file 		against your changes
git diff --theirs $file 	against theirs changes	 

git diff committed.js
	compare the changes to a single file

git diff `commit`

git diff --staged
	compares any staged (added) files to the most recent commit.
	compare the changes in the staging area against the previous commit you provide 

git diff HEAD 			circumventing any comparison of working directory changes to staged ones
						directly compare modified files to the most recent commit.

git diff HEAD~2 HEAD   	to compare what's changed between commits

git diff HEAD..HEAD~3

git diff --cached
	compare staging area and last commit

git diff 05db2cc 8c10510
	compare files across a couple of executed by using their commit ids


* Discard conflicting patch
git reset $file 	unstaged the file but preserve is content
git reset --hard
got rebase --skip