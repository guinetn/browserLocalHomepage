# OS

|---|---|
|Hardware||
||Memory, CPU, ALU, I/O devices, peripheral devices, storage devices
keyboards, mice, disk drives, printers, network adapters, display devices|
|OS||
||manager for (sharing) hardware resources. Drivers that interact with the kernel|
|Programs||
||compilers, loaders, editors, 
application program: business programs, database programs|

## kernel 

En général, le kernel est la partie qui comprend essentiellement ce qui est critique au bon fonctionnement de la machine comme l’accès au matériel, la gestion des ressources ou la sécurité. L’OS quant à lui regroupe le kernel et les programmes/bibliothèques qui sont au dessus, le runtime, comme la libc sous linux, le binaire init etc.

Pour travailler sereinement et de manière sûre, le kernel a besoin de poser des barrières entre les actions critiques et les autres. Pour cela, il le fait au niveau matériel et au niveau logiciel.

Au niveau matériel, la majorité des CPU ont des jeux d’instruction qui proposent deux modes d’exécution. Le premier est un mode privilégié dans lequel toutes les instructions sont disponibles tandis que le second est un mode non privilégié, ne donnant accès qu’à une partie des instructions.
Au niveau logiciel, le kernel s’arrange pour avoir accès aux plages mémoires de tous les processus en cours d’exécution, tout en interdisant l’accès de sa propre plage mémoire aux autre processus. La plage mémoire du kernel est appelée Kernel-Land, tandis que la plage mémoire que voit chaque processus est appelée User-Land

Multiuser --> tous les utilisateurs ont un identifiant unique appelé UID (User ID), mais il y a un UID 	qui est spécial, et qui permet d’avoir des droits plus élevés que tous les autres. 
C’est celui de l’administrateur chez windows, ou du root chez Unix, généralement le 0. 


collection inseparable pieces — hence the name — which run independently of any user/process. 
It acts as a bridge between applications and the data processing performed at the hardware level.
The kernel is the central module of an operating system (OS). It is the part of the operating system that loads first, and it remains in main memory.
loaded into a protected area of memory to prevent it from being overwritten by programs or other parts of the operating system.

is responsible for:
	Process management for application execution
	Memory management, allocation, and I/O
	Device management through the use of device drivers
	System call control, which is essential for the execution of kernel services

The kernel performs its tasks such as executing processes and handling interrupts, in kernel space, whereas everything a user normally does, such as writing text in a text editor or running programs in a GUI (graphical user interface), is done in userspace.
This separation prevents user data and kernel data from interfering with each other and thereby diminishing performance or causing the system to become unstable
system call: a process makes a request of the kernel
IPC (interprocess communication): Kernels methods for synchronization and communication between processes

### KERNEL MODE
Processor execute code having limited access to components/memory
For basic and safe operations
### USER MODE
Executed code have not access to components/memory
Delegate it to system API

### Virtual memory
La mémoire physique est divisée en frames
La mémoire virtuelle en pages

Lorsqu’un processus a besoin d’espace mémoire, il demande à la mémoire physique de lui allouer des pages. 
C’est la table de pages qui fait le lien entre les pages et les frames, avec une table de pages par processus.

- https://beta.hackndo.com/le-monde-du-kernel/
https://beta.hackndo.com/rappels-d-architecture/

::::
download.md(assets/slides/computer_science/os_posix.md)
::::
download.md(assets/slides/computer_science/os_linux.md)
::::
download.md(assets/slides/computer_science/os_windows.md)
::::
download.md(assets/slides/computer_science/os_unix.md)
::::
download.md(assets/slides/computer_science/os_unix-bash.md)
