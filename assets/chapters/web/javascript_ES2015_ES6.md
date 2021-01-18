# ES6 (ECMAScript 2015) Features

Modules, classes, portée lexicale au niveau des blocs, itérateurs et générateurs, promesses pour la programmation asynchrone, patrons de destructuration, optimisation des appels terminaux, nouvelles structures de données (tableaux associatifs, ensembles, tableaux binaires), support de caractères Unicode supplémentaires dans les chaînes de caractères et les expressions rationnelles, possibilité d'étendre les structures de données prédéfinies.
- http://www.ecma-international.org/ecma-262/6.0/

## ES6 → ES5
- [traceur.js](https://github.com/google/traceur-compiler/wiki/Getting-Started)
- [Babel](https://babeljs.io/)
>[1, 2, 3].map((n) => n + 1); // Babel Input: ES2015 (ES6) arrow function  
>[1, 2, 3].map(function(n) { return n + 1;});  // Babel Output: ES5 equivalent

## ARROWS: No binding of ‘this’

Share the same lexical this as their surrounding code
Preserve the lexical value of this (ie static binding to current object, not context based)
It doesn’t create a new scope as normal functions do. Instead, it Shares the same scope with its first outer function. It helps to avoid the issue with keyword ‘this’ not being the object that is intended.
Arrow functions are always anonymous. These function expressions are best suited for non-method functions and they can not be used as constructors.

Statements vs expressions  
a function  
* expression 	produces a value
* statement 	performs an action
		
Arrow function simplify and eliminate a common source of mistakes when referencing "this" inside an anonymous function. 
- In classic function expressions, the `this` keyword is bound to different values based on the context in which it is called. 
- In arrow functions, the `this` is `lexically bound`: It means that it uses the `this` from the code that contains the arrow function.
- `this` DOESN'T CHANGE WITH call, apply or bind, IT MAINTAIN THE BINDING OF ITS LEXICAL CONTEXT

Suited for callbacks (setTimeout). But not for object method
arrow functions don’t bind this to the object that called them. They just use the value of this in the scope in which they were defined. In this case, that’s the global object. So arrow functions are unusable for object methods!

```js

ES5  var add = function(a, b) { return a + b; }
ES6  let add = (a, b) => a + b;    

/* cleaner syntax for declaring anonymous functions (lambdas)
dropping the function keyword and the return keyword when the body function only has one expression*/
let square = x => x*x;

let pi = () => 3.1415;
console.log(square(5));
console.log(add(3, 4));
console.log(pi());


function Person(){
	this.age = 0;

	// ES5
	setInterval(function() {
	this.age++; // 'this' refers to the global object
	}, 1000);

	// ES2015
	setInterval(() => {
	this.age++; // 'this' properly refers to the person object. Arrow function inherit the value of 'this' from the context in which they are defined
	}, 1000);
}
var p = new Person();


// Expression bodies
var odds = evens.map(v => v + 1);
var nums = evens.map((v, i) => v + i);
var pairs = evens.map(v => ({even: v, odd: v + 1}));

// Statement bodies
nums.forEach(v => {
  if (v % 5 === 0)
    fives.push(v);
});

 const sum = (...args) => {
            	let sum = 0;
            	for(let i=0; i<args.length; i++)
            		sum += args[i];
            	return sum;
            }

// Lexical this
var bob = {
  _name: "Bob",
  _friends: [],
  printFriends() {
    this._friends.forEach(f =>
      console.log(this._name + " knows " + f));
  }
}
```
Why arrow functions?

Behaviour of traditional functions (context based) 
while robust is often unnecessary and a source of errors for developers not appreciating fully how "this" works or simply through carelessness. For example, the following example attempts to call the start() method of a custom object to increment its counter property by 1 every second, though it fails due to incorrect assumption of the "this" object reference:

```js
var countup = {
	counter: 0,			     
	start:function(){
		setInterval(function(){ this.counter++; }, 1000);   // **INCORRECT**- doesn't increment countup's counter property
	}
};			 
countup.start();  //  failed because `this` points to the global window object due to the context "this" is being called -inside the global window method setInterval()-
```

The result is a reference to a non existent window.counter property that will repeatedly return NaN when we try to increment it. 

Fix  
To properly reference the countup object then inside the anonymous function, we should cache a reference to the correct "this" object before the context changes to a different one:

```js
var countup = {
	counter: 0,			     
	start:function(){
		var countup = this; 		                          // cache reference to the countup object. `this` takes the reference of the immediate object calling the function
		setInterval(function(){ countup.counter++; }, 1000);  // NOW CORRECT- increments countup's counter property
	}
};			 
countup.start();
```

Arrow function simplify and eliminate a common source of mistakes when referencing "this" inside an anonymous function. 

The "this" object inside a arrow function is lexically bound: 

*** ITS VALUE IS STATIC AND DETERMINED BY THE SCOPE "THIS" IS DEFINED IN ***

Contrast that with regular functions, where "this" is dynamic and based on the context it's called regardless of the scope at the time "this" was defined.

```js
var countup = {
	counter: 0,			     
	start:function(){
		setInterval( () => { this.counter++; }, 1000);  // Increments countup's counter property
	}
};			 
countup.start();
```
Since the "this" object inside the arrow function is bound at the time of definition based on the scope it's part of (in this case, the countup object), the code above works right out of the box without worrying about the context in which "this" is called. 

## CLASSES: syntaxic sugar 

- No class hoisting: cannot use a class before declaring it
- ```static method``` are 'class level' (no need to create a new object of that class)
- prototype-based inheritance: extends
- constructors
- super calls
>super() refers to the parent constructor
>super.xxx refers to the parent object: property/method access
- instance methods
- static methods
- private fields, methods: #
- Getters-Setters: in class or object

class ClassWithPrivateField {
  #privateField

  constructor() {
    this.#privateField = 42
    this.#randomField = 666 // Erreur de syntaxe
  }
}

const instance = new ClassWithPrivateField()
instance.#privateField === 42 // Erreur de syntaxe
```js
/* MyComponent class accepts a DOM element and 
* implements the EventListener interface
* attaches/detaches event listeners to it automatically
*/

class Animal {
 
  // private fields
  static #count = 0
  #count2 = 0

  constructor(name) {
	this.name = name;  //  or this._name = name; 
	// prefixed underscore are just convention for private fields
	this.#count += 1;
  }
  present() {
    return `I'm ' + ${this.name}`;
  }
  
  // private method
  #privateMethod() {
    return 40;
  }
  static #privateStaticMethod() {
    return 50;
  }

  // Getters-Setters: in class or object
  #message
  get #decoratedMessage() {
    return `✨${this.#message}✨`
  }
  set #decoratedMessage(msg) {
    this.#message = msg
  }
}    

const instance = new Animal('xxx')
instance.#count = 42 // Error

class Cat extends Animal {
  constructor (name, el) {
	super('joe');
    this.el = el
    this.el.addEventListener('click', this)
  }
  handleEvent (event) {
	super.handleEvent(event);
    console.log('cat element was clicked')
  }
  destroy () {
    this.el.removeEventListener('click', this)
  }
  static defaultName(){          
    return 'John';
  }
}  

