# RDC - REMOTE DESKTOP CONNECTION

Easiest and most common method for managing a Windows server. Included in all versions of Windows server and has a built-in client on all Windows desktops

Because it is so widely used, RDP is also the target of a large number of brute force attacks on the server. Malicious users will use compromised computers to attempt to connect to your server using RDP. Even if the attack is unsuccessful in guessing your administrator password, just the flood of attempted connections can cause instability and other performance issues on your server. Fortunately, there are some approaches you can use to minimize your exposure to these types of attacks.

Changing the RDP Port
    Most brute force attacks on RDP use the default port of 3389
    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp

https://www.liquidweb.com/kb/improving-security-for-your-remote-desktop-connection/