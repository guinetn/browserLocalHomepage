# ES10 (ECMAScript 2018) Features

## String:  trimStart() & trimEnd()

Removes whitespace from the beginning/end of a string.

```js
let result = '      hello!'.trimStart();	// "hello!"
let cadena = 'hello      '.trimEnd()	    // "hello!"
```

## Array#{flat,flatMap}

Array.flat(): new array with all sub-array elements concatenated up to the specified depth.
Array.flatMap(): map elements then flattens the result into a new array = map() + flat() of depth 1

```js
const names = [['a','b'],['c','d']];
names.flat();
names.flat(1);
names.flat(Infinity);

const ages = ['1','4','2','3'];
const mapOnly = names.flat().map((n,i) => [n, ages[i]]);
// 0: (2) ["a", "1"]
// 1: (2) ["b", "4"]
// 2: (2) ["c", "2"]
// 3: (2) ["d", "3"]
const flatMap = names.flat().flatMap((n,i) => [n, ages[i]]);
// ) ["a", "1", "b", "4", "c", "2", "d", "3"]
```

## Object.fromEntries

Transform a list of key and value pairs into an object.

```js
const fruits = { lemon: 'l', pineapple: 'p', banana:'b' };
const entries = Object.entries(fruits); 
/*
0: (2) ["lemon", "l"]
1: (2) ["pineapple", "p"]
2: (2) ["banana", "b"] */
const fromEntries = Object.fromEntries(entries);  
/* 
{lemon: "l", pineapple: "p", banana: "b"}
banana: "b"
lemon: "l"
pineapple: "p"*/
```

## String.protype.matchAll()

returns an iterator of all results matching a string against a regular expression, including capturing groups.

```js
// 1. string.match 
// We find all words that consist of hexadecimal digits on ly 
const string = 'Magic hex numbers: DEADBEEF CAFE'; 
const regex = /\b\p{ASCII_Hex_Digit}+\b/gu
for (const match of string.match(regex)) { 
	console.log( match) ; 
Output: 
	'DEADBEEF 
	'CAFE' 

// 2. string.matchAll
const string = 'Magic hex numbers: DEADBEEF CAFE'; 
const regex = /\b\p{ASCII_Hex_Digit}+\b/gu 
for (const match of string.matchAll( regex)) 
	console.log( match); 
Output : 
	[ 'DEADBEEF', index : 19, input: 'Magic hex numbers DEADBEEF CAFE' ] 
	[ 'CAFE',     index : 28, input: 'Magic hex numbers DEADBEEF CAFE' ] 
```

## Symbol#description

At symbol creation, provide a string as a description  
in ES10 there is an accessor to this property.

```js
const symbol = Symbol("x description"); 
console.log(symbol.toString());  // Symbol("x description")

ES10:
const symbol = Symbol("x description"); 
console.log(symbol.description); // x description 
```

## try { } catch {} // optional binding

use try/catch without creating an unused binding variable.

```js
// Old way 

try { 
	undefined_Function("I' m trying" ); 
}
catch(error) { 
	console.log( 'action' ) ; 
}

// ESIO 
try { 
	undefined_Function("I' m trying" ); 
}
catch { 
	console.log( 'action' ) ; 
}
```

## JSON ⊂ ECMAScript

U+2028 	paragraph separator
U+2029 	line separator

```js
const LS = " ";
const PS = eval("'\u2029'");
```

## well-formed JSON.stringify

JSON.stringify() may return characters between U+D800 and U+DFFF as values for which there are no equivalent UTF-8 characters. However, JSON format requires UTF-8 encoding. The proposed solution is to represent unpaired surrogate code points as JSON escape sequences rather than returning them as single UTF-16 code units.

```js
JSON.stringify('\uDF06\uD384'); // \\uDF06\\uD384
JSON.stringify('\uDEAD'); // 	// \\uDEAD
```

## stable Array.sort()

V8 previous implementation used an unstable quick-sort algorithm for arrays containing more than 10 items.  
A stable sorting algorithm is when two objects with equal keys appear in the same order in the sorted output as they appear in the unsorted input.

```js
const fruits = [
	{name: 'a', units: 13 },
	{name: 'y', units: 12 },
	{name: 'e', units: 12 },
	{name: 'r', units: 11 },
	{name: 'z', units: 11 },
	{name: 's', units: 10 },
	{name: 'p', units: 10 }
]; 
// create our own sort criteria function: 
const sortCriteria = (fruit1, fruit2) => fruit1.units - fruit2.units; 

// Perform stable ESI0 sort : 
const sorted = fruits.sort(sortCriteria); 
console.log( sorted ); 
/*
0: {name: "s", units: 10}
1: {name: "p", units: 10}
2: {name: "r", units: 11}
3: {name: "z", units: 11}
4: {name: "y", units: 12}
5: {name: "e", units: 12}
6: {name: "a", units: 13}
*/
```

## revised Function.toString()

When possible, it would return the source code, otherwise it would return a standardized placeholder.

```js
this.fruits = [];
function buyFruits(fruit){ 
	this.fruits = [...this.fruits, fruit];
} 
console.log(buyFruits.toString() ) ; 
/*
function buyFruits(fruit){ 
	this.fruits = [...this.fruits, fruit];
}
*/
```

## BigInt primitive type (stage 3)

BigInt is the 7th primitive type: an arbitrary precision integer. The variables can now represent 253 numbers and not just max out at 9007199254740992.

```js
const limit = Number.MAX_SAFE_INTEGER; // 9007199254740991 
limit+1; // 9007199254740992 
limit+2; // 9007199254740992 <--- MAX SAFE INTEGER + 1 exceeded 
// Biglnt (constructor) 
const larger = 9007199254740991n; 1/9007199254740991n 
const integer = Biglnt(9007199254740991); // 9007199254740991n 
const same = Biglnt( "9007199254740991"); // 9007199254740991n 

// Typeof 
typeof 10; 		// 'number' 
typeof 10n; 	// 'bigtnt' 

// Equality 
10n === BigInt(10); // true  
10n === 10; 		// true  

// Math operators only work within i ts own type 
20n/10n;  // 2n
20n/2     // Uncaught TypeError: Cannot mix Biglnt and other types 
```

## Dynamic import (stage 3)

import() returns a promise for the module namespace object of the requested module.   
Therefore, imports can now be assigned to a variable using async/await.

```js
// Option 1 
const moduleSpecifier = './utils.js'; 
import(moduleSpecifier).then((module) { 
	module.doStuff1(); 
	module.doStuff2(); 
});

// Option 2 - using async/await 
(async function( ){ 
const moduleSpecifier = './utils.js'; 
const module = await import(moduleSpecifier); 
module.doStuff1(); 
module.doStuff2(); 
})();
```

## Standardized globalThis object (stage 3)

```globalThis``` object was not standardized before ES10.  
In production code you would “standardize” it across multiple platforms on your own by writing this monstrosity:

```js
// The global this was not standardized before ES10. The solution was 
var getGlobal = function ( ) { 
	if (typeof self 'undeftned') { return self; } 
	if (typeof window !== 'undefined') { return window; } 
	if (typeof global !== 'undefined') { return global; }
	throw new Error('unable to locate global object') ; 
};

// ES10 added globalThis object which sould be used from now on to access global scope on any plat form 

// Access global array 
globalThis.Array(0, 1, 2); /// [0, 1, 2]
```