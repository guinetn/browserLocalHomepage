## git clean

removes untracked files from your working directory. 
see which files are untracked with 'git status' and remove them manually. 
Like an ordinary rm command, git clean is not undoable, so make sure you really want to delete the untracked files before you run it.

often executed in conjunction with git reset --hard. Remember that resetting only affects tracked files, so a separate command is required for cleaning up untracked ones. Combined, these two commands let you return the working directory to the exact state of a particular commit.

git clean -n 			Shows which files would be removed from working directory without actually doing it
						Perform a “dry run” of git clean. This will show you which files are going to be removed without actually doing it.
git clean -f 			Remove untracked files from the current directory
						Remove untracked files from the current directory. The -f (force) flag is required unless the clean.requireForce configuration option is set to false (it's true by default). 
						This will not remove untracked folders or files specified by .gitignore.
git clean -f `path`		Remove untracked files, but limit the operation to the specified path
						Remove untracked files, but limit the operation to the specified path.
git clean -df 			Remove untracked files and untracked directories from the current directory.
						Remove untracked files and untracked directories from the current directory.
git clean -xf 			Remove untracked files from the current directory as well as any files that Git usually ignores.
						Remove untracked files from the current directory as well as any files that Git usually ignores.

