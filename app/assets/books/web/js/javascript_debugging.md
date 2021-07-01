# JAVASCRIPT DEBUGGING


## Chrome DevTools

Google Chrome browser offers a built-in developer tools (aka DevTools) that help developers edit their code directly on the browser, add breakpoints to detect issues and debug their code quicker.

* Keyboard Shortcuts
- Open DevTools Elements panel: CTRL + SHIFT + C
- Open DevTools Console panel: CTRL + SHIFT + J

* DevTools Panels
- Elements: Inspect and edit DOM nodes and style attributes
- Console: View and run JavaScript code
- Sources: Debug JavaScript, add breakpoints, etc.
- Network: View and debug network-related activities
- Performance: Analyse speed and optimization
- Memory: Track memory usage and fix related issues
- Application: Inspect localStorage, sessionStorage, cookies, IndexDB, etc.
- Security: Debug certificate and other security issues
- Lighthouse: Audit the app quality, performance, accessibility, SEO, etc

* console.log('b');
debugger;

* Adding a Breakpoint
Open DevTools Sources Panel  
On left navigation panel to select the .js file where a breakpoint will be added.  
Right-click the line where you want to add a breakpoint on, then select 'Add Breakpoint  

| Breakpoint Type | Use This When You Want To Pause...|
|---|---|
| Line-of-code | On an exact region of code.|
| Conditional line-of-code | On an exact region of code, but only when |some other condition is true.
| DOM | On the code that changes or removes a specific DOM node, or its |children.
| XHR | When an XHR URL contains a string pattern.|
| Event listener | On the code that runs after an event, such as click, |is fired.
| Exception | On the line of code that is throwing a caught or uncaught |exception.
| Function | Whenever a specific function is called.|

* View/Make Changes to Local, Closure and Global Properties
When app is paused you can view and edit the local, closure and global properties. Expand the 'Scope' panel

* Create, Save and Run Snippets
execute and reuse scripts in any part of your app  
Sources tab → Snippets  
$$("img").forEach(e=>console.log(e.currentSrc))  

* View the Call Stack
 useful when you have a lot of asynchronous functions  

* Blackboxing
exclude some scripts from running (errors...)  
Sources tab → right-click on the middle panel → click 'Add script to ignore list'

- https://buddy.works/tutorials/debugging-javascript-efficiently-with-chrome-devtools
- https://developers.google.com/web/tools/chrome-devtools/javascript/reference