## WOL - Wake-on-LAN

WakeOnLan (or for short just WOL) is a mechanism with which a network Interface Card (NIC) could turn a machine on by receiving a special packet through the LAN.

While your computer is Turned Off, The Network Interface Card remains on and looks forward to hearing a message! More accurately, a packet does, which is called a magic packet. Whenever the card receives information, a magic packet tries to switch on the computer. This packet must contain a certain byte-sequence, but can be encapsulated in any kind of packet (IPX, IP, anything). So the mechanism relies on the Hardware's ability, and that's why we need some ingredients!

ipconfig /all
Adresse physique . . . . . . . . . . . : AC-2B-6E-68-6E-73    ← MAC address