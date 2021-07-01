## git commit

SAVE STAGED SNAPSHOT
A commit is essentially a snapshot of all the files in your project at a particular point in time
commit commits the staged snapshot to the project history

!!!	ANYTHING THAT IS STILL UNSTAGED (FILES CREATED/MODIFIED AND HAVEN’T RUN GIT ADD ON) WON’T GO INTO THIS COMMIT
!!!	THEY WILL STAY AS MODIFIED FILES ON YOUR DISK


git commit 		Commits the staged snapshot to the project history. Ask for a commit message.
				Launch editor for comment prompt
				Record changes to the repository				
				Git records the entire contents of each file in every commit
git commit –m ”Your commit message”		Commit the staged snapshot in your working directory with a descriptive commit message				
git commit -a 							Commit a snapshot of all changes in the working directory. This only includes modifications to tracked files 
git commit --amend                  	If you made a mistake in the message for your last commit, you can edit the text (WHILE LEAVING THE CHANGED FILE(S) UNTOUCHED)

git commit FileName -m “Message Text”     Commits the changes for the specific file(s) and includes the commit message specified:
		↑
		OR TO SKIP THE STAGING AREA
					↓
			$ git commit -a
			$ git commit -a -m 'added new benchmarks'
							↓
						Git automatically stage every file that is already tracked before doing the commit

git commit [options] [`File_1`] [`File_2`] . . . [`File_n`] [-m `“Commit Message”`]
			↓
			-a 								Commit ALL CHANGES to tracked files since last commit
			-v 								Verbose: include the diffs of committed items in the commit message screen
			--amend							Edit the commit message associated with the most recent commit
			--amend `File_1` `File_2` ..  	Redo the previous commit and include changes to specified files.

Goup of files (Snapshots of altered files, Not Differences)
Every commit takes a picture of what ALL your files look like at that moment and stores a reference to that snapshot
Git doesnt just store changed files BUT ALL the FILES (a link to previous file if not changed) = miniature filesystem 

Contains
. a pointer to the snapshot of the content you staged.
. author’s name & email
. message
. pointers to the parent´s commit(s)
	zero parents : initial commit
	one parent   : normal commit
	++  parents  : a commit that results from a merge of two or more branches

Each file in your working directory can be
. TRACKED
		were in the last snapshot
		unmodified, modified, or staged:  U  M  A
. UNTRACKED
		any files in your working directory that were not in your last snapshot and are not in your staging area.
		When you first clone a repository, all of your files will be tracked and unmodified because you just checked them out
		and haven’t edited anything.

every commit refers to a complete and immutable state of the entire source tree. Therefore, as long as you remember a commit's ID you can always go back to that state.

Saved changes are called commits. Each commit has an associated commit message, which is a description explaining why a particular change was made. Commit messages capture the history of your changes, so other contributors can understand what you’ve done and why.