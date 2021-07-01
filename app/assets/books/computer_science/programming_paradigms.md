# PROGRAMMING PARADIGMS

Based on the concept of
objects: which may contain data (fields, attributes)
code: in the form of procedures (often known as methods)

***Paradigm*** (=worldview, pattern, example)
In science and epistemology (the theory of knowledge), a paradigm is a distinct concept or thought pattern.
A set of practices, templates
A model, enable progress
System of assumptions (hypothèses), concepts, ways of thinking, values, practices (methodology) accepted by members of a community

* IMPERATIVE (DEFINE HOW)
Define exact steps of instr.: follow my commands in the order I give them
Allows side effects

* FUNCTIONAL         
Mutable is dangerous
Pure functions are safe (disallows side effects)

* DECLARATIVE: SQL, XSLT
You define WHAT you want (desired "end state") rather then describing exactly each step or HOW to do it.
Do this
This is what I want, I dont care how you did it
Doesnt state the order in which operations execute
Better than imperative programming (steps instruc.) for wiring up user interfaces and creating modular components.

* OBJECT-ORIENTED: C++, Java, C#, Eiffel
Groups code together with the state the code modifies

* PROCEDURAL: C, fortran, basic
Groups code into functions        

* LOGIC 
Has a particular style of execution model coupled to a particular style of syntax and grammar

* SYMBOLIC 
Programming which has a particular style of syntax and grammar


## Static Languages vs Dynamic Languages

* DYNAMIC LANGUAGES 

let you change the type of data held by the variable when the program is running;
JavaScript, PHP, and Perl

* STATIC OR “STRONGLY TYPED” LANGUAGES

you provide the type of data it will hold (such as integer, float, or string)
C++, C#, Java

Historically, computer languages have been divided into two groups: 
static languages (e.g., Fortran or C, where variables are statically typed at compile time), and dynamic languages (e.g., Smalltalk or JavaScript, where the type of a variable can change at run time). Static languages were typically compiled to produce native machine code (or assembly code) programs for the target machine, which at run time were executed directly by the hardware. Dynamic languages were executed by an interpreter, without producing machine language code.
https://hackernoon.com/why-flutter-uses-dart-dd635a054ebf

## PROGRAMMING PARADIGM (PATTERN, EXAMPLE)

The way you choose to code: functional, oo...

In science and epistemology (the theory of knowledge), a paradigm is a distinct concept or thought pattern.
A set of practices, templates
System of assumptions (hypothèses), concepts, ways of thinking, values, practices (methodology) accepted by members of a community
A worldview	
A model
Enables progress

ex: Floating buttons - the new UI paradigm

Un paradigme est une représentation du monde, une manière de voir les choses, un modèle cohérent de vision
du monde QUI REPOSE SUR UNE BASE DÉFINIE (matrice disciplinaire, modèle théorique ou courant de pensée). c´est une
forme de rail de la pensée dont les lois ne doivent pas être confondues avec celles d´un autre paradigme et qui,
le cas échéant, peuvent aussi faire obstacle à l’introduction de nouvelles solutions mieux adaptées.

“In learning a paradigm the scientist acquires theory, methods, and standards together, usually in an inextricable mixture.” Thomas S. Kuhn

## Un paradigme de programmation est en quelque sorte la manière dont nous allons écrire le code. Il existe plusieurs paradigmes de programmations qui offrent divers méthodes de pensées pour créer notre application. Il faut savoir qu'un paradigme de programmation impose littéralement une méthode de pensée afin de vous aider lors de la conception. Nous verrons ces divers paradigmes plus tard, vous comprendrez mieux. Comme la programmation procédurale, la programmation orientée objet et la programmation générique.

https://www.freecodecamp.org/news/what-exactly-is-a-programming-paradigm/
http://en.wikipedia.org/wiki/Comparison_of_programming_paradigms
a fundamental style of computer programming
The lowest level programming paradigms are machine code
The term programming paradigm refers to a style of programming. It does not refer to a specific language, but rather it refers to the way you program.
There are lots of programming languages that are well-known but all of them need to follow some strategy when they are implemented. And that strategy is a paradigm.

main differences are that imperative tells you how to do something and declarative tells you what to do.



MAJORS PARADIGM

which paradigm is the best
“All models are wrong but some are useful”
Each paradigm supports a set of concepts that makes it the best for a certain kind of problem. 
Its a good idea to know at least one multi-paradigm programming languages like Python, Java, C++ or C#.

Multi-paradigm programming language
	This means that you can, for example, write programs in an object-oriented style if you want. 
	Ex: F# is on the functional style of programming

IMPERATIVE PROGRAMMING (instruction step by step, tasks list): C, VB
follow my commands. suivez les ordres
in the order I give them
remember state
Imperative programming is about the how (steps list). Declarative programming is about the what (what we have and what we need)

