# SSH - SECURE SHELL PROTOCOL

Most common method to
- securely communicate with remote machines
- controlling remote machines over the command line in the Linux world. 

No need to supply your username and password each time
Use SSH keys pair

## Clients
OpenSSH client: pre-installed on GNU/Linux, macOS, Windows 10 
SSH >= 6.5. Earlier versions used an MD5 signature, which is not secure.

C:\Windows\System32\OpenSSH
    scp.exe
    sftp-server.exe
    sftp.exe
    ssh-add.exe
    ssh-agent.exe
    ssh-keygen.exe
    ssh-keyscan.exe
    ssh-shellhost.exe
    ssh.exe
        connect to remote machines
            ssh nom_utilisateur@ip_ou_nom_machine -p numero_de_port
            ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name
    sshd.exe
    sshd_config_default

Protect data transferred through remote connections
A cryptographic network protocol for operating network services securely over an unsecured network. Typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.

Use SSH to control almost any Linux machine (running as a virtual machine or as a physical device on your network). A common use case is the headless configuration of embedded devices, including the Raspberry Pi. SSH can also be used to tunnel other network services. Because SSH traffic is encrypted, you can use SSH as a transport layer for any protocol that does not provide encryption by default.

Client-server architecture:  
an SSH client establishes a connection to an SSH server usually running as a system daemon often called SSHD. 


Windows 10 uses OpenSSH as its default SSH client and SSH server
Windows documentation for SSH, which covers controlling Windows machines using OpenSSH: 
https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview


                                                                             
PS>Get-ChildItem -Path Cert:\LocalMachine\CA

## Existing SSH key pairs: have you a $HOME/.ssh Directory?

cd $HOME/.ssh 
mkdir -p $HOME/.ssh 
chmod 0700 $HOME/.ssh

C:\Users\[you]\.ssh
/home/myuser/.ssh/

C:\Users\jonhdoe\.ssh
/home/johndoe/.ssh
    -a---          14/02/2017    15:50           1679 github_rsa
    -a---          14/02/2017    15:50            392 github_rsa.pub
    -a---          13/11/2020    15:50           1700 privatekey.pem
    -a---          03/03/2019    14:50           2719 root@inmotionhostring.ppk
    -a---          03/03/2019    18:27            738 root@inmotionhostring.pub
    -a---          13/11/2020    16:10           2228 known_hosts


SSH uses public/private key pairs, so id_rsa is your RSA private key (based on prime numbers), which is more secure than your id_dsa DSA private key (based on exponents). 
Keep your private keys safe and share your id_rsa.pub and id_dsa.pub public keys broadly

### STEP 1. Generating public/private ssh keys pair
ssh-keygen -t rsa 
stronger keys:
ssh-keygen -t rsa -b 2048    key size of at least 2048 bits is recommended
ssh-keygen -t rsa -b 4096 -C "$(whoami)@$(hostname)-$(date -u +%Y-%m-%d-%H:%M:%S%z)"

    . You will be asked where you would like to save the newly created key
    . You will be prompted to enter a passphrase (space are ok)
      sshkeygen -p     To change your passphrase at any time

$HOME/.ssh/id_rsa       private key
$HOME/.ssh/id_rsa.pub   public key

PS> ssh-keygen.exe
        \___ file01         Private
        \___ file01.pub     Public
             ssh-rsa AAA.........B4d jonhdoe@server01

## ssh-key permissions
SSH will not allow connections until key is read only!

    Permissions for '.ssh/i-4644gdfg6413-privatekey.pem' are too open.
    It is required that your private key files are NOT accessible by others.
    This private key will be ignored.

    Windows fix:
        1. Locate the file in Windows Explorer
           Right-click on it then select "Properties"
           Navigate to the "Security" tab and click "Advanced"
        2. Change the owner to you
           Disable inheritance 
           Delete all permissions
           Grant yourself "Full control"
           Save the permissions
        Now SSH won't complain about file permission too open anymore

chmod 400 ~/.ssh                400 = readonly
chmod 700 ~/.ssh
chmod 644 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
chmod 644 ~/.ssh/config
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/github_rsa
chmod 644 ~/.ssh/github_rsa.pub

### Step 2: Copying Your Personal Key To The Server
cd ~/.ssh 
cp id_rsa.pub authorized_keys      add public key to the local 'authorized_keys' file
If existing 'authorized_keys' file, add the key manually to the 'authorized_keys' file 

Copy your public key to the server
Every user on the server has their own .ssh directory and their own authorized_keys file.
/root/.ssh is the root user’s ssh files 

cd ~/.ssh 
I want to use that key to connect as root using SSH:
scp authorized_keys root@host.servername.com:/root/.ssh/   
If the authorized_keys exists on the server, add the new key to the file manually
chmod 0700 /home/youruser/.ssh/

ssh nom_utilisateur@ip_ou_nom_machine -p numero_de_port
ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name

### Step 3: Logging In With Your New Key
ssh user@host.domain.com
ssh root@host.servername.com

## authorized_keys file

/home/[you]/.ssh/authorized_keys

Each row has a public key to authorize this account access witha private key
$ nano authorized_keys
ssh-dss AAAAB3NzaC1kc3MAAACBAO0ZWeTNYwTkNuj ... CF7sro/Q== account@machine
ssh-dss AAAAB3NzaC1kc3MAAACBAO0ZWeTNYwTkNuj ... CF7sro/Q== joe@pc-sport

download.page(security/known_hosts.md)

