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
 
## More
- https://dev.to/codetraveling/how-to-manage-multiple-github-accounts-on-your-local-machine-3gj0
- https://help.github.com/articles/generating-ssh-keys