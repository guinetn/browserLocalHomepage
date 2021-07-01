## git revert (safe)

	  _____  
	 /     \ 
	/       ↓  
o---x---o---N---→ reverting
		↓
		this will be 'undoes' by the creation of a new commt (N)

similar to reset but its approach is different
git reset will move the branch pointer back in the chain (typically) to "undo" changes
revert command adds a new commit at the end of the chain to "cancel" changes

If we add a line to a file in each commit in the chain
git reset HEAD~1     one way to get back to the version with only two lines is to reset to that commit: 
git revert HEAD      Another way to end up with the two-line version is
Because this adds a new commit, Git will prompt for the commit message:
Revert "File with three lines"
This reverts commit b764644bad524b804577684bf74e7bca3117f554.

						 main
						  ↓
9ef9173  ←  7c709f0  ←  b764644 
line1       line1 		line1
            line2       line2
            			line3
git log --oneline
b764644 File with three lines
7c709f0 File with two lines
9ef9173 File with one line

git revert HEAD
						 			main
						  	  		 ↓
9ef9173  ←  7c709f0  ←  b764644 ←  11b7712
line1       line1 		line1      line1 
            line2       line2      line2
            			line3
git log --oneline
11b7712 Revert "File with three lines"
b764644 File with three lines
7c709f0 File with two lines
9ef9173 File with one line



git checkout hotfix
git revert commit       Create new commit that undoes all of the changes made in `commit`, then apply it to the current branch.
git revert HEAD~2

Reverting undoes a commit by creating a new commit. 
This is a safe way to undo changes, as it has no chance of re-writing the commit history.

Undoes a committed snapshot (do not delete it) safely
Generate a new commit that undoes all of the changes introduced in `commit`, then apply it to the current branch.
It doesn’t change the project history

To remove a bug introduced by a single commit instead of manually fixing it and committing a new snapshot
Able to target an individual commit at an arbitrary point in the history, whereas git reset can only work backwards from the current commit

git revert `commit` 	Undo an old commit on the current branch (without deleting it, ie not modifying history)
						GENERATE A NEW COMMIT that undoes all of the changes introduced in `commit`
						Then apply it to the current branch
						it does not “revert” back to the previous state of a project by removing all subsequent commits

	git commit -m "Make some changes that will be undone"
	git revert HEAD    # Revert the commit we just created

	git revert HEAD
		revert the last commit (create new one)	

	# Edit some tracked files
	# Commit a snapshot
	git commit -m "Make some changes that will be undone"
	# Revert the commit we just created
	git revert HEAD


git revert `commit`    	Create new commit that undoes all of the changes made in `commit`, then apply it to the current branch.

