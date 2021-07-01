# JAVASCRIPT

https://www.freecodecamp.org/news/javascript-hacks/ to add

https://github.com/ProgrammingHero1/oop-object-oriented-programming
https://github.com/ProgrammingHero1/data-structure-algorithm-time-complexity
https://github.com/microsoft/Web-Dev-For-Beginners
https://www.dofactory.com/products/dofactory-js
https://www.dofactory.com/javascript/reference
https://dev.to/rahxuls/17-pro-javascript-tricks-you-didn-t-know-5gog
https://davidwalsh.name/cache
https://krasimirtsonev.com/blog/article/Javascript-template-engine-in-just-20-line
https://www.i-programmer.info/programming/javascript/13092-javascript-canvas-offscreencanvas.html

Specifications: Standard ECMA-262
## PLAYGROUND
- http://liveweave.com
- http://jsfiddle.net
- http://codepen.io
- https://jsbin.com
- https://v8.dev : V8 = ECMAScript + WebAssembly: C++ application can expose its objects/functions to JS code

## Tools

### Minify JavaScript Files
 - [Google Closure Compiler](https://developers.google.com/closure/compiler)
 Parses JavaScript, analyzes it, removes dead code, rewrites and minimizes what's left
 
 - [Microsoft Ajax Minifier](https://archive.codeplex.com/?p=ajaxmin)
 Improve application’s performance by reducing the size of your JavaScript files.
## CORE JS 
Interpreted scripting language conforms to ECMAScript specification
Prototype-based language
    prototypical object: an object used as a template from which to get the initial properties for a new object
Single threaded (monothread, two bits of script cannot run at the same time: One task at the same time. Rest of tasks are queued in the "Execution Context")
Case sensitive:  myVar != myvar
Readability: camelCase convention  	showMessage()
Curly-bracket syntax
Uses the Unicode character 
Object Oriented with Functional Programming Features: First-class functions
Dynamic typed language (Loosely typed)
JS is everywhere: on server-side with Node.js

## EXECUTE JS 

#### Node JS: SHEBANG
    
```
my.js
    #!/usr/bin/js
    console.log("hi node");

sudo chmod +x my.js
./my.js
```
#### SCRIPT TAG
    
All `<script>` in  `<head>` are loaded before loading and rendering body html. 
#### INLINE SCRIPT
```
<script type="text/javascript"> HTML 4 </script>
<script> HTML 5	</script>
```
#### EXTERNAL SCRIPT
```  
<script src="test.js"></script>
</body>    Put scripts before </body> because web page are loaded in linear steps
```

    src 		address of the external script resource to use
    async 		<script src="script-lent.js" async></script>
                Script EXECUTED ASYNCHRONOUSLY, as soon as it becomes available, NO EXECUTOPN IN LOAD ORDER
    defer		<script src="code.js" defer></script>
                Load scripts in parallel without stopping ui rendering. 
                Executed in order of declaration
                Scripts executed after the DOM has been parsed (before DOMContentLoaded event)
    charset 	Character encoding of the external script resource (no need if source is present)
    type 		MIME type: Language of the script / Format of the data:
                application/javascript  		←  DEFAULT VALUE IF MISSING
                Servers should use "text/javascript" for JavaScript resources

When a web page is loaded, JS reads the file and asap it see a code
it wrapped the code within an anonymous function with a global scope as its own function scope and is self-executing
```js
(function () {
    // JS file content goes here
})();
```
This JS code is executed as soon as possible after the inline element or file reference is found
<mark>IT DOESN’T WAIT FOR THE CREATION OF THE DOM TREE TO EXECUTE</mark>
During this code execution both the creation of the DOM and the rendering of the page is paused (blank page, user needs to wait)

```js
<!-- See nothing -->
<script src=...>
    or             
<script>
    var divElement = document.getElementById('someId');
    divElement.innerText = 'Hello, world!'
</script>
<div id="someId"></div>

<!-- See ! -->
<div id="someId"></div>
<button id="button" type='button'>Get Joke</button>
<!-- type=button tells the browser that this isnt a typical form submission button. -->
<script>
    var divElement = document.getElementById('someId');
    divElement.innerText = 'Hello, world!'
    
    document.addEventListener("click", function (event) {
    // Checking if the button was clicked
    if (!event.target.matches("#button")) return;

    fetch("https://official-joke-api.appspot.com/random_joke")
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch(() => renderError());
    });
</script>
```

FIX 1: place your code at the end of the page or at least execute it after page is loaded.
FIX 2: “async” and “defer” attributes of the script element to handle JS file loading                
#### DYNAMIC SCRIPT
```
setTimeout(function () {
            var a = document.createElement("script");
            var b = document.getElementsByTagName("script")[0];
            a.src = document.location.protocol + "//script.js?" + Math.floor(new Date().getTime() / 3600000);
            a.async = true; 
            a.type = "text/javascript"; 
            b.parentNode.insertBefore(a, b)
}, 1);    
```

#### IIFE (keep it out of the global scope)
```
;(function () {
  // Some amazing code...
})();
```

#### HOW JS WORKS

Browser internal softwares that are compiled by JIT to bytecode
* DOM INTERPRETER
* CSS INTERPRETER
* JS ENGINE 
> Chrome 	V8 engine       https://v8.dev/
> Safari 	Nitro
> FireFox 	spiderMonkey
> ie 		Chakra

* EVENT LOOP

    http://latentflip.com/loupe/    
                            
                            click, mouseover, load, change, readystatechange…
                            element.addEventListener('click', function () { code … } );
                                ↓
                                ↓ Events can be queued while code is running, but they can´t fire until the runtime is free.
                                ↓
         ...............> CALLBACK/MESSAGE QUEUE: a queue of event handlers that are waiting to be executed.
        .   callback            ↓
        .   (timeout end…)     ... one by one when stack is free          
        .                       ↓
        .                       ↓      ___ Browser main thread: A thread waiting for and dispatches incoming events
        .                       ↓     /    Process that checks whether events handlers queue is not empty and if it 
        .                   EVENT LOOP     is – calls top event handler and removes it from queue.
        .                       ↓
        .                   CALL STACK         HEAP: where objects resides (name = memory region)        .                       ↓  \
    Browser API - C++ ←────────  \___Function calls form a stack of frames
                                        The single thread of js code
                                        where the currently running functions get added. If function A() runs function B(), well you’re two levels deep in the stack. EACH TIME ONE OF THESE FUNCTIONS IS ADDED TO THE STACK, IT IS CALLED A FRAME. These frames contain pointers to the functions in the heap, as well as the objects available to the function depending on its current scope, and of course the arguments to the function itself. Different JavaScript engines likely have different maximum stack sizes, and unless you have a runaway recursive function, you’ve probably never hit this limit. Once a function call is complete, it gets removed from the stack. Once the stack is empty, we’re ready for the next item in the Queue.

Each window or WebWorker has its own event loop.         

The browser has an event loop which checks the event queue and processes pending events.   
UI events (click, scroll, and so on), Ajax callbacks, and callback provided to setTimeout() and setInterval() are all
processed one at a time by the event loop. Therefore, when calling the setTimeout() function the callback
provided is queued, even if the delay specified is zero. The callback stays in the queue until the time
specified has elapsed and the engine is ready to perform the action (i.e. if it isn’t performing another
action at the moment). So, although a callback passed to setTimeout() is delayed by zero milliseconds,
it’ll be queued and executed after other non-delayed statements declared in the same function.

* JAVASCRIPT SINGLE-THREADED LANGUAGE		
One task at the same time. Rest of tasks are queued in the "Execution Context"  
BECAUSE THE DOM TREE IS NOT THREAD-SAFE AND IT WOULD BE A MESS IF WE TRIED TO DO IT: WE CANT CHANGE IT IN PARALLEL
Because of this limitation, all our JavaScript code should be executed in single thread, while at the same time ensuring that it handles all the events and doesn’t lose any callback ==> For these reasons we come to the Event loop.
We don’t want to change DOM tree in different threads

JAVASCRIPT CODE IS SINGLE-THREADED IN THE SAME CONTEXT, BUT ALL OTHER STUFF WHICH IS DONE BY BROWSER (AJAX REQUEST, RENDERING, EVENT TRIGGERS ETC.) ARE NOT


## TYPES


## Object

### Using the Object.create method approach, the above translates to:

		Object.setPrototypeOf() takes two arguments. it replace __proto__ 
			- the object (first argument) 
			- the desired prototype (second argument)
			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf 
			Avoid setting the [[Prototype]] of an object. Instead, create a new object with the desired [[Prototype]] using Object.create().

			function Animals(name, age) {
			    let newAnimal = Object.create(animalConstructor);
			    newAnimal.name = name;
			    newAnimal.age = age;
			    return newAnimal;
			}
			let animalConstructor = {
			    sing: function() {
			        return `${this.name} can sing`;
			    },
			    dance: function() {
			        return `${this.name} can dance`;
			    }
			}


			function Cats(name, age, whiskerColor) {
			    let newCat = Animals(name, age);
			    Object.setPrototypeOf(newCat, catConstructor);
			    newCat.whiskerColor = whiskerColor;
			    return newCat;
			}
			let catConstructor = {
			    whiskers() {
			        return `I have ${this.whiskerColor} whiskers`;
			    }
			}
			Object.setPrototypeOf(catConstructor, animalConstructor);
			const clara = Cats("Clara", 33, "purple");
			clara.sing();
			clara.whiskers();
			// Expected Output
			// "Clara can sing"
            
::::
download.page(web/js/javascript_ES2009_ES5.md)
::::
download.page(web/js/javascript_ES2015_ES6.md)
::::
download.page(web/js/javascript_ES2016_ES7.md)
::::
download.page(web/js/javascript_ES2017_ES8.md)
::::
download.page(web/js/javascript_ES2019_ES10.md)
::::
download.page(web/js/javascript_ES2020_ES11.md)            
::::
download.page(web/js/typescript.md)            
::::
download.page(web/js/javascript_debugging.md)            