## git merge

Test Branch is ahead of the Master by 1 commit.
To merge the code from the test branch into the master branch:
git checkout master 				First go back to the master branch:
git merge test                      Merge the code from the test branch into the master branch
The merge should be successful (if there are no conflicts)
In real projects, there will be conflicts when a merge is being done. 


Git allows you to merge one or more branches into the current branch.
git merge `branch one`
git merge `branch one` `branch two`

If any conflicts are encountered.
- a notification message is displayed 
- Files are internally marked with ````````` and ```````` around the conflicting portion of the file contents. 

Once these conflicts are manually resolved:
git add `resolved_filename`     
git commit -m "fixed"           commit in the usual manner


- [Merge vs rebase](https://www.youtube.com/watch?v=CRlGDDprdOQ)

main 				m1  →  m2  → m3
						   ↓
feature 			       m2  →  f1  → f2

way 1
git merge feature 		will merge all changes + all commitsof the feature branch (not a pb as git track how the project elvolve)

way 2
git merge --squash feature 		will merge all changes + all commitsof the feature branch (not a pb as git track how the project elvolve)
                                --squash allow to summarize all "feature" branch commits in one commit message:
git commit -m "feature and master merged"      must be added
main combined      m1  →  m2  → m3 → "feature and master merged"



git merge

If another developer has worked on the same file as you, when you pull their changes you find that a conflict between both of your changes. git fetch command downloads changes into a separate branch which can be checked out and merge. 
During a merge Git will attempt to automatically combine the commits.
When no conflicts exist then the merge will be 'fast-forwarded' and you won't have to do anything. If a conflict does exist then you will retrieve an error and the repository will be in a merging state.

Viewing Conflict
When a conflict occurs the changes from both the local and remote will appear in the same file in the unix diff format. This is the same format used by git diff.

To read the format, the local changes will appear at the top between ``````` HEAD and ======= with the remote changes being underneath between ======= and ``````` remotes/origin/master.

To resolve the conflict the files need to be edited (manually or using git checkout) to match our desired end state  
THE SIMPLEST WAY TO FIX A CONFLICT IS TO PICK EITHER THE LOCAL OR REMOTE VERSION USING 
git checkout --ours staging.txt 
git checkout --theirs staging.txt


Sometimhes Git is unable to fast-forward the changes from Developer B because Developer A has made a number of changes.
When this happens, Git will attempt to auto-merge the changes. If no conflicts exist then the merge will be completed and a new commit will be created to indicate the merge happening at that point in time.
The default commit message for merges is "Merge branch '' of ". 
Ex: Merge branch 'master' of github.com:kernow/Project-X
These commits can be useful to indicate synchronisation points between repositories but also produce a noisy commit log. In the next step we'll investigate alternative approaches.
see "git pull --rebase"


git mergetool 
will launch an external tool
http://kdiff3.sourceforge.net/		a diff and merge program

Integrate two independent lines of development (git branchs) into a single branch, putting a forked history back together again (integrate the history of independent branches) 

Current branch will be updated to reflect the merge
Target branch will be completely unaffected

git merge `branch_to_merge`
Merge the specified branch into THE CURRENT BRANC
Git will determine the merge algorithm automatically

git merge --no-ff `branch_to_merge`
Merge the specified branch into the current branch, but always generate a merge commit (even if it was a fast-forward merge). This is useful for documenting all merges that occur in your repository.

git branch -d `old_branch`
for deleting the obsolete target branch.

git checkout master
git merge my_new_feature
git branch -d my_new_feature	

Once you’ve finished developing a feature in an isolated branch, it's important to be able to get it back into the main code base. Depending on the structure of your repository, Git has several distinct algorithms to accomplish this: 

* A FAST-FORWARD MERGE 

(facilitated through rebasing) for small features or bug fixes

When there is a linear path from the current branch tip to the target branch. Instead of “actually” merging the branches, all Git has to do to integrate the histories is move (i.e., “fast forward”) the current branch tip up to the target branch tip. This effectively combines the histories, since all of the commits reachable from the target branch are now available through the current one.

linear path = master haven't progresses while the feature has progressed (no new commit on master since feature has been forked)

not possible if the branches have diverged. 
When there is not a linear path to the target branch, Git has no choice but to combine them via a 3-way merge. 

FAST-FORWARD MERGE SAMPLE

	Common workflow for short-lived topic branches

	. creates a new branch
	. adds two commits to it
	. integrates it into the main line with a fast-forward merge.

		# Start a new feature
		git checkout -b new-feature master
		# Edit some files
		git add `file`
		git commit -m "Start a feature"
		# Edit some files
		git add `file`
		git commit -m "Finish a feature"
		# Merge in the new-feature branch
		git checkout master
		git merge new-feature
		git branch -d new-feature

* 3-WAY MERGE

For the integration of longer-running features.

use a dedicated commit to tie together the two histories. The nomenclature comes from the fact that Git uses three commits to generate the merge commit: the two branch tips and their common ancestor.

3-WAY MERGE SAMPLE

	requires a 3-way merge because master progresses while the feature is in-progress. This is a common scenario for large features or when several developers are working on a project simultaneously.

	# Start a new feature
	git checkout -b new-feature master
	# Edit some files
	git add `file`
	git commit -m "Start a feature"
	# Edit some files
	git add `file`
	git commit -m "Finish a feature"
	# Develop the master branch
	git checkout master
	# Edit some files
	git add `file`
	git commit -m "Make some super-stable changes to master"
	# Merge in the new-feature branch
	git merge new-feature
	git branch -d new-feature

RESOLVING CONFLICTS

Merge conflicts will only occur in the event of a 3-way merge. It’s not possible to have conflicting changes in a fast-forward merge.

When the two branches you're trying to merge both changed the same part of the same file: which version to use. When such a situation occurs, git stops right before the merge commit so that you can resolve the conflicts manually.

When you encounter a merge conflict
. git status 		show files to be resolved
# On branch master
# Unmerged paths:
# (use "git add/rm ..." as appropriate to mark resolution)
#
# both modified: hello.py
#
Then, you can go in and fix up the merge to your liking. When you're ready to finish the merge, all you have to do is run git add on the conflicted file(s) to tell Git they're resolved. Then, you run a normal git commit to generate the merge commit. It’s the exact same process as committing an ordinary snapshot, which means it’s easy for normal developers to manage their own merges.