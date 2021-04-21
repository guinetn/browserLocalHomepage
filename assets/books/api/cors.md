# Cors - Cross-origin resource sharing

2009

Allows resources to be requested from another domain 
web application security model
"cross-domain" requests (Ajax, XmlHttpRequest) are forbidden by default by the same-origin security policy.


## Same-origin policy (SOP)
Wser permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same origin (combination of URI scheme, host name, port number)
Prevents a malicious script on one page from obtaining access to sensitive data on another web page through that page's Document Object Model.
             
The api Same-origin policy fights one of the most common cyber attacks out there: CSRF in wich  a malicious website attempts to take advantage of the browser’s cookie storage system.

download.page(security/attack_csrf.md)

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

## FIX CORS

* Build your own proxy

Use the fact that the same origin policy is not enforced within server-to-server communication

create a proxy that uses express middleware to apply a `Access-Control-Allow-Origin: *` header to every response from the server.

express-cors-proxy-server.example.js
```js
const express = require('express');
const request = require('request');

const app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  next();
});

app.get('/jokes/random', (req, res) => {
  request(
    { url: 'https://joke-api-strict-cors.appspot.com/jokes/random' },
    (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return res.status(500).json({ type: 'error', message: err.message });
      }

      res.json(JSON.parse(body));
    }
  )
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`listening on ${PORT}`));
```

CORS Anywhere is a NodeJS reverse proxy which adds CORS headers to the proxied request.
- https://github.com/Rob--W/cors-anywhere/#documentation

- https://blog.bitsrc.io/how-and-why-you-should-avoid-cors-in-single-page-apps-db25452ad2f8