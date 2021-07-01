# known_hosts file 

For verifying the identity of other systems. 
The file contains a list of public keys for all the hosts which the user has connected to.  
SSH can automatically add keys to the user's file, but they can be added manually as well. 

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
