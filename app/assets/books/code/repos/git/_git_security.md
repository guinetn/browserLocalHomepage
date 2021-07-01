## GIT SECURITY
Git doesn't support repository authentication or authorization. It delegates this by way of the protocol (SSH or HTTPS) or operating system (file system permissions) serving the
repository. We don't want to reauthenticate every time

## SSH protocol
connect and authenticate to remote servers and services
connect to GitHub without supplying username/personal access token at each visit

## SSH keys generation

1. Create unique keys (SSH keys) on your local machine

ssh-keygen -t rsa    Generate SSH keys. Prompted: folder/file targetted 
Press ENTER to go with the default location and generate the ~/.ssh folder
- ~/.ssh
- C:\Users\nguin\.ssh
Set Passphrase

ssh-keygen -t rsa -C "email@githubworkemail.com" -f "id_rsa_workname"
    -C  Adds a comment/tag  
    -f  Filename to save the key to

2. Setup the ssh config/known_hosts file to manage multiple keys

The reason why your computer knows which SSH key to use, is because we defined the URL in our config/known_hosts file (contains url + public key):
- C:\Users\nguin\.ssh\known_hosts
- ~/.ssh/config 
- $HOME/.ssh/known_hosts       user-specific file
- /etc/ssh/ssh_known_hosts     system-wide file
 
`touch ~/.ssh/config && code ~/.ssh/config
`type config
config
```yaml
## personal account
Host github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa

## work account 1
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
`ssh-add ~/.ssh/id_rsa && ssh-add ~/.ssh/id_rsa_workname

3. Add them to your Github accounts

a. Copy your public key to your clipboard
pbcopy ` ~/.ssh/id_rsa.pub   
b. Add the key in your gitub dashboard 
https://github.com/settings/keys.

4. Clone the github repo

https://github.com/guinetn/braincache
    Code → Clone → SSH
    git@github.com:guinetn/braincache.git           ↓ CHANGE THE URL TO ↓
    git@github.com-guinetn/braincache:braincache.git


`type known_hosts

download.page(security/known_hosts.md)


- https://help.github.com/articles/caching-your-github-password-in-git/
- https://help.github.com/articles/connecting-to-github-with-ssh/
