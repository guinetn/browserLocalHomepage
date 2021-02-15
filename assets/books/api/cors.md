# Cors - Cross-origin resource sharing

2009

Allows resources to be requested from another domain 
web application security model
"cross-domain" requests (Ajax, XmlHttpRequest) are forbidden by default by the same-origin security policy.


## Same-origin policy (SOP)
Xeb browser permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same origin (combination of URI scheme, host name, port number)
Prevents a malicious script on one page from obtaining access to sensitive data on another web page through that page's Document Object Model.

## Cors 

Allows to request data from another domain (from outside the page's originating site)

Request to a ***foreign service*** http://server.example.com/Users/1234 may return a record for a person:
{
    "Name": "Alice",
    "Id": 1234,
    "Rank": 7
}
Without CORS support, an attempt to use the data across domains results in a JavaScript error:
<script type="application/javascript" src="http://server.example.com/Users/1234"></script>

1. Browser will download the <script> file, evaluate its contents
2. Misinterpret the raw JSON data as a block and throw a syntax error. Even if the data were interpreted as a JavaScript object literal, it could not be accessed by JavaScript running in the browser, since without a variable assignment, object literals are inaccessible.


## Access-Control-Allow-Origin (ACAO) header

A user visits http://www.example.com 
The page attempts a cross-origin request to fetch the user's data from http://service.example.com. 
A CORS-compatible browser will attempt to make a cross-origin request to service.example.com as follows:

1. Browser request to service.example.com 
Origin: http://www.example.com        Add an extra Origin HTTP header

2. Server (service.example.com) may respond
Access-Control-Allow-Origin: http://www.example.com          requests from the origin are allowed
Access-Control-Allow-Origin: *                               requests from all domains are allowed