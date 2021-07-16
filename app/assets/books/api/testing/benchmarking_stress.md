## BENCHMARKING STRESS API

https://httpd.apache.org/docs/2.4/fr/programs/ab.html
ab - L'outil de test des performances du serveur HTTP Apache

https://www.tecmint.com/linux-cpu-load-stress-test-with-stress-ng-tool/
1. stress
is a workload generator tool designed to subject your system to a configurable measure of CPU, memory, I/O and disk stress.
[autoscaling + stress ★★★](https://www.red-gate.com/simple-talk/cloud/azure/autoscaling-in-microsoft-azure)
>sudo apt-get install stress

To spawn 8 workers spinning on sqrt() with a timeout of 20 seconds
>uptime    
 17:20:00 up  7:51,  2 users,  load average: 1.91, 2.16, 1.93     [<-- Watch Load Average]
>sudo stress --cpu 8 --timeout 20
stress: info: [17246] dispatching hogs: 8 cpu, 0 io, 0 vm, 0 hdd
stress: info: [17246] successful run completed in 21s
>uptime
 17:20:24 up  7:51,  2 users,  load average: 5.14, 2.88, 2.17     [<-- Watch Load Average]

To spawn 8 workers spinning on sqrt() with a timeout of 30 seconds
>sudo stress --cpu 8 -v --timeout 30s
To spwan one worker of malloc() and free() functions with a timeout of 60 seconds
>sudo stress --vm 1 --timeout 60s 

2. stress-ng
is an updated version of the stress workload generator tool which tests your system for following features:

CPU compute
drive stress
I/O syncs
Pipe I/O
cache thrashing
VM stress
socket stressing
process creation and termination
context switching properties

- https://www.tecmint.com/tag/stress-ng/


## More
- https://www.tecmint.com/linux-cpu-load-stress-test-with-stress-ng-tool/
