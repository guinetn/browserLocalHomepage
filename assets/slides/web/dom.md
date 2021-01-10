# DOM (Document Object Model) 

Api: HTML programming interface 
Represents the document as nodes and objects (structure, style, content) that can be changed 

- https://vanillajstoolkit.com/reference/#DOM-Injection

# data-* custom attributes

    HTML5 supports  'data-'custom attributes within all HTML elements
	    <div id="myDiv" data-custom-attr="My Value"> Bla Bla </div>
	    var theDiv = document.getElementById('myDiv');
	    attr = theDiv.getAttribute('data-custom-attr');

  	darkThemeSelected ? 
    document.body.setAttribute('data-theme', 'dark') : document.body.removeAttribute('data-theme');

    <button class="todocompleted" data-todo="my data">
    var index = event.target.getAttribute('data-todo');