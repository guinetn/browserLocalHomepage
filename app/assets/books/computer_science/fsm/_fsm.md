# FSM - Finite State Machines

State machines are composed of a set of states and transitions. The state is the status in which the system is in a given moment. The change of state (i.e. transition) of the system from one state to another needs to be triggered by a new input to the system (also referred to as an event). More formally:

States represent the internal "memory" of the system by implicitly storing information about what has happened before.
Transitions represent the "response" of the system to its environment. Transitions depend upon the current state of the machine as well as the current input and often result in a change of state.
In finite state machines, the number of states is finite. 


an abstract model of the behaviour of a system
Modelling systems using FSMs gives a tractable way to reason about the design and operation of complex systems. It offers a way to predictively evaluate the behaviour of a system when it is in a certain state, and a specific event happens. State machine models are great to design complex systems that need to handle asynchronous inputs triggered by multiple sources, as they can be easily verified in a formal way. For all of these reasons (and probably many more), finite state machines are such a great tool to design hardware systems.

they can be found anywhere. Finite state machines are used for small embedded systems (like your alarm clock), in large systems (such as your city's traffic light network), in programmable circuits such as FPGAs (you'll see is really common to implement finite state machines over FPGAs using VHDL, something I extensively did in college), and in large and complex software systems such as a blockchain network.

### More
- https://blockchain.works-hub.com/learn/finite-state-machines-e4882