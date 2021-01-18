# ES9 (ECMAScript 2018) Features

## Lifting template literal restriction

Illegal escape sequences in template returns 'undefined'
.raw contains the raw string
```js
const bad = `bad escape sequence \unicode`;
```

## /s (dotAll) flag for regular expressions

Add the regex flag /s
before ES2018 the dot (.) in regex doesn't match line terminator characters

```js

/^.$/.test('\n');   // false 
/^[^]$/.test('\n'); // alternative - true 
/^.$/s.test('\n');  // ES2018 - true 

Line terminators by ECMAScript: 
LINE FEED (LF) (\n) 
CARRIAGE RETURN (CR) (\r) 
0+2028 LINE SEPARATOR 
0+2029 PARAGRAPH SEPARATOR 

Newline-ish characters not considered line terminators by ECMAScript: 
U+000B  VERTICAL TAB (\v) 
U+000C  FORM FEED (\f) 
U+0085  NEXT LINE 
```

## Regexp named capture groups:  ```(?<name>...```

before ES2018: Numbered capture groups
2018: Named Capture Groups

```js
const regExp = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/u;
const result = regExp.exec( '2020-11-02' );
//result.groups
//{year: "2020", month: "11", day: "02"}
result.groups["year"]
result.groups.year === '2020'
result.groups.month === '11'
result.groups.day === '02'
result[0] === '2020-11-02'
result[l] === '2020'
result[2] === '11'
result[3] === '02'

// Destructurtng
let { groups : { pear, apple }} = /^(?<pear>.*):(?<apple>.*)$/u.exec('p:P');
console.log(`pear: ${pear}, apple: ${apple}`); // pear: p, apple: P

/^(?<pear>.*):(?<apple>.*)$/u.exec('p:P').groups;
{pear: "p", apple: "P"}apple: "P"pear: "p"
```

## Regexp lookbehind assertions

* Positive lookbehind: (?<=...)   
Pattern contained within precedes the pattern following the assertion.
```js
/(?<=\$)\d+(\.\d*)?/   match '$10.53', returns '10.53'
```

* Negative lookbehind (?<!...)  
Pattern within doesn't precede the pattern following the assertion.

```js
/(?<!\$)\d+(\.\d*)?/   won't match '$10.53' but match '€10.53'
```

## Regexp Unicode property escapes

match characters by mentioning their Unicode character properties inside the curly braces of \p{}

```js
/\p{White_Space}+$}/u.test('\n \r \t'); // true: match whitespace
/\p{Letter}+$}/u.test('éün');           // true: 

```

## Rest/spread properties for object

ES6: rest elements for array destructuring assignments and spread elements for array literals.
ES9: rest properties for object destructuring assignment and spread properties for object literals.

```js
Rest properties collect the remaining own enumerable property keys that are not al ready picked off by the destructuring pattern. 
Those keys and their values are copied onto a new object. 

// Rest Properties 
const { pear, apple, ...cars } = {pear: p, apple: P, police: po, racing: rac};
pear;  // p 
apple; // P 
cars;  // { police: po , racing: rac }
```

Spread properties in object initializers copies own enumerable properttes from a provided object onto the newly created object. 
```js
// Spread Properties 
const things = { pear, apple, ...cars};
things; // {pear: p, apple: P, police: po, racing: rac};
```


## Promise.prototype.finally

A finally callback execute logic once your Promise has been settled one way or the other.   
No impact on the value that your promise will resolve to.

```js
Promise.resolve({some: 'data'} ) 
.finally(()=>{ console.log('WHALE HELLO THERE')}) 
.then(data => ( {...data, anAdditional: 'key'}))
.finally(()=>{ console.log('GOAT HELLO THERE')}) 
.then(data => ( {...data, yetAnother: 'thing added'}))
.finally(()=>{ console.log('SHEEP HELLO THERE')}) 
.then(data => ( console.log('Final result:',data) })
 WHALE HELLO THERE 
GOAT HELLO THERE 
SHEEP HELLO THERE 
Final result: {some: "data" , anAddittonal: "key" , yetAnother: "thing added"} 
```

## Asynchronous iteration
 
variation of the for-of iteration statement which iterates over async iterable objects.

```js
async function asyncFunction() { 
const promises = [
    fetch( 'filel.json'), 
    fetch( 'file2.json'), 
    fetch( 'file3.json'), 
    fetch( 'file4.json') ];
// Normal iterator 
for (const item of promises) 
    console. log(item); // Logs a promise 

// Async iterator 
for await (const item of promises) { 
    console. log(item) ; // Logs a resolved response 
```
