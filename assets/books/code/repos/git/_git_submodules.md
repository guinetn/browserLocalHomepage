# git submodules 

Submodules and subtrees help you manage child projects across multiple repositories.

## To incorporate external code in your repository

	Ex with hugo:
		git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke

	* Cut/paste (has the downside of losing any upstream changes to the external repository)
	
	* Package management (npm) (has the downside of requiring installation and version management at all places the origin code is deployed)

	* Git submodule
	To keep a git repository as a subdirectory of another git repository (~ dependency management tool)
	A reference to another repository at a particular snapshot in time. Git submodules enable a Git repository  to incorporate and track version history of external code.
	
	A record within a host git repository that points to a specific commit in another external repository. - Submodules are very static 
	- only track specific commits
	- don't track git refs/branches
	- are not automatically updated when the host repository is updated

	When adding a submodule to a repository 
	- a new .gitmodules file will be created
	- contains meta data about the mapping between the submodule project's URL and local directory. 
	- If the host repository has multiple submodules, the .gitmodules file will have an entry  for each submodule.

	## when to use a fit submodule

		to maintain a strict version management over your external dependencies,  it can make sense to use git submodules. The following are a few best use cases for git submodules.

	 	- When an external component or subproject is changing too fast or upcoming changes will break the API, you can lock the code to a specific commit for your own safety.
	 	- When you have a component that isn’t updated very often and you want to track it as a vendor dependency.
	 	- When you are delegating a piece of the project to a third party and you want to integrate their work at a specific time or release. Again this works when updates are not too frequent.

	## git submodules commands

	**Add git submodule**

	```bash
	$ mkdir git-submodule-demo
	$ cd git-submodule-demo/               ____ URL parameter that points to a git repository 
	$ git init                            /
	$ git submodule add https://bitbucket.org/jaredw/awesomelibrary
	Cloning into '/Users/atlassian/git-submodule-demo/awesomelibrary'...
	remote: Counting objects: 8, done.
	remote: Compressing objects: 100% (6/6), done.
	remote: Total 8 (delta 1), reused 0 (delta 0)
	Unpacking objects: 100% (8/8), done.
	$ git status
	On branch master
	No commits yet
	Changes to be committed:
	  (use "git rm --cached `file`..." to unstage)
	 new file:   .gitmodules
	 new file:   awesomelibrary
	```

	There are now two new files in the repository 
	`- awesomelibrary directory  
	- .gitmodules. Looking at the contents of .gitmodules shows the new submodule mapping  
	[submodule "awesomelibrary"]  
	 path = awesomelibrary  
	 url = https://bitbucket.org/jaredw/awesomelibrary  

## These files can now be committed to the original repository by using git add and git commit.

	```bash
	$ git add .gitmodules awesomelibrary/
	$ git commit -m "added submodule"
	[master (root-commit) d5002d0] added submodule
	 2 files changed, 4 insertions(+)
	 create mode 100644 .gitmodules
	 create mode 160000 awesomelibrary
	```


	**Cloning git submodules**

	When a project with submodules is cloned using **git clone, it creates the directories that contain submodules, but none of the files within them**. The submodule files are not created until **two additional commands are run**. 
	- git submodule init  
	will update the local .git/config with the mapping from the .gitmodules file
	- git submodule update  
	will then fetch all the data from the submodule project and check out the mapped commit in the parent project.

## There is a -recursive option that can be passed to git clone this a convenience parameter that will tell git clone to also initialize and update any submodules. Using the -recursive option is equivalent to executing:

	```bash
	git clone /url/to/repo/with/submodules
	git submodule init
	git submodule update
	Git submodule Init
	```

The default behavior of git submodule init is to copy the mapping from the .gitmodules file into the local ./.git/config file. This may seem redundant and lead to questioning git submodule init usefulness. git submodule init has extend behavior in which it accepts a list of explicit module names. This enables a workflow of activating only specific submodules that are needed for work on the repository. This can be helpful if there are many submodules in a repo but they don't all need to be fetched for work you are doing.



	**Submodule workflows**

Once submodules are properly initialized and updated within a parent repository they can be utilized exactly like stand-alone repositories. This means that **submodules have their own branches and history**. When making changes to a submodule it is important to publish submodule changes and then update the parent repositories reference to the submodule. Let’s continue with the awesomelibrary example and make some changes:

	```bash
	$ cd awesomelibrary/
	$ git checkout -b new_awesome
	Switched to a new branch 'new_awesome'
	$ echo "new awesome file" ` new_awesome.txt
	$ git status
	On branch new_awesome
	Untracked files:
	  (use "git add `file`..." to include in what will be committed)
	 new_awesome.txt
	nothing added to commit but untracked files present (use "git add" to track)
	$ git add new_awesome.txt
	$ git commit -m "added new awesome textfile"
	[new_awesome 0567ce8] added new awesome textfile
	 1 file changed, 1 insertion(+)
	 create mode 100644 new_awesome.txt
	$ git branch
	  master
	* new_awesome

	Here we have changed directory to the awesomelibrary submodule. We have created a new text file new_awesome.txt with some content and we have added and committed this new file to the submodule. Now let us change directories back to the parent repository and review the current state of the parent repo.
	$ cd ..
	$ git status
	On branch master
	Changes not staged for commit:
	  (use "git add `file`..." to update what will be committed)
	  (use "git checkout -- `file`..." to discard changes in working directory)
	 modified:   awesomelibrary (new commits)
	```
	no changes added to commit (use "git add" and/or "git commit -a")
	Executing git status shows us that the parent repository is aware of the new commits to the awesomelibrary submodule. It doesn't go into detail about the specific updates because that is the submodule repositories responsibility. **The parent repository is only concerned with pinning the submodule to a commit**. Now we can update the parent repository again by doing a git add and git commit on the submodule. This will put everything into a good state with the local content. If you are working in a team environment it is critical that you then git push the submodule updates, and the parent repository updates.

