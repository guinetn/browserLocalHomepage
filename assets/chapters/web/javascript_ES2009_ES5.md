# ES5 (ECMAScript 2009) Features

## Date.now()

returns the number of milliseconds since zero date (January 1. 1970 00:00:00 UTC)
```js
var timInMSs = Date.now();
```

## "strict mode"

- Prevents certain actions from being taken and throws more exceptions
- Quirks (bizarreries) of earlier versions would throw errors rather than result in unintended behaviour.

Enables Strict Mode, which catches common coding mistakes and "unsafe" actions. For instance:

STRICT MODE DOESN'T ALLOW:
* Use of undefined variables
* Use of reserved keywords as variable or function name
* Duplicate properties of an object
* Duplicate parameters of function
* Assign values to read-only properties
* Modifying arguments object
* Octal numeric literals
* with statement
* eval function to create a variable

```js
"use strict"; // Use it at the top of your file or inside a function
x = 3.14; 	  // throws an error because x is not declared

function strictFunction() {
    'use strict';	// Use it at the top of your file or inside a function
     myVar = 4; 	// ReferenceError 

var x = 1; // valid in strict mode
y = 1;     // invalid in strict mode
```

## String.trim()

removes whitespace from both sides of a string.

```js
var str = "       Hello World!        ";
alert(str.trim());
```

## JSON support: parse, stringify

JSON.parse(json_string_object)  to receive string data from a web server
JSON.stringify(json_object)     to send data to a web server

```js
var john = '{"name":"John", "age":30, "city":"New York"}';
var obj = JSON.parse(john);
console.log(obj);
var johnString = JSON.stringify(john);
console.log(johnString); // "{"name":"John","age":30,"city":"New York"}"
```


## Array: .isArray() .forEach() .map() .filter() .reduce() .reduceRight() .every() .some() .indexOf() .lastIndexOf() 

Array.isArray(): checks whether an object is an array.
```js
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var x = document.getElementById("demo");
x.innerHTML = Array.isArray(fruits);
```
Array.forEach() : calls a function once for each array element.
```js
var txt = "";
var numbers = [45, 4, 9, 16, 25];
numbers.forEach( n => console.log(n) );

```

Array.map():  creates a new array
```js
var numbers1 = [45, 4, 9, 16, 25];
var doubled = numbers1.map(n=> n*2);
console.log(doubled); // [90, 8, 18, 32, 50]
```

Array.filter(): creates a new array
```js
var numbers1 = [45, 4, 9, 16, 25];
var doubled = numbers1.filter(n=> n>18);
console.log(doubled); // [45, 25]
```

Array.reduce()
```js
var numbers1 = [45, 4, 9, 16, 25];
var sum = numbers1.reduce( (acc, val) => acc+ val);
console.log(sum); // 99 
```

Array.reduceRight(): applies a function against an accumulator and each value of the array (from right-to-left)
```js
const array1 = [[0, 1], [2, 3], [4, 5]].reduceRight(
  (accumulator, currentValue) => accumulator.concat(currentValue)
);
console.log(array1); //  [4, 5, 2, 3, 0, 1]
```

Array.every(): checks if all values are...
```js
var numbers = [45, 4, 9, 16, 25];
var allOver18 = numbers.every(n => n>18);
console.log(allOver18); //  false
```

Array.some(): checks if some values are...
```js
var numbers = [45, 4, 9, 16, 25];
var allOver18 = numbers.some(n => n>18);
console.log(allOver18); //  false
```

Array.indexOf(): Search an array for an element value and returns its position.
```js
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var a = fruits.indexOf("Apple");
console.log(a); //  2
```

Array.lastIndexOf(): same as Array.indexOf(), but searches from the end of the array.
```js
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var a = fruits.lastIndexOf("Apple");
console.log(a); //  2
```

## Getters and Setters: accesseurs property

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  get fullName() {
    return this.firstName + " " + this.lastName;
  }

  language : "NO",
  get lang() {
    return this.language;
  },
  set lang(value) {
    this.language = value;
  }  
};

person.lang = "en";   // Set an object property using a setter:
document.getElementById("demo").innerHTML = person.lang;
document.getElementById("demo").innerHTML = person.fullName;
```

## Object Methods

// Adding or changing an object property
Object.defineProperty(object, property, descriptor)

// Adding or changing many object properties
Object.defineProperties(object, descriptors)

// Accessing Properties
Object.getOwnPropertyDescriptor(object, property)

// Returns all properties as an array
Object.getOwnPropertyNames(object)

// Returns enumerable properties as an array
Object.keys(object)

// Accessing the prototype
Object.getPrototypeOf(object)

// Prevents adding properties to an object
Object.preventExtensions(object)
// Returns true if properties can be added to an object
Object.isExtensible(object)

// Prevents changes of object properties (not values)
Object.seal(object)
// Returns true if object is sealed
Object.isSealed(object)

// Prevents any changes to an object
Object.freeze(object)
// Returns true if object is frozen
Object.isFrozen(object)


Object.defineProperty(): define an object property and/or change a property's value and/or metadata.

```js
// Create an Object:
var person = {
  firstName: "John",
  lastName : "Doe",
  language : "NO",
};

// Change a Property:
Object.defineProperty(person, "language", {
  value: "EN",
  writable : true,
  enumerable : true,    // 'false' to hides the language property from enumeration
  configurable : true
});

// Enumerate Properties
var txt = "";
for (var x in person) {
  txt += person[x] + "<br>";
}
document.getElementById("demo").innerHTML = txt;
```

```js
var person = {
  firstName: "John",
  lastName : "Doe",
  language : "NO"
};

// Change a Property:
Object.defineProperty(person, "language", {
  get : function() { return language },
  set : function(value) { language = value.toUpperCase()}
});

// Change Language
person.language = "en";

// Display Language
document.getElementById("demo").innerHTML = person.language;
```


## Reserved Words as Property Names

```js
var obj = {name: "John", new: "yes"}
```
## charAt() 

returns the character at a specified index (position) in a string

```js
var str = "HELLO WORLD";
str.charAt(0);   
```

## ES5 "class" equivalent

JavaScript inheritance = object prototypes (most languages use classes)
1. constructor function 
2. add properties by extending the prototype

```js

var  Person = function(name) {	    
     this.name = name;
     }
Person.prototype.getName = function(age) { return 'I am ' + this.name + ', ' + age; }

var p = new Person('Joe');
console.log(p.getName(33));
// --> logs 'I´m Joe, 33'


function Person(name, age, gender) {
    this.name   = name;
    this.age    = age;
    this.gender = gender;
}

Person.prototype.incrementAge = function () {
    return this.age += 1;
};
```

Extend classes (inheritance):
```js

function Personal(name, age, gender, occupation, hobby) {
    Person.call(this, name, age, gender);
    this.occupation = occupation;
    this.hobby = hobby;
}

Personal.prototype = Object.create(Person.prototype);
Personal.prototype.constructor = Personal;
Personal.prototype.incrementAge = function () {
    Person.prototype.incrementAge.call(this);
    this.age += 20;
    console.log(this.age);
};			
```