const cat = new Cat('paul', document.querySelector('button'));
```

```js

```

## ENHANCED OBJECT LITERALS

Object literals are extended to support setting the prototype at construction, shorthand for foo: foo assignments, defining methods, making super calls, and computing property names with expressions. Together, these also bring object literals and class declarations closer together, and let object-based design benefit from some of the same conveniences.
```js

Skip key-pair like ‘name : name’ to make it look cleaner.

function createPony () {
	const name = 'Rainbow Dash ';
	const color = 'blue ';
	return
	{ name: name, color: color }; 
	{ name , color };  // when pty to create has the same name as the var
}

(function() {
	var name = 'Manish';
	var age = 25;

	var person_oldWay = {
		name: name,
		age: age,
		log: function() {
			console.log('I am an object');
		}
	}

	var person_ES6 = {
		name, age,
		log(x) {
			console.log('I am a cleaner ES6 Object');
		}
	}

	person_oldWay.log();
	person_ES6.log();
})();
// I am an object
// I am a cleaner ES6 Object
		
var obj = {
    // __proto__
    __proto__: theProtoObj,
    // Shorthand for ‘handler: handler’
    handler,
    // Methods
    toString() {
     // Super calls
     return "d " + super.toString();
    },
    // Computed (dynamic) property names
    [ 'prop_' + (() => 42)() ]: 42
};
```

## TEMPLATE STRINGS: string interpolation 

```js
var name = "Bob", time = "today";
console.log(`Hello ${name}, how are you ${time}?`);
```

## DESTRUCTURING

binding with pattern on arrays and objects matching 

Easily store in variables extracted values from arrays and objects (even deeply nested) 

```js
// list matching
var [a, , b] = [1,2,3];

// object matching
var { op: a, lhs: { op: b }, rhs: c }
       = getASTNode()

// object matching shorthand
// binds `op`, `lhs` and `rhs` in scope
var {op, lhs, rhs} = getASTNode()

// Can be used in parameter position
function g({name: x}) {
  console.log(x);
}
g({name: 5})

// Fail-soft destructuring
var [a] = [];
a === undefined;

// Fail-soft destructuring with defaults
var [a = 1] = [];
a === 1;



* DESTRUCTURING ARRAYS

shorthand syntactic sugar to assign variables from items in an array
Destructuring then takes items in the array at corresponding indexes and assigns them to the variables in the square brackets []
let [firstVar, secondVar, thirdVar] = [100,150,200];

var arr = [1, 2, 3, 4];		
ES5			var a = arr[0]; var b = arr[1]; var c = arr[2]; var d = arr[3];
ES6 		let [a, b, c, d] = [1, 2, 3, 4];
console.log(a, b); // 1 2

Old:
	let items = [1, 2];
	let one = items[0], two = items[1];

es6:	
	let items = [1, 2];
	let [one, two] = items; // or = [1, 2];
	let {three, four} = {three: 3, four:  4};
	console.log(one, two, three, four); // 1 2 3 4
	// swap variables
	[one, two] = [two, one];
	
	//a variable for the remaining items 
	let [first, ...rest] = [1, 2, 3, 4];
	console.log(first); // outputs 1
	console.log(rest); // outputs [ 2, 3, 4 ]
	
	// ignore trailing elements 
	let [first] = [1, 2, 3, 4];
	let [, second, , fourth] = [1, 2, 3, 4];

* DESTRUCTURING OBJECTS

to assign variables from specific attributes on that object.

var luke = { occupation: 'jedi', father: 'anakin' };

ES5
	var occupation = luke.occupation; // 'jedi'
	var father = luke.father; // 'anakin'
ES6	
	let {occupation, father} = luke;

console.log(occupation); // 'jedi'
console.log(father); // 'anakin'

var { x, a:y, z } = { x: 1, y: 2} // x=1 a=2 z=undefined 

Exploding args parameter into several variables
		function sayHello(args){
		let 
			name = args.firstName,
			surname = args.lastName,
			message = args.message
		;

		console.log(`${message} ${name} ${surname}`);
		}

	The args example using destructuring
		function sayHello(args){
			let {firstName: name, lastName: surname, message: message} = args;

			console.log(`${message} ${name} ${surname}`);
		}

		sayHello({firstName: 'Hendrik', lastName: 'Swanepoel', message: 'Hi there '});

		//output: Hi there Hendrik Swanepoel
		
		
let o = {
a: "foo",
b: 12,
c: "bar"
}
let {a, b} = o; // This creates new variables a and b from o.a and o.b
({a, b} = {a: "baz", b: 101}); 		// assignment without declaration
let {a: newName1, b: newName2} = o;	// renaming

* OBJECT SHORTHAND

Copying from one object to another is common task
	let genre = 'Alternative';
	let band = 'Radiohead';
	let searchRequest = {
		genre: genre,
		band: band
	};

let searchRequest = {genre, band};

var x = 12;
var y = 'Yes!';
var z = { one: '1', two: '2' };

// The old way:
var obj = {x: x, y: y, z: z };

var obj = { x, y, z }; // {x: 12, y: "Yes!", z: { one: '1', two: '2' } }
```

## DEFAULT ARGS

set default arguments in function which will be used as fallback when arguments are not passed in functional call

```js
function f(x, y=12) {
	// y is 12 if not passed (or passed as undefined)
  return x + y;
}
f(3) == 15


function foo(a = 10, b = 10) {
		console.log(a, b);
}

(function() {
	function otherFunc(data) {
		console.log(data);
	}
	otherFunc();
})(); // undefined

(function() {
	function otherFunc(data = 2) {
		console.log(data);
	}
	otherFunc();
})();  // 2

(function() {
	function otherFunc(data = 2) {
		console.log(data);
	}
	otherFunc(5);
})();  // 5
```

## REST (...collect remain.) 

Rest parameter: collects all remaining elements into an array.
same syntax as the spread operator, but instead of expanding an array into parameters, it collects parameters and turns them into an array. 	
can gather any number of arguments into an array
Rest parameters have to be at the last argument because it collects all remaining/ excess arguments into an array. function abc(a, ...b, c) { = error }
To extract Object properties that are not already extracted.

```js
function myFunction(...options) {
		return options;
}
myFunction('a', 'b', 'c');      // ["a", "b", "c"]


// Rest: collects remaining into an array...
function rest(x, ...y) {
	// y is an Array
  return x * y.length;
}
rest(3, "hello", true) == 6

// Concat array literals easily with this intuitive syntax:
let cities = ['San Francisco', 'Los Angeles'];
let places = ['Miami', ...cities, 'Chicago']; // ['Miami', 'San Francisco', 'Los Angeles', 'Chicago']
```

## SPREAD (...[expand into args])

Spread an array into individual elements. Replace Apply()   
Spread operator: allows iterables( arrays / objects / strings ) to be expanded into single arguments/elements. 
It is used in places where multiple arguments or variables are expected

```js

// Spread: array exploDE
(function() {
	var arr = [1, 2, 3];
	console.log(arr);
	console.log(...arr);
})();
// [1, 2, 3]
// 1 2 3

Copying arrays
const arr = [1, 2, 3];
const arr2 = [...arr];  // any changes done to arr2 will not have any effect arr