DECLARATIVE PROGRAMMING (do this !, ordres): SQL
these are the facts. "Do this"
this is what I want
I don’t care how you do it
Languages: SQL, XSLT, Regular Expressions...

OBJECT-ORIENTED PROGRAMMING
keep your state to yourself
receive my messages
respond as you see fit
Languages: Smalltalk, Java, C++, C#...

FUNCTIONAL PROGRAMMING (no side effect)
All is function
Pure function            Safe, determinist: return is determined by inputs, no side effects, dont change exterior, don't change interior (static var…i++)
First class function 	 Fcts ~ args, return. Function can be an argument or returned, can be assigned to variable
First order function     No fcts as args/return
Higher order function    Have fcts as args/return
Closure 				 Function wih attached data, capture environment outside its scope. Function that return a function

mutable state is dangerous

data goes in, data comes out




























### Languages: F#, Javascript, Erlang, Clojure...

PROCEDURAL PROGRAMMING LANGUAGES
C, COBOL, PL/I, FORTAN...


## FUNCTIONAL PROGRAMMING (closures, first class functions, lambdas)




Programs by composing mathematical functions and avoids shared state & mutable data.


Functions themselves can be stored in variables and passed around as parameters to other languages
C++ has always let you pass around pointers to functions.
JavaScript make it much easier to handle functions as objects
Haskell is usually considered the best example of a functional language.

declares a set of mathematical/logical functions which define how input is translated to output. eg. f(y) = y * y. it is a type of declarative
language.
a subset of declarative languages that has heavy focus on recursion
programming by evaluating functions and functions of functions... As (strictly defined) functional programming means 	programming by defining side-effect free mathematical functions so it is a form of declarative programming but it isn´t the only kind of declarative
programming.

	basic concepts involved with functional programming:
	http://abdulapopoola.com/2014/08/18/understanding-partial-application-and-currying/
	arity: nb of arguments

	.partial application
		help cut code replication in certain scenarios
		In pure functional languages, functions are not ‘invoked’, rather a set of arguments is ‘applied’ to them. Now, if all the arguments are not passed in, then the function is being  ‘partially‘ applied.
		Partial application converts variadic functions (i.e. functions with multiple parameters) into functions of lesser arity by pre-specifying certain argument values.
		function add(a,b) {return a + b;}
		//partial application
		function increment(n) {return add.bind(null,n); }

		var add2 = increment(2);
		add2(2); //4

		var add4 = increment(4);
		add4(10); //14

	. currying
		help cut code replication in certain scenarios

		When passing functions around, sometimes we’ll want to partially apply (or curry) functions to create new functions

		Currying is a method of making functions more flexible. 
		With a curried function, you can pass all of the arguments that the function is expecting and get the result, or you can pass only a subset of arguments and receive a function back that waits for the rest of the arguments. A simple example of a curry is given below:
		http://www.infoworld.com/article/3196070/application-development/10-javascript-concepts-nodejs-programmers-must-master.html

			technique for converting function calls with N arguments into chains of N function calls with a single argument for each function call.

			Currying always returns another function with only one argument until all of the arguments have been applied. So, we just keep calling the returned function until we’ve exhausted all the arguments and the final value gets returned.

			// Normal function
			function addition(x, y) {
				return x + y;
			}
			// Curried function
			function addition(x) {
				return function(y) {
					return x + y;
				}
			}

	. function pipelines

	. recursion

	. continuations

## DYNAMIC PROGRAMMING

Used to solve optimization problems. 

Purpose of dynamic programming is to not calculate the same thing twice. 
See either "shortest/longest, minimized/maximized, least/most, fewest/greatest, “biggest/smallest"? It’s an optimisation problem.
Mastering dynamic programming is all about understanding the problem. 
- Identify all inputs/outputs
- Identify whether the problem can be broken into subproblems
- When subproblems are identified, Dynamic Programming can probably be used

Dynamic programming is a powerful technique for solving a certain class of problems, typically in a more efficient manner than the corresponding recursive strategy. Specifically, when a problem consists of “overlapping subproblems,” a recursive strategy may lead to redundant computation. The corresponding dynamic programming strategy may avoid such waste by addressing and solving the subproblems one at a time in a manner without overlap.

https://bradfieldcs.com/algos/recursion/dynamic-programming/
https://medium.freecodecamp.org/demystifying-dynamic-programming-24fbdb831d3a

*writes down "1+1+1+1+1+1+1+1 =" on a sheet of paper*
"What's that equal to?"
*counting* "Eight!"
*writes down another "1+" on the left*
"What about that?"
*quickly* "Nine!"
"How'd you know it was nine so fast?"
"You just added one more"
"So you didn't need to recount because you remembered there were eight!"

