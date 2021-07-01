## HEAD

	The HEAD	Last commit snapshot, next parent. 
				A pointer to the last commit you made or the last commit that was checked out into your working directory. 
	The Index	proposed next commit snapshot. the snapshot of your next commit.

	The HEAD is the pointer to the current branch reference, which is in turn a pointer to the last commit you made or the last commit that was checked out into your working directory. 
	That also means it will be the parent of the next commit you do. It's generally simplest to think of it as HEAD is the snapshot of your last commit.

	HEAD is a pointer to the current branch (master by default)
	is the context of the current branch
	every commit done is recorded in this branch
	when change are ok: git merge `branch_to_integrate_to`

	git checkout HEAD~2 		check out out the grandparent of the current commit:
	![][git_checkout_Detached_Head.svg]
	This is useful for quickly inspecting an old version of your project. However, since there is no branch reference to the current HEAD, this puts you in a detached HEAD state. This can be dangerous if you start adding new commits because there will be no way to get back to them after you switch to another branch. For this reason, you should always create a new branch before adding commits to a detached HEAD.

	If checkout a SHA1 hash ec1ec42... and not a branch → 'DETACHED HEAD' → changes do NOT belong to any branch, 'lost' 
	git checkout master 	to solve detached state

	TREEISH AND HASHES

		Rather than a sequential revision ID, Git marks each commit with a SHA-1 hash that is unique to the person committing the changes, the folders, and the files comprising the changeset. This allows commits to be made independent of any central coordinating server.
		A full SHA-1 hash is 40 hex characters 64de179becc3ed324daab72f7238df1404723672
		
		To efficiently navigate the history of hashes, several symbolic shorthand notations can be used as listed in the table below.
		Additionally, any unique sub-portion of the hash can be used. Git will let you know when the characters supplied are not enough to be unique. In most cases, 4-5 characters are sufficient.

		TREEISH DEFINITION
		HEAD HEAD 			The current committed version
		HEAD^ 				One commit ago
		HEAD-1 				One commit ago
		HEAD~1 				One commit ago
		HEAD^^ 				Two commits ago
		HEAD-3 				Three commits ago
		HEAD~3 				Three commits ago
		:/”Reformatting all” Hybrid method of types 1, 2, and 3.
		RELEASE-1.0 User-defined tag applied to the code when it was certified for release.

		typing: git help rev-parse 				view the complete set of revision specifications 

	HEAD^ and HEAD~

		Both ~ and ^ on their own refer to the parent of the commit (~ and ^ both refer to the grandparent commit, etc.) 
		But they differ in meaning when they are used with numbers:
		~2 means up two levels in the hierarchy, via the first parent if a commit has more than one parent
		^2 means the second parent where a commit has more than one parent (i.e. because it's a merge)
		These can be combined, so HEAD~2^3 means HEAD's grandparent commit's third parent commit.

		^`n` format allows you to select the nth parent of the commit (relevant in merges)
		~`n` format allows you to select the nth ancestor commit, always following the first parent.

		HEAD^ is the parent commit of HEAD
				means the first parent of the tip of the current branch
		ref^ is the shortcut for ref^1 where ref^1 is the commit's first parent 
		ref~ which is also commit's first parent. It is also a shortcut for ref~1

		G   H   I   J      J = F^2  = B^3^2   = A^^3^2                
			\ /     \ /       I = F^   = B^3^    = A^^3^               
			D   E   F        H = D^2  = B^^2    = A^^^2  = A~2^2              
			\  |  / \       G = A^^^ = A^1^1^1 = A~3               
			\ | /   |      F = B^3  = A^^3                
				\|/    |      E = B^2  = A^^2                
				B     C      D = A^^  = A^1^1   = A~2                
				\   /       C = A^2  = A^2               
				\ /        B = A^   = A^1     = A~1              
					A         A =      = A^0             


## DETACHED HEADS

HEAD is pointing directly to a commit instead of a branch. (you have done a git checkout 87ec91dxxx)

A detached HEAD occurs when you check out a commit that is not a branch. The term detached HEAD tells you that you are not viewing the HEAD of any repository. The HEAD is the most recent version of a branch



Bad idea...
git checkout e35ec42d48807d0666646ba4cbf65febbaf103ac    go back in time and checkout your app from a previous commit
Note: checking out 'e35ec42d48807d0666646ba4cbf65febbaf103ac'.

You are in 'detached HEAD' state. You can look around, make experimental changes and commit them, and you can discard any commits you make in this state without impacting any branches by performing another checkout.If you want to create a new branch to retain commits you create, you may	do so (now or later) by using -b with the checkout command again. 

git checkout -b `new-branch-name`
HEAD is now at e35ec42...initial project version
git checkout master 		TO SOLVE



HEAD is Git’s way of referring to the current snapshot
HEAD is a pointer to the current branch (master by default)
is the context of the current branch
every commit done is recorded in this branch
when change are ok: git merge `branch_to_integrate_to`
If checkout a SHA1 hash ec1ec42... and not a branch → 'DETACHED HEAD' → changes do NOT belong to any branch, 'lost'

git checkout updates the HEAD to point to either the specified branch or commit. 
When it points to a branch, Git doesn't complain
when you check out a commit, it switches into a “detached HEAD” state.
This is a warning telling you that everything you’re doing is “detached” from the rest of your project’s development. If you were to start developing a feature while in a detached HEAD state, there would be no branch allowing you to get back to it. When you inevitably check out another branch (e.g., to merge your feature in), there would be no way to reference your feature

YOUR DEVELOPMENT SHOULD ALWAYS TAKE PLACE ON A BRANCH—NEVER ON A DETACHED HEAD.


DETACHED HEAD:
appears when a specific commit is checked out instead of a branch 
$ git checkout devbranch   		...usually
							Git moves the HEAD pointer along
$ git checkout 56a4e5c08 		provide the SHA1 hash of a specific commit...
Note: checking out '56a4e5c08'.
You are in 'detached HEAD' state...
							Git doesnt moves the HEAD pointer along
							Changes do NOT belong to any branch....
This means they can easily get lost once you check out a different revision or branch: not being recorded in the context of a branch, you lack the possibility to access that state easily (unless you have a brilliant memory and can remember the commit hash of that new commit...).

HEAD pointer determines your current working revision (files that are placed in your project's working directory)	

TO AVOID DETACHED HEAD:
Create a (temporary) branch and delete it once you're done.
$ git checkout -b test-branch 56a4e5c08
...do your thing...
$ git checkout master
$ git branch -d test-branch
