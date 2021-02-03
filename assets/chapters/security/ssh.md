# SSH - SECURE SHELL 

Protect data transferred through remote connections
A cryptographic network protocol for operating network services securely over an unsecured network. Typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.

Windows 10 uses OpenSSH as its default SSH client and SSH server

ssh nom_utilisateur@ip_ou_nom_machine -p numero_de_port
ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name
                                                                             
## Have a SSH Directory

mkdir -p $HOME/.ssh chmod 0700 $HOME/.ssh

C:\Users\&lt;you&gt;\.ssh
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
stronger key:
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

/home/&lt;user&gt;/.ssh/authorized_keys

Each row has a public key to authorize this account access witha private key
$ nano authorized_keys
ssh-dss AAAAB3NzaC1kc3MAAACBAO0ZWeTNYwTkNuj ... CF7sro/Q== account@machine
ssh-dss AAAAB3NzaC1kc3MAAACBAO0ZWeTNYwTkNuj ... CF7sro/Q== joe@pc-sport
 
## known_hosts file

~/.ssh/known_hosts
/home/&lt;user&gt;/.ssh/known_hosts

Public keys of all ssh servers to which the user has been connected
From the server folder /etc/ssh/ssh_host_dsa_key.pub

Contains rows, each is a server public key the user connect to
    github.com,192.30.253.112 ssh-rsa AAAA...AaQ=
    192.30.253.113 ssh-rsa AAAA...Q=
    140.82.118.3 ssh-rsa AAAA...Q=
    140.82.118.4 ssh-rsa AAAA...aQ=
    ec2-15-256-926-822.eu-west-3.compute.amazonaws.com,15.222.333.404 ecdsa-sha2-nistp256 AAAA...V0=
    vps47217.inhosting.com,173.235.215.56 ecdsa-sha2-nistp256 AAAA...TBARs=
    vps47217.inhosting.com,173.145.215.11 ecdsa-sha2-nistp256 AAAA...TDFbRs=

## SSH key fingerprint
It is the fingerprint of a key that is verified when you try to login to a remote computer using SSH
Adding the fingerprint from a remote serve to a local machine:
>ssh-keyscan -H 192.168.1.162 >> ~/.ssh/known_hosts

Only work properly if you have ssh key authentication setup. Otherwise, you'd have to enter the remote machine's password.

### FILE TRANSFER: SCP-SECURE COPY 
    Remote file copy program

    Transfer local--> server
    scp -i ~\.ssh\i-029b44db36e034bd1.pem  I:\_langs\python-flask\02_routing\main.py ec2-user@ec2-3-10-170-46.eu-west-2.compute.amazonaws.com:/var/www/html
    main.py  


	Copy something from another system to this system:
	scp username@hostname:/path/to/remote/file /path/to/local/file

	Copy something from this system to some other system:
	scp /path/to/local/file username@hostname:/path/to/remote/file          

	Copy something from some system to some other system:
	scp username1@hostname1:/path/to/file username2@hostname2:/path/to/other/file  


	scp [-12346BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-S program] [[user@]host1:]file1 ... [[user@]host2:]file2

	scp file.txt server2:/tmp
	rsync	Secure copy file.txt to remote host /tmp folder
	rsync	
	rsync -a /home/apps /backup/	Synchronize source to destination

    From your local windows10-ubuntu bash use this command:

	for download: (from your remote server folder to d:/ubuntu):	scp username@ipaddress:/folder/file.txt /mnt/d/ubuntu
	Then type your remote server password if there is need.

	for upload: (from d:/ubuntu to remote server ) :	       	     scp /mnt/d/ubuntu/file.txt username@ipaddress:/folder/file.txt    

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

https://www.youtube.com/watch?v=ZFp-FKPpUQc&feature=youtu.be