Pass elements of an array to a function as separate arguments
function add(a, b, c) { return a + b + c ; }
const args = [1, 2, 3];
add(...args);

const arr = [1, 2, 3, 4, 5];
const add = (...args) => args.reduce((a, b) => a + b, 0);
console.log(add(...arr));

function spread(x, y, z) {
  return x + y + z;
}
// Pass each elem of array as argument
spread(...[1,2,3]) == 6

// Find the max of values in an array
ES5: Math.max.apply(null, [-1, 100, 9001, -32]); // 9001
ES6: Math.max(...[-1, 100, 9001, -32]); // 9001

```

## LET VARIABLES

- block-scoped (only exist in the blocks they are defined in)
- Not hoisted like 'var': cannot be referenced before used

let 	is the new var. Visible only inside block 		 					for( let i = 0; i < 5; i++ ) …
		let variables can have local scope with-in {} brackets 
		Replacing iifes with blocks
var 	visible inside & outside block
		for( var i = 0; i < 5; i++ ) …
		Variables declared with ‘var’ keyword have functional scope 

```js
{
	let a = 1;
	const b = 1;
}
console.log(a); // ReferenceError
console.log(b); // ReferenceError

(function() {
	var count = 5;
	if (true) {
		let count = 2;
		console.log('lcount : ' + count);
	}
	console.log('vcount : ' + count);
})(); // 2 5

(function() {
	for (var i = 0; i < 3; i++) {
		setTimeout(function() {
			console.log(i);
		}, 1000);
	}
})(); // 3 3 3 

(function() {
	for (let i = 0; i < 3; i++) {
		setTimeout(function() {
			console.log(i);
		}, 1000);
	}
})(); // 0 1 2
```

## CONST VARIABLES

- can’t be mutated
- But you can mutate the arrays or objects assigned to variable
- block-scoped (only exist in the blocks they are defined in)
- Not hoisted like 'var': cannot be referenced before used

```js

	const nums = [1,2,3];
	nums.pop(); nums.push(4);
	[1,2,4]

	const nums = { a:1 };
	nums.a = 4;

	To avoid const mutation:
	const val = [1, 2, 3];
	Object.freeze(val);
	val[0] = 4;
	val[1] = 5;
	val[2] = 6;
	val // [1, 2, 3]

	const PONY = {};  
	PONY.color = 'blue'; // when init with an object, it can be later changed 
	PONY = {color = 'blue'} // Error: ne peux pas assigner à la constante un nouvel objet 
	
	const PONIES = [] ; 
	PONIES.push ({color : 'blue '}) ; // works
	PONIES = [] ; // Syntax Error

Its value can’t be changed but can be overridden in nested functional scope for local usage.
(function() {
		const count = 3;

		function otherFunction() {
			const count = 5;
			console.log(count);
		}
		otherFunction();
		console.log(count);
	})(); // 5 3


function createPony () {
const name = 'Rainbow Dash ';
const color = 'blue ';
return
{ name: name, color: color }; 
{ name , color };                   // ES6 shortcut when a property to create has the same name as the var
}
```

## ITERATORS + FOR..OF

Custom iteration ~ CLR IEnumerable
Iterators: a pattern for pulling data from a data source one at a time

Based on 
```js
interface IteratorResult {
  done: boolean;
  value: any;
}
interface Iterator {
  next(): IteratorResult;
}
interface Iterable {
  [Symbol.iterator](): Iterator
}
```

```js

let v of arr
js iterating through a collection with for, loop, map, filter, forEach…

let arr = [1, 2, 3, 4, 5];
let sum = 0;

for (let v of arr) { sum += v; }
console.log('1 + 2 + 3 + 4 + 5 =', sum);  // 1 + 2 + 3 + 4 + 5 = 15

Iterability
Looping through a collection and processing each item of the collection is a very common operation. 
Javascript provides a number of ways for iterating through a collection such as for loop, map, filter, forEach… 

ES6 iterator brings the concept of iterability to the language.
It’s nearly impossible (and unwise) for data consumers to support all data sources. The introduction of iterator interfaces solves the problem: Any data source that wants to be consumed by data consumers just need to implement the interface. Data consumers just use the iterator to get the values from data sources they are consuming.


## for..of loop
	
to loop over iterable objects (Arrays, strings, Maps, Sets…)

const arrayLike = { length: 2, 0: 'a', 1: 'b' };  // Array-like, but not iterable!

const iterable = ['a', 'b'];
for (const x of iterable) { console.log(x); }

Arrays and Typed Arrays are iterable.
let arr = [1, 2, 3];
for(let item of arr) {
	console.log(item); // 1 2 3
}

let x;
for (x of ['a', 'b']) { console.log(x); }

Strings are also iterables.
for(let c of "hello") {
	console.log(c); // h e l l o
}

// break and continue
for (const x of ['a', '', 'b']) {
	if (x.length === 0) break;
	console.log(x);
}


