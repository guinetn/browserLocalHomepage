## git stash

Git stash is a very useful command, where git will 'hide' the changes on a dirty directory - but no worries you can re-apply them later. The command will save your local changes away and revert the working directory to match the HEAD commit.

```sh
## Stash local changes
$ git stash

## Stash local changes with a custom message
$ git stash save "this is your custom message"

## Re-apply the changes you saved in your latest stash
$ git stash apply

## Re-apply the changes you saved in a given stash number
$ git stash apply stash@{stash_number}

## Drops any stash by its number
$ git stash drop stash@{0}

## Apply the stash and then immediately drop it from your stack
$ git stash pop

## 'Release' a particular stash from your list of stashes
$ git stash pop stash@{stash_number}

## List all stashes
$ git stash list

## Show the latest stash changes
$ git stash show

## See diff details of a given stash number
$ git diff stash@{0}
```




git stash
git stash add current changes to a stash (~ clipboard with multiple slots)
git stash apply apply the stash to your current branch, so you could stash, change branch and apply to move your changes to another branch
git stash pop does the same thing as apply but also remove the last change from the stash
git stash list will list all changes on the stash

git stash (planque)

Makes a temporary, local save of your uncommitted changes so you can work on something else, and then come back and re-apply them later on
! Git won't stash changes made to untracked or ignored files

git stash
you're free to make changes, create new commits, switch branches, and perform any other Git operations except push
…. do things
git stash pop
When you are ready to write the stashed changes back into the working copies of the files, simply pop them back of the stack.

To quickly switch context and work on something else, but you're mid-way through a code change and aren't quite ready to commit.
To swap code in and out: 'soft reset'
Stashing is like saving a temporary local commit to your branch.
It isn't possible to push a stash to a remote repository, so a stash is just for your own personal use.

Your branch now appears as it was when you made your last commit.
Now, you can safely change branches without losing your code or having a messy commit.
When you switch back to your branch and run git stash list you’ll see a list of stashes that look something like this:

Git offers a useful feature for those times when your changes are in an incomplete state, you aren’t ready to commit them, and you need to temporarily return to the last committed (e.g. a fresh checkout). This feature is named “stash” and pushes all your uncommitted changes onto a stack.

git stash
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage

! Git won't stash changes made to untracked or ignored files
stashed:
    changes that have been added to your index (staged changes)
    changes made to files that are currently tracked by Git
not stashed:
    new files in your working copy that have not yet been staged
    files that have been ignored
git stash -u
--include-untracked : stash also untracked files
git stash -a
include changes to ignored files

git stash show
view a summary of a stash
git stash show -p
view a summary of a stash with full diff

git stash list
stash@{0}: WIP on master: 5002d47 our new homepage
stash@{1}: WIP on master: 5002d47 our new homepage
stash@{2}: WIP on master: 5002d47 our new homepage

run git stash several times to create multiple stashes
stashes are identified as "WIP" (work in progress)
Annotate your stashes with a description
git stash save "add style to our site"  

git stash pop
reapply previously stashed changes
removes the changes from your stash and reapplies them to your working copy

re-apply the most recently created stash: stash@{0}
git stash pop stash@{2}
choose which stash to re-apply

git stash apply
reapply the stashed content
reapply the changes to your working copy and keep them in your stash

git stash apply stash@{1}
apply a specific stash (if you stashed more than once). ‘1’ denotes the second before last stash
git checkout .
which resets all uncommitted code.

git checkout -f         undo changes: check out HEAD
works only with files that are staged for commit or are already part of the repository, but sometimes you want to get rid of new files as well. Using touch, create a file with a name of your choice, then git add it. Verify that running git checkout -f gets rid of it.
git drop # Discards the most recently stashed changeset
when you have applied a stash, the stash is not deleted.
You can remove stashes individually

git stash drop stash@{1}
    drop a particular stash
git stash clear
remove all stashes      

Partial stashes
You can also choose to stash just a single file, a collection of files, or individual changes from within files. If you pass the -p option (or --patch) to git stash, it will iterate through each changed "hunk" in your working copy and ask whether you wish to stash it:

Creating a branch from your stash
git stash branch
carry over your stashed commits to a new feature branch or debugging branch

git stash branch add-style stash@{1}
If the changes on your branch diverge from the changes in your stash, you may run into conflicts when popping or applying your stash. Instead, you can use git stash branch 