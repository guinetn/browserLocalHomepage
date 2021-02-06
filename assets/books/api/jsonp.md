# JSONP - JSON with Padding

2005

Enables sharing of data bypassing same-origin policy which disallows running JavaScript code to read media DOM elements or XMLHttpRequest data fetched from outside the page's originating site

JSONP is vulnerable to the data source replacing the innocuous function call with malicious code, which is why it has been superseded by cross-origin resource sharing 

A server must reply with a response that includes the JSONP function agreed upon by the client and server
Convention: server providing the JSON data offers the requesting website to name the JSONP function, typically using the name jsonp or callback as the named query-string parameter, in its request to the server: 
<script src="http://server.example.com/Users/1234?callback=parseResponse"></script>