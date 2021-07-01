## git alias

git config -l  		view them

git config --global alias.cl clone
git config --global alias.co checkout 					git checkout → git co
git config --global alias.br branch 					git branch 	 → git br
git config --global alias.ci commit 					git commit   → git ci
git config --global alias.st status
git config --global alias.st status -a
git config --global alias.unstage 'reset HEAD --'		git reset HEAD fileA  →	 git unstage fileA
git config --global alias.visual "!gitk" 				start an external command, here gitk
git config --global alias.last 'log -1 HEAD' 			see the last commit easily
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)`%an`%Creset'"