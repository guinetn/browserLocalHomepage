### PROCESSORS - CPU

* RISC-V
New 
Ppen source architecture 
Norme ISA (Instruction Set Architecture)
Simplify central processor, dedicated co-rpocessors 

* ARM - Advanced RISC Machine
Family of reduced instruction set computing (RISC) architectures for computer processors
power efficiency (not too much heat). 
technology of choice for passively-cooled, battery-powered mobile devices
mobile-friendly: smartphones
Cortex-A9	
M1 		Apple 
ARM SoC (Advanced RISC Machines - System on a Chip, which includes the CPU, the GPU and the MMU, etc.)

* AMD
Ryzen 5000   16 coeurs, 7nm
             architecture Zen 3
Ryzen 9 5980HS 35 watts
        5900HX 5980HX 45 watts

* x64 	x86/x64 processors are CISC (Complex Instruction Set Computing: many instructions set)

* x86

## CPU Architecture

A CPU is the main processor of a computer that executes the instructions of a program. In this case, it consists of various bits of state, described below, and an instruction cycle with fetch, decode, and execute steps.

#### Memory
4 kilobytes of memory (RAM)
#### Program counter
address of the current instruction as an 16-bit integer. Every single instruction in Chip-8 will update the program counter (PC) when it is done to go on to the next instruction, by accessing memory with PC as the index.
#### Registers
Memory is generally used for long-term storage and program data, so registers exist as a kind of "short-term memory" for immediate data and computations. Chip-8 has 16 8-bit registers. They're referred as V0 through VF.
#### Index register
special 16-bit register that accesses a specific point in memory, referred to as I. The I register exists mostly for reading and writing to memory in general, since the addressable memory is 16-bit as well.
#### Stack
to go into subroutines, and a stack for keeping track of where to return to. The stack is 16 16-bit values, meaning the program can go into 16 nested subroutines before experiencing a "stack overflow".
#### Stack pointer (SP)
is an 8-bit integer that points to a location in the stack. It only needs to be 8-bit even though the stack is 16-bit because it's only referencing the index of the stack, so only needs to be 0 thorough 15.
#### Key input
#### Graphical output
#### Timers

#### CoreMark
CPU benchmarking tool
Based on basic cpu pipeline functions (r/w, control)
