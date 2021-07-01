## CONFLICTS

git diff --base $file 		against base file
git diff --ours $file 		against your changes
git diff --theirs $file 	against theirs changes	 
git log --merge
gitk --merge

* Discard conflicting patch
git reset --hard
got rebase --skip

* After resolving conflicts, merge with
git add $conflicting_file   (do for all resolved files)
git rebase --continue