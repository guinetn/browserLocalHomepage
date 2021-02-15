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