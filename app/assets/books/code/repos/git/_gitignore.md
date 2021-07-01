## .gitignore

Ignoring certain files and file patterns
By using this file, you are telling Git not to store many unwanted files like binaries, temporary files...

## Where to put .gitignore?

touch .gitignore 	name of files or folders you want to be ignored from your repository
git add .gitignore
touch .gitignore

You can have a .gitignore in every single directory of your project.
However, the best practice is to have on single .gitignore file on the project root directory, 
and place all files that you want to ignore in it

The '.gitignore' file lets git completely ignoring files (.obj .exe ...)
cat .gitignore
*.[oa]  			tells Git to ignore any files ending in “.o” or “.a” – object and archive files that may be the product of building your code
*~					tells Git to ignore all files that end with a tilde (~)

RULES
    A separate line for each file
    Blank lines or lines starting with # are ignored.
    Standard glob patterns work (Glob patterns are like simplified regular expressions that shells use)
    You can start patterns with a forward slash (/) to avoid recursivity.
    You can end patterns with a forward slash / to specify a directory.
    You can negate a pattern by starting it with an exclamation point (!).
                        
    
    # no .a files
    *.a


## but do track lib.a, even though you´re ignoring .a files above
!lib.a
## only ignore the root TODO file, not subdir/TODO
/TODO
## ignore all files in the build/ directory
build/
## ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt
## ignore all .txt files in the doc/ directory
doc/**/*.txt

https://github.com/Atrejoe/gitignore

Global configuration applied to all projects
git config --global core.excludesfile ~/.global_ignore
... will apply the rules in ~/.global_ignore for all of your repos.

.gitignore
------------------------------
*.dll
*.exe
*.ipch
*.sdf
*.suo
*.filters
*.tlog
*.obj
*.res
*.rc
*.log
*.pdb
*.idb
*.ilk
*.lastbuildstate
*.lib
*.manifest
*.exp
*.zip
*.opensdf
*.user.*
*.xcuserstate
*.xcworkspace
*.xcuserdata
*.xcuserdatad
*.orig
*.meta
*.unityPackage
obj/
Binaries/
XInputUnity/Library/
Temp/