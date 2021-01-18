# ES8 (ECMAScript 2017) Features

ECMAScript 2016 and 2017 was not called ES7 and ES8.
Since 2016 new versions are named by year (ECMAScript 2016, ECMAScript 2017).

## Shared memory 

Pour allouer ou partager de la mémoire entre plusieurs agents:
```js
sab = new SharedArrayBuffer(1024);  // 1 Kb shared memory
```

## Atomics 

Global variable whose methods have three main use cases.

* Synchronization

  Atomics methods can be used to synchronize with other workers. 

  // main.js 
  console. log('notifying...') 
  Atomics.store(sharedArray, 0, 'x') ; 
  // worker.js 
  while (Atomics.load(sharedArray, 0) != 'x') 
  console.log( 'notified'); 

* Waiting to be notified

  Atomics has operations that are more useful than a simple loop. 

  Atomics.wait(elements: Int32Array, index, value, timeout) 
  waits for a notification at elements[index], but on ly if elements[index] is value. 

  Atomics.wake( elements : Int32Array, index, count) 
  // wakes up count workers that are waiting at elements[index]

* Atomic operations

  There are Atomics operations perform arithmetic 
  Atomics.add(elements: TypedArray<T>, index, value) : T 
  Vs 
  elements[index] += value; 

## Object.values/entries

. Object.values(obj)    return an array with the values
. Object.entries(obj)   return an array of keys and values

```js
const myObject = { 
  name: 'Joe', 
  age: 29 
}; 
  
Object.entries(myObject);   [ 0: (2) ["name", "Joe"]
                              1: (2) ["age", 29] ]
Object.values(myObject);    [ 0: "Joe"
                              1: 29 ]

const cars = { BMW: 3, Tesla: 2, Toyota :1 };

// extracting values
const vals =  Object.keys(car).map(k=> cars[k]); // ES 2015
const vals = Object.values(cars);                // ES 2017 
console.log(vals);
```

## Trailing commas

```js
let obj = { 
    prop1: 'val1', 
    prop2: 'val2', 
};               ↑___ allowed
```
  

## String padding: padStart, padEnd

```js

('000' + num).slice(-4)
ES2017: String(n).padStart(4, '0')

'someString'.padStart(numberOfCharcters [,stringForPadding]); 
'5'.padStart(10)       // '         5'
'5'.padStart(10, '+-') // '+-+-+-+-+5'

'someString'.padEnd(numberOfCharcters [,stringForPadding]); 

'5'.padEnd(10)       // '5         '
'5'.padEnd(10, '+-') // '5+-+-+-+-+'
```



## Object.getOwnPropertyDescriptors

Returns all own property descriptors of a given object.
value         The value associated with the property (data descriptors only).
writable      True if, and only if, the value associated with the property may be changed.
get           A function that serves as a getter for the property.
set           A function that serves as a setter for the property.
configurable  True if, and only if, the type of this property descriptor may be changed.
enumerable    True if, and only if, this property shows up during enumeration of the property.

returns all the details (including getter getand setter set methods) for all the properties of a given object. 
Motivation: allow shallow copying / cloning an object into another object that also copies getter and setter functions as opposed to Object.assign

```js

const obj = { 
    [Symbol('foo')]: 123, 
    get bar() { return 'abc' }, 
}; 
console.log(Object.getOwnPropertyDescriptors(obj)); 
  
// Output: 
// { [Symbol('foo')]: 
//    { value: 123, 
//      writable: true, 
//      enumerable: true, 
//      configurable: true }, 
//   bar: 
//    { get: [Function: bar], 
//      set: undefined, 
//      enumerable: true, 
//      configurable: true } }
```

## async/await: Bye bye chained promise callbacks

Async/Await returns a promise

