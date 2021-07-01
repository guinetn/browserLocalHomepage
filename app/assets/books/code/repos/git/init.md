## git init       

SETTING UP A NEW REPOSITORY

git init       				Create an empty Git repository or reinitialize an existing one
				 			Transform the current directory into a Git repository. This adds a .git folder to the
							current directory and makes it possible to start recording revisions of the project.
							Create files required in the current directory to perform version control
							Creates a new '/.git' subdirectory  containing a Git repository skeleton. Nothing in your project is tracked yet
												|____
													C:\Documents\GitHub\.git\config
													C:\Documents\GitHub\.git\description
													C:\Documents\GitHub\.git\HEAD
													C:\Documents\GitHub\.git\...
							The /.git is where Git stores all of your commits, as well as everything else it needs

git init `ProjectName` 		Create the directory `ProjectName` and Initializes a new Git repository. 
							Transforms a regular folder into a directory that can accept Git commands.
							Tip: explorer . 		open directory in windows explorer
git init `directory` 		Create an empty Git repository in the specified directory (also created)
git init --bare `directory`	Initialize an empty Git repository, but omit the working directory
							--bare flag creates a repository that doesn’t have a working directory, making it impossible to
							* edit files and commit changes in that repository.
							* a storage facility and not a development environment

See also
>git flow init