F[n] = F[n-2] + F[n-1]
const fibonacci = n =>
	Array.from({ length: n }).reduce(
	(acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
	[]
	);
fibonacci(6); // [0, 1, 1, 2, 3, 5]


### Iterable Computed Data

Some ES6 data structures such as Map, Set, Arrays have following methods that return iterables:

const set = new Set();
set.add('a');
set.add('b');
set.add('c');
for(let e of set.entries()) {
	console.log(e); //['a', 'a']
					//['b', 'b']
					//['c', 'c']
}
const m = new Map();
m.set('a', 'A');
m.set('b', 'B');
for(let pair of m.entries()) {
	console.log(pair); //['a', 'A']
						//['b', 'B']
}
const set = new Set();
set.add('a');
set.add('b');
set.add('c');
for(let e of set.keys()) {
	console.log(e); //['a' ]
					//['b']
					//['c']
}
const m = new Map();
m.set('a', 'A');
m.set('b', 'B');
for(let pair of m.keys()) {
	console.log(pair); //['a']
						//['b']
}
const set = new Set();
set.add('a');
set.add('b');
set.add('c');
for(let e of set.values()) {
	console.log(e); //['a']
					//['b']
					//['c']
}
const m = new Map();
m.set('a', 'A');
m.set('b', 'B');
for(let pair of m.values()) {
	console.log(pair); //['A']
						//['B']
}

const map = new Map([
	[false, 'no'],
	[true, 'yes'],
]);
for (const [key, value] of map) {
	console.log(`${key} => ${value}`);
}



APIs Accepting Iterables
There are APIs accepting iterables:

Map([iterable]), WeakMap([iterable]), Set([iterable]), WeakSet([iterable])
Array.from([iterable]), Promise.all([iterable]), Promise.race([iterable])
let set = new Set("abca");
let map = new Map([[1,"a"],[2,"b"],[3,"c"]]);

### Custom Iterator
In addition to the built-in iterators, we can create our own. All we need to do is adhere to above interfaces. That means we need to implement a method whose key is [Symbol.iterator]. That method must return an iterator, an object that iterate over items of the iterable.

let idGen = {
	[Symbol.iterator](){
	return this;
	},
	next(){
	return {value: Math.random(), done: false}
	}
}
let count = 0;
for(let id of idGen) {
	console.log(id);
	if (count > 4) {
	break;
	}
	count++;
}
Array-like objects are not iterable by default

let arrayLikeObj = {
	0: 'a',
	1: 'b',
	2: 'c',
	3: 'd',
	length: 4
}
for(var e of arrayLikeObj) {
	console.log(e);//TypeError: arrayLikeObj[Symbol.iterator] is not a function
}
We can make array-like objects iterable by implementing the method @@iterator:

let arrayLikeObj = {
	0: 'a',
	1: 'b',
	2: 'c',
	3: 'd',
	length: 4
	[Symbol.iterator]: Array.prototype[Symbol.iterator]
}
for(var e of arrayLikeObj) {
	console.log(e);
}
//Output:
//a
//b
//c
//d
Optional return(..) and throw(..)
The optional methods return(..) and throw(..) are not implemented in built in iterators.
return(..) is a signal to an iterator that the consumer code is complete and will not pull any value from it. This signal can be used to notified the producer to perform clean up step such as closing file handle, database, etc.

throw(..) is used to signal an exception/error to an iterator. We will take a deep look at this in Generators topic.



let fibonacci = {
  [Symbol.iterator]() {
    let pre = 0, cur = 1;
    return {
      next() {
        [pre, cur] = [cur, pre + cur];
        return { done: false, value: cur }
      }
    }
  }
}

for (var n of fibonacci) {
  // truncate the sequence at 1000
  if (n > 1000)
    break;
  console.log(n);
}
```

## GENERATORS

Something that you can iterate over (for us, usually using for) but whose values are produced only as needed (lazily).
		Ex: A list of 1 million elements...you only need to deal with them one at a time = inefficiency 

simplify iterator-authoring using function* and yield  
function* returns a Generator instance  
Generators are subtypes of iterators including next and throw  and
These enable values to flow back into the generator, so yield is an expression form which returns a value (or throws).

   Generators are a special class of functions that simplify the task of writing iterators.
        A generator is a function that produces a sequence of results instead of a single value, i.e you generate ​a series of values.

		Function pointers which can provide you play and pause like function and make synchronous code asynchronous.
		Function keyword followed by an asterisk is used to define a generator function, which returns a Generator object.
		We can exit and re-entered the generator function later on. In case of re-entrances, their context (variable bindings) will be saved.
		Important point to note here is that calling a generator function does not execute its body immediately, in fact it returns an iterator object for the function.
		In short, a generator appears to be a function but it behaves like an iterator.


```js
interface Generator extends Iterator {
    next(value?: any): IteratorResult;
    throw(exception: any);
}


function* generatorFunctionName([param[, param[, ... param]]]) {
	statements
}

function* generator(i) {
	yield i;
	yield i + 1;
}
const gen = generator(1);
console.log(gen.next().value);  // 1
console.log(gen.next().value);  // 2
console.log(gen.next().value);  // undefined




var fibonacci = {
  [Symbol.iterator]: function*() {
    var pre = 0, cur = 1;
    for (;;) {
      var temp = pre;
      pre = cur;
      cur += temp;
      yield cur;
    }
  }
}

for (var n of fibonacci) {
  // truncate the sequence at 1000
  if (n > 1000)
    break;
  console.log(n);
}


     

		function* generatorFunctionName([param[, param[, ... param]]]) {
		   statements
		}


		function* generator(i) {
		  yield i;
		  yield i + 1;
		}
		const gen = generator(1);
		console.log(gen.next().value);  // 1
		console.log(gen.next().value);  // 2

		Generate body will get executed only when the iterator’s next() method is called. Execution take place until the first yield expression, which specifies the value to be returned from the iterator or, with yield*, delegates to another generator function.
		The next() method returns an object with a value property containing the yielded value and a done property which indicates whether the generator has yielded its last value, as a Boolean.
		{ 
		  value: AnyValue,
		  done: true|false
		}
		To resume the generator function execution, we can call the next() method with an argument. This action will also results in replacing the yield expression where execution was paused with the argument from next().
		To finish the execution of the generator function, we can use the return statement. Returned value will be used to set the value property of the object returned by the generator. Any exception thrown inside the generator function, will also result in making the generator finish, unless it has been caught inside it’s body.

		GeneratorFunction constructor, or the function expression syntax can also be used to define Generator functions. However, we should keep in mind that Generators are not constructable.
		function* generatorFunction() {}
		var obj = new generatorFunction;
		// Uncaught TypeError: generatorFunction is not a constructor
		
		Once generator is finished, we will not be able to execute any of the generator’s code using subsequent next() calls. 
		They will just return an object of this form: {value: undefined, done: true}. 



		(function() {
		    function* genFunc() {
		        yield 1;
		        yield 2;
		        return 3;
		    }

		    var gen = genFunc();
		    console.log(gen.next());
		    console.log(gen.next());
		    console.log(gen.next());
		   
		    console.log(gen.next());
		})();
		// Object {value: 1, done: false}
		// Object {value: 2, done: false}
		// Object {value: 3, done: true}
		// {value: undefined, done: true}

		(function() {
		    function* genFunc() {
		        var index = 0;
		        var arr = [1, 3, 5, 7, 9, 11]
		        while (true)
		            yield arr[index++];
		    }

		    var gen = genFunc();

		    console.log(gen.next().value);
		    console.log(gen.next().value);
		    console.log(gen.next().value);
		})(); // 1 3 5

		/* In Above Example, We avoided to have
		    an global index variable to return next odd number from array */
		JavaScript is read from right to left and pause is held at yield, So one can pass any value in gen.next(value) to be assigned in left assignment ( see example below ).

		(function() {
		    function* genFunc() {
		        var arr = [1, 2, 3, 4, 5, 6];
		        var length = yield arr;
		        console.log(length);
		        return "yay";
		    }

		    var gen = genFunc();

		    var larr = gen.next().value;
		    console.log(gen.next(larr.length).value);
		})();   // 6 yay		


	    




	    http://exploringjs.com/es6/ch_generators.html

		Functions that can be paused and resumed (think cooperative multitasking or coroutines=async/await)
		.next() 		resumes execution
		yield xxx 		pauses execution

		function* is a new “keyword” for generator functions 

		4 KINDS OF GENERATORS 
			
			* GENERATOR FUNCTION DECLARATIONS
			 function* genFunc() { ··· }
			 const genObj = genFunc();
		
			* GENERATOR FUNCTION EXPRESSIONS
			 const genFunc = function* () { ··· };
			 const genObj = genFunc();
		
			* GENERATOR METHOD DEFINITIONS IN OBJECT LITERALS
			 const obj = {
			     * generatorMethod() {
			         ···
			     }
			 };
			 const genObj = obj.generatorMethod();
		
			* GENERATOR METHOD DEFINITIONS IN CLASS DEFINITIONS (class declarations or class expressions)
			 class MyClass {
			     * generatorMethod() {
			         ···
			     }
			 }
			 const myInst = new MyClass();
			 const genObj = myInst.generatorMethod();

		Use Case
			
			Iterators (implementing iterables)
			Asynchronous code 		
			Receiving asynchronous data 
			Communicating Sequential Processes (CSP) 

			Iterators (data producers)
				Each yield can return a value via next(), which means that generators can produce sequences of values via loops and recursion. Due to generator objects implementing the interface Iterable (which is explained in the chapter on iteration), these sequences can be processed by any ECMAScript 6 construct that supports iterables. Two examples are: for-of loops and the spread operator '...'
			
			Observers (data consumers)
				yield can also receive a value from next() (via a parameter). That means that generators become data consumers that pause until a new value is pushed into them via next().
			
			Coroutines (data producers and consumers)
				Given that generators are pausable and can be both data producers and data consumers, not much work is needed to turn them into coroutines (cooperatively multitasked tasks).

		write asynchronous code in a synchronous manner
		flatten our code - giving our asynchronous code a synchronous feel. 
		Generators are essentially functions which we can pause their execution and subsequently return the value of an expression.

		function* sillyGenerator() {
		    yield 1;
		    yield 2;
		    yield 3;
		    yield 4;
		}

		var generator = sillyGenerator();
		> console.log(generator.next()); // { value: 1, done: false }  // next() push our generator forward and evaluate a new expression
		> console.log(generator.next()); // { value: 2, done: false }
		> console.log(generator.next()); // { value: 3, done: false }
		> console.log(generator.next()); // { value: 4, done: false }


		// Hiding asynchronousity with Generators
		function request(url) {
		    getJSON(url, function(response) {
		        generator.next(response);
		    });
		}

		And here we write a generator function that will return our data:
		function* getData() {
		    var entry1 = yield request('http://some_api/item1'); // yield guaranteed that entry1 will have the data needed 
		    var data1  = JSON.parse(entry1);  					 // to be parsed and stored in data1
		    var entry2 = yield request('http://some_api/item2');
		    var data2  = JSON.parse(entry2);
		}

		Augmenting our Generator with Promises, we have a clear way of propagating errors through the use of our Promise 
		function request(url) {
		    return new Promise((resolve, reject) => {
		        getJSON(url, resolve);
		    });
		}

### And we write a function which will step through our generator using next which in turn will utilize our request method above to yield a Promise:

		function iterateGenerator(gen) {
		    var generator = gen();
		    (function iterate(val) {
		        var ret = generator.next();
		        if(!ret.done) {
		            ret.value.then(iterate);
		        }
		    })();
		}

		use our newly augmented Generator, it is as simple as before:

		iterateGenerator(function* getData() {
		    var entry1 = yield request('http://some_api/item1');
		    var data1  = JSON.parse(entry1);
		    var entry2 = yield request('http://some_api/item2');
		    var data2  = JSON.parse(entry2);
		});	

		write JS code with less callbacks, as it provides a way to let a piece of code stop executing, 
		while retaining it´s state (closures and stack), until something resumes it.
		Make async programming a bit more pleasant 
	 	it actually suspends code until the next function is called again, so can help us with async coding practices.

		purest use of generators: generating sequences

			generate5 object retains state and only calculates the next number as it is requested, so on demand.
			* next to the function keyword tell the JS engine that the function is a generator function
			With ES6 generators the code stops executing, regardless of the loop, as soon as we´ve returned a value 
			from the generator by using the yield keyword. It then waits until next is called on it again before it resumes execution.

			function* generate5(){
			    let i = 0;
			    while(true){
			        i += 5;
			        yield i;
			    }
			}

			let gen5 = generate5();
			for(;;){ console.log(gen5.next().value); } // 0,5,10,15,20,25,30,35…




		function* range(start, end, step) {
			while (start < end) {
				yield start;
				start += step;
			}
		}

		for (let i of range(0, 10, 2)) {
			console.log(i); 					// 0 2 4 6 8
		}






		function* add(nb) {
		}

### Ces fonctions sont spéciales parce qu'elles peuvent stopper leurs propres exécutions et retourner une valeur intermédiaire grâce au mot clé ***yield**

		function* addition() {
		  yield 1
		  yield 2
		  return 3
		}

		const add = addition()

		console.log(add.next()) // { value: 1, done: false }
		console.log(add.next()) // { value: 2, done: false }
		console.log(add.next()) // { value: 3, done: true }

		yield is working similar to return, but in a generator.

### The function containing the yield keyword is a generator. When you call it, its formal parameters are bound to actual arguments, but its body isn't actually evaluated. Instead, a generator-iterator is returned. Each call to the generator-iterator's next() method performs another pass through the iterative algorithm. Each step's value is the value specified by the yield keyword. Think of yield as the generator-iterator version of return, indicating the boundary between each iteration of the algorithm. Each time you call next(), the generator code resumes from the statement following the yield.

		function * foo(x) {
		    while (true) {
		        x = x * 2;
		        yield x;
		    }
		}
		"When you call foo, you get back a Generator object which has a next method."
		var g = foo(2);
		g.next(); // -> 4
		g.next(); // -> 8
		g.next(); // -> 16

		So yield is kind of like return: you get something back.  
		return x returns the value of x, but yield x returns a function, which gives you a method to iterate toward the next value. 

### Useful if you have a potentially memory intensive procedure that you might want to interrupt during the iteration.
```

## UNICODE

Support full Unicode  
Unicode literal form in strings and new RegExp u mode to handle code points, as well as new APIs to process strings at the 21bit code points level. 

```js

// same as ES5.1
"𠮷".length == 2

// new RegExp behaviour, opt-in ‘u’
"𠮷".match(/./u)[0].length == 2

// new form
"\u{20BB7}"=="𠮷"=="\uD842\uDFB7"

// new String ops
"𠮷".codePointAt(0) == 0x20BB7

// for-of iterates code points
for(var c of "𠮷") {
  console.log(c);
}
```

## MODULES

	<script type="module" src="js/app.js"></script>
		__________________________/
		/
	app.js
		import * as assets from "./addons.js"
									/
			________________________/
			/
	addons.js                
		export const assets = `not used`;

Modules are singletons. Even if a module is imported multiple times, only a single “instance” of it exists.
Modules import things from other modules
	Relative paths 	'../model/user' 	The file extension .js can usually be omitted.
	Absolute paths  '/lib/js/helpers' 
	Names  			'util' 				What modules names refer to has to be configured.

Each module is a piece of code that is executed once it is loaded.
In that code, there may be declarations (variable declarations, function declarations, etc.).
By default, these declarations stay local to the module.
You can mark some of them as exports, then other modules can import them.

Prior to ES6
	client-side:  Browserify library to create modules 
	server-side:  require() in Node.js


import with curly brackets {} if importing/exporting multiple functions/classes
	import { function/class } from "filename" // an import 
	export { function/class }                 // an export 

Import default, Export default
	an export default is made importing does not have {} while importing default.
	import function/class from "filename" // an import default
	export default function/class         // an export default

ES6 module design pattern
```js

// math.js
function add(num1, num2) {
	console.log('Add:', num1, num2);
	return num1 + num2;
}
function sub(num1, num2) {
	console.log('Sub:', num1, num2);
	return num1 - num2;
}
export {add, sub};

// main.js
import { add, sub } from './math.js';
console.log(add(2, 2)); //4
console.log(sub(2, 2)); //0
```

```js

// lib/math.js
export function sum(x, y) {
  return x + y;
}
export var pi = 3.141593;
// app.js
import * as math from "lib/math";
alert("2π = " + math.sum(math.pi, math.pi));
// otherApp.js
import {sum, pi} from "lib/math";
alert("2π = " + sum(pi, pi));
Some additional features include export default and export *:

// lib/mathplusplus.js
export * from "lib/math";
export var e = 2.71828182846;
export default function(x) {
    return Math.log(x);
}
// app.js
import ln, {pi, e} from "lib/mathplusplus";
alert("2π = " + ln(e)*pi*2);
```


## MODULE LOADERS

Module loaders support:

Dynamic loading
State isolation
Global namespace isolation
Compilation hooks
Nested virtualization
The default module loader can be configured, and new loaders can be constructed to evaluate and load code in isolated or constrained contexts.

```js

// Dynamic loading – ‘System’ is default loader
System.import('lib/math').then(function(m) {
  alert("2π = " + m.sum(m.pi, m.pi));
});

// Create execution sandboxes – new Loaders
var loader = new Loader({
  global: fixup(window) // replace ‘console.log’
});
loader.eval("console.log('hello world!');");

// Directly manipulate module cache
System.get('jquery');
System.set('jquery', Module({$: $})); // WARNING: not yet finalized
```

## Set: collection of unique elements

helpful data-objects to get rid of duplicate variables in array like structure.  
Efficient data structures for common algorithms

```js
var s = new Set();
s.add("hello").add("goodbye").add("hello");
s.size === 2;
s.has("hello") === true;

const arr = [5, 1, 5, 7, 7, 5];
const unique = [...new Set(arr)]; // [ 5, 1, 7 ]

a Set data structure: No duplicates (Adding an element a second time has no effect)	
elements are always iterated over in the order in which they were inserted.

Iterating 
	Sets are iterable and the for-of loop works as you’d expect:
	Sets preserve iteration order. 

	const set = new Set(['red', 'green', 'blue', 'red']);
	for (const x of set) {
		console.log(x);
	}
	// Output:
	// red
	// green
	// blue

Mapping:
	const set = new Set([1, 2, 3]);
	set = new Set([...set].map(x => x * 2));
	// Resulting Set: {2, 4, 6}

Filtering:
	const set = new Set([1, 2, 3, 4, 5]);
	set = new Set([...set].filter(x => (x % 2) == 0));
	// Resulting Set: {2, 4}

Union (a ∪ b): create a Set that contains the elements of both Set a and Set b.
	const a = new Set([1,2,3]);
	const b = new Set([4,3,2]);
	const union = new Set([...a, ...b]);
		// {1,2,3,4}
	
	The spread operator (...) inserts the elements of something iterable (such as a Set) into an Array. 
	Therefore, [...a, ...b] means that a and b are converted to Arrays and concatenated. It is equivalent to [...a].concat([...b]).

Intersection (a ∩ b): create a Set that contains those elements of Set a that are also in Set b.
	const a = new Set([1,2,3]);
	const b = new Set([4,3,2]);
	const intersection = new Set(
		[...a].filter(x => b.has(x)));
		// {2,3}
	Steps: Convert a to an Array, filter the elements, convert the result to a Set.

Difference (a \ b): create a Set that contains those elements of Set a that are not in Set b. This operation is also sometimes called minus (-).
	const a = new Set([1,2,3]);
	const b = new Set([4,3,2]);
	const difference = new Set(
		[...a].filter(x => !b.has(x)));
		// {1}



const set = new Set(['red', 'green', 'blue']);
const arr = [...set]; // ['red', 'green', 'blue']

We now have a concise way to convert an Array to a Set and back, which has the effect of eliminating duplicates from the Array:
const arr = [3, 5, 2, 2, 5, 5];
const unique = [...new Set(arr)]; // [3, 5, 2]

const set = new Set();
set.add('a');
set.add('b');
set.add('c');
for(let e of set) {
	console.log(e); //a
					//b
					//c
}

let x = new Set([1, 2, 3, 4, 4, 4, 5]);
x.add(6);
x.delete(2);

console.log('The set contains', x.size, 'elements.');
console.log('The set has 1:', x.has(1));
console.log('The set has 8:', x.has(8));

//values and keys are the same in a set
x.forEach((value, key, set) => console.log(value, key, set));

//iterable
for (let value of x) {
	console.log(value);
}

//iterable values
for (let value of x.values()) {
	console.log(value);
}

//iterable keys
for (let value of x.keys()) {
	console.log(value);
}

//iterable entries (key, value)
for (let value of x.entries()) {
	console.log(value);
}

### Out:

	The set contains 5 elements.
	The set has 1: true
	The set has 8: false
	1 1 [object Set]
	3 3 [object Set]
	4 4 [object Set]
	5 5 [object Set]
	6 6 [object Set]
	1
	...
	6
	1,1
	3,3
	4,4
	5,5
	6,6
```

## Maps: Dictionary K,V, better perf

Efficient data structures for common algorithms
create hash maps or dictionaries without using JavaScript objects with string keys to do so
	
```js

var m = new Map();
m.set("hello", 42);
m.set(s, 34);
m.get(s) == 34;


const dict = {
		'foo': 1,
		'bar': 2
	}
is replaced by
const dict = new Map([ ['foo', 1], ['bar', 2] ])
		
console.log(dict.get('foo')); // get an entry
dict.set('foo', 2);
dict.has('baz');
console.log(dict.keys());

var map1 = new Map();
	map1.set('bar', 'foo');

	console.log(map1.get('bar'));
	// expected output: "foo"

	console.log(map1.get('baz'));
	// expected output: undefined

The keys of a Map can be arbitrary values:
const map = new Map(); // create an empty Map
const KEY = {};
map.set(KEY, 123);
map.get(KEY)
map.has(KEY)
map.delete(KEY);
map.has(KEY)

Maps are iterables over their entries. Each entry is an array [key, value]
const m = new Map();
m.set('a', 'A');
m.set('b', 'B');
m.has('a')
m.size
for(let pair of m) {
  console.log(pair); //['a', 'A']
                     //['b', 'B']
}
m.delete('a')
m.size

const map = new Map([
[ 1, 'one' ],
[ 2, 'two' ],
[ 3, 'three' ], // trailing comma is ignored
]);

	let x = new Map([[1, 'is a number key']]);
let today = new Date()

//anything can be a key
x.set(today.toString(), 111)
x.set(today, 222);
x.delete(today.toString());

console.log('The map contains', x.size, 'elements.');
console.log('The map has a today Date key:', x.has(today));
console.log('The map has a today string key:', x.has(today.toString()));

//values and keys
x.forEach((value, key, map) => console.log(value, key, map));

//iterable
for (let value of x) {
  console.log(value);
}

//iterable values
for (let value of x.values()) {
  console.log(value);
}

//iterable keys
for (let value of x.keys()) {
  console.log(value);
}

//iterable entries (key, value)
for (let value of x.entries()) {
  console.log(value);
}

Output:
The map contains 2 elements.
The map has a today Date key: true
The map has a today string key: false
is a number key 1 [object Map]
222 Fri Mar 20 2015 09:05:38 GMT+0100 (Romance Standard Time) [object Map]
1,is a number key
Fri Mar 20 2015 09:05:38 GMT+0100 (Romance Standard Time),222
is a number key
222
1
Fri Mar 20 2015 09:05:38 GMT+0100 (Romance Standard Time)
1,is a number key
Fri Mar 20 2015 09:05:38 GMT+0100 (Romance Standard Time),222



let map = new Map();
> map.set('name', 'david');
> map.get('name'); // david
> map.has('name'); // true


iterate over maps using .entries():
for (let [key, value] of map.entries()) {
    console.log(key, value);
}

let map = new Map([
    ['name', 'david'],
    [true, 'false'],  // use any type as key
    [1, 'one'],
    [{}, 'object'],
    [function () {}, 'function']
]);

for (let key of map.keys()) {
    console.log(typeof key);
    // > string, boolean, number, object, function
}
```

## Weak Maps
Efficient data structures for common algorithms

A WeakMap is a Map that doesn’t prevent its keys from being garbage-collected. 
That means that you can associate data with objects without having to worry about memory leaks.

WeakMaps are useful for associating data with objects whose life cycle you can’t (or don’t want to) control. In this section, we look at two examples:
* Caching computed results
* Managing listeners
* Keeping private data

Weakmaps 
	Collection of keys/values 
	Main constraint being the key has to be an object
	Store bits of data associated with a particular object in our application and when the object is destroyed, its reference is too destroyed and memory is free’d up to be used for something else.
	To ensure that I only associate data with an object inside of my application and keep it nice and contained


```js
var wm = new WeakMap();
wm.set(s, { extra: 42 });
wm.size === undefined


new WeakMap(entries? : Iterable<[any,any]>)
WeakMap.prototype.get(key) : any
WeakMap.prototype.set(key, value) : this
WeakMap.prototype.has(key) : boolean
WeakMap.prototype.delete(key) : boolean


* MANAGE LISTENERS

	const _objToListeners = new WeakMap();

	function addListener(obj, listener) {
		if (! _objToListeners.has(obj)) {
			_objToListeners.set(obj, new Set());
		}
		_objToListeners.get(obj).add(listener);
	}

	function triggerListeners(obj) {
		const listeners = _objToListeners.get(obj);
		if (listeners) {
			for (const listener of listeners) {
				listener();
			}
		}
	}

	// Example: attach listeners to an object

	const obj = {};
	addListener(obj, () => console.log('hello'));
	addListener(obj, () => console.log('world'));
 
	// Example: trigger listeners

	triggerListeners(obj);
	// hello
	// world

* Private class variables with weakmap

	prefixed underscore are just convention for private fields
	// Define as constant
	const privateData = new WeakMap();
	class MyClass {
		constructor(name, age) {
			privateData(this, { name: name, age: age });
		}
		getName() { return privateData.get(this).name; }
		getAge() { return privateData.get(this).age; }
	}
	export default MyClass;

* Storing data on a DOM element

	to store data which is associated to a DOM element without having to pollute the DOM itself:

	let myElement = document.getElementById('logo');
	let myWeakmap = new WeakMap();
	myWeakmap.set(myElement, {timesClicked: 0});

	myElement.addEventListener('click', function() {
		let logoData = myWeakmap.get(myElement);
		logoData.timesClicked++;

		myWeakmap.set(myElement, logoData);
	}, false);


	let map = new WeakMap();
	let el  = document.getElementById('someElement');

	// Store a weak reference to the element with a key
	map.set(el, 'reference');

	// Access the value of the element
	let value = map.get(el); // 'reference'

	// Remove the reference
	el.parentNode.removeChild(el);
	el = null;

	// map is empty, since the element is destroyed	
```

## Weak Sets
Efficient data structures for common algorithms
```js
var ws = new WeakSet();
ws.add({ data: 42 });
// Added object has no other references: it isn't held in the set
```

## PROXIES

Create objects with the full range of behaviors available to host objects  
Can be used for 
- interception
- object virtualization
- logging/profiling

```js

// Proxying a normal object
var target = {};
var handler = {
  get: function (receiver, name) {
    return `Hello, ${name}!`;
  }
};

var p = new Proxy(target, handler);
p.world === 'Hello, world!';
// Proxying a function object
var target = function () { return 'I am the target'; };
var handler = {
  apply: function (receiver, ...args) {
    return 'I am the proxy';
  }
};

var p = new Proxy(target, handler);
p() === 'I am the proxy';
There are traps available for all of the runtime-level meta-operations:

var handler =
{
  get:...,
  set:...,
  has:...,
  deleteProperty:...,
  apply:...,
  construct:...,
  getOwnPropertyDescriptor:...,
  defineProperty:...,
  getPrototypeOf:...,
  setPrototypeOf:...,
  enumerate:...,
  ownKeys:...,
  preventExtensions:...,
  isExtensible:...
}
```

## SYMBOLS: UUID

new primitive type  
Object properties are 'keyed' by either string (ES5) or symbol.   
Optional description parameter used in debugging - but is not part of identity. Symbols are unique (like gensym), but not private since they are exposed via reflection features like Object.getOwnPropertySymbols.

Built-in datatype for unique identifiers
primitive data type  (not an object and has no methods attached to it)
return unique values
You never use the symbol value directly
use them as object properties do not show up in the property enumeration (e.g. for..of loop), which makes them perfect for meta-programming and defining hidden/internal methods of objects.

```js

var MyClass = (function() {

  // module scoped symbol
  var key = Symbol("key");

  function MyClass(privateData) {
    this[key] = privateData;
  }

  MyClass.prototype = {
    doStuff: function() {
      ... this[key] ...
    }
  };

  return MyClass;
})();

var c = new MyClass("hello")
c["key"] === undefined


Symbol() == Symbol()					// false
Symbol('abacaba') == Symbol('abacaba')	// false
const s = Symbol('sym');
s == s									// true

Symbol.for() to access the same symbol elsewhere 
	const sym1 = Symbol.for('some-key'); // Symbol is created in global registry
	// Elsewhere in project:
	const sym2 = Symbol.for('some-key'); // Symbol is retrieved from global registry
	// They are the same symbol:
	console.log(sym1 === sym2); // true
	// You can even access the key property:
	console.log(Symbol.keyFor(sym1)); // some-key

		Symbol() or Symbol(description) will create a unique symbol that cannot be looked up globally.
		A Use case for Symbol() is to patch objects or namespaces from third parties with your own logic, but be confident that you won't collide with updates to that library. 
		For example, if you wanted to add a method refreshComponent to the React.Component class, and be certain that you didn't trample a method they add in a later update:

		const MY_KEY = Symbol();
		let obj = {};	     
		obj[MY_KEY] = 789;
		console.log(obj[MY_KEY]); // 789


		const totalSymbol = Symbol('total'); // Create a Symbol for the "private" key
		class Cart {
		  constructor(total) {
		      this.total = total; // Use the setter here ;)
		  }
		  get total() { return this[totalSymbol] || 0; } // Default to 0
		  set total(v) { this[totalSymbol] = Number(v); }

		  get totalWithTax() { return this.total * 1.1; } /* 10% tax */
		}

		var cart = new Cart(100);
		cart.totalWithTax === 110;

		// You cannot change cart._total anymore (and thus, break your getter and setters behaviour)
		// cart[totalSymbol] will work only with the totalSymbol reference
		// cart[Symbol('total')] won't since it is a new Symbol


		const refreshComponent = Symbol();
		React.Component.prototype[refreshComponent] = () => {
		    // do something
		}

		
		* Symbol.for(key)

		Symbol.for(key) will create a Symbol that is still immutable and unique, but can be looked up globally. 
		Two identical calls to Symbol.for(key) will return the same Symbol instance. NOTE: This is not true for Symbol(description):

		Symbol('foo') === Symbol('foo') // false
		Symbol.for('foo') === Symbol('foo') // false
		Symbol.for('foo') === Symbol.for('foo') // true
		A common use case for Symbols, and in particular with Symbol.for(key) is for interoperability. This can be achieved by having your code look for a Symbol member on object arguments from third parties that contain some known interface. For example:

		function reader(obj) {
		    const specialRead = Symbol.for('specialRead');
		    if (obj[specialRead]) {
		        const reader = obj[specialRead]();
		        // do something with reader
		    } else {
		        throw new TypeError('object cannot be read');
		    }
		}
		And then in another library:

		const specialRead = Symbol.for('specialRead');

		class SomeReadableType {
		    [specialRead]() {
		        const reader = createSomeReaderFrom(this);
		        return reader;
		    }
		}
		A notable example of Symbol use for interoperability is Symbol.iterator which exists on all iterable types in ES6: Arrays, strings, generators, etc. When called as a method it returns an object with an Iterator interface.
```

## SUBCLASSABLE BUILT-INS: Array, Date, DOM Elements

Object construction for a function named Ctor now uses two-phases 
- Call Ctor[@@create] to allocate the object, installing any special behavior
- Invoke constructor on new instance to initialize

```js
// Pseudo-code of Array
class Array {
    constructor(...args) { /* ... */ }
    static [Symbol.create]() {
        // Install special [[DefineOwnProperty]]
        // to magically update 'length'
    }
}

// USER CODE OF ARRAY SUBCLASS
class MyArray extends Array {
    constructor(...args) { super(...args); }
}

// Two-phase 'new':
// 1) Call @@create to allocate object
// 2) Invoke constructor on new instance
var arr = new MyArray();
arr[1] = 12;
arr.length == 2
```

## PROMISES

Asynchronous programming library  
First class representation of a value that may be made available in the future   

```js

function timeout(duration = 0) {
    return new Promise((resolve, reject) => {
		setTimeout(resolve, duration);
    })
}

var p = timeout(1000).then(() => {
    return timeout(2000);
}).then(() => {
    throw new Error("hmm");
}).catch(err => {
    return Promise.all([timeout(100), timeout(200)]);
})


ES8: async/await: Bye bye chained promise callbacks

// instead of
function getAmount(userId) { 
	getUser(userId) 
		.then(getBankBalance) 
   		.then(amount => { 
			console.log(amount); 
		});
}

// Use...async...await
async function getAmount2( userld) { 
	var user = await getUser(userId); 
	var amount = await getBankBalance(user); 
	console.log(amount); 
}

```

## New String Methods: repeat, startsWith, endsWith, includes

```js
* repeat
"abc".repeat(3) // "abcabcabc"
var name = 'Manish ';
console.log(name.repeat(3)); 				// Manish Manish Manish

* startsWith
console.log(name.startsWith('Man'));        // true
console.log(name.startsWith('ani'));        // false

* endsWith 
console.log(name.endsWith('ish'));          // false
console.log(name.endsWith('ish '));         // true

* includes
"abcde".includes("cd") // true
console.log(name.includes('ani'));          // true

```

## New Math library
```js
Number.EPSILON
Number.isInteger(Infinity) // false
Number.isNaN("NaN") // false

Math.acosh(3) // 1.762747174039086
Math.hypot(3, 4) // 5
Math.imul(Math.pow(2, 32) - 1, Math.pow(2, 32) - 2) // 2

Math.sign(-8.1) 	-1
Math.trunc(-3.1) 	-3
Math.log10(100) 	 2	
Math.log2(8)         3
Math.hypot(3, 4)     5
Math.cbrt(8) 		 2   cube root

Support for compiling to JavaScript 
	Emscripten pioneered a coding style that was later picked up by asm.js: The operations of a virtual machine (think bytecode) are expressed in static subset of JavaScript. That subset can be executed efficiently by JavaScript engines: If it is the result of a compilation from C++, it runs at about 70% of native speed.
The following Math methods were mainly added to support asm.js and similar compilation strategies, they are not that useful for other applications.
Math.fround(x) rounds x to a 32 bit floating point value (float). Used by asm.js to tell an engine to internally use a float value.
Math.imul(x, y) 
The following Math methods were mainly added to support asm.js and similar compilation strategies, they are not that useful for other applications.
```

## New Number

```js
Number.isFinite
Number.isNaN(num)  checks whether num is the value NaN. In contrast to the global function isNaN(), it doesn’t coerce its argument to a number (safer for non-numbers)
isNaN('?')  	
Number.isNaN('?')  
Number.isInteger(2.3)   number without a decimal fraction ?
Number.SafeInteger() 	safe (within the signed 53 bit range in which there is no loss of precision) ?
Number.MIN_SAFE_INTEGER
Number.MAX_SAFE_INTEGER
Number.ESPILON 			.2204e-16 for comparing floating point numbers with a tolerance for rounding errors.
Number.MIN_SAFE_INTEGER 	-9007199254740991
Number.MAX_SAFE_INTEGER 	+9007199254740991
Number.parseInt(string, radix?)
Number.parseInt('0xFF', 16) 	255
Number.parseFloat(string)
```

## New ARRAY
Array conversion helpers
```js

Array.from(document.querySelectorAll('*')) // Returns a real Array
Array.of(1, 2, 3) // Similar to new Array(...), but without special one-arg behavior
[0, 0, 0].fill(7, 1) // [0,7,7]
[1, 2, 3].find(x => x == 3) // 3
[1, 2, 3].findIndex(x => x == 2) // 1
[1, 2, 3, 4, 5].copyWithin(3, 0) // [1, 2, 3, 1, 2]
["a", "b", "c"].entries() // iterator [0, "a"], [1,"b"], [2,"c"]
["a", "b", "c"].keys() // iterator 0, 1, 2
["a", "b", "c"].values() // iterator "a", "b", "c"
```

## New OBJECT APIS
Object.assign for copying
```js
Object.assign(Point, { origin: new Point(0,0) })
```

## BINARY AND OCTAL LITERALS

New numeric literal 

```js
binary (b) 
0b111110111 === 503 // true

octal (o)
0o767 === 503 // true
```

## REFLECT API

Full reflection API exposing the runtime-level meta-operations on objects. This is effectively the inverse of the Proxy API, and allows making calls corresponding to the same meta-operations as the proxy traps. Especially useful for implementing proxies.

## TAIL CALLS

Makes recursive algorithms safe in the face of unbounded inputs.
To not grow the stack unboundedly  

```js

function factorial(n, acc = 1) {
    'use strict';
    if (n <= 1) return acc;
    return factorial(n - 1, n * acc);
}

// Stack overflow in most implementations today,
// but safe on arbitrary inputs in ES6
factorial(100000)
```

