# DOM - Document Object Model

Represents the document as JavaScript nodes and objects (structure, style, content) that can be changed 
An API: HTML programming interface 

- https://vanillajstoolkit.com/reference/#DOM-Injection


|           | Node Objects | | |    
|---|---|---|--- |    
|<!DOCTYPE html>           | DOCUMENT_TYPE_NODE | window.document  | |    
|<html lang="en">          | DOCUMENT_NODE | | |                       
|  <head>                  | | | |               
|    <title>HTML</title>   | | | |                              
|  </head>                 | | | |                
|  <body>                  | ELEMENT_NODE:body, a, p ,h1… | window.document.body |  |
|    <p>                   | ELEMENT_NODE | | |
|      <a id='a1'>xxx</a>  | ATTRIBUTE_NODE: id=…, class=… | | |                               
|                          | DOCUMENT_FRAGMENT_NODE | | |
|                          | | | |
|  </body>                 | | | |                
|</html>                   | | | |   

document.ELEMENT_NODE
- 03 TEXT_NODE
- 02 ATTRIBUTE_NODE
- 09 DOCUMENT_NODE                  ex: document.nodeType
- 11 DOCUMENT_FRAGMENT_NODE
- 10 DOCUMENT_TYPE_NODE
           
for (const key in document.querySelector('body')) console.log(key) //  node properties 

## Nodes Properties
||||
|---|---|---|
| childNodes       | child nodes ||
| firstChild       | first child ||
| lastChild       | last child ||
| nextSibling       | next sibling node ||
| nodeName       | name of the node | document.nodeName → '#document' |
| nodeType       | type of the node ||
| nodeValue        | value of the node |null, except when used to extract Text and Comment|
| parentNode       | parent of the current node ||
| previousSibling       | previous sibling of the current node ||

console.log(document.querySelector('a').firstChild.nodeValue);

## Nodes Methods 

|||
|---|---|
| appendChild      |   adds a new child |
| cloneNode      |   clones the current node and returns it |
| compareDocumentPosition      |   compares the position of each node |
| contains      |   check if the node has another node as a child |
| insertBefore      |   adds a node before the current node |
| isEqualNode      |   checks if it’s the same |
| removeChild      |   removes a given child node |
| replaceChild      |   replaces one child element with another |

Document methods include:
- document.createElement()
- document.createTextNode()
          
## HTML Element Properties        

|||
|---|---|
|innerHTML                | HTML content inside an element|
|outerHTML                | innerHTML + enclosing tags|
|textContent              | textual content inside an element|
|innerText                | textual content inside an element|
|outerText                | innerText + enclosing tags|
|firstElementChild        | first child node that’s an HTML element|
|lastElementChild         | last child node that’s an HTML element|
|nextElementChild         | element node after the current node|
|previousElementChild     | element node before the current node|
|children                 | child nodes of the current node|

HTML element.insertAdjacentHTML() insert a node according to the position specified.
   
## data-* custom attributes

    HTML5 supports  'data-'custom attributes within all HTML elements
	    <div id="myDiv" data-custom-attr="My Value"> Bla Bla </div>
	    var theDiv = document.getElementById('myDiv');
	    attr = theDiv.getAttribute('data-custom-attr');

  	darkThemeSelected ? 
    document.body.setAttribute('data-theme', 'dark') : document.body.removeAttribute('data-theme');

    <button class="todocompleted" data-todo="my data">
    var index =
    
## DOM Manipulation    

***Creating a new element*** 
```js
let div = document.createElement('div');
let link = document.createElement('a');
let article = document.createElement('article');

let chicken = document.createElement('news'); // <news></news>
let placeholder = document.createElement('_'); // <_></_>

// Add classes, attributes, styles...
let div = document.createElement('div');
div.textContent = 'Hi the world!';
div.className = 'new-div';
div.id = 'new-div';
div.setAttribute('data-div', 'new');
div.style.color = '#F00';
div.style.backgroundColor = 'darkorange';
```


***Injecting one element after another: Node.after(target, payload)***
```js
div id="app">Good morning</div>
let p = document.createElement('p');
p.textContent = 'Hello!';
// Get the target node
let app = document.querySelector('#app');
app.after(p);                   // <div id="app">Good morning</div><p>Hello!</p>
app.after(p, `What's poppin?`); // <div id="app">Good morning</div><p>Hello!</p>What's poppin'
```

***Injecting one element before another: Node.before(target, payload)***

```js
<div id="app">Good evening</div>
let p = document.createElement('p');
p.textContent = 'Hello!';
// Get the target node
let app = document.querySelector('#app');
app.before(p);                    // <p>Hello!</p><div id="elem">Good evening</div>
app.before(p, `What's poppin?`);  // <p>Hello!</p>What's poppin'<div id="elem">Good evening</div>
```

## DOM EVENTS

 CustomEvent object:  a way to create and emit custom events, as well as pass in custom event details.
 
 As an optional second argument, pass in an object of options, including whether or not the event bubbles and is cancelable. Both booleans, and both are false by default.

```js

// Create a custom event
let event = new CustomEvent('my-custom-event', {
	bubbles: true,
	cancelable: true,
  detail: 'This could also be an object or array'   	 // Including additional information with your event
});

// Emit the event
document.dispatchEvent(event);

// listening for the custom event
document.addEventListener('my-custom-event', function (event) {
	console.log('The event happened!', event.detail);
});
```

***canceling an event***
```js
document.addEventListener('my-custom-event', function (event) {
  ...
	// Cancel the event
	event.preventDefault();
});

let canceled = !document.dispatchEvent(event);
Element.dispatchEvent() method returns false if the event was canceled, and true if it was not.
```
 
 ***event naming conventions***
 prefix them with your library name to prevent naming collisions between the custom events in your library and others
emitEvent('greetings-before-hi');
emitEvent('greetings-before-hi');       // kebab-case naming
emitEvent('greetings:before-hi');       // prefix-kebab: events more readable (put a colon (:) between the library name and the event type)

// prefix-kebab naming

***custom event helper function***
```js
/**
 * Emit a custom event
 * @param  {String} type   The event type
 * @param  {Object} detail Any details to pass along with the event
 * @param  {Node}   elem   The element to attach the event to
 */
function emitEvent (type, detail = {}, elem = document) {

	// Make sure there's an event type
	if (!type) return;

	// Create a new event
	let event = new CustomEvent(type, {
		bubbles: true,
		cancelable: true,
		detail: detail
	});

	// Dispatch the event
	return elem.dispatchEvent(event);
}
```


```js
```



```js
```