Dynamic Programming store the solution to a problem so we do not need to recalculate it. Memoisation is the act of storing a solution.

Dynamic Programming is just a fancy way to say 'remembering stuff to save time later'"

Dynamic programming is breaking down a problem into smaller sub-problems, solving each sub-problem and storing the solutions to each of these sub-problems in an array... so each sub-problem is only calculated once.

**Divide and conquer**
- **Divide** the problem into smaller sub-problems of the same type.
- **Conquer** solve the sub-problems recursively.
- **Combine** Combine all the sub-problems to create a solution to the original problem.

How do you put together a jigsaw puzzle?  You find pieces that fit together and connect
them.  What happens when you connect two big chunks of pieces together?  You get an even
bigger chunk? Dynamic Programming is the same kind of thing.  You solve the easy small problems first
(finding individual pieces that fit together), and then use the results to solve the larger problem (combining all the little pieces into the whole puzzle)

* Fibonacci sequence
```python
def F(n):
	if n<2:
		return n
	else:
		return F(n-1)+F(n-2)
```
  F(4) calculation is
          4     
      ┌───┴───┐
      3       2      F(2) is computed twice!
    ┌─┴─┐   ┌─┴─┐    Need to retain a memory of the previous calculations
    1   2   0   1  
      ┌─┴─┐
      1   0   
	  
```python
# Fibonacci sequence
def fibonacciVal(n):
	memo[0], memo[1] = 0, 1
	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]
```


* IMPERATIVE/ITERATIVE: how to do something 

sequences of commands (statements) that change a program state
from the Latin “impero” meaning “I command”
the order of the steps is crucial, because a given step will have different consequences depending on the current values of variables when the step is executed.

## imperative language
C, C++, Java
series of instructions that the computer executes in sequence (do this, then do that).
The focus is on what steps the computer should take rather than what the computer will do
The traditional "step by step recipe" approach
Program is structured out of instructions describing how the operations performed by a computer will happen.
how to achieve our goal
		Take the next customer from a list.
		If the customer lives in Spain, show their details.
		If there are more customers in the list, go to the beginning

PROCEDURAL
allows splitting ordered instructions into procedures.
specifies the steps the program must take to reach the desired state
C C++ Java ColdFusion Pascal

Procedures aren't functions. The difference between them is that functions return a value, and procedures do not. More specifically, functions are designed to have minimal side effects, and always produce the same output when given the same input. Procedures, on the other hand, do not have any return value. Their primary purpose is to accomplish a given task and cause a desired side effect.

A great example of procedures would be the well known for loop. The for loop's main purpose is to cause side effects and it does not return a value.

OBJECT-ORIENTED
	organizes programs as objects: data structures consisting of datafields and methods together with their interactions.
	data, and methods manipulating data are kept as a single unit called an object
	a program = a collection of interacting objects
	C++, C#, Java

PARALLEL PROCESSING APPROACH
	Parallel processing is the processing of program instructions by dividing them among multiple processors.

	A parallel processing system allows many processors to run a program in less time by dividing them up.

	Languages that support the Parallel processing approach:

	NESL (one of the oldest ones)
	C
	C++

* DECLARATIVE: what to do

programs describe their desired results without explicitly listing commands or steps that must be performed
defines computation logic without defining its control flow
Instructing a program on what needs to be done, instead of telling it how to do it. this involves providing a domain-specific language (DSL) for expressing what the user wants
ex: Angular. DP (do this) is better than IT programming (steps instructions)
Most successful declarative programming tool is the relational database (RDB): SQL is the DSL that hides the lower level layer from the user
https://www.toptal.com/software/declarative-programming

## DECLARATIVE LANGUAGE
	
SQL
declares a set of rules about what outputs should result from which inputs (eg. if you have A, then the result is B). An engine will apply these rules
to inputs, and give an output.
	The focus is on what the computer should do rather than how it should do it
"this is what i want, now you work out how to do it".
Your program is a description either of the problem or the solution - but doesn´t explicitly state how the work will be done.
	what we want to achieve
		Show customer details of every customer living in Spain

FUNCTIONAL
	Do everything with functions: input -> output
	sequence of stateless function evaluations
	all functions are without side effects, and state changes are only represented as functions that transform the state
	treats computation as the evaluation of mathematical functions and avoids state and mutable data

	.use pures functions, no bord effects
	.write apps from only functions
	.function is a data type (like int...)
	.Dont use vars, only ctes
	. there are no for and while loops in functional programming. Instead, functional programming languages rely on recursion for iteration

	Haskell OCaml Scala Clojure Racket JavaScript 

LOGIC

SYMBOLIC

Database processing approach