## GIT BASH

## Git Bash opens by default in the user 'Home' directory

Case-sensitive
Spaces count: use ''
Paths
    *nix application (Unix/Linux) convention for paths

    WINDOWS DIRECTORY PATH	 ← →  *NIX DIRECTORY PATH
    C:\Users\MyUserFolder	  	  /c/Users/MyUserFolder
    C:\Users\nicolas 			  /c/Users/nicolas

## BASH COMMANDS

$ CommandName [options] [directory]

Current directory
    $pwd

Navigating
    $ cd 			Return you to the root level of the current user home directory
    $ cd -			Go back to the previous Location
    $ cd ..			Move Up One Directory Level
    $ cd /c/....

Show directory contents
    $ ls `option`
            ↓
            -d   List only directories
            -l   (letter L, lowercase) = Use a long listing format (more info per item, arranged in columns, vertical listing)
            -1   List 1 item per line
            -r   Reverse the sort order
            -a   Show Everything, including hidden items

    $ ls
    $ ls –d */ 		List only subdirectories (folders) within the current directory

Clear console
    clear

Create a new directory
    mkdir [options] `folderName`
        -p = Create parent directories as needed
    $ mkdir -p --verbose /c/NewParentFolder/NewFolderName

Create files
    $ touch newFile.txt
    $ touch /c/SomeFolder/newFile.txt

    If the file does not exist, one is created:
    $ echo “This text is ADDED to the end of the file” `` newFile.txt
    $ echo “This text REPLACES existing text in the file” ` newFile.txt

Remove files
    rm [options] -`FileName`
        -I (or --interactive) 	Prompt before removal
        -v (or --verbose) 		Explain what is being done
    $ rm DeleteFileName

Remove directories
    rmdir [options] `FolderName`
            -rf  	Removes the specified folder if empty. Operation fails if folder is  not empty:
    $ rmdir DeleteFolderName
    $ rm -rf DeleteFolderName