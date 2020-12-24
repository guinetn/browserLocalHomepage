# SSH

C:\Users\&lt;you&gt;\.ssh

## ssh-key permissions
chmod 400 ~/.ssh    SSH will bot allow connections until key is read only
chmod 700 ~/.ssh
chmod 644 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
chmod 644 ~/.ssh/config
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/github_rsa
chmod 644 ~/.ssh/github_rsa.pub

### Generating public/private rsa key pair
PS> ssh-keygen.exe
        \___ file01 to      Private
        \___ file01.pub     Public
        ssh-rsa AAA....B4d jonhdoe@server01
    
C:\Users\jonhdoe\.ssh
    -a---          14/02/2017    15:50           1679 github_rsa
    -a---          14/02/2017    15:50            392 github_rsa.pub
    -a---          13/11/2020    15:50           1700 privatekey.pem
    -a---          03/03/2019    14:50           2719 root@inmotionhostring.ppk
    -a---          03/03/2019    18:27            738 root@inmotionhostring.pub
    -a---          13/11/2020    16:10           2228 known_hosts

known_hosts
    github.com,192.30.253.112 ssh-rsa AAAA...AaQ=
    192.30.253.113 ssh-rsa AAAA...Q=
    140.82.118.3 ssh-rsa AAAA...Q=
    140.82.118.4 ssh-rsa AAAA...aQ=
    ec2-15-256-926-822.eu-west-3.compute.amazonaws.com,15.222.333.404 ecdsa-sha2-nistp256 AAAA...V0=
    vps47217.inhosting.com,173.235.215.56 ecdsa-sha2-nistp256 AAAA...TBARs=
    vps47217.inhosting.com,173.145.215.11 ecdsa-sha2-nistp256 AAAA...TDFbRs=