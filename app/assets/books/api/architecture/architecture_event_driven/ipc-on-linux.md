# IPC - INTER-PROCESS-COMMUNICATION

Getting one software process to talk to another software
To monitor an action being performed by a peripheral or over a network; or to detect a signal from some other source, when your software relies on something outside of its own code to know what to do next or when to do it, you need to think about inter-process communication (IPC).

Linux kernel features several IPC methods
[util-linux](https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/) package contains some commands for monitoring and managing IPC messages:

- ipcmk

- ipcrm

- ipcs: view current activity in each of those subsystems
    ------ Message Queues --------
    key        msqid      owner      perms      used-bytes   messages

    ------ Shared Memory Segments --------
    key        shmid      owner      perms      bytes      nattch     status

    ------ Semaphore Arrays --------
    key        semid      owner      perms      nsems
    0x00000000 1245184    apache     600        1
    0x00000000 1277953    apache     600        1
    0x00000000 1310722    apache     600        1
    0x00000000 1343491    apache     600        1
    0x00000000 1376260    apache     600        1
    
    no messages or no shared memory segments, but a number of semaphore arrays are in use.

- lsipc:  what IPC facilities are already on your system
    Here, 3 different IPC mechanisms (each available in the Linux kernel): 
    - messages (MSG)
    - shared memory (SHM)
    - semaphores (SEM)
    RESOURCE DESCRIPTION                                              LIMIT USED  USE%
    MSGMNI   Number of message queues                                 32000    0 0.00%
    MSGMAX   Max size of message (bytes)                               8192    -     -
    MSGMNB   Default max size of queue (bytes)                        16384    -     -
    SHMMNI   Shared memory segments                                    4096    0 0.00%
    SHMALL   Shared memory pages                       18446744073692774399    0 0.00%
    SHMMAX   Max size of shared memory segment (bytes) 18446744073692774399    -     -
    SHMMIN   Min size of shared memory segment (bytes)                    1    -     -
    SEMMNI   Number of semaphore identifiers                          32000    5 0.02%
    SEMMNS   Total number of semaphores                          1024000000    5 0.00%
    SEMMSL   Max semaphores per semaphore set.                        32000    -     -
    SEMOPM   Max number of operations per semop(2)                      500    -     -
    SEMVMX   Semaphore max value                                      32767    -     -

## More
- https://opensource.com/article/20/1/inter-process-communication-linux