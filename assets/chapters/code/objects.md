### VARIABLE

a named quantity
have to be initialized
allow you to save data and reuse that data while a program runs
can be made from custom types (objects) that include both data and functionality

### FUNCTION, METHOD, PROCEDURE, SUBROUTINES

a callable sub-program within a larger program

### FUNCTION

return values

Function expression 	produces a value
Function statement 	    performs an action

### HIGHER-ORDER-FUNCTIONS

Functions that take functions as an argument. 
Used in functional languages 

### PURE FUNCTION

Always returns the same result for same argument values 
No side effects like modifying an argument (or global variable) or outputting something.

    C++ functions are pure:
    floor, returning the floor of a number;
    max, returning the maximum of two values.
    void f() {
        static std::atomic<unsigned int> x = 0;
        ++x;
    }

impure:
    void f() { ++x; } // because of mutation of a non-local variable


### METHOD

Function associated with an object (class)

### PROCEDURE
Function that don't return values 
Pascal 

### FUNCTION COMPOSITION 

Mechanism to combine simple functions to build more complicated ones. 
Like the usual composition of functions in mathematics, the result of each function is passed as the argument of the next, and the result of the last one is the result of the whole.
Not to be confused with object composition
Composition 	(f⋅g⋅h)(x) ←→ f(g(h(x)))

### FACTORY FUNCTION

In JavaScript, any function can instantiate and return objects. 
When you do so without a constructor, it’s called a factory function. 
`class` can’t compete with the power and flexibility of factories 

The bottom line: Class doesn’t give you any power that isn’t already supplied by factory functions and 
the prototypal OO built into the language. All you’re doing when you create a class is opting into a 
less powerfull, less flexible mechanism and a whole lot of pitfalls and pain.

### CURRYING 

Breaking a multiple args function into a series of nesting functions. 
Each nesting function expect to have the next argument(s) to the function

Make functions more flexible. With a curried function, you can pass all of the arguments that the function is expecting and get the result, or you can pass only a subset of arguments and receive a function back that waits for the rest of the arguments.

Partially apply (or curry) functions to create new functions

Composition 	(f⋅g⋅h)(x) ←→ f(g(h(x)))
Currying		f(x, y)	  ←→ f(x)(y)

```js
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
var curriedAdd = addition(2);
curriedAdd(3);



function add(a,b,c) { return a+b+c; }  
function curriedAdd(a) {  
    return function(b) {
        return function(c) {
        return a+b+c;
        }
    }
}   
var curriedAdd1 = curriedAdd(2);
var curriedAdd2 = curriedAdd1(3);
curriedAdd2(4);


Curry Factory Method(ES6)
const compose = (...fns) =>
    fns.reduce((f, g) => (...args) => f(g(...args)));


const func1 = () => console.log ('Hey');
const firstClassfunc1 = argsFunc => argsFunc();
const firstClassfunc2 = () => func1;
firstClassfunc1 (firstClassfunc2()); // Hey Medium.


var myFirstCurry = function(word) {
    return function(user) {
            return [word, ", " , user].join("");
    };
};
var HelloUser = myFirstCurry("Hello");
HelloUser("Rahul"); // Output: "Hello, Rahul"
// Original curried function can be called directly by passing each of the parameters
myFirstCurry("Hey, wassup!")("Rahul"); // Output: "Hey, wassup!, Rahul"

 


```

Usages
* Function composition.e.g., p(x) = q(r(x))
* Memoization is another good use case for curry function.
* Handling error throwing functions and exiting immediately after an error.
* Catching multiple error and use it as a validator on API’s and client side code.
* Can create First class functions which means that we can use functions as arguments and return values. Eg:


### SUBROUTINES

Invoked once and executes until it completed
Can be translated to a coroutine which does not call yield
FORTRAN 

### COROUTINE

Function that has the ability to pause execution and return control
but then to continue where it left off on the following frame. 

Can control where execution continues immediately after they yield, while generators cannot, instead transferring control back to the generator's caller.

Generalized form of subroutines.
can be entered, exited, and resumed at many different points.
can pause execution and yield control back to the caller or another coroutine. The caller can then resume the coroutine when appropriate.
used for cooperative multitasking and are often compared to fibers, lightweight threads and green threads

// C# coroutine
IEnumerator Fade() {
    for (float f = 1f; f >= 0; f -= 0.1f) {
        Color c = renderer.material.color;
        c.a = f;
        renderer.material.color = c;
        yield return;
    }
}

