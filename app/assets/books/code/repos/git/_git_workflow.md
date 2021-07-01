## GIT WORKFLOW


1) Create branch from master
2) Commit on branch
3) Rebase on master periodically to keep up with master (minimize conflicts)
4) Clean up branch (squash commits, etc)
5) Final rebase on master
6) Checkout master and merge branch (bow-shape)




- A develop branch is created from master
- A release branch is created from develop
- Feature branches are created from develop
- When a feature is complete it is merged into the develop branch
- When the release branch is done it is merged into develop and master
- If an issue in master is detected a hotfix branch is created from master
- Once the hotfix is complete it is merged to both develop and master



# Creating a feature branch
	git checkout develop
	git checkout -b feature_branch
# Finishing a feature branch
	When you’re done with the development work on the feature, the next step is to merge the feature_branch into develop.
	git checkout develop
	git merge feature_branch

# Creating a hotfix branch
	git checkout master
	git checkout -b hotfix_branch
	
	Similar to finishing a release branch, a hotfix branch gets merged into both master and develop.
	git checkout master
	git merge hotfix_branch
	git checkout develop
	git merge hotfix_branch
	git branch -D hotfix_branch



Git Flow

In the Git flow development model, you have one main development branch with strict access to it. It’s often called the develop branch.

Developers create feature branches from this main branch and work on them. Once they are done, they create pull requests. In pull requests, other developers comment on changes and may have discussions, often quite lengthy ones.

It takes some time to agree on a final version of changes. Once it’s agreed upon, the pull request is accepted and merged to the main branch. Once it’s decided that the main branch has reached enough maturity to be released, a separate branch is created to prepare the final version. The application from this branch is tested and bug fixes are applied up to the moment that it’s ready to be published to final users. Once that is done, we merge the final product to the master branch and tag it with the release version. In the meantime, new features can be developed on the develop branch.

One of the advantages of Git flow is strict control. Only authorized developers can approve changes after looking at them closely. It ensures code quality and helps eliminate bugs early.

However, you need to remember that it can also be a huge disadvantage. It creates a funnel slowing down software development. If speed is your primary concern, then it might be a serious problem. Features developed separately can create long-living branches that might be hard to combine with the main project.

What’s more, pull requests focus code review solely on new code. Instead of looking at code as a whole and working to improve it as such, they check only newly introduced changes. In some cases, they might lead to premature optimization since it’s always possible to implement something to perform faster.

Moreover, pull requests might lead to extensive micromanagement, where the lead developer literally manages every single line of code. If you have experienced developers you can trust, they can handle it, but you might be wasting their time and skills. It can also severely de-motivate developers.

In larger organizations, office politics during pull requests are another concern. It is conceivable that people who approve pull requests might use their position to purposefully block certain developers from making any changes to the code base. They could do this due to a lack of confidence, while some may abuse their position to settle personal scores.


## WORKFLOW

The goal of really any version control system is to save periodic snapshots of your projects. 
Once you have a snapshot saved, you can feel safe working on your project as you can always revert back to an earlier snapshot if you make a huge error.
If saving the snapshot is the goal, then staging is the actual act of taking the snapshot before you add it to the photo album (repository) for safe keeping.


REMOTE REPOSITORY (DVCS Distributed version control system) 
	\	 
     \____ LOCAL REPOSITORY (Git directory): snapshots store, what is copied when cloning (commits accumulator)
			   \	
			    \____  INDEX (Staging area - zone de transit): what will go in next commit (marked ▲ files)
				   		  \				
					       \____ WORKING DIRECTORY: new files or pulled files OF THE CURRENT BRANCH 
							  	    HEAD point to it
								    HEAD is an alias for the last commit-hash of the branch

## The Index	
Proposed next commit snapshot (staging area)

## The HEAD	
last commit snapshot, next parent (working directory)

HEAD always points to the last commit of the current branch. The code you're building
HEAD is a pointer to the current branch (master by default)
		is the context of the current branch
		every commit done is recorded in this branch
		when change are ok: git merge `branch_to_integrate_to`
	If checkout a SHA1 hash ec1ec42... and not a branch → 'DETACHED HEAD' → changes do NOT belong to any branch, 'lost' 
	git checkout master 	to solve detached state

## GIT FILES (in your working directory)

Files workflow:  MODIFIED, STAGED, COMMITED + TRACKED/UNTRACKED		

Git is a miniature filesystem like (every commit takes a picture of what ALL your files). A stream of snapshots
Git stores a series of snapshots (Git is a mini filesystem) AND NOT A SERIES OF CHANGESETS OR DIFFERENCES.
Commit / Save your project --`  Takes a picture of what ALL your files look like and stores a reference to that snapshot.
								FILE NOT CHANGED ? --` GIT DOESN’T STORE THE FILE AGAIN—JUST A LINK TO THE PREVIOUS IDENTICAL FILE IT HAS ALREADY STORED


Binary media files: not well with Git. Use a specific service (video and music: Vimeo or Youtube)
Design files like (PSDs and 3D models): Use Dropbox usually

each file in your working directory can be

	. TRACKED
		Were in the last snapshot
		Unmodified, Modified or Staged				 	

	. UNTRACKED
		wasn't in last snapshot
		aren't in your staging area
		any files in your working directory that were not in your last snapshot and are not in your staging area.
		When you first clone a repository, all of your files will be tracked and unmodified because you just checked them out and haven’t edited anything.


Git directory 		where Git stores the metadata and object database for your project.
					This is the most important part of Git, and it is what is copied when you clone a repository from another computer.

Working directory 	A single checkout of one version of the project.
					These files are pulled out of the compressed database in the Git directory and placed on disk for you to use or modify.

Staging area 		Sometimes referred to as 'the index', but it’s becoming standard to refer to it as the staging area
					A simple file, generally contained in your Git directory, that stores information about what will go into your next commit.
					staging: mise en scène

Git workflow
1. You modify files in your working directory.
2. You stage the files, adding snapshots of them to your staging area.
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
	

## THE THREE STATES OF GIT FILES
. MODIFIED		file changed but not yet committed 
. STAGED		file marked modified, will go in next commit snapshot
. COMMITTED		file safely stored in your local database. Stores that snapshot permanently to your Git directory

Git ‘sees’ your work in 4 different ways:
* Untracked work
your work: staging with 'git add .'
* Tracked work that hasn’t been changed
your work: staging with 'git add .'
* Tracked work that has been changed
your work: commit your change with 'git commit'
* Tracked work that’s been changed & is ready to be saved
your work: git push

Cloning a repository  
When you first clone a repository, all of your files will be tracked BUT UNMODIFIED because you just checked them out and haven’t edited anything. 

## REMOVING FILES

git rm files 		    Remove files from the working tree and from the index		 
git rm \*~ 	 			Removes all files whose names end with a ~.
git rm projects.md 		Next time you commit, the file will be gone and no longer tracked
git rm -f projects.md 	To force if file modified (prevent accidental removal of data that hasn’t yet been recorded in a snapshot)
git rm --cached README  Keep the file in your working tree (on disk) but remove it from your staging area
git rm --cached filename.extension    		Remove the file from the staging area and sets it to be untracked. remove entirely from tracking

To remove a file from Git, you have to remove it from your tracked files (staging area) and then commit. 
The git rm command does that, and also removes the file from your working directory so you don’t see it as an untracked file the next time around.

## MOVING FILES

Move or rename a file, a directory, or a symlink
git mv old new  		Git doesn’t explicitly track file movement but has a mv command
