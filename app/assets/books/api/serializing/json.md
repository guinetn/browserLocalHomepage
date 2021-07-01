# JSON (JAVASCRIPT OBJECT NOTATION)

[JSON modules landed in Chrome](https://2ality.com/2021/01/import-assertions.html)

```js
import config from './data/config.json' assert { type: 'json' };
```
A core architectural principle of the web is to never use the filename extension to determine what’s inside a file. Instead, content types are used.
JavaScript engine can’t use the filename extension to determine that this is JSON data


- Can be used in JS
- Less overhead than xml
- Use in NoSQL db

# Defined in 
	IETF RFC 7159 		https://tools.ietf.org/html/rfc7159
	ECMA Standard 404	https://www.ecma-international.org/publications/standards/Ecma-404.htm
	Binary version 		https://bsonspec.org   BSON

# JSON value 
	object 	{…}
	array 	[…]
	number
	string
	true
	false
	null

# Official MIME type 		"application/json"
# Unofficial MIME type 	"text/json"
					 	"text/javascript"

• JSON is built on two universal data structures: object and array.

• An object is denoted by braces ({}) that can hold multiple name-value pairs.For each name-value pair, a colon (:) is used to separate the name 
and thevalue, whilst multiple name-value pairs are separated by comma (,) as in thefollowing example: {"id": 1, "eﬀect": "permit"}.

• An array is denoted by brackets ([ ]) that can hold multiple values separatedby commas (,) as in the following example: ["Monday", "Friday", 
"Sunday"].

• A value can be a string in double quotes, or a number, or a Boolean value(true or false), or null, or an object or an array.

• Whitespace can be inserted between any pair of JSON tokens ({ } [ ] " , :).

• JSON is weakly typed { “userName”: “Yos”, “favouriteNumber”: 42, “interests”: [“programming”, “swimming”] }

• JSON Schema Basic Types 
	● string 
	● Numeric types 
	● object 
	● array 
	● boolean 
	● null


	Json objects use 	{}		:
		var obj = {
			property: value
			property: ['a','b']
			property: function() { }
			property: { /* another object (have no access to 'this' of the parent ) */ }
		}


		var parent={
			a:1, b:2,
			child: { c:3, add: function() {  log(this.a+this.b+this.c)   ===> this.a & this.b undefined}}
		parent.child.add() -> NaN

	var JSON = JSON || {};

    JSON.parse( {"message": "Hello" } ) 	NOT OK
    JSON.parse( '{"message": "Hello" }') 	OK

    var datas = '{"services": {  "aquisition": 0,  "bps" :1} }';
	var data = JSON.parse(datas);
	console.log(data.services);
	console.log(data["services"]);
	console.log(data.services.aquisition);
	console.log(data.services.bps);
	for (var key in data.services)
	{
		console.log("k=" + key);
		console.log("v=" + data.services[key]);		
	}


	# GET ALL CHILD PROPERTIES
	function setProperties(o) {
		for(var key in o) {		
			if (typeof(o[key])=="object" || typeof(o[key])=="array")
				setProperties(o[key]);
			else
			{			
				var element = document.getElementById(key);
				if (element != undefined)
					element.innerText = o[key];
			}
		}	
	}



	JSON is a standard data format for exchanging data over the net and between applications. It became popular as a more readable alternative to XML, with the added benefit that Javascript code can read and write JSON data out of the box.
	Its base form, JSON data is a list of name-value entities

	• Numbers, booleans, a null value, arrays, and objects
	• No date type. Any date value is converted to and from an ISO-8601 date string. 
	• Javascript’s special values NaN, Infinity, and -Infinity are simply turned into a null value

	{
		"location": "Zzyzx",
		"weather": "sunny",
		"temperature": 30,
		"celsius": true,
		"temp_forecast": [ 27, 25, 28 ],
		"wind": {
			"direction": "NW",
			"speed": 15
		}
	}

	
var hotel = {
	name: 'Classic',
	menu:{
		A: ['Burgers', 'Fries'],
		B: ['Noodles']
	},
	displayMenu: function (location) {
		console.log('Menu for', this.name, '-', this.menu[1ocation].join(', ));    ← easy access to property by name
	}
hote1.displayMenu('A')    // → Menu for Classic - Burgers, Fries

var ccd ={
	name: 'CCD',
	menu: {
		A: ['Espresso'],
		B: ['Latte', 'Cappucino']
	},
}
var pizzaCentre = {
	name: 'Pizza Centre',
	menu: {
		A: ['Cheese Corn Pizza'],
		B: ['Chicken Delight']
	}
}
hotel.displayMenu.ca11(ccd, 'B') 			// → Menu for CCD - Latte, Cappucino
hotel.displayMenu.ca11(pizzaCentre, 'A')    // → Menu for Pizza Centre - Cheese Corn Pizza




## Create object, properties from variables and assign it a value:

	console.log(json_list["foo"]);
	console.log(json_list["foo"]["alert"]["type"]);
	console.log(json_list["bar"]["alert"]["time"]); 


## To see all this object converted in string, just put it out in a console with console.log(jsonstr):

	var json_list = {}; /* Create an object as JSON root */

	var user = "foo"; /* Create an 'user' variable and assign it 'foo' as property name */
	json_list[user] = {}; /* Creates new 'foo' property as object */

	json_list[user].alert = {}; /* Creates an 'alert' property as object in 'foo' property */
	json_list[user].alert.time = 30; /* You can assign a value using a variable ...  */
	json_list.foo.alert.type = "sec"; /* ... or directly with the property name */

	user = "bar"; /* Use the same 'user' variable but assign it a new 'bar' value */
	json_list[user] = {}; /* Creates new 'bar' property as object */

	var objAlert = { "type": "sec", time: 60 }; /* Create an 'alert' objet filled with properties */
	json_list[user].alert = objAlert; /* Assign an 'alert' property as object from 'objAlert' variable */
	json_list[user].alert.type = "min"; /* You can change his value using a variable... */
	json_list.bar.alert.time = 80; /* ... or directly with the property name */

	// Convert JSON object to string
	var jsonstr = JSON.stringify(json_list);

	access information without loops

	console.log(json_list["foo"]);
	console.log(json_list["foo"]["alert"]["type"]);
	console.log(json_list["bar"]["alert"]["time"]); 





	var items = JSON.parse("{....}")		convert a string into a js object
	var s = JSON.stringify(items)			convert a json object into a string

					 	 ____ No \r\n
				↓		↓
	 var data = '{"name": "mkyong","age": 30,"address": {"streetAddress": "88 8nd Street","city": "New York"},"phoneNumber": [{"type": "home","number": "111 111-1111"},{"type": "fax","number": "222 222-2222"}]}';

		var json = JSON.parse(data);
				
		alert(json["name"]); //mkyong
		alert(json.name); //mkyong
		
		alert(json.address.streetAddress); //88 8nd Street
		alert(json["address"].city); //New York
				
		alert(json.phoneNumber[0].number); //111 111-1111
		alert(json.phoneNumber[1].type); //fax
				
		alert(json.phoneNumber.number); //undefined

 		arr.forEach(function(x) { ...}

  $.getJSON(apiUrl)
	        .done(function (data) {
	            // On success, 'data' contains a list of products.
	            $.each(data, function (key, item) {
	                // Add a list item for the product.
	                $('<li>', { text: formatItem(item) }).appendTo($('#products'));
	            });
	        });				



# List

	 <div id="articles-list">
    	<div class="articles-container" />
  	</div>


	var posts_list = document.getElementById('articles-list');
	var posts_container = posts_list.querySelector('.articles-container');

	var items = JSON.parse('{"posts": {"101": {"title": "....

	let list = document.createElement('div');

	  Object.keys(items.posts).forEach(function(key) {
	  	 console.log(key);

	    let ts = new Date(items.posts[key].created);
	    list.innerHTML += `<article class="article-block">
	      <h2>${items.posts[key].title}</h2>
	      <time>${ts.toDateString()}</time>
	      <div class="excerpt">
	        <p>${items.posts[key].content.substr(0, 150)}...</p>
	      </div>
	      <a href="#${key}" data-post="${key}">Read Post</a>
	    </article>`;
	  });
	  posts_container.insertBefore(list, posts_container.firstChild);




# LINKS	
	http://www.ietf.org/rfc/rfc7159.txt

	https://github.com/flosse/json-file-store
	http://www.json.org
	http://www.json-generator.com/
	http://www.codeproject.com/Articles/779303/JSON-and-Microsoft-technologies
	http://www.codeproject.com/Articles/778374/JQUERY-JSON-and-Angular-Interview-questions
	http://hjson.org/
	[Bidirectional Relationship Support in JSON](https://www.toptal.com/javascript/bidirectional-relationship-in-json)

	http://www.tutorialspoint.com/online_json_editor.htm

# WHAT IS JSON?

	A text format for serializing structured data (objects) in an unordered collection of name-value pairs
	Allow communication
	RFC 7159
	See also jQuery_Succinctly.pdf
	JSON can be a lot slimmer than xml

# JSON SYNTAX RULES

 	Comments of the form //… or /*…*/ are not allowed in JSON. See HJson

## JSON data is written as "name":"value" pairs.  e.g. "firstName":"John"

	, SEPARATE DATA

	: colon, separate name and value

	{} Curly braces  HOLD OBJECTS

	[] Square brackets HOLD ARRAYS
		Just like in JavaScript, an array can contain multiple objects:
		"employees":[ {"firstName":"John", "lastName":"Doe"},
					  {"firstName":"Anna", "lastName":"Smith"},
					  {"firstName":"Peter", "lastName":"Jones"}
					]


		var Post = function(a,b,c,d) { this.a = a; this.b=b; this.c= c; this.d = d}
		let data = [
	      new Post(
	        'Vue.js', 
	        'https://vuejs.org/', 
	        'Chris', 
	        'https://vuejs.org//images/logo.png'
	      ),
	      new Post(
	        'React.js', 
	        'https://facebook.github.io/react/', 
	        'Tim',
	        'http://daynin.github.io/clojurescript-presentation/img/react-logo.png'
	      ), ... 
	    ]



	Strict JSON requires you to do this:					{ "foo":"bar", "red":1 }
	The JavaScript language itself is a little easier:		{ foo:"bar", red:1, }
	Some libraries allows you to be lazy (jsonic…)			foo:bar, red:1,


# Use Envelopes

	you should envelope your data responses!

	// enveloped, a top level object is secure and succinct
	{
	  data: [
	    { ... },
	    { ... },
	    // ...
	  ]
	}
	// non-enveloped, potential security risk
	[
	  { ... },
	  { ... },
	  // ...
	]


# JSON FILES

	File´s extension is '.json'
	MIME type for JSON text is 'application/json'

# Access JSON object in JavaScript
	
	var app = {tom:"1", "joe":2};
	console.log(app.joe);



	var myArray  = '{ "employees" : [' +
	'{ "firstName":"John" , "lastName":"Doe" },' +
	'{ "firstName":"Anna" , "lastName":"Smith" },' +
	'{ "firstName":"Peter" , "lastName":"Jones" } ]}';

	var s = myArray [0].firstName + " " + myArray [0].lastName;
	for(i = 0; i < myArray.length; i++) { out += '<a href="' + myArray[i].url + '">' + myArray[i].display + '</a><br>'; }

	var obj = JSON.parse(myArray);
	document.getElementById("demo").innerHTML =	obj.employees[1].firstName + " " + obj.employees[1].lastName;



	<script>
	       var data = '{"name": "mkyong","age": 30,"address": {"streetAddress": "88 8nd Street","city": "New York"},"phoneNumber": [{"type": "home","number": "111 111-1111"},{"type": "fax","number": "222 222-2222"}]}';

		var json = JSON.parse(data);
				
		alert(json["name"]); //mkyong
		alert(json.name); //mkyong
		
		alert(json.address.streetAddress); //88 8nd Street
		alert(json["address"].city); //New York
				
		alert(json.phoneNumber[0].number); //111 111-1111
		alert(json.phoneNumber[1].type); //fax
				
		alert(json.phoneNumber.number); //undefined
	</script>	






native parsers:  window.JSON or simply the global JSON variable gives you access to the parser.
if (!JSON) { alert("JSON parser missing."); }
# JSON has been part of the EcmaScript 3.1 specification

# BROWSER F12
	window.JSON.parse('{ "foo":"bar", "red":1 }')

	var o = JSON.parse('{"foo":"bar", "red":1 }')
	o.foo
	o.red = 9
	JSON.stringify( o , function censure(key, value) { 
	                    if (typeof value === "string") {return "undefined"; } return value; } )
	"{"foo":"undefined","red":1}"
	JSON.stringify( o , function censure(key, value) { if (typeof value === "number") {return value*10; } return value; } )
	"{"foo":"bar","red":10}"

	JSON.parse()		convert a string into a js object
	JSON.stringify()	convert a json object into a string

	var obj = { index: 'contenu' };

	var string = JSON.stringify(obj);
	alert(typeof string + ' : ' + string); // string : {"index":"contenu"} »

	obj = JSON.parse(string);
	alert(typeof obj + ' : ' + obj); 		// « object : [object Object] »


## Catching errors

			try {
			    JSON.parse("a"); // Error, not a json
			} catch (error) {
			    // Handle the error
			    alert(error.message);
			}

# The native JSON object is based on Douglas Crockford’s JSON2 interface, which provides

		JSON.stringify()  	encode JSON data
						var foo = {};
							foo.address = "my address....";
							foo.age = 3;
						var stringJSON = JSON.stringify(foo);

		var stringJSON = JSON.stringify(foo, censure);
												↓
									function censure(key, value) {
									  if (typeof value === "string") {
									    return undefined;
									  }
									  return value;
									}

 JSON.stringify( JSON.parse('{ "foo":"bar", "red":1 }'), function censure(key, value) {if (typeof value === "string") {return undefined; } return value*10; }} )


# ITERATE

  $.getJSON(apiUrl)
	        .done(function (data) {
	            // On success, 'data' contains a list of products.
	            $.each(data, function (key, item) {
	                // Add a list item for the product.
	                $('<li>', { text: formatItem(item) }).appendTo($('#products'));
	            });
	        });				


	        	

iterate over a JSON structure = tree traversal routine
	Because of the quirks of JavaScript, you have to treat the three main kinds of JavaScript "things" (objects, arrays, primitive values) differently
	a simple traversal function that accepts any JavaScript object tree and traverses it, printing out an indented view of the tree:

// --------------------------------------------------
//                      UTILS
// --------------------------------------------------

	Object.prototype.iterate = function () {
	    var iter = function (that) {
	    for (var property in that) {
	        if (typeof(that[property]) !== 'function') {
	            console.log(that[property]);
	            if (!!that[property] && typeof(that[property]) === 'object') {
	                iter(that[property]);
	            }
	      }
	    }
	   }
	  iter(this);
	}

	yourObject.iterate();






	function traverse(x, level) {
	  if (isArray(x)) {
	    traverseArray(x, level);
	  } else if ((typeof x === 'object') && (x !== null)) {
	    traverseObject(x, level);
	  } else {
	    console.log(level + x);
	  }
	}
	 
	function isArray(o) {
	  return Object.prototype.toString.call(o) === '[object Array]';
	}
	 
	function traverseArray(arr, level) {
	  console.log(level + "<array>");
	  arr.forEach(function(x) {
	    traverse(x, level + "  ");
	  });
	}
	 
	function traverseObject(obj, level) {
	  console.log(level + "<object>");
	  for (var key in obj) {
	    if (obj.hasOwnProperty(key)) {
	      console.log(level + "  " + key + ":");
	      traverse(obj[key], level + "    ");
	    }
	  }
	}





# ITERATE

		var Jim= { name: "Jimbo", age: 60 }
		for (var propertyKey in Jim)
		{
			console.log(propertyKey);
			console.log(Jim[propertyKey]);
		}
		// name, Jimbo, age, 60

	for (var i in dictionary) {
	    dictionary[i].forEach(function(elem, index) {
	        console.log(elem, index);
	    });
	}

	 find yourself iterating over inherited properties
	  for (var key in object) {
	    if (object.hasOwnProperty(key)) {
	        // Do stuff
	    }
	  }

	Object.keys(dictionary).forEach(function(key) {
	    dictionary[key].forEach(function(elem, index) {
	        console.log(elem, index);
	    });
	});


	for (var i in dictionary) {
	    // do something with i
	    // here i will contain the dates

	    for (n = 0; n < dictionary[i].length; n++) {
	        // do something with the inner array of your objects    
	        // dictionary[i][n].id contains the "id" of nth object in the object i
	        // dictionary[i][n].name contains the "name" of nth object in the object i
	    }
	}  

    The for in statement can loop over all of the property names in an object. The enumeration will include functions and prototype properties.
	var fruit = {
    apple: 2,
    orange:5,
    pear:1
	},
	sentence = 'I have ',
	quantity;
	for (kind in fruit){
	    quantity = fruit[kind];
	    sentence += quantity+' '+kind+
	                (quantity===1?'':'s')+
	                ', ';
	}
	 // The following line removes the trailing coma.
	sentence = sentence.substr(0,sentence.length-2)+'.';
	 // I have 2 apples, 5 oranges, 1 pear.



# JSON & XMLHTTPREQUEST

	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://www.example.com/hello.json');
	xhr.onload = function(e) {
	  var data = JSON.parse(this.response);
	  …
	}
	xhr.send();



	<div id="id01"></div>

	<script>
	var xmlhttp = new XMLHttpRequest();
	var url = "myTutorials.txt";

	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
	    {
	        var myArr = JSON.parse(xmlhttp.responseText);
	        myFunction(myArr);
	    }
	}
	xmlhttp.open("GET", url, true);
	xmlhttp.send();

	function myFunction(arr) {
	    var out = "";
	    var i;
	    for(i = 0; i < arr.length; i++) {
	        out += '<a href="' + arr[i].url + '">' +
	        arr[i].display + '</a><br>';
	    }
	    document.getElementById("id01").innerHTML = out;
	}
	</script>




	$("#foo").text("fetching...");
    var url = "http://services.odata.org/V4/TripPinServiceRW/People";
    $.getJSON(url, function (result) {
      $("#foo").text(result.value[0].FirstName);
    });

# JSON
	The line of PHP code that performs the magic of taking a result set from a database and converting it into JSON that can be streamed into our web page is this:	print json_encode($rows);
	This sort of capability is not unique to PHP. With JSON fast eclipsing XML as the preferred way of slinging data around in a web environment, other server-side scripting languages, such as Ruby, VBScript, Perl, and C# have equivalent functionality.


# FETCH
https://github.com/samdutton/simpl/blob/gh-pages/fetch/js/main.js
https://davidwalsh.name/fetch


fetch API.  look at the new window.fetch() method, available now in Firefox and Chrome Canary.

  <p id="data"></p>

  <script src="js/main.js"></script>
	'use strict';

	var data = document.getElementById('data');

	fetch('json/foo.json').then(function(response) {
	  return response.json();
	}).then(function(j) {
	  data.textContent = 'JSON fetched:\n\n' + JSON.stringify(j, null, 2);
	});


	  var url = host_prefix + '/json';
	  $.getJSON(url, function(json){
	    $("#json-response").html(JSON.stringify(json, null, 2));
	  });


# JSONP (JSON WITH PADDING) - A CALLBACK FUNCTION

	JSONP = JSON with Padding = JSON with a callback
	A way to overcome browser restrictions when sending JSON responses from different domains from the client.
    Cross-domain communications with JSONP


## JSONP allows you to specify a callback function that is passed your JSON object. This allows you to bypass the same origin policy and load JSON from an external server into the javascript on your webpage.

	
	Basically, you're not allowed to request JSON data from another domain via AJAX due to same-origin policy. AJAX allows you to fetch data after a page has already loaded, and then execute some code/call a function once it returns. We can't use AJAX but we are allowed to inject <script> tags into our own page and those are allowed to reference scripts hosted at other domains.


## JSONP is JSON with padding, that is, you put a string at the beginning and a pair of parenthesis around it. For example:

	//JSON
	{"name":"stackoverflow","id":5}
	//JSONP
	func({"name":"stackoverflow","id":5});

## The result is that you can load the JSON as a script file. If you previously set up a function called func, then that function will be called with one argument, which is the JSON data, when the script file is done loading. This is usually used to allow for cross-site AJAX with JSON data. If you know that example.com is serving JSON files that look like the JSONP example given above, then you can use code like this to retrieve it, even if you are not on the example.com domain:

	function func(json){
	  alert(json.name);
	}
	var elm = document.createElement("script");
	elm.setAttribute("type", "text/javascript");
	elm.src = "http://example.com/jsonp";
	document.body.appendChild(elm);





	Technic to request data from a server on a different domain (cross-domain request), something prohibited because of the
	Ajax 'same origin policy' (SOP) security. Allow to avoid CORS issues

## JSONP (as in "JSON with Padding") is a method commonly used to bypass the cross-domain policies in web browsers (you are not allowed to make AJAX requests to a webpage perceived to be on a different server by the browser). JSON and JSONP behave differently on both the client and the server


	 SAME-ORIGIN POLICY only permits scripts running on pages originating from the same site – a combination 
	 of scheme, hostname, and port number – to access each other´s DOM with no specific restrictions, but prevents 
	 access to DOM on different sites. When you request JSON or other data from other sites using JavaScript, you may 
	 encounter this error which can be solved multiple ways: JSONP allows you to make a request from one site for JSON 
	 data from another site.


	$.getJSON("http://api.open-notify.org/iss-now.json", function (data) {
	  console.log("data from space", data);
	});

	 Typical error on Chrome:
		 XMLHttpRequest cannot load http:api.open-notify.org/iss-now.json. 
		 No 'Access-Control-Allow-Origin' header is present on the requested resource. 
		 Origin 'file://' is therefore not allowed access.

	With classic xhr request of json data, the browser will, in order
	* download the script file
	* evaluate its contents
	* interpret the raw JSON data as a block
	* throw a syntax error
	In the JSONP usage pattern, the URL request pointed to by the <script> src attribute returns JSON data, with a function call wrapped around it.

												   The padding is a callback function: '?jsoncallback=?'
												   				|
	<script type="application/javascript"						v
			 src="http://server2.example.com/Users/1234?jsonp=parseResponse">
	</script>
	In this example, the received payload would be:
	parseResponse({"Name": "Foo", "Id": 1234, "Rank": 7});

## In this way, a function that is already defined in the JavaScript environment can manipulate the JSON data.

	Essentially, when you try to load JSON from another domain, it fails because there is a domain boundary you can not cross.
	To avoid this, you have to PAD it (P in JSONP). Padding it is essentially wrapping it in a function call (where the function name resides on your client)
		A "normal" JSON response (say, for example, getjson.php):	{foo:'bar'}
		JSONP becomes (Say, getjson.php?callback=parseJSON):    	parseJSON({foo:'bar'})

	Notice how the value that was supplied in callback becomes the name of the function your JSON response is now wrapped in.
	Then your client will want to pass it to parseJSON, a function that exists on your client (that you´ve defined). jQuery (and other libraries) try to take
	care of this for you by generating some "random" function and then sending the response back through your original callback (all this is done under the hood).
	If you have control over the server page generating the JSON, implement a callback method so you can supply how the JSON should be wrapped so you can then work
	with it on your end. (This is only necessary when you´re dealing with data from a domain other than the page the client is currently on).


    https://www.raymondcamden.com/2014/03/12/Reprint-What-in-the-heck-is-JSONP-and-why-would-you-use-it/
	Finally, everything clicked. Turns out, there is a back door to the whole cross domain issue. If you dynamically create a new script block, you are allowed to point this new script block at any domain you want. So for example, I could dynamically create a script block that acts as if I had done:

	<script src="http://search.yahooapis.com/someJSLibrary.js"></script>
	So with that being possible (and with the way browsers are updated this little backdoor probably won't ever be shut) you can now dynamically request dat from another server. But how do you actually work with the data? Normally script tags like the one above load a library of code into your browser. They aren't just used to load data by itself. Another problem is handling the data. If my intent was to request Yahoo search data and present it within my own UI, I'd need to be able to make the request as well as handle the result manually. This is where the whole 'with Padding' thing comes to play. An API that supports JSONP will return not only the pure JSON data you want, but will also wrap it in a function call. So in English, I can tell Yahoo: "Please return search results for 'finances'. I want the data in JSON format and I want you to wrap it in a call to a function called handleIt that I've defined below."

		jsonCallback(
		{
		    "sites":
		    [
		        {
		            "siteName": "JQUERY4U",
		            "domainName": "http://www.jquery4u.com",
		            "description": "#1 jQuery Blog for your Daily News, Plugins, Tuts/Tips &amp; Code Snippets."
		        },
		        {
		            "siteName": "BLOGOOLA",
		            "domainName": "http://www.blogoola.com",
		            "description": "Expose your blog to millions and increase your audience."
		        },
		        {
		            "siteName": "PHPSCRIPTS4U",
		            "domainName": "http://www.phpscripts4u.com",
		            "description": "The Blog of Enthusiastic PHP Scripters"
		        }
		    ]
		});

		(function($) {
		var url = 'http://www.jquery4u.com/scripts/jquery4u-sites.json?callback=?';

		$.ajax({
		   type: 'GET',
		    url: url,
		    async: false,
		    jsonpCallback: 'jsonCallback',
		    contentType: "application/json",
		    dataType: 'jsonp',
		    success: function(json) {
		       console.dir(json.sites);
		    },
		    error: function(e) {
		       console.log(e.message);
		    }
		});

		})(jQuery);


# BSON (BINARY JSON)

	http://bsonspec.org/
	http://en.wikipedia.org/wiki/BSON
	http://www.asp.net/web-api/overview/formats-and-model-binding/bson-support-in-web-api-21
	http://visualstudiomagazine.com/Articles/2014/10/01/Parsing-the-BSON-Beast.aspx?Page=1

## Lightweight  	Traversable 	Efficient (C data type)

	a document storing key/value pairs
	Binary JSON, is a binary-encoded serialization of JSON-like documents.
	It´s lightweigh, easy to parse, and it means more efficient encoding and decoding
	Data interchange format used mainly as a data storage and network transfer format in the MongoDB database.
	It is a binary form for representing simple data structures and associative arrays (called objects or documents in MongoDB).

	BSON adds some "extra" information to documents, like length prefixes, that make it easy and fast to traverse.
	MongoDB, the document-oriented database, uses BSON as both the network and on-disk representation of documents.


	{"hello": "world"}	→	"\x16\x00\x00\x00\x02hello\x00\x06\x00\x00\x00world\x00\x00"
	{"BSON": ["awesome", 5.05, 1986]}	→	"\x31\x00\x00\x00\x04BSON\x00\x26\x00\x00\x00\x020\x00\x08\x00\x00\x00awesome\x00\x011\x00\x33\x33\x33\x33\x33\x33\x14\x40\x102\x00\xc2\x07\x00\x00\x00\x00"

	> npm install bson

	BSON objects consist of an ordered LIST OF ELEMENTS
													↓
											Each element contains FIELD TYPE, name and value
																  ----------
																      ↓
																	string
																	integer (32-bit)
																	integer (64-bit)
																	double (64-bit)
																	date (integer number of milliseconds)
																	byte array
																	boolean
																	null
																	BSON object
																	BSON array
																	Regular expression
																	JavaScript code

## BSON DATA TYPE DESIGNATION

### TYPE VALUE (HEX)						TYPE DESCRIPTION

		\x00								BSON Document : init32 refers to the total number of bytes of the document
		e_list ::= element e_list | ""		Sequence of elements
		\x01								Floating point
		\x02								UTF-8 string
		\x03								Embedded document
		\x04								Array
		\x05								Binary data
		\x06								Deprecated
		\x07								(byte*12) ObjectId
		\x08								\x00 Boolean "false"
		\x08								\x01 Boolean "true"
		\x09								int64 UTC milliseconds in Unix epoch
		\x0A								Null value
		\x0B								Regular expression
		\x0C								Deprecated
		\x0D								JavaScript Code
		\x0E								Symbol
		\x0F								JavaScript code w/ scope
		\x10								32-bit Integer
		\x11								Timestamp.
		\x12								64-bit integer
		\xFF								Min key
		\x7F								Max key
		e_name ::= cstring	Key 			name
		string ::= int32 (byte*) "\x00"		String
		cstring ::= (byte*) "\x00"			CString
		binary ::= int32 subtype (byte*)	Binary
		subtype ::= "\x00"	Binary / 		Generic
		subtype ::= "\x01"					Function
		subtype ::= "\x02"	Old generic 	subtype
		subtype ::= "\x03"					UUID
		subtype ::= "\x05"					MD5
		subtype ::= "\x80"	User 			defined
		code_w_s ::= int32 string document	Code w/ scope


	CORS - Cross-origin resource sharing
		See security.md
		Allow code from different domains to share resources.

## ASP.NET Web API 2.2 Client Libraries can parse BSON using the built-in media type formatters.




# JSONPATCH

	http://jsonpatch.com
	a format for describing changes to a JSON document. It can be used to avoid sending a whole document when only a part has changed.

	The original document
	{
	  "baz": "qux",
	  "foo": "bar"
	}

	The patch
	[
	  { "op": "replace", "path": "/baz", "value": "boo" },
	  { "op": "add", "path": "/hello", "value": ["world"] },
	  { "op": "remove", "path": "/foo"}
	]

	The result
	{
	   "baz": "boo",
	   "hello": ["world"]
	}




# JSON-LD
	http://www.w3.org/TR/json-ld/
	https://dzone.com/articles/what-is-json-ld-and-how-does-it-relate-to-the-sema?edition=115054&utm_source=Spotlight&utm_medium=email&utm_campaign=web%20dev%202015-11-24
	
	JSON is JavaScript Object Notation (said "Jason," like the name) while "LD" stands for "Linked Data." 
	The principles behind JSON  (and its LD offspring), are simplicity and interchangeability.

	JSON-based data format that can be used to implement structured data describing content on your site to Google 
	and other search engines. For example, if you have a list of events, cafes, people or more, you can include this 
	data in your pages in a structured way using the schema.org vocabulary embedded in webpages as a JSON-LD snippet. 
	The structured data helps Google understand your pages better and highlight your content in search features, such 
	events in the Knowledge Graph and rich snippets.



# HJson
	
	http://hjson.org/
	format that caters to humans and helps reduce the errors they make.

	{
	  # specify rate in requests/second
	  "rate": 1000
	  // maybe you prefer js style comments
	  /* or if you feel old fashioned */
	   key: "value"
	   text: look ma, no quotes!
  	   # quoteless strings end with the new-line.
	}




# JSONIQ - THE JSON QUERY LANGUAGE
	
	http://www.jsoniq.org/

	a query and processing language designed for JSON data model. 
	XQuery (standard XML query language) based query language 

	JSONiq fully support XQuery language, with the help of JSONiq we can write a queries which 
	can run on JSON, XML and HTML. JSON expression perform SQL like operations like FOR, LET, 
	WHERE, GROUP BY and SELECT. 

	JSONiq supports JSON to JSON transformations. 
	JSONiq is licensed under the Creative Commons Attribution-ShareAlike 3.0 License.

	See following JSONiq example:
	let $stats := collection("stats")
	for $access in $stats
	group by $url := $access.url
	return
	{
	  "url": $url,
	  "avg": avg($access.response_time),
	  "hits": count($access)
	}


# JWT - JSON WEB TOKEN (pronounced jot)

	<JSON_JWT.md>

	


# GeoJSON http://geojson.org/geojson-spec.html

	format for encoding a variety of geographic data structures”. 
	It is designed to represent discrete geometry objects grouped into feature collections of name/value pairs.
	GeoJSON format—a standard way of representing geographic features in JavaScript.

	https://github.com/mbostock/d3/wiki/Geo-Paths
	
	https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
	GeoJSON is a format for encoding a variety of geographic data structures. A GeoJSON object may represent a geometry, a feature, or a collection of features. GeoJSON uses the JSON standard. The GeoJSONP feed uses the same JSON response, but the GeoJSONP response is wrapped inside the function call, eqfeed_callback. See the GeoJSON site for more information.



# TopoJSON https://github.com/mbostock/topojson

	an extension of GeoJSON that is significantly more compact.) To convert shapefiles to GeoJSON
 	extension of GeoJSON, which can encode topology where geometries are “stitched together from shared line segments called arcs”.
 	TopoJSON eliminates redundancy by storing relational information between geographic features, not merely spatial information.
 	As a result, geometry is much more compact and combined where geometries share features.
 	This results with 80% smaller typical TopoJSON file than its GeoJSON equivalent.




# NATIVE JSON PARSING

		Format
				{ jsonkey1: "value1", jsonkey2: "value2",  }

				Sample:
						{

						  Membre1: {
						    posts: 6230,
						    inscription: '22/08/2003'
						  },

						  Membre2: {
						    posts: 200,
						    inscription: '04/06/2011'
						  }

						}

				Methods

						JSON.parse()		convert a string into a js object
						JSON.stringify()	convert a json object into a string

						var obj = { index: 'contenu' };

						var string = JSON.stringify(obj);
						alert(typeof string + ' : ' + string); // string : {"index":"contenu"} »

						obj = JSON.parse(string);
						alert(typeof obj + ' : ' + obj); 		// « object : [object Object] »


						Catching errors

								try {
								    JSON.parse("a"); // Error, not a json
								} catch (error) {
								    // Handle the error
								    alert(error.message);
								}


	var myArray  = '{ "employees" : [' +
	'{ "firstName":"John" , "lastName":"Doe" },' +
	'{ "firstName":"Anna" , "lastName":"Smith" },' +
	'{ "firstName":"Peter" , "lastName":"Jones" } ]}';

	var s = myArray [0].firstName + " " + myArray [0].lastName;
	for(i = 0; i < myArray.length; i++) { out += '<a href="' + myArray[i].url + '">' + myArray[i].display + '</a><br>'; }

	var obj = JSON.parse(myArray);
	document.getElementById("demo").innerHTML =	obj.employees[1].firstName + " " + obj.employees[1].lastName;


		Standard data transfer for client-side Web applications that use JavaScript.
		internally, the JavaScript engine can evaluate a JSON string and re-materialize an object from it
		JSON has been part of the EcmaScript 3.1 specification
		JSON has become a key component to encode that data that travels over the network.

### The native JSON object is based on Douglas Crockford’s JSON2 interface, which provides

		JSON.stringify()  	encode JSON data
						var foo = {};
							foo.address = "my address....";
							foo.age = 3;
						var stringJSON = JSON.stringify(foo);

						var stringJSON = JSON.stringify(foo, censure);
																↓
													function censure(key, value) {
													  if (typeof value === "string") {
													    return undefined;
													  }
													  return value;
													}


### JSON.parse()  		decode JSON data

		window.JSON or simply the global JSON variable gives you access to the parser.
		The JSON2 implementation also includes .toJSON() methods for the elementary JavaScript types (string, number, boolean, date)
		which are also implemented by the native parsers.

		JSON encoding and decoding
		- - - - - - - - - - - - - - - - - - - - - - - - - - -
		var inst = { entered: new Date(2009, 1, 1, 10, 10),
		   name: "Rick",
		   company: "West Wind Technologies",
		   address: { street: "32 Kaiea Place",
		       city: "Paia",
		       zip: "96779"
		   },
		   visits: 100
		};

		if (!JSON) {
		   alert("JSON parser missing.");
		   return;
		}

		var json = JSON.stringify(inst);
		alert(json);

		var inst2 = JSON.parse(json);
		assert(inst2.name == inst.name &&
		inst2.accesses == inst.accesses);


		pricly dates
		there’s no official way to represent a date literal value in JSON. JSON2 and the native JSON parsers encode dates in an ISO
		string format:
		ISO Encoded Date	"2009-01-03T18:10:00Z"

		Unfortunately the JSON.parse() method does NOT actually convert these ISO date strings back into date objects. So the
		following code is not going to provide what you might expect:

		var date = new Date(2009, 0, 1, 10, 55);
		var json = JSON.stringify(date);
		alert(json);
		var date2 = JSON.parse(json);
		alert(date2 + "\r\n" + typeof date2);

		You’ll end up with a date string in ISO format as shown above rather than data object, and some additional conversion
		is required to turn the date string into a date object.



# JSON on PHP


	.	json_encode() 	convert to json
	.	json_decode()	json to object

		$s = '{"email":"nguinet.progmail.com"}';
	$obj = json_decode($s);
	$file = $s->email;

	http://www.php.net/manual/en/function.json-decode.php


	json_decode works only with a propper json string:
	<?php
	var_dump(json_encode('Hello'));					string(7) ""Hello""

	var_dump(json_decode('Hello'));    // wrong		NULL
	var_dump(json_decode("Hello"));    // wrong		NULL
	var_dump(json_decode('"Hello"'));  // correct 	string(5) "Hello"
	var_dump(json_decode("'Hello'"));  // wrong		NULL

	function isValidJson($strJson) {
	    json_decode($strJson);
	    return (json_last_error() === JSON_ERROR_NONE);
	}


	If you store your json-string in an utf8-file and read it with file_get_contents, please make sure to
	strip leading BOM (byte order mark) before decoding it with json_decode.
	Otherwise json_decode will fail creating an associative array. Instead it will return your data as a string.

	<?php
	$contents = file_get_contents($url);
	$contents = utf8_encode($contents);
	$results = json_decode($contents);
	?>

## LOAD JSON FILE

		view also Dynamic Script Loading (DSL) in DOM.md
		dsl_script_json.php

				<?php
				header("Content-type: text/javascript");
				echo 'var softwares = {
				    "Adobe": ["Acrobat","Dreamweaver","Photoshop","Flash"],
				    "Mozilla": ["Firefox","Thunderbird","Lightning"],
				    "Microsoft": ["Office","Visual C# Express","Azure"]
				};';
				?>
				receiveMessage(softwares);


		client.htm
				function sendDSL() {
				    var scriptElement = document.createElement('script');
				        scriptElement.src = 'dsl_script_json.php';
				    document.body.appendChild(scriptElement);
				}

				function receiveMessage(json) {
				    var tree = '', nbItems, i;

				    for (node in json) {
				        tree   += node + "\n";
				        nbItems = json[node].length;

				        for (i=0; i<nbItems; i++) {
				            tree += '\t' + json[node][i] + '\n';
				        }
				    }
				    alert(tree);
				}
				<p><button type="button" onclick="sendDSL()">Charger le JSON</button></p>




# JSON on jQuery


	getJSON
		console.log("calling for ISS location data...");
		$.getJSON("http://api.open-notify.org/iss-now.json", function (data) {
			console.log("data from space", data);
		});


	[{
	        "position":"1", "category":"A",
	        "title":"Title to first story",     "description":"The first story."
	    },
	    {
	        "position":"2", "category":"B",
	        "title":"Title to second story",    "description":"The second story"
	    },
	    {
	        "position":"3", "category":"B",
	        "title":"Title to third story",    "description":"The third story"
	    }
	]

	jQuery to parse through and put on an html page using this function:
	$.getJSON('page.json', function(data) { … } );

	$.getJSON('page.json', function(data) {
	  var items = [];

	  $.each(data.reponse, function(item, i) {
	    items.push('<li id="' + i.position + '">' + i.title + ' - ' + i.description + '</li>');
	  });

	  $('<ul/>', {
	    'class': 'my-new-list',
	    html: items.join('')
	  }).appendTo('body');
	});



	http://api.jquery.com/jquery.getjson/
	function getListOfCards() {
	    var url = "http://bolaslenses.catuhe.com/Home/ListOfCards/?jsoncallback=?";
	    $.getJSON(url, { colorString: "0" }, function (data) {
	        listOfCards = data;
	        $("#cardsCount").text(listOfCards.length + " cards displayed");
	        $("#waitText").slideToggle("fast");
	    });
	}

	$(document).ready(function () {
	    // Send an AJAX request
	    $.getJSON(apiUrl)
	        .done(function (data) {
	            // On success, 'data' contains a list of products.
	            $.each(data, function (key, item) {
	                // Add a list item for the product.
	                $('<li>', { text: formatItem(item) }).appendTo($('#products'));
	            });
	        });
	});



## AJAX

    $.getJSON('page.json', function(data) { … } );

    $.ajax({
            url: url,
            dataType: 'json',
            success: function (result) {
                ok(true, 'GET succeeded for ' + url);
                ok(!!result, 'Successfully Fetched the Data');
                start();
            },
            error: function (result) {
                ok(false,
                    stringformat('GET on \'{0}\' failed with status=\'{1}\': {2}',
                        url, result.status, result.responseText));
                start();
            }
        });



# JSON ON .NET

## Json is the default data format used by ASP.NET AJAX services created in WCF

	Json.NET
		http://james.newtonking.com/json
	 	a popular high-performance JSON framework for .NET
	 	Include BSON


		dynamic ir = JObject.Parse(rule.Internal);
    	dynamic er = JObject.Parse(rule.External);
    	string destinationType = er.type;
    	string inQueue= ir.queue;


### PM> Install-Package Newtonsoft.Json

		using Newtonsoft.Json;

### SERIALIZE JSON

			Product product = new Product();
			product.Name = "Apple";
			product.Expiry = new DateTime(2008, 12, 28);
			product.Sizes = new string[] { "Small" };

			string json = JsonConvert.SerializeObject(product);
			//{
			//  "Name": "Apple",
			//  "Expiry": "2008-12-28T00:00:00",
			//  "Sizes": [
			//    "Small"
			//  ]
			//}

			string json = @"{
			  'Name': 'Bad Boys',
			  'ReleaseDate': '1995-4-7T00:00:00',
			  'Genres': [
			    'Action',
			    'Comedy'
			  ]
			}";


### DESERIALIZE JSON

			Movie m = JsonConvert.DeserializeObject<Movie>(json);
			string name = m.Name;
			// Bad Boys

		LINQ TO JSON
			JArray array = new JArray();
			array.Add("Manual text");
			array.Add(new DateTime(2000, 5, 23));

			JObject o = new JObject();
			o["MyArray"] = array;

			string json = o.ToString();
			// {
			//   "MyArray": [
			//     "Manual text",
			//     "2000-05-23T00:00:00"
			//   ]
			// }

			VALIDATE JSON
				JsonSchema schema = JsonSchema.Parse(@"{
				  'type': 'object',
				  'properties': {
				    'name': {'type':'string'},
				    'hobbies': {'type': 'array'}
				  }
				}");

				JObject person = JObject.Parse(@"{
				  'name': 'James',
				  'hobbies': ['.NET', 'LOLCATS']
				}");

				bool valid = person.IsValid(schema);
				// true

## JavaScriptSerializer

	DataContractJsonSerializer	(Microsoft)

			http://msdn.microsoft.com/fr-fr/library/bb412179(v=vs.110).aspx
			[DataContract]
		    internal class Person
		    {
		        [DataMember]
		        internal string name;

		        [DataMember]
		        internal int age;
		    }

		    Person p = new Person();  p.name = "John";  p.age = 42;

		    // Serialization
		    MemoryStream stream1 = new MemoryStream();
			DataContractJsonSerializer ser = new DataContractJsonSerializer(typeof(Person));
			ser.WriteObject(stream1, p);
			stream1.Position = 0;
			StreamReader sr = new StreamReader(stream1);
			Console.Write("JSON form of Person object: ");
			Console.WriteLine(sr.ReadToEnd());

			// Deserialization
			stream1.Position = 0;
			Person p2 = (Person)ser.ReadObject(stream1);

			Console.Write("Deserialized back, got name=");
			Console.Write(p2.name);
			Console.Write(", age=");
			Console.WriteLine(p2.age);



			using System.Runtime.Serialization;
			using System.Runtime.Serialization.Json;

			public class JSONHelper
			{
			    public static string Serialize<T>(T obj)
			    {
			        DataContractJsonSerializer serializer =
			              new DataContractJsonSerializer(obj.GetType());
			        using( MemoryStream ms = new MemoryStream() )
			        {
			            serializer.WriteObject(ms, obj);
			            string retVal = Encoding.Default.GetString(ms.ToArray());
			            return retVal;
			        }
			    }

			    public static T Deserialize<T>(string json)
			    {
			        using( MemoryStream ms = new MemoryStream(Encoding.Unicode.GetBytes(json)) )
			        {
			            DataContractJsonSerializer serializer =
			                  new DataContractJsonSerializer(obj.GetType());
			            T obj = (T)serializer.ReadObject(ms);
			            ms.Close();
			            return obj;
			        }
			    }
			}

# WEBMATRIX JSON

	string json = "{\"name\":\"Joe\"}";
    Json.Write(json, Response.Output);

	string distancematrix = "http://maps.googleapis.com/maps/api/distancematrix/json? origins=34746+Florida&destinations=Universal+Studios+Florida|Orlando+Internation+Airport&mode=driving&units=imperial&sensor=false";
	Json.Write(distancematrix, Response.ToString);

	@{
	    var json = File.ReadAllText(Server.MapPath("~/TestJSON.json"));
	    var data = Json.Decode(json);
	}

	<html>
	    <head>
	    </head>
	    <body>
	        <p>
	            @data.destination_addresses <br/>
	            @data.origin_addresses <br/>
	            @data.rows <br/>
	            @data.status
	        </p>
	    </body>
	</html>



# BIDIRECTIONAL RELATIONSHIP SUPPORT IN JSON
https://www.toptal.com/javascript/bidirectional-relationship-in-json

# JSON data structure including entities with parent/child (bidirectional relationship= circular reference) = JavaScript error “Uncaught TypeError: Converting circular structure to JSON”. 

# SAMPLE
var obj = {"name": "I'm parent"}
obj.children = [
	{
		"name": "I'm first child",
		"parent": obj
	},
	{
		"name": "I'm second child",
		"parent": obj
	}
]
var parentJson = JSON.stringify(parent);   → exception Uncaught TypeError: Converting circular structure to JSON

# SOLUTION: add some form of object ID to each object 
var obj = {"id": 100, "name": "I'm parent"}
obj.children = [
	{
		"id": 101,
		"name": "I'm first child",
		"parent": 100
	},
	{
		"id": 102,
		"name": "I'm second child",
		"parent": 100
	}
]
# Issue will be now on serializing and deserializing these references because "100" could be the value of another property
# Then: need for unique values by using Globally Unique Identifiers (GUIDs). For example:
var obj = {
	"id": "28dddab1-4aa7-6e2b-b0b2-7ed9096aa9bc",
	"name": "I'm parent"
}

obj.children = [
	{
		"id": "6616c598-0a0a-8263-7a56-fb0c0e16225a",
		"name": "I'm first child",
        "priority": 100,
		"parent": "28dddab1-4aa7-6e2b-b0b2-7ed9096aa9bc" // matches unique parent id
	},
	{
		"id": "940e60e4-9497-7c0d-3467-297ff8bb9ef2",
		"name": "I'm second child",
        "priority": 200,
		"parent": "28dddab1-4aa7-6e2b-b0b2-7ed9096aa9bc" // matches unique parent id
	}.


# Serializer in JavaScript
serializer that will properly handle a bidirectional relationship without throwing any exceptions
	var convertToJson = function(obj) {

    // Generate a random value structured as a GUID
    var guid = function() {
        function s4() {
            return Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1);
        }

        return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
    };

    // Check if a value is an object
    var isObject = function(value) {
        return (typeof value === 'object');
    }

    // Check if an object is an array
    var isArray = function(obj) {
        return (Object.prototype.toString.call(obj) === '[object Array]');
    }

    var convertToJsonHelper = function(obj, key, objects) {
        // Initialize objects array and 
        // put root object into if it exist
        if(!objects) {
            objects = [];

            if (isObject(obj) && (! isArray(obj))) {
                obj[key] = guid();
                objects.push(obj);
            }
        }

        for (var i in obj) {
            // Skip methods
            if (!obj.hasOwnProperty(i)) {
                continue;
            }

            if (isObject(obj[i])) {
                var objIndex = objects.indexOf(obj[i]);

                if(objIndex === -1) {
                    // Object has not been processed; generate key and continue
                    // (but don't generate key for arrays!)
                    if(! isArray(obj)) {
                        obj[i][key] = guid();
                        objects.push(obj[i]);
                    }

                    // Process child properties
                    // (note well: recursive call)
                    convertToJsonHelper(obj[i], key, objects);
                } else {
                    // Current object has already been processed;
                    // replace it with existing reference
                    obj[i] = objects[objIndex][key];
                }
            }
        }

        return obj;
    }

    // As discussed above, the serializer needs to use some unique property name for
    // the IDs it generates. Here we use "@id" since presumably prepending the "@" to
    // the property name is adequate to ensure that it is unique. But any unique
    // property name can be used, as long as the same one is used by the serializer
    // and deserializer.
    //
    // Also note that we leave off the 3rd parameter in our call to
    // convertToJsonHelper since it will be initialized within that function if it
    // is not provided.
    return convertToJsonHelper(obj, "@id");
}

# Deserializer in JavaScript
	 var convertToObject = function(json) {

    // Check if an object is an array
    var isObject = function(value) {
        return (typeof value === 'object');
    }

    // Iterate object properties and store all reference keys and references
    var getKeys = function(obj, key) {
        var keys = [];
        for (var i in obj) {
            // Skip methods
            if (!obj.hasOwnProperty(i)) {
                continue;
            }

            if (isObject(obj[i])) {
                keys = keys.concat(getKeys(obj[i], key));
            } else if (i === key) {
                keys.push( { key: obj[key], obj: obj } );
            }
        }

        return keys;
    };

    var convertToObjectHelper = function(json, key, keys) {
        // Store all reference keys and references to object map
        if(!keys) {
            keys = getKeys(json, key);

            var convertedKeys = {};

            for(var i = 0; i < keys.length; i++) {
                convertedKeys[keys[i].key] = keys[i].obj;
            }

            keys = convertedKeys;
        }

        var obj = json;

        // Iterate all object properties and object children 
        // recursively and replace references with real objects
        for (var j in obj) {
            // Skip methods
            if (!obj.hasOwnProperty(j)) {
                continue;
            }

            if (isObject(obj[j])) {
                // Property is an object, so process its children
                // (note well: recursive call)
                convertToObjectHelper(obj[j], key, keys);
            } else if( j === key) {
                // Remove reference id
                delete obj[j];
            } else if (keys[obj[j]]) {
                // Replace reference with real object
                obj[j] = keys[obj[j]];
            }
        }

        return obj;
    };

    // As discussed above, the serializer needs to use some unique property name for
    // the IDs it generates. Here we use "@id" since presumably prepending the "@" to
    // the property name is adequate to ensure that it is unique. But any unique
    // property name can be used, as long as the same one is used by the serializer
    // and deserializer.
    //
    // Also note that we leave off the 3rd parameter in our call to
    // convertToObjectHelper since it will be initialized within that function if it
    // is not provided.
    return convertToObjectHelper(json, "@id");
}


### Easily query values from JSON

http://www.sqlservercentral.com/articles/JSON/128550/  
# JSON Select is a new library that exposes several CLR functions that make it easy to pull values out of JSON strings in SQL Server 2005+.
http://www.jsonselect.com/





# Newtonsoft

	using Newtonsoft.Json;
	 
	    class sqlr
	    {
	        public string name;
	        public string description;
	        public string sql;
	    }
	 
	    class sql
	    {
	        public string env;
	        public sqlr[] requests;           
	    }
	 
	 
	     var e = new sql() { env = "aa", requests = new sqlr[2] { new sqlr() { sql = "s1", description = "d1" }, new sqlr() { sql = "s2", description = "d2" } } };
	    var e2 = JsonConvert.SerializeObject(e);
	 
	    sql oo = JsonConvert.DeserializeObject<sql>(jsonSql);
	   
	    orclCmd.CommandText = "SELECT * FROM SITR_EMC.D_METER WHERE ROWNUM <= 10";
	 
	 
	    // Open requests json file
	var jsonSql = File.ReadAllText(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "sql.json"));
	Requests requests = JsonConvert.DeserializeObject<Requests>(jsonSql);
	var req = requests.sqlRequests.FirstOrDefault(r => r.name == "meters_sept_2018");
	if (req == null)
	{
	    Console.WriteLine($"No request named meters_sept_2018 found. Check 'json.sql' file. Stopping");
	    }
	 
	 
	 
	{
	 
	    "env": "dev",
	    "sqlRequests": [
	        {
	            "name": "meters_sept_2018",
	            "description": "meters on september 2018, fast",
	            "sql": "SELECT * FROM SITR_EMC.D_METER WHERE ROWNUM <= 10"
	        },
	        {
	            "name": "meters_sept_2018 II",
	            "description": "meters on september 2018, fast II",
	            "sql": "SELECT * FROM SITR_EMC.D_METER WHERE ROWNUM <= 20"
	        }
	    ]
	    }               

# json types

	https://fr.slideshare.net/yosriady/writing-domain-specific-languages-with-json-schema


# samples

	luckey.fr

	<script type="text/javascript">

	  // City Managers
	  window.cities = {
	          "Aix-en-Provence": {
	        "icon": "/assets/city_icons/aix.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Sami",
	                "photo":  "/assets/team_members/Sami1.jpg" 
	              },
	             
	              {
	                "first_name": "Modesty",
	                "photo":  "/assets/team_members/Modesty.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.529742" || "43.529742",
	          "address_lng": "5.4474270000000615" || "5.4474270000001",
	          "city_address_lat": "43.529742" || null,
	          "city_address_lng": "5.4474270000001" || null
	      },

	          "Ajaccio": {
	        "icon": "/assets/city_icons/icone-ajaccio.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/ajaccio" 
	              },
	             
	          ],
	          "address_lat": "" || "41.919229",
	          "address_lng": "" || "8.7386349999999",
	          "city_address_lat": "41.919229" || null,
	          "city_address_lng": "8.7386349999999" || null
	      },

	          "Annecy": {
	        "icon": "/assets/city_icons/iconeannecy.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/annecy" 
	              },
	             
	          ],
	          "address_lat": "" || "45.899247",
	          "address_lng": "" || "6.129384",
	          "city_address_lat": "45.899247" || null,
	          "city_address_lng": "6.129384" || null
	      },

	          "Arles": {
	        "icon": "/assets/city_icons/if_travel_Colloseum_1045177.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/arles" 
	              },
	             
	          ],
	          "address_lat": "" || "43.676647",
	          "address_lng": "" || "4.6277769",
	          "city_address_lat": "43.676647" || null,
	          "city_address_lng": "4.6277769" || null
	      },

	          "Avignon": {
	        "icon": "/assets/city_icons/avignon.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Zohra",
	                "photo":  "/assets/team_members/Zohra3.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.59848899999999" || "43.949317",
	          "address_lng": "5.486460999999963" || "4.805528",
	          "city_address_lat": "43.949317" || null,
	          "city_address_lng": "4.805528" || null
	      },

	          "Bassin d'Arcachon": {
	        "icon": "/assets/city_icons/bassin-d-arcachon-icon-1537350686.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/bassin-arcachon" 
	              },
	             
	          ],
	          "address_lat": "" || "44.6764023",
	          "address_lng": "" || "-1.1161165999999",
	          "city_address_lat": "44.6764023" || null,
	          "city_address_lng": "-1.1161165999999" || null
	      },

	          "Biarritz": {
	        "icon": "/assets/city_icons/basque.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Julie",
	                "photo":  "/assets/team_members/Juleq.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.4741023" || "43.4831519",
	          "address_lng": "-1.5621191999999837" || "-1.558626",
	          "city_address_lat": "43.4831519" || null,
	          "city_address_lng": "-1.558626" || null
	      },

	          "Bordeaux": {
	        "icon": "/assets/city_icons/bordeaux.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Karine",
	                "photo":  "/assets/team_members/karine1.jpg" 
	              },
	             
	          ],
	          "address_lat": "44.857447" || "44.837789",
	          "address_lng": "2.287592000000018" || "-0.57917999999995",
	          "city_address_lat": "44.837789" || null,
	          "city_address_lng": "-0.57917999999995" || null
	      },

	          "Cabourg": {
	        "icon": "/assets/city_icons/cabourg-icon-1537348091.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/cabourg" 
	              },
	             
	          ],
	          "address_lat": "" || "49.287981",
	          "address_lng": "" || "-0.11629199999993",
	          "city_address_lat": "49.287981" || null,
	          "city_address_lng": "-0.11629199999993" || null
	      },

	          "Caen": {
	        "icon": "/assets/city_icons/Caen11.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Estelle",
	                "photo":  "/assets/team_members/Estelle6.jpg" 
	              },
	             
	          ],
	          "address_lat": "49.1870574" || "49.182863",
	          "address_lng": "-0.2993203999999423" || "-0.370679",
	          "city_address_lat": "49.182863" || null,
	          "city_address_lng": "-0.370679" || null
	      },

	          "Calvi": {
	        "icon": "/assets/city_icons/icone-calvi.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/calvi" 
	              },
	             
	          ],
	          "address_lat": "" || "42.567651",
	          "address_lng": "" || "8.757222",
	          "city_address_lat": "42.567651" || null,
	          "city_address_lng": "8.757222" || null
	      },

	          "Cannes": {
	        "icon": "/assets/city_icons/cannes.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Luis",
	                "photo":  "/assets/team_members/Luis2.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.55665779999999" || "43.552847",
	          "address_lng": "7.008082300000069" || "7.017369",
	          "city_address_lat": "43.552847" || null,
	          "city_address_lng": "7.017369" || null
	      },

	          "Carcassonne": {
	        "icon": "/assets/city_icons/carcassone.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/carcassonne" 
	              },
	             
	          ],
	          "address_lat": "" || "43.212161",
	          "address_lng": "" || "2.353663",
	          "city_address_lat": "43.212161" || null,
	          "city_address_lng": "2.353663" || null
	      },

	          "Chamonix": {
	        "icon": "/assets/city_icons/chamonix-logo-2.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/chamonix" 
	              },
	             
	          ],
	          "address_lat": "" || "45.923697",
	          "address_lng": "" || "6.8694330000001",
	          "city_address_lat": "45.923697" || null,
	          "city_address_lng": "6.8694330000001" || null
	      },

	          "Courchevel": {
	        "icon": "/assets/city_icons/courchevel.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/courchevel" 
	              },
	             
	          ],
	          "address_lat": "" || "45.4203",
	          "address_lng": "" || "6.61409",
	          "city_address_lat": "45.4203" || null,
	          "city_address_lng": "6.61409" || null
	      },

	          "Deauville": {
	        "icon": "/assets/city_icons/if_beach_umbrella_1223444.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Estelle",
	                "photo":  "/assets/team_members/Estelle6.jpg" 
	              },
	             
	          ],
	          "address_lat": "" || "49.353976",
	          "address_lng": "" || "0.075121999999965",
	          "city_address_lat": "49.353976" || null,
	          "city_address_lng": "0.075121999999965" || null
	      },

	          "Genève": {
	        "icon": "/assets/city_icons/geneve3.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/geneve" 
	              },
	             
	          ],
	          "address_lat": "" || "46.2043907",
	          "address_lng": "" || "6.1431577",
	          "city_address_lat": "46.2043907" || null,
	          "city_address_lng": "6.1431577" || null
	      },

	          "Grenoble": {
	        "icon": "/assets/city_icons/grenoble.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "François",
	                "photo":  "/assets/team_members/François4.jpg" 
	              },
	             
	              {
	                "first_name": "Thibaud",
	                "photo":  "/assets/team_members/Thibaud.png" 
	              },
	             
	          ],
	          "address_lat": "45.1951438" || "45.188529",
	          "address_lng": "5.714443899999992" || "5.724524",
	          "city_address_lat": "45.188529" || null,
	          "city_address_lng": "5.724524" || null
	      },

	          "Guéthary": {
	        "icon": "/assets/city_icons/if_flip-flops-travel-holidays-fashion-summertime-sandals-footwear_3027563.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Julie",
	                "photo":  "/assets/team_members/Juleq.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.4741023" || "43.421216",
	          "address_lng": "-1.5621191999999837" || "-1.609933",
	          "city_address_lat": "43.421216" || null,
	          "city_address_lng": "-1.609933" || null
	      },

	          "Honfleur": {
	        "icon": "/assets/city_icons/honfleur.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Estelle",
	                "photo":  "/assets/team_members/Estelle6.jpg" 
	              },
	             
	          ],
	          "address_lat": "49.418762" || "49.418762",
	          "address_lng": "0.23326199999996788" || "0.23326199999997",
	          "city_address_lat": "49.418762" || null,
	          "city_address_lng": "0.23326199999997" || null
	      },

	          "La Baule": {
	        "icon": "/assets/city_icons/laBaule.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/la-baule" 
	              },
	             
	          ],
	          "address_lat": "" || "47.2869183",
	          "address_lng": "" || "-2.3913777",
	          "city_address_lat": "47.2869183" || null,
	          "city_address_lng": "-2.3913777" || null
	      },

	          "La Rochelle": {
	        "icon": "/assets/city_icons/larochelle.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/la-rochelle" 
	              },
	             
	          ],
	          "address_lat": "" || "46.160329",
	          "address_lng": "" || "-1.1511390000001",
	          "city_address_lat": "46.160329" || null,
	          "city_address_lng": "-1.1511390000001" || null
	      },

	          "Le Touquet Paris Plage": {
	        "icon": "/assets/city_icons/if_travel_sunhat_1047426.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/le-touquet-paris-plage" 
	              },
	             
	          ],
	          "address_lat": "" || "50.521276",
	          "address_lng": "" || "1.590675",
	          "city_address_lat": "50.521276" || null,
	          "city_address_lng": "1.590675" || null
	      },

	          "Lille": {
	        "icon": "/assets/city_icons/lille.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/lille" 
	              },
	             
	          ],
	          "address_lat": "" || "50.62925",
	          "address_lng": "" || "3.0572560000001",
	          "city_address_lat": "50.62925" || null,
	          "city_address_lng": "3.0572560000001" || null
	      },

	          "Londres": {
	        "icon": "/assets/city_icons/Call London.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/londres" 
	              },
	             
	          ],
	          "address_lat": "" || "51.5073509",
	          "address_lng": "" || "-0.12775829999998",
	          "city_address_lat": "51.5073509" || null,
	          "city_address_lng": "-0.12775829999998" || null
	      },

	          "Lubéron": {
	        "icon": "/assets/city_icons/luberon.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/luberon" 
	              },
	             
	          ],
	          "address_lat": "" || "43.949317",
	          "address_lng": "" || "4.805528",
	          "city_address_lat": "43.949317" || null,
	          "city_address_lng": "4.805528" || null
	      },

	          "Lyon": {
	        "icon": "/assets/city_icons/lyon.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Christophe",
	                "photo":  "/assets/team_members/Christophe.jpg" 
	              },
	             
	              {
	                "first_name": "Pierre",
	                "photo":  "/assets/team_members/Pierre.png" 
	              },
	             
	          ],
	          "address_lat": "45.750777" || "45.764043",
	          "address_lng": "4.81958080000004" || "4.835659",
	          "city_address_lat": "45.764043" || null,
	          "city_address_lng": "4.835659" || null
	      },

	          "Marseille": {
	        "icon": "/assets/city_icons/marseille.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Sami",
	                "photo":  "/assets/team_members/Sami1.jpg" 
	              },
	             
	              {
	                "first_name": "Modesty",
	                "photo":  "/assets/team_members/Modesty.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.28756670000001" || "43.296482",
	          "address_lng": "5.388710500000002" || "5.36978",
	          "city_address_lat": "43.296482" || null,
	          "city_address_lng": "5.36978" || null
	      },

	          "Megève": {
	        "icon": "/assets/city_icons/megeve.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Christophe",
	                "photo":  "/assets/team_members/Christophe.jpg" 
	              },
	             
	          ],
	          "address_lat": "45.856876" || "45.856876",
	          "address_lng": "6.617750000000001" || "6.61775",
	          "city_address_lat": "45.856876" || null,
	          "city_address_lng": "6.61775" || null
	      },

	          "Monaco": {
	        "icon": "/assets/city_icons/monaco-icon-1537364834.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/monaco" 
	              },
	             
	          ],
	          "address_lat": "" || "43.7384176",
	          "address_lng": "" || "7.4246158",
	          "city_address_lat": "43.7384176" || null,
	          "city_address_lng": "7.4246158" || null
	      },

	          "Montpellier": {
	        "icon": "/assets/city_icons/montpellier.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Simon",
	                "photo":  "/assets/team_members/Simon.jpg" 
	              },
	             
	              {
	                "first_name": "Franck",
	                "photo":  "/" 
	              },
	             
	          ],
	          "address_lat": "43.60565699999999" || "43.610769",
	          "address_lng": "3.8755201999999827" || "3.876716",
	          "city_address_lat": "43.610769" || null,
	          "city_address_lng": "3.876716" || null
	      },

	          "Montréal": {
	        "icon": "/assets/city_icons/montreal-1483467822.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Soumaly",
	                "photo":  "/assets/team_members/Soumaly2.jpg" 
	              },
	             
	              {
	                "first_name": "Côme",
	                "photo":  "/assets/team_members/Come.jpg" 
	              },
	             
	          ],
	          "address_lat": "45.50428" || "45.5016889",
	          "address_lng": "-73.55747400000001" || "-73.567256",
	          "city_address_lat": "45.5016889" || null,
	          "city_address_lng": "-73.567256" || null
	      },

	          "Nantes": {
	        "icon": "/assets/city_icons/nantes.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Alexis",
	                "photo":  "/assets/team_members/Alexis.jpg" 
	              },
	             
	          ],
	          "address_lat": "47.2143472" || "47.218371",
	          "address_lng": "-1.5657165999999734" || "-1.553621",
	          "city_address_lat": "47.218371" || null,
	          "city_address_lng": "-1.553621" || null
	      },

	          "Nice": {
	        "icon": "/assets/city_icons/nice-1483467430.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Louise",
	                "photo":  "/assets/team_members/LouiseD.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.7328248" || "43.7101728",
	          "address_lng": "7.249282499999936" || "7.2619532",
	          "city_address_lat": "43.7101728" || null,
	          "city_address_lng": "7.2619532" || null
	      },

	          "Nîmes": {
	        "icon": "/assets/city_icons/iconnimes2.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/nimes" 
	              },
	             
	          ],
	          "address_lat": "" || "43.836699",
	          "address_lng": "" || "4.360054",
	          "city_address_lat": "43.836699" || null,
	          "city_address_lng": "4.360054" || null
	      },

	          "Paris": {
	        "icon": "/assets/city_icons/paris.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Arnaud",
	                "photo":  "/assets/team_members/arnaud2.jpg" 
	              },
	             
	              {
	                "first_name": "Nils",
	                "photo":  "/assets/team_members/Nils.jpg" 
	              },
	             
	              {
	                "first_name": "Yassine",
	                "photo":  "/" 
	              },
	             
	          ],
	          "address_lat": "48.8964081" || "48.856614",
	          "address_lng": "2.3363217999999506" || "2.3522219",
	          "city_address_lat": "48.856614" || null,
	          "city_address_lng": "2.3522219" || null
	      },

	          "Québec": {
	        "icon": "/assets/city_icons/quebec2.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Yannick",
	                "photo":  "/assets/team_members/yannick-1544571665.jpg" 
	              },
	             
	          ],
	          "address_lat": "46.8369601" || "52.9399159",
	          "address_lng": "-71.2214353" || "-73.5491361",
	          "city_address_lat": "52.9399159" || null,
	          "city_address_lng": "-73.5491361" || null
	      },

	          "Reims": {
	        "icon": "/assets/city_icons/reims1.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/reims" 
	              },
	             
	          ],
	          "address_lat": "" || "49.258329",
	          "address_lng": "" || "4.031696",
	          "city_address_lat": "49.258329" || null,
	          "city_address_lng": "4.031696" || null
	      },

	          "Rennes": {
	        "icon": "/assets/city_icons/rennes.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Stéphane",
	                "photo":  "/assets/team_members/stephane.jpg" 
	              },
	             
	          ],
	          "address_lat": "" || "48.117266",
	          "address_lng": "" || "-1.6777926",
	          "city_address_lat": "48.117266" || null,
	          "city_address_lng": "-1.6777926" || null
	      },

	          "Saint-Jean-de-Luz": {
	        "icon": "/assets/city_icons/stTropez.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Julie",
	                "photo":  "/assets/team_members/Juleq.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.4741023" || "43.388051",
	          "address_lng": "-1.5621191999999837" || "-1.663055",
	          "city_address_lat": "43.388051" || null,
	          "city_address_lng": "-1.663055" || null
	      },

	          "Saint-Malo": {
	        "icon": "/assets/city_icons/logostmalo.png",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/saint-malo" 
	              },
	             
	          ],
	          "address_lat": "" || "48.649337",
	          "address_lng": "" || "-2.025674",
	          "city_address_lat": "48.649337" || null,
	          "city_address_lng": "-2.025674" || null
	      },

	          "Saint-Raphaël ": {
	        "icon": "/assets/city_icons/if_glasses_308397.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Luis",
	                "photo":  "/assets/team_members/Luis2.jpg" 
	              },
	             
	          ],
	          "address_lat": "" || "43.42519",
	          "address_lng": "" || "6.76837",
	          "city_address_lat": "43.42519" || null,
	          "city_address_lng": "6.76837" || null
	      },

	          "Saint-Tropez": {
	        "icon": "/assets/city_icons/if_Cocktail_490201.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/st-tropez" 
	              },
	             
	          ],
	          "address_lat": "" || "43.2676808",
	          "address_lng": "" || "6.6407108999999",
	          "city_address_lat": "43.2676808" || null,
	          "city_address_lng": "6.6407108999999" || null
	      },

	          "Ski": {
	        "icon": "/assets/city_icons/ski.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/ski" 
	              },
	             
	          ],
	          "address_lat": "" || "",
	          "address_lng": "" || "",
	          "city_address_lat": "" || null,
	          "city_address_lng": "" || null
	      },

	          "Strasbourg": {
	        "icon": "/assets/city_icons/strasbourg.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Amaury",
	                "photo":  "/assets/team_members/Amaury3.png" 
	              },
	             
	          ],
	          "address_lat": "48.8964081" || "48.5734053",
	          "address_lng": "2.3363217999999506" || "7.7521113",
	          "city_address_lat": "48.5734053" || null,
	          "city_address_lng": "7.7521113" || null
	      },

	          "Toronto": {
	        "icon": "/assets/city_icons/icone.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Yvan",
	                "photo":  "/assets/team_members/Yvan3.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.63558450000001" || "43.653226",
	          "address_lng": "-79.3989259" || "-79.3831843",
	          "city_address_lat": "43.653226" || null,
	          "city_address_lng": "-79.3831843" || null
	      },

	          "Toulon": {
	        "icon": "/assets/city_icons/iconfinder_sunny_307930.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Sami",
	                "photo":  "/assets/team_members/Sami1.jpg" 
	              },
	             
	          ],
	          "address_lat": "" || "43.124228",
	          "address_lng": "" || "5.928",
	          "city_address_lat": "43.124228" || null,
	          "city_address_lng": "5.928" || null
	      },

	          "Toulouse": {
	        "icon": "/assets/city_icons/toulouse.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "Hanna",
	                "photo":  "/assets/team_members/Hanna3.jpg" 
	              },
	             
	          ],
	          "address_lat": "43.604652" || "43.604652",
	          "address_lng": "1.4442090000000007" || "1.444209",
	          "city_address_lat": "43.604652" || null,
	          "city_address_lng": "1.444209" || null
	      },

	          "Vancouver": {
	        "icon": "/assets/city_icons/if_nature-natural_87_1163040.svg",
	        "city_managers": [
	             
	              {
	                "first_name": "",
	                "photo":  "/vancouver" 
	              },
	             
	          ],
	          "address_lat": "" || "49.2827291",
	          "address_lng": "" || "-123.1207375",
	          "city_address_lat": "49.2827291" || null,
	          "city_address_lng": "-123.1207375" || null
	      },

	    
	  };

	  window.locale = "fr";

	  window.environment = "production";

	  window.country_code =  "fr" ;

	  window.partner = "Luckey".toLowerCase();


	  // Get environment and API keys
	  window.raygunApiKey = "E0mGPp+AcJvYNMxEQctguw==" || null

	  // Translations for Dropzone
	      window.dictDefaultMessage = "Glissez les photos de votre bien ici (ou cliquez)";
	    window.dictRemoveFile = "Retirer";
	    window.dictFileTooBig = "Le fichier est trop lourd. Taille maximale : 5Mo";
	    window.dictResponseError = "Une erreur est survenue. Merci de réessayer ou de choisir une autre image.";
	  

	  // Translations for Bootstrap Validators
	  window.validatorAddress = "L'adresse du logement est nécessaire";
	  window.validatorName = "Merci d'entrer votre prénom et nom";
	  window.validatorPhone = "Merci d'entrer un numéro de téléphone";
	  window.validatorPhoneValid = "Merci d'entrer un numéro valide";
	  window.validatorEmail = "L'adresse mail est nécessaire";
	  window.validatorEmailValid = "Merci d'entrer une adresse email valide";
	  window.validatorAvailability = "Merci d'entrer la disponibilité";
	  window.validatorSurface = "Merci d'entrer la surface du logement";
	  window.validatorSurfaceValid = "Merci d'entrer un nombre";
	  window.validatorMessage = "Merci d'entrer un message";

	  // Set window gift if gift page
	   
	    window.gift = null;
	  
	</script>	    



