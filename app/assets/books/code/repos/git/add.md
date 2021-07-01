## git add 

Use .giignore to avoid committing things like 
- compressed files (zips, rars, jars),
- compiled code (object files, libraries, executables),
- database backups, and media files (flv, psd, music, movies)

Adds a change in the working directory to the staging area (the "index")
Tell wich elements to include in the next commit.

The staging area (the index) lets you group related changes into highly focused snapshots before actually committing it to the project history. Its a buffer between the working directory and the project history

git add . 					Adds everything from the project folder in the staging area
git add *.html        		Add all .html files to your staging area
git add `file`				Stage all changes in `file` for the next commit
git add `directory`			Stage all changes in `directory` for the next commit
git add -p					Begin an interactive staging session that lets you choose portions of a file to add to the next commit. This will present you with a chunk of changes and prompt you for a command
							Interactively ask what to stage, this will show you all the changes again and will show you comment / logging that you forgot to remove as well. Also commit often, as large changes tend to be hard to review / oversee.