```js

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

Async functions themselves return a Promise
If you are waiting for the result from an async function, you need to use Promise’s then syntax to capture its result.


### Calling async/await in parallel

parallelize it since a and b are not dependent on each other using Promise.all


### Error handling async/await functions
Use try catch within the function

```js
//Option 1 - Use try catch within the function
async function doubleAndAdd(a, b) {
 try {
  a = await doubleAfter1Sec(a);
  b = await doubleAfter1Sec(b);
 } catch (e) {
  return NaN; //return something
 }
return a + b;
}

// Usage:
doubleAndAdd('one', 2).then(console.log); // NaN
doubleAndAdd(1, 2).then(console.log); // 6
function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

### Catch error on every await line

```js
async function doubleAndAdd(a, b) {
 a = await doubleAfter1Sec(a).catch(e => console.log('"a" is NaN')); 
 b = await doubleAfter1Sec(b).catch(e => console.log('"b" is NaN'));  if (!a || !b) {
  return NaN;
 }
 return a + b;
}
```

### Catch the entire async-await function

```js
async function doubleAndAdd(a, b) {
 a = await doubleAfter1Sec(a);
 b = await doubleAfter1Sec(b);
 return a + b;
}
// Usage:
doubleAndAdd('one', 2).then(console.log)
.catch(console.log); // 👈👈🏼<──── use "catch"
```











## ASYNC AWAIT
	upcoming ES2016 feature, async await allows us to perform the same thing we accomplished using Generators and Promises with less effort
	Under the hood, it performs similarly to Generators. I highly recommend using them over Generators + Promises.

	var request = require('request');

	function getJSON(url) {
	  return new Promise(function(resolve, reject) {
	    request(url, function(error, response, body) {
	      resolve(body);
	    });
	  });
	}

	async function main() {
	  var data = await getJSON();
	  console.log(data); // NOT undefined!
	}

	main();	


# ASYNC/AWAIT
https://runkit.com/docs/await
http://rossboucher.com/await
https://github.com/lukehoban/ecmascript-asyncawait/

var got = require("got");
var githubStatusJson = (await got("https://status.github.com/api/status.json", { json : true })).body;


# Asynchronous javascript

## JS promises are similar to Java’s Future or C#’s Task

	http://www.codeproject.com/Articles/1046507/JavaScript-goes-Asynchronous-and-it-s-awesome

	https://developers.google.com/web/fundamentals/getting-started/primers/async-functions
		chrome 55 as async functions:
		async function logFetch(url) {
		  try {
		    const response = await fetch(url);
		    console.log(await response.text());
		  }
		  catch (err) {
		    console.log('fetch failed', err);
		  }
		}

	// wait ms milliseconds
	function wait(ms) {
	  return new Promise(r => setTimeout(r, ms));
	}

	async function hello() {
	  await wait(500);
	  return 'world';
	}
	…calling hello() returns a promise that fulfills with "world".

	async function foo() {
	  await wait(500);
	  throw Error('bar');
	}
	…calling foo() returns a promise that rejects with Error('bar').


async/await, est une nouvelle fonctionnalité qui devait apparaître dans ES2016 et qui finalement sera dans ES2017. Elle résout des problèmes liés à l'asynchrone en JavaScript. Les promises en JavaScript sont un moyen de résoudre cela mais certains les trouvent complexe à manier et quand nous manipulons les promises nous résolvons le problème, mais la lisibilité en prend parfois un coup.

# Grâce à async on peut dire qu'une fonction traite des données asynchrones (qui viennent d'une api, file system, etc..).
async function fetchData() {
}

await quant à lui, permet de dire à une fonction asynchrone(avec le mot clé async) d'attendre tant que l'appel asynchrone n'est pas terminé. Ce mécanisme rend la fonction asynchrone à l'intérieur d'elle-même synchrone ! Ce qui est vraiment génial c'est que la gestion du flux de données sur nos appels API deviens beaucoup plus simple à comprendre et à maintenir.

# En voici un exemple :

async function fetchData() {
 const result = await fetch('http://reqres.in/api/users/2')
 const jsonResult = await result.json()
 console.log(jsonResult.first_name) // Lucille
}