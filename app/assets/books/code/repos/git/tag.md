## git tag

Tag specific points in history as being important. (mark release points v1.0…)
Mark a specific commit in your timeline of changes and serve as a useful identifier in history.

git tag `tag name`                    If no commit hash is provided, the most recent commit (i.e. HEAD) will be used by default.
git tag `tag name` `commithash`

git tag v1.0        Mark a version/milestone

git tag             List all tags of the current Git repository:
v0.1
v1.3
git tag -l "v1.8.5*"



* Annotated Tags 		
git tag -a v1.4 -m "my version 1.4"
git show v1.4

* Lightweight Tags	
git tag v1.4-lw   	like a branch that doesn’t change – it’s just a pointer to a specific commit.
git checkout -b [branchname] [tagname]


git tag v1.4-lightweight-tag
git tag -a v1.4-annotated-tag -m "my annotation message"
git tag -a v1.2 9fceb02			Tagging later	

📌 TAGS ARE NOT PUSHED BY DEFAUT, EXPLICITLY PUSH TAGS
git push origin v1.4
git push origin --tags          Transfer all of your tags to the remote server that are not already there

git checkout v2.0.0 			Checking out Tags = detached HEAD
                                Any new commit won’t belong to any branch and will be unreachable, except by the exact commit hash.
git checkout -b version2 v2.0.0   To make changes(say you’re fixing a bug on an older version)



https://git-scm.com/book/en/v2/Git-Basics-Tagging

Specific points in a repository’s history marked as being important, typically used to identify release versions.
a pointer to a specific commit, and if done consistently, it helps you roll back to previous version of your code without referencing specific commits.

Speaking of releases, GitHub enhanced the Git tag functionality by introducing releases.	
A GitHub release builds on top of Git tags and represents a complete release of your code, along with Zip files, 
release notes, and binary assets that might represent a fully working version of your code’s end product.

## get latest tag
t=$(git describe --tags `git rev-list --tags --max-count=1`)
## print latest
echo $t
1.0.0

Semantic versioning (aka SemVer) is currently the best known and most widely adopted version scheme. 
Since SemVer is so popular, plenty of tools already exist to produce a semantic version tag, so I ultimately decided to use fsaintjacques/semver-tool: https://github.com/fsaintjacques/semver-tool
semver-tool is a bash script which, given a valid SemVer tag, will bump the version to it’s next value based on major, minor, or patch argument.



## Git supports two types of tags: 

    like a branch that doesn’t change—it’s just a pointer to a specific commit.
    stored as full objects in the Git database. 
    They’re checksummed; 
    contain the tagger name, email, and date; 
    have a tagging message
    can be signed and verified with GNU Privacy Guard (GPG). 
    It’s generally recommended that you create annotated tags so you can have all this information; 
    but if you want a temporary tag or for some reason don’t want to keep the other information, 
    lightweight tags are available too.

    * lightweight tags
        
        git tag v1.4-lw
        git tag

    * annotated tags
        
        git tag -a v1.4 -m "my version 1.4"
        git show v1.4

    * Tagging Later

## You can also tag commits after you’ve moved past them. Suppose your commit history looks like this:

    git log --pretty=oneline
    15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment'
    a6b4c97498bd301d84096da251c98a07c7723e65 Create write support
    0d52aaab4479697da7686c15f77a3d64d9165190 One more thing
    6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'
    0b7434d86859cc7b8c3d5e1dddfed66ff742fcbc Add commit function
    4682c3261057305bdd616e23b64b0857d832627b Add todo file
    166ae0c4d3f420721acbb115cc33848dfcc2121a Create write support
    9fceb02d0ae598e95dc970b74767f19372d61af8 Update rakefile
    964f16d36dfccde844893cac5b347e7b3d44abbc Commit the todo
    8a5cbc430f1a9c3d00faaeffd07798508422908a Update readme
    
    Now, suppose you forgot to tag the project at v1.2, which was at the “Update rakefile” commit. 
    You can add it after the fact. 
    To tag that commit, you specify the commit checksum (or part of it) at the end of the command:

    git tag -a v1.2 9fceb02		
    git push origin --tags

Push Tags
    
    By default, the git push command doesn’t transfer tags to remote servers. 
    You will have to explicitly push tags to a shared server after you have created them. 
    This process is just like sharing remote branches—you can run git push origin `tagname`.

    git push origin v1.5
    
    If you have a lot of tags that you want to push up at once, you can also use the --tags option 
    to the git push command. This will transfer all of your tags to the remote server that are not already there.
    git push origin --tags


Checking out Tags = detached HEAD
    If you want to view the versions of files a tag is pointing to, you can do a git checkout of that tag, 
    although this puts your repository in “detached HEAD” state, which has some ill side effects:

    git checkout v2.0.0
    Note: switching to 'v2.0.0'.

    You are in 'detached HEAD' state. You can 
        look around
        make experimental changes and commit them
        discard any commits you make in this state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -c with the switch command. Example:

        git switch -c `new-branch-name`


## Or undo this operation with:

		  git switch -

## Turn off this advice by setting config variable advice.detachedHead to false

		HEAD is now at 99ada87... Merge pull request #89 from schacon/appendix-final

		$ git checkout v2.0-beta-0.1
		Previous HEAD position was 99ada87... Merge pull request #89 from schacon/appendix-final
		HEAD is now at df3f601... Add atlas.json and cover image
		In “detached HEAD” state, if you make changes and then create a commit, the tag will stay the same, 
		but your new commit won’t belong to any branch and will be unreachable, except by the exact commit hash. 
		
		Thus, if you need to make changes—say you’re fixing a bug on an older version, for instance—
		you will generally want to create a branch:
		$ git checkout -b version2 v2.0.0
		Switched to a new branch 'version2'
		If you do this and make a commit, your version2 branch will be slightly different than your 
		v2.0.0 tag since it will move forward with your new changes, so do be careful.


## TAGGING CHANGES

		git tag
			Create, list, delete or verify a tag object signed with GPG

			Tag: specific point in history as being important (mark release points v1.0, and so on)

			git tag [options] [`TagName`] [`CommitChecksum`] [`TagMessage?]
					-a = Annotated Tag
					-m = Annotated Tag Message
			$ git tag 							List all tags in the current repository
			$ git tag TagName 					Create a tag at the current revision
			$ git tag `tag name` `treeish`
			$ git tag TagName CommitChecksum 	Create a tag at the commit specified by the partial checksum (six characters is usually plenty)
			$ git tag -a TagName -m TagMessage 	Create an annotated tag
			$ git tag -a TagName CommitChecksum Create an annotated tag at the commit specified by the partial checksum
			$ git push --tags 					Push tags to a remote repository
			$ git show TagName 					Print information about a specific tag to the console window


				git tag 					Display all tags
				git tag -l 'v1.8.5*' 		search specific tag

						 Annotated Tags
						 ↑
				git tag -a v1.4 -m 'my version 1.4'
				or
				git tag v1.4-lw
							  ↓
							Lightweight Tags

				git show v1.4

				git tag -a v1.2 9fceb02		Late tagging
									↓
								  specify the commit checksum (or part of it)
								  git log
								  166ae0c4d3f420721acbb115cc33848dfcc2121a started write support
								← 9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile
								  964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo

				git push origin [tagname] 			push tags to a shared server (push command doesn’t autom. transfer tags to remote servers)
				git push origin --tags 				transfer all of your tags to the remote server that are not already there
				git checkout -b version2 v2.0.0 	create a new branch 'version2' at a specific tag 'v2.0.0'
