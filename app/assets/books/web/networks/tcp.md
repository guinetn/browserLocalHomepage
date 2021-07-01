### TCP - Transmission Control Protocol
A connection-based protocol that provides a reliable flow of data between two computers.
Example: HTTP, FTP, Telnet
Use socket

TCP job is merely to take a stream of messages produced by one HOST and reproduce the stream on a remote receiving HOST without change.
TCP breaks data into packets and distribute them. Those packets travel from router to router over the Internet. During this time the IP protocol is in charge of the addressing and forwarding of those packets. At the end, TCP reassembles the packets to their original state.

Don't use datagram (see UDP)
Use TCP segment:
| Port Source | Port Destination | ??? | Flags | ??? | Checksum | ??? | Données à envoyer |

- https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip/855085-cest-quoi-une-application