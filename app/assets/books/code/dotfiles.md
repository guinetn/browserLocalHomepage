# DotFiles

Configurations for command line-based tools and shells.

Dotfiles projects store configuration files such as .zshrc or .gitconfig and often also include complete machine setup scripts. A new machine setup takes 1 hour instead of days.

https://dotfiles.github.io lists various approaches to excellent dotfiles.

Plain text configuration files system floating around our machines used to customize system
Named with a leading period . (or “dot”) indicating these are not regular documents and operating systems often hide them by default (`ls -a` to view all files)

To list them: 
ls -a 
ls -a | grep "^\."

To find them:
find / -type f | grep '.bashrc'  

On Unix-y systems:
- shell: ~/.zshrc .oh-my-zsh
- editor: ~/.vimrc
- git: ~/.gitconfig ~/.gitignore  .gitmodules

## rc files

"rc" is a convention for naming configuration files that has been adopted by some GNU/Linux programs like vim, screen, bash…: ~/.vimrc… ~/.zshrc

## Why sharing dotfiles?

You have customized files on your system, foe example: 

~/.bashrc
>find / -type f | grep '.bashrc'                 
>vi ./root/.bashrc 
    alias cp='cp -i'
    alias kstop='systemctl stop kafka.service'
    ...
        
~/.gitconfig  has many lines of customization (account, aliases, log, colors…)
    ....    
    lall   = log --oneline --decorate --graph --all
    # Diff latest commit / current state
    d = !"git diff-index --quiet HEAD -- || clear; git --no-pager diff --patch-with-stat"
    ....
    
Over time, these configuration files become highly customized with many lines and managing them becomes increasingly more challenging, keeping them synchronized between multiple computers is critical for large organizations.
I have no interest in rewriting them on every new computer or system I use. So sharing dotfiles on GitHub/Gilab to back-up/sync your configurations across your systems with myself and others is time saving.
You can then set up a new system using these dotfiles with an installation script or tool like rcm in minutes. 

⚠: Don't push your .ssh folder to github
⚠: Don't push your files containing API tokens

## A. Setting up a dotfiles repository

1. On Github creates a public `dotfiles` repository 
2. Clone it to your local environment
3. Add a .gitignore file with `*.ssh` inside (we don't want to be at risk)
3. Add a copy of your dotfiles into the local github folder, either by
* Copy them 
* Symlink them 
The workflow is to symlink from your dotfiles folder to the dotfiles destination so that any updates to your dotfiles are easily pushed to the remote repository.

    cd dotfiles/
    ln -nfs ~/dotfiles/.gitconfig ~/.gitconfig
    gives `/Users/bjorn/.gitconfig -> /Users/bjorn/dotfiles/.gitconfig
    
    ln -nfs /Users/mbbroberg/Develop/.gitconfig /Users/mbbroberg/.gitconfig
    -s creates a symbolic link (instead of a hard link)
    -f ignore errors, continue
    -n avoids symlinking a symlink (same as -h for other versions of ln)

RCM is a tool that can helps for the whole process, see below

4. Push them to the remote repository

### rcm - symlink manager

Mac, Linux, and Windows (WSL)

rcm is a "rc" file management tool providing commands to manage and list files it tracks. 
- mkrc – convert a file into a dotfile managed by rcm
- lsrc – list files managed by rcm
- rcup – synchronize dotfiles managed by rcm
- rcdn – remove all the symlinks managed by rcm

By default, rcm uses ~/.dotfiles for storing all the dotfiles it manages
- A managed dotfile is actually stored inside ~/.dotfiles
- A symlink is placed in the expected file’s location. 
For example, if ~/.bashrc is tracked by rcm, a long listing would look like this.
[me@localhost ~]$ ls -l ~/.bashrc
lrwxrwxrwx. 1 link link 27 Dec 21 08:00 .bashrc -> /home/me/.dotfiles/bashrc
[me@localhost ~]$

>sudo apt update
>sudo apt install rcm

>mkrc -v ~/.bashrc
  Moving...   '/home/link/.bashrc' -> '/home/link/.dotfiles/bashrc'
  Linking...  '/home/link/.dotfiles/bashrc' -> '/home/link/.bashrc'
Check:
>lsrc
  /home/link/.bashrc:/home/link/.dotfiles/bashrc
Create a git repository inside ~/.dotfiles and push
> cd ~/.dotfiles
> git init
> git remote add origin git@github.com:linkdupont/dotfiles.git
> git add bashrc
> git commit -m "initial commit"
> git push -u origin master

Now clone this repository on a second machine into ~/.dotfiles
> git clone git@github.com:linkdupont/dotfiles.git ~/.dotfiles
update the symlinks managed by rcm:
> rcup -v
  replacing identical but unlinked /home/link/.bashrc
  removed '/home/link/.bashrc' 
  '/home/link/.dotfiles/bashrc' -> '/home/link/.bashrc'

- https://github.com/thoughtbot/rcm

## B. Activate your dotfiles on a new system

Keeping dotfiles synchronized between those computers must not be a challenge!

>git clone https://github.com/webpro/dotfiles.git
>cd dotfiles



// create a symlink from here to the directory where they are expected
ln -sv “~/.dotfiles/runcom/.bash_profile” ~
ln -sv “~/.dotfiles/runcom/.inputrc” ~
ln -sv “~/.dotfiles/git/.gitconfig” ~

an installation script can automate symlinking: 


## DotFiles Repo
.
├── git
│ ├── .gitconfig
│ └── .gitignore_global
├── install.sh
├── osxdefaults.sh
├── runcom
│ ├── .bash_profile
│ └── .inputrc
└── system
 ├── .alias
 ├── .env
 ├── .function
 ├── .path
 └── .prompt
 
## Samples
- https://github.com/webpro/dotfiles
- https://github.com/webpro/awesome-dotfiles
- https://github.com/brennanfee/dotfiles

## Tools
- https://github.com/twpayne/chezmoi
- http://dotfiles.github.io/
- https://fedoramagazine.org/managing-dotfiles-rcm/