When working with submodules, a common pattern of confusion and error is forgetting to push updates for remote users. If we revisit the awesomelibrary work we just did, we pushed only the updates to the parent repository. Another developer would go to pull the latest parent repository and it would be pointing at a commit of awesomelibrary that they were unable to pull because we had forgotten to push the submodule. This would break the remote developers local repo. To avoid this failure scenario **make sure to always commit and push the submodule and parent repository.**



Split complex project into manageable chunks. Git supports this process using submodules.

	CREATING YOUR SUBMODULE: pointing it to the destination branch
	git submodule add -b `branch` `repository_url` `submodule_folder`

	TRACK THE REMOTE BRANCH
	Once you have your submodule, and you are checked out on a branch, ensure that it is configured to track the remote branch of the submodule
	cd `submodule_folder`
	git branch --set-upstream-to=origin/`branch`
	Now you are tracking the remote branch. You can make changes to the sub-module, and push them to the remote repository as required.

When you create a reference to a submodule within your repository, you actually include a reference to a specific commit. If the repository you are referencing is updated, those changes aren’t automatically reflected in your repository. This sort of makes sense, since git has no idea whether the submodule you are referencing is under your control or not.

	By default, the submodule is checked out in a detached head state. This is fine if you want a read-only copy, but a bit of a pain if you want to commit changes. In addition, by default, submodules aren’t updated when you pull changes to your repository meaning you can get out of sync.

Working with submodules on a specific branch, where you want to commit changes to the submodule, requires a slight change to your CLI commands. Because you are no longer working with one repository, but multiple repositories.

	UPDATING YOUR REPOSITORY (Including Submodules)
	When you make changes to your submodule, then you need to commit the change in the parent to ensure that the pointer is kept up to date. However, this results in two commits - one to the submodule and one to the parent, and this may not always be desirable at the same time. In order to ensure the submodules are up to date, when pulling changes, use the following commands:

	cd `parent_repository`
	git pull
	git submodule foreach git pull
	This will ensure that the repository and submodules are kept up to date on the appropriate branch.

https://opensource.com/article/20/5/git-submodules-subtrees