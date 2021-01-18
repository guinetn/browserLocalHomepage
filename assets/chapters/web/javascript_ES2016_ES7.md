# ES7 (ECMAScript 2016) Features

ECMAScript 2016 and 2017 was not called ES7 and ES8.
Since 2016 new versions are named by year (ECMAScript 2016, ECMAScript 2017).

## Exponentiation operator **

```js
Math.pow(x,y)   same as   x ** y
Math.pow(7,2)   same as	  7 ** 2   // 49
const powEight= 2 ** 8
console.log(powEight) // 256	
```
## Array.prototype.includes 				

Does an array includes a certain value among its entries 

```js
const fruits = [🍐, 🥑, 🍇]
fruits.includes(🥑)      // true
fruits.includes(🍉)      // false
fruits.includes(🍇, 3)   // false. If fromIndex >= array length, false is returned. The array won’t be searched.
fruits.includes(🍇, 100) // false
fruits.includes(🍇, -1)  // true
fruits.includes(NaN)      // true
```

find if an item is in the Array (including NaN unlike indexOf)
```js
const arr = [1, 2, 3, 4, NaN]; 

if (arr.indexOf(3)>=0)	same as   if (arr.includes(3))
	
// Note the indexOf doesnt work for searching NaN 
arr.includes(NaN) //true 
arr.indexOf(NaN) //-1 (doesnt work for NaN) 
```

## DECORATOR @

a decorator is simply a way of wrapping one piece of code with another — literally “decorating” it. This is a concept you might well have heard of previously as functional composition, or higher-order functions.

This is already possible in standard JavaScript for many use cases, simply by calling on one function to wrap another:

```js

function doSomething(name) {
  console.log('Hello, ' + name);
}

function loggingDecorator(wrapped) {
  return function() {
    console.log('Starting');
    const result = wrapped.apply(this, arguments);
    console.log('Finished');
    return result;
  }
}

const wrapped = loggingDecorator(doSomething);

doSomething('Graham');
// Hello, Graham

wrapped('Graham');
// Starting
// Hello, Graham
// Finished

JavaScript decorator are prefixed with an @ symbol and placed immediately before the code being decorated.

const router = (target) => {
  // Ajouter une propriété route à la classe ciblé
  target.route = '/home'
}

@router
class MyClass { }
console.log(MyClass.route) // /home


@log()
@immutable()
class Example {
  @time('demo')
  doSomething() {
    //
  }
}
```

# SIMD - Single Instruction Multiple Data

Llow level JavaScript: 3D, images, son...cpu high usage
Ask the cpu to use one instruction for a series of numbers

```js

const arr1 = SIMD.Float32x4(1, 2, 3, 4);
const arr2 = SIMD.Float32x4(2, 4, 6, 8);

const newArr = SIMD.Float32x4.add(arr1,arr2); // float32x4[3,6,9,12]
```