## SSH key fingerprint
It is the fingerprint of a key that is verified when you try to login to a remote computer using SSH
Adding the fingerprint from a remote serve to a local machine:
>ssh-keyscan -H 192.168.1.162 >> ~/.ssh/known_hosts

Only work properly if you have ssh key authentication setup. Otherwise, you'd have to enter the remote machine's password.

### FILE TRANSFER: SCP-SECURE COPY 
    Remote file copy program

    Transfer local--> server
    scp -i ~\.ssh\i-029b44db36e034bd1.pem  I:\_langs\python-flask\02_routing\main.py ec2-user@ec2-9-127-170-46.eu-west-2.compute.amazonaws.com:/var/www/html
    main.py  


	Copy something from another system to this system:
	scp username@hostname:/path/to/remote/file /path/to/local/file

	Copy something from this system to some other system:
	scp /path/to/local/file username@hostname:/path/to/remote/file          

	Copy something from some system to some other system:
	scp username1@hostname1:/path/to/file username2@hostname2:/path/to/other/file  


	scp [-12346BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-S program] [[user@]host1:]file1 ... [[user@]host2:]file2

	scp file.txt server2:/tmp
    
download.page(web/networks/tools/rsync.md)
    

    From your local windows10-ubuntu bash use this command:

	for download: (from your remote server folder to d:/ubuntu):	scp username@ipaddress:/folder/file.txt /mnt/d/ubuntu
	Then type your remote server password if there is need.

	for upload: (from d:/ubuntu to remote server ) :	       	     scp /mnt/d/ubuntu/file.txt username@ipaddress:/folder/file.txt    

## SSH Servers

https://codeburst.io/direct-connection-to-a-docker-container-with-ssh-56e1d2744ee5


## SSH clients

A program which uses the secure shell protocol to connect to a remote computer. 

Windows
* PuTTY http://www.chiark.greenend.org.uk/~sgtatham/putty/
* MobaXterm

# OpenSSH - OpenBSD Secure Shell   

Tools based on the SSH protocol, which provides a secure channel over an unsecured network in a client–server architecture
A suite of programs that serve as alternatives to unencrypted protocols like Telnet and FTP.

Windows 10 uses OpenSSH as its default SSH client and SSH server  
https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview

**Command-line utilities and daemons:**

* scp, a replacement for rcp.
* sftp, a replacement for ftp to copy files between computers.
* ssh, a replacement for rlogin, rsh and telnet to allow shell access to a remote machine.
* ssh-add and ssh-agent, utilities to ease authentication by holding keys ready and avoid the need * to enter passphrases every time they are used.
* ssh-keygen, a tool to inspect and generate the RSA, DSA and elliptic-curve keys that are used  for user and host authentication.
* ssh-keyscan, which scans a list of hosts and collects their public keys.
* sshd, the SSH server daemon (server for ssh connections)
* sshd.exe            which is the SSH server component that must be running on the system being managed remotely
* ssh.exe             which is the SSH client component that runs on the user's local system
* ssh-keygen.exe      generates, manages and converts authentication keys for SSH
* ssh-agent.exe       stores private keys used for public key authentication
* ssh-add.exe         adds private keys to the list allowed by the server
* ssh-keyscan.exe     aids in collecting the public SSH host keys from a number of hosts
* sftp.exe            is the service that provides the Secure File Transfer Protocol, and runs over SSH
* scp.exe             is a file copy utility that runs on SSH

* stunnel             https://www.stunnel.org/ proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code
## FORWARDING 

* Local forwarding 

* Remote forwarding 

- https://www.youtube.com/watch?v=ZFp-FKPpUQc&feature=youtu.be
- https://www.youtube.com/watch?v=M0eEwqUpKDc&t=698s

## SECURITY

>docker scan 

https://docs.docker.com/engine/scan/

## SSH connection Windows- Linux using PuTTY

1. how to configure the SSH daemon on the Linux side
/etc/ssh/sshd_config
systemctl status sshd
systemctl start sshd

2. how to set up a remote console connection

Putty install: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
Host Name (or IP address)
Port 22

PuTTY Security Alert to prevent a man-in-the-middle attack: The fingerprint in the message should match the key on the Linux system at /etc/ssh/ssh_host_ed25519_key.pub  
PuTTY prints the key as an MD5 hash. To check its authenticity, switch to the Linux system, open a command shell, and enter:
>ssh-keygen -l -E md5 -f /etc/ssh/ssh_host_ed25519_key.pub

The host system's fingerprint is now in PuTTYs trust list: HKEY_CURRENT_USER\SOFTWARE\SimonTatham\PuTTY\SshHostKeys
Enter your correct login credentials

3. how to copy files over the network
C:\Program Files (x86)\PuTTY\pscp.exe to copy files to and from a Linux system
pscp.exe <source> <target> 

Copy Linux user home/MyFile.txt to your Windows home
C:\"Program Files (x86)"\PuTTY\pscp.exe stephan@192.168.1.60:/home/stephan/MyFile.txt .
Copy from Windows home to Linux user home
C:\"Program Files (x86)"\PuTTY\pscp.exe MyFile.txt stephan@192.168.1.60:/home/stephan/

4. how to tunnel a certain protocol over SSH


https://docs.gitlab.com/ee/ssh/













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

Algorithm | Public key | Private key
---|---|---
ED25519 (preferred) | id_ed25519.pub | id_ed25519
RSA (at least 2048-bit key size) | id_rsa.pub | id_rsa
DSA (deprecated) | id_dsa.pub | id_dsa
ECDSA | id_ecdsa.pub | id_ecdsa