use cases:

data structure iterators
event-driven code without the inversion of control
cooperative multitasking
concurrency frameworks such as actors, async-await and dataflow networks
expressing asynchrony, and better composition of asynchronous systems
capturing continuations
expressing backtracking algorithms
AI agents such as behavior trees

Coroutines are computer program components that generalize subroutines to allow multiple entry points
for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing
more familiar program components such as cooperative tasks, exceptions, event loop, iterators,
infinite lists and pipes.
Coroutines are used is lexers and parsers. Without coroutines in the language or emulated somehow, lexing and parsing code needs to be mixed together even though they're really two separate concerns. But using a coroutine, you can separate out the lexing and parsing code.

### GENERATORS: lazy producer/iterator

Generalisation of subroutines, but are more limited than coroutines
Used to simplify the writing of iterators

Function whose execution is not continuous: return (yield) a value and then suspend their execution. When they're called again, they will start up from where they last suspended execution and do their thing again.
A generator is essentially a cut down (asymmetric) coroutine. The difference between a coroutine and generator is that a coroutine can accept arguments after it's been initially called, whereas a generator can't.

Pause the execution of the function and continue it later
Avoid to keep in memory thousands of data
Out a value, "pause" execution of the method and then proceed from the same point when asked for the next value.

In JS:
function* avengersGenerator() { // Declaring the generator
    yield "Hulk"; // Pausing the execution
    yield "Thor";
    yield "Iron man";
    return "Ultron"; 		// Example of finishing the generator
    yield "Spiderman";	//  Sad Thor and Spiderman wouldn't be called		   
}
const iterator = avengersGenerator(); // Creating iterator
iterator.next(); // Iterating on the generator


function* generator(i) {
    yield i;
    yield i + 1;
}
const gen = generator(1);
console.log(gen.next().value);  // 1
console.log(gen.next().value);  // 2
console.log(gen.next().value);  // undefined

Something that you can iterate over (for us, usually using for) but whose values are produced only as needed (lazily).
Ex: A list of 1 million elements...you only need to deal with them one at a time = inefficiency 
Generators are a special class of functions that simplify the task of writing iterators.
A generator is a function that produces a sequence of results instead of a single value, i.e you generate ​a series of values.

### CLOSURES

Function wih attached data, capture environment outside its scope. Function that return a function
A closure is a function returning another function
If inner function access the variables of outer function then only it is called closure.

A type of function that is linked to its referencing environment: "Environment (context) capture"
Accessing variable outside of your scope create a closure.

closure is a first-class function with free variables that are bound in the lexical environment.”
Closures are usually associated with functional programming languages, where they link a function to its referencing environment, permitting access to variables outside of the function's scope.

Usage
    
    to create private variables or functions

    Closures are a powerful tool that allow to write very elegant code	
    The returned function (the inner function) is created inside the called function (the outer function) so
    - due to the scoping rules - the inner has access to the variables and arguments of the outer (function)


https://www.code-sample.com/2015/06/closure-in-javascript.html

* SAMPLES

function ourterFun(i) {
    var x = 3;

    return function (j) {
        console.log(i + j + (++x)); // It will return the 16.
    }
}

var innerFun = ourterFun(2); 	// innerFun() function is now a closure.
innerFun(10);


Explicit closure
    var add = function (a) { 
        return function (b) { return a + b; };
    };
    var addFive = add(5);
    alert(addFive(10));


means that an inner function always has access to the vars and parameters of its outer function, even after the outer function has returned.
    
    
    a function having access to the parent scope, even after the parent function has closed.
    an outer function that returns an inner function (mechanism returning an enclosed scope on demand)

    

    var count = (function () {
                var _counter = 0;
                return function () {return _counter += 1;}
    })();
    count();
    count();
    count();
    // the counter is now 3


    * NESTED FUNCTIONS 
        Inner function can access variables and parameters of an outer function
        Outer function cannot access arguments object of inner function

        function OuterFunction() {
            var outerVariable = 1;
            function InnerFunction() {
                alert(outerVariable);
            }
            InnerFunction();
        }

    * CLOSURE (fermeture, act of closing something)
    
        Implicit closure
            var data = "hi";
            setTimeout( function() { console.log(data); }, 5000);

        Trap

            for (var i = 0; i < 5; i++) {
                setTimeout(() => console.log(i), 1000); 				// 5 5 5 5 5, not 0 1 2 3 4
            }
            If we will use let instead of var or will use ((j) => { return () => console.log(j); })(i) — the value of i will be saved by the IIFE in the new function’s scope argument j. This is so relevant because it gather some important concepts of the language — closure, context, scope, IIFE and let vs var.

            IIFE are replaced by ES6 Block !

        Explicit closure
            var add = function (a) { 
            return function (b) { return a + b; };
            };
            var addFive = add(5);
            alert(addFive(10));


        function OuterFunction() {
            var outerVariable = 100;

            function InnerFunction() {
                alert(outerVariable);
            }

            return InnerFunction;
        }
        var innerFunc = OuterFunction();
        innerFunc(); // 100

        Outer variables can keep their states between multiple calls. 
        Inner function does not keep the separate copy of outer variables but it reference outer variables, that means value of the outer variables will be changed if you change it using inner function.

