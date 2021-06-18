# GIT CONFIGURATION  

>git --version  
>git version  


Stored in three places, EACH LEVEL OVERRIDES VALUES IN THE PREVIOUS LEVEL, IF SAME KEY, THE LAST VALUE WIN  

git config --system -l 		Values for all users 	.git/config 	 	

C:\Program Files (x86)\Git\etc\config  
git config --global -l 		Specific to your user 	~/.gitconfig 		

C:\Users\`username`\.gitconfig  
git config --local -l 		Current directory 		.git/config  


## SET USER PARAMETER - ESTABLISHING USER IDENTITY  
To credit your efforts on commits. Should be done for each machine on which you’ll be using Git.  

git config --global user.name "John Doe"              name identifiable for credit when review version history  
git config --global user.email "jdoe@gmail.com"       email associated with each history marker (commit)  

## SET YOUR DEFAULT TEXT EDITOR (VIM BY DEFAULT)  

git config --global core.editor emacs  
git config --global core.editor notepad  
git config -- global core.editor "nano"  

Vim and Emacs are popular text editors often used by developers on Unix based systems like Linux and Mac  

git config --global color.ui auto                         
git config --global core.excludesfile [file] 		   system wide ignore pattern for all local repositories  

download.page(code/repos/git/alias.md)  

## CHECKING YOUR SETTINGS  

git config -l  
git config user.name  

## LIST CONFIGURATIONS  

`git config -l                   ← list all configuration together  
`git config --global --edit      ← machine level  
`git config --system -l          ← user level 
`git config --local --edit       ← project level  


## SET YOUR DIFF TOOL  

git config --global merge.tool vimdiff  

## SET HTTP.POSTBUFFER  

Deployement error: 
	Unable to rewind rpc post data - try increasing http.postBuffer:  

	git config http.postBuffer 524288000		    
	To allow up to the file size 500M and then my push worked. 
	It may have been that this was the problem initially with pushing a big repo over the http protocol  


## CONFIG AT PROJECT LEVEL  

Run from C:\github\projet01  
C:\github\projet01\.git\config 
`git config --local --edit  
```vb  
[core]  
        repositoryformatversion = 0  
        filemode = false  
        bare = false  
        logallrefupdates = true  
        ignorecase = true  
[remote "origin"]  
        url = https://github.com/guinetn/braincache.git  
        fetch = +refs/heads/*:refs/remotes/origin/*  
[branch "main"]  
        remote = origin  
        merge = refs/heads/main  
```  

## CONFIG AT USER LEVEL  

C:/Program Files/Git/etc/gitconfig          
`git config --system --edit  
```vb  
[diff "astextplain"]  
        textconv = astextplain  
[filter "lfs"]  
        clean = git-lfs clean -- %f  
        smudge = git-lfs smudge -- %f  
        process = git-lfs filter-process  
        required = true  
[http]  
        sslBackend = openssl  
        sslCAInfo = C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt  
[core]  
        autocrlf = true  
        fscache = true  
        symlinks = false  
[pull]  
        rebase = false  
[credential]  
        helper = manager-core  
[credential "https://dev.azure.com"]  
        useHttpPath = true  
[init]  
        defaultBranch = main  
```  

## CONFIG AT MACHINE LEVEL  

%USERPROFILE%\.gitconfig  
C:/Users/nguin/.gitconfig 
`git config --global --edit  
```vb  
## Git per-user configuration file  
[user]  
## Please adapt and uncomment the following lines:  
        name = Nicolas Guinet  
        email = nguinet.pro@gmail.com  
[alias]  
        st = status  
        cl = clone  
        br = branch  
        ci = commit  
        co = checkout  
        lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)`%an`%Creset'  
```  

## COMMUNITY CONFIGURATIONS  

[user]  
	name   = Tania Rascia  
	email  = taniarascia@gmail.com  
[github]  
	user   = taniarascia  
[alias]  
	a      = add  
	ca     = commit -a  
	cam    = commit -am  
	cm     = commit -m  
	s      = status  
	pom    = push origin master  
	pog    = push origin gh-pages  
	puom   = pull origin master  
	puog   = pull origin gh-pages  
	cob    = checkout -b  
	co     = checkout  
	l      = log --oneline --decorate --graph  
	lall   = log --oneline --decorate --graph --all  
	ls     = log --oneline --decorate --graph --stat  
	lt     = log --graph --decorate --pretty=format:'%C(yellow)%h%Creset%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)%an%Creset'  

Show the diff between the latest commit and the current state  
d = !"git diff-index --quiet HEAD -- || clear; git --no-pager diff --patch-with-stat"  

`git di $number` shows the diff between the state `$number` revisions ago and the current state  
di = !"d() { git diff --patch-with-stat HEAD~$1; }; git diff-index --quiet HEAD -- || clear; d"  

Pull in remote changes for the current repository and all its submodules  
p = !"git pull; git submodule foreach git pull origin master"  

Checkout a pull request from origin (of a github repository)  
pr = !"pr() { git fetch origin pull/$1/head:pr-$1; git checkout pr-$1; }; pr"  

