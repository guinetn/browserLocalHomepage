# Git

Version control system

Example of event sourcing: each commit is stored as an event representing a change of state - files/lines to be added/removed.

![](assets/books/code/repos/git01.jpg)

## Connect

We don't want to reauthenticate every time


### Learn to dig
- git blame   author name, last modified date, commit hash 
- git log to look at the commit history of the overall repo.
  git log | grep someFunction -C 3  (3 lines of context)
- git log -p index.js   file history  


### SSH protocol
connect and authenticate to remote servers and services


### SSH keys
connect to GitHub without supplying username/personal access token at each visit

1. Create unique keys (SSH keys) on your local machine

ssh-keygen -t rsa    Generate SSH keys. Prompted: folder/file targetted 
Press ENTER to go with the default location and generate the ~/.ssh folder
- ~/.ssh
- C:\Users\nguin\.ssh
Set Passphrase

ssh-keygen -t rsa -C "email@githubworkemail.com" -f "id_rsa_workname"
-C adds a comment/tag and 
-f specifies the name of the file we want to save the key to

[ssh-keygen](https://www.ssh.com/ssh/keygen/#command-and-option-summary)

2. Setup the ssh config/known_hosts file to manage multiple keys

The reason why your computer knows which SSH key to use, is because we defined the URL in our config/known_hosts file (contains url + public key):
- C:\Users\nguin\.ssh\known_hosts
- ~/.ssh/config 
- $HOME/.ssh/known_hosts       user-specific file
- /etc/ssh/ssh_known_hosts     system-wide file
 
>touch ~/.ssh/config && code ~/.ssh/config
>type config
config
```yaml
# personal account
Host github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa

# work account 1
Host github.com-workname
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_workname
```

* ssh-agent
service that manage SSH keys and their configurations
|||
|---|---|
|ssh-add -D            | Removes all currently registered ssh keys from the ssh-agent|
|ssh-add -l            | Lists all currently in the ssh-agent registered ssh keys|
|ssh-add ~/.ssh/id_rsa | Adds the specified key to the ssh-agent|

Registering our keys with their ids
>ssh-add ~/.ssh/id_rsa && ssh-add ~/.ssh/id_rsa_workname

3. Add them to your Github accounts

a. Copy your public key to your clipboard
pbcopy < ~/.ssh/id_rsa.pub   
b. Add the key in your gitub dashboard 
https://github.com/settings/keys.

4. Clone the github repo

https://github.com/guinetn/braincache
    Code → Clone → SSH
    git@github.com:guinetn/braincache.git           ↓ CHANGE THE URL TO ↓
    git@github.com-guinetn/braincache:braincache.git


>type known_hosts

### Set up different accounts on your local machine

using SSH keys instead of the usual HTTPS connection.

### Git Bash

Provides a UNIX-based environment on Windows OS machines when we install Git.
 
 ### git-internals

- https://betterprogramming.pub/a-short-journey-to-git-internals-fc9d11dd80b7

Git = key-value database. You insert any kind of content into a Git repository, for which Git will give you back a unique identifier (a key) that you can use to retrieve that content.

.git directories 
$ tree -L 1 .git/
.git/
├── HEAD          file that references the HEAD of the master branch
├── config
├── description
├── hooks
├── info
├── objects
└── refs

A “blob”: a sequence of bytes. 
Git blob: contains the exact data as a file stored in the Git key-value data store (while the “actual” file is stored on the file system)
Let’s create a blob:
$ echo hello | git hash-object --stdin -w        -w flag to actually write the object into the object database
ce013625030ba8dba906f756967f9e9ca394464a         “hello” is the “value” in the Git data store
$ git cat-file -p ce013625030ba8dba906f756967f9e9ca394464a
hello
check its type using the -t flag:
$ git cat-file -t ce013625030ba8dba906f756967f9e9ca394464a
blob
$ tree .git/objects/
.git/objects/
├── ce
│   └── 013625030ba8dba906f756967f9e9ca394464a
├── info
└── pack

save another object:
$ echo world | git hash-object --stdin -w
cc628ccd10742baea8241c5924df992b5c019f71
As expected, we now have two directories under .git/objects/:
$ tree .git/objects/
.git/objects/
├── cc
│   └── 628ccd10742baea8241c5924df992b5c019f71
├── ce
│   └── 013625030ba8dba906f756967f9e9ca394464a
├── info
└── pack

Tree Objects
solves the problem of storing the filename and allows storing a group of files together.

## More
- https://medium.com/pragmatic-programmers/managing-files-with-git-5272e699b9cf
- https://dev.to/codetraveling/how-to-manage-multiple-github-accounts-on-your-local-machine-3gj0
- https://help.github.com/articles/generating-ssh-keys