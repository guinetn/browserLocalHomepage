## PULL REQUEST	= Code Review

Ask another developer to merge one of your branches into their repository.
Makes it easier for project leads to keep track of changes
Initiate discussions around their work before integrating it with the rest of the codebase.
When a developer gets stuck with a hard problem, they can open a pull request to ask for help from the rest of the team. Alternatively, junior developers can be confident that they aren’t destroying the entire project by treating pull requests as a formal code review.

## SUBMITING A PULL REQUEST

Pull requests notify team members (others) about the proposed feature changes you have pushed to a repository.
Interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary before integrating them 

If there are any problems with the changes, teammates can post feedback in the pull request and even tweak the feature by pushing follow-up commits. All of this activity is tracked directly inside of the pull request.

On a forked project, you contribute back to the original fork by sending a pull request to the original author

PULL REQUEST SAMPLE

When you open a pull request, you’re proposing your changes and requesting that someone review and pull in your contribution and merge them into their branch. Pull requests show diffs, or differences, of the content from both branches. The changes, additions, and subtractions are shown in green and red.

As soon as you make a commit, you can open a pull request and start a discussion, even before the code is finished.

$ git checkout dev 				# switch to dev branch
$ git pull upstream dev 		# pull recent version
$ git branch MyFeature 			# create a branch for your PR
$ git checkout MyFeature 		# switch your feature branch

Don't use your dev branch for PRs, even if it only contains minor changes. 
It is possible, but very complicated

$ git status 													will show your changes
$ git add MyChangedFile MyAllNewFile dirWithChanges/ newDir/	to add your changes to your branch do
$ git commit
...commit...xx
$ git push origin MyFeature  	# push the branch to your fork at Github
When your feature has been merged into dev you can delete the branch:
$ git checkout dev 				# switch back to dev
$ git branch -D MyFeature
$ git push origin --delete MyFeature 	# To remove a remote branch

$ git reset HEAD 						# accidentally staged (== added) a file i don't want to commit
unstages everything you added for the upcoming commit. It does not change your files.
(use "git reset HEAD `file`..." to unstage)

Remove my (not yet commited) edits from a file
$ git checkout MyChangedFile 			# resets the file back to its checked-in state. It also works with directories.

Github says my branch is conflicting and cannot be merged, what do
merge upstream dev 		not really good because it buries your changes underneath the merge

$ git checkout dev 			# to my dev branch
$ git pull upstream dev 	# pull changes
$ git checkout MyFeature 	# back to my feature branch
$ git rebase dev 			# let me rewrite it
Once your branch is rebased, test that everything is still working
$ git push --force MyFeature 	# to rewrite your PR

git init
git add --all
git commit -am "`message`"
git push origin master               remote repo (GitHub…) default name is 'origin'
git remote -v		                 list the URL of the remote repo
git remote add origin `github_url`   associate your own Git repo with GitHub 

git clone `url`                      copy a repo
the remote repository will be linked to the account from which you cloned the repo. 
So if you cloned a repo that belongs to someone else, you will not be able to push to GitHub until you change the origin using the commands below
you copied a repo from someone else and want to change the remote repository from the original owner’s to your own GitHub account
git remote -v
git remote add origin `url`
git remote set-url origin `url`

git branch 		               lists all branches on your local machine. 
git branch `name`              create a new branch
git checkout `name`            switches to an existing branch
git checkout -b `name`         create a new branch and immediately switch to it
git merge `branch`             merge that branch back into your master branch
git pull origin `branch`       to get remote changes done by multiple people on your local machine. 

git status                     to see what files have been changed and what’s being tracked
git diff --stat                to see the number of lines changed in each file
