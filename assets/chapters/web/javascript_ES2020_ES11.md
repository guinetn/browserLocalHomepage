# # ES11 (ECMAScript 2020) Features

	
## Promise.allSettled

Promise.allSettled returns a promise that’s fulfilled with an array of promise state snapshots, but only after all the original promises have settled; i.e. become either fulfilled or rejected.

Settled promise: it is not pending (is either fulfilled or rejected)

ES 2015 Promise.all() 
ES 2020 Promise.allSettled() 

```js
const pl = new Promise( resolve => resolve('1')); 
const p2 = new Promise((_,reject) => reject('There is no 1')); 
const p3 = new Promise( resolve => resolve('2')); 

// any promises is rejected: Promise.all() immediately rejects With that error
Promise.all([pl, p2, p3]).then(response => console.log( response)) 
.then(error => console.log(error)); 
// Result: 'There is no 1' 

// Wait for all passed promises to settle 
Promise.allSettled([Pl, p2, p3])
.then(response => console.log(response)); 
/* Result:
[ {status: 'fullfilled', value: '1'},
  {status: 'rejected', reason: 'There is no 1'},
  {status: 'fullfilled', value: '2'} ]
```


## for-in mechanics
	
Different engines have agreed on how properties are iterated when using the for (a in b) control structure so that the behavior is standardized.	

## Optional Chaining

When looking for a property value that’s deep in a tree-like structure, one often has to check whether intermediate nodes exist.
The Optional Chaining Operator allows developers to handle many of those cases without repeating themselves and/or assigning intermediate results in temporary variables.

```js
The Optional Chaining operator && Nullish Coalesctng Operator 
const book = {
	"created at": "Thu Jun 22 2017", 
	"id": 877994604561387500, 
	"text" : "Creating a Grocery List Manager Us ing Angular, https://t.co/xFox78juL1 #Angular", 
	"entities " : {
		"hashtags" : [ "Angular" ]
	} 
}
	
const hashtags = book.entities && book.entities.hashtags; 

// Optional Chaining Operator 
const hashtags = book.entities?.hashtags; 
const hashtags = book.entities?.hashtags ?? ['Angular']; 
```

## Nullish coalescing Operator ??

Provide a default value if the result of that property access is null or undefined. 
Typical way was || but not always good

```js
// ok for common case of null and undefined values, but there are a number of falsy values that might produce surprising results:
const value = values.A || 300;

// null coalescing operator is intended to handle these cases better
const values ={
	nullValue: null, 
	numberValue: 400, 
	zeroValue: 0, 
	emptyText : '',
	falseValue: false 
}
	
// Coalesctng operator 
const value = values.undefinedVaIue || 'some other default'; // 'some other default'
const value = values.nullValue ?? 'some other default';      // 'some other default'
const value = values.emptyText ?? 'Hello, world !';          // ''
const value = values.zeroValue ?? 300; // 0 
const value = values.falseValue ?? true; // false
```

