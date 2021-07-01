## git clone

Cloning an existing repository
No need 'git init'
Many transfer protocols (https, SSH, git://…)

git clone `url`  	clone a remote repository onto your local machine in current directory 
					!! WILL CREATE A FOLDER WITH THE CLONED's PROJECT NAME
					!! CLONE IS NOT CHECKOUT !!

git clone remoteGitHubURL        Copies down a remote GitHub repository along with all the version history to a local working directory. Maps the directory for further commands.
git clone url [newfolder]
			|
			|______ git clone https://github.com/libgit2/libgit2
					git clone git://github.com/schacon/grit.git
					git clone user@server:path/to/repo/repo.git
					git clone https://github.com/libgit2/libgit2 mylibgit
																	|___ target directory   

CLONING BY SSH
	git clone user@server:path/to/repo.git
	git clone git@github.com:nodejs/node.git

git clone https://github.com/guinetn/project01 				Create the folder 'project01'. Clone + Checkout a working copy of the latest version. Files are tracked and unmodified
git clone https://github.com/guinetn/project01 myFolder     Create the folder 'myFolder'
cd myFolder
git status
`On branch master  
Your branch is up-to-date with 'origin/master'    
nothing to commit, working tree clean

git clone https://github.com/simplx-fr/basic-html5-boil.git new-project && cd new-project && git remote remove origin

git checkout ... 	Check out a particular branch or a tagged version of the code to hack on
					git checkout -f 		undo changes: check out HEAD
					works only with files that are staged for commit or are already part of the repository, but sometimes you want to get rid of new files as well. 
					Using touch, create a file with a name of your choice, then git add it. 
					Verify that running git checkout -f gets rid of it.


No intention of updating the source ? Discard everything "git-like" by deleting the \.git folder:  
rm -rf .git 
	-r = directory 
	-f = force

## FORKING
clone, then...
git checkout -b my-new-feature 				Create your feature branch
git commit -am 'Add some feature' 			Commit your changes
git push origin my-new-feature 				Push to the branch
Submit a pull request :D