### C# closures

closure is a first-class function with free variables that are bound in the lexical environment.”
Closures are usually associated with functional programming languages, where they link a function to its referencing environment, permitting access to variables outside of the function's scope. With the use of delegates, closures are available in C#.

First Class Functions: 
    a function which your language treats as a first class data type. 
    It means that you can assign a function to a variable, pass it around, and invoke it… just like a normal function. 
    In C# we can create a first class function using anonymous methods:

    Func<string,string> myFunc = delegate(string var1) {return "some value"; };
    Func<string,string> myFunc = var1 => "some value"; 	// we can do it using lambdas

    Both of those are functionally equivalent, and they just create a method that takes a string 
    and returns a string. We can call that method by invoking the variable just like we would any 
    method:
        string myVar = myFunc("something");
        This means that C# supports first class functions, yay!


I Like My Variables Free
    And so now we have first-class functions with free variables… 

    Free variable: a variable which is referenced in a function which is not a parameter of the function or a local variable of the function
    var myVar = "this is good";  // That variable isn’t a parameter, and it isn’t a local variable. So it is a free variable
    Func<string,string> myFunc = delegate(string var1) {return var1 + myVar; };
    Okay, so the anonymous delegate is referencing a variable that is in its enclosing scope. 

    static void Main(string[] args)
    {
        var inc = GetAFunc();
        Console.WriteLine(inc(5));
        Console.WriteLine(inc(6));
    }

    public static Func<int,int> GetAFunc()
    {
        var myVar = 1;
        Func<int, int> inc = delegate(int var1) {
            myVar = myVar + 1;
            return var1 + myVar;
        };
        return inc;
    }	


    class Program
    {
        static Action _closure;
        
        static void Main(string[] args)
        {
            SetUpClosure();
            _closure();     // 1 + 1 = 2
        }
        
        private static void SetUpClosure()
        {
            int nonLocal = 1;
            _closure = () => { Console.WriteLine("{0} + 1 = {1}", nonLocal, nonLocal + 1); };   // a field
        }
    }

    The "nonLocal" variable was captured, or "closed over", by the delegate code, causing it to remain in scope beyond the normal limits. In fact, it will remain available until the no further references to the delegate remain.
    the compiler generates a new, hidden class that encapsulates the non-local variables and the code you include in the anonymous method or lambda expression. The code is included in a method and the non-local variables are represented as fields. This new class's method is called when the delegate is executed.

### The automatically generated class for our simple closure is similar to the following:

    [CompilerGenerated]
    private sealed class <>c__DisplayClass1
    {
        public int nonLocal;
        
        public void <SetUpClosure>b__0()
        {
            Console.WriteLine("{0} + 1 = {1}", this.nonLocal, this.nonLocal + 1);
        }
    }
 
### Variance 

modifiers: out, in

                INVARIANCE          COVARIANCE          CONTRAVARIANCE
                ______________________________________________________
                class Box<T>        class Box<out T>    class Box<in T>    
Number          Box<Number>           Box<Number>         Box<Number>
    ↑                 X                     ↑                   ↓
    int            Box<int>               Box<int>            Box<int>

# Functor

a data structure that you can map functions over with the purpose of lifting values into a wrapper, modifying them, and then putting them back into a wrapper. It’s a design pattern that defines semantics for how fmap should work. 

purpose is to create a context or an abstraction that allows you to securely manipulate and apply operations to values without changing any original values

To safely chain functions that are applied on a value.
The Maybe monad enriches functors with the capability of handling errors.