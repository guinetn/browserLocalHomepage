# API

/api/v1
X-MyGreatApi-Token : apiKey
Rate Limits: 30... API calls/second. Else Status Code 429

APIs provide you with an endpoint or a specific URL where the data or functions you want are exposed. 

APIs provide a layer of abstraction for the user. Abstraction hides everything but what is relevant to the user, making it simple to use.
It hides internals complexity

- You're APIs
- Web APIs are 'Web Browser APIs': Chrome, Firefox, Safari, etc., have them built-in so that we can use them to add features to our sites, speech, audio, gamepad, events. https://developer.mozilla.org/en-US/docs/Web/API/Event


## Web resources
First defined as documents/files identified by their URLs
Today definition is much more generic and abstract, and includes every thing, entity, or action that can be identified, named, addressed, handled, or performed in any way on the Web. 

curl https://api.openai.com/v1/engines/curie/completions


![](assets\books\api\assets\api-diagram.webp)


- https://github.com/public-apis/public-apis
- https://public-apis.io/

- https://developer.spotify.com/
- https://developers.google.com/youtube/v3
- https://developer.twitter.com/en/docs/twitter-api
- https://www.twilio.com/docs/sms/send-messages
- https://cloud.google.com/maps-platform
- https://www.edamam.com/ (nutrition, food, recipes)
- https://stripe.com/docs/api

- https://finnhub.io/ retrieve data from the stock market
- https://www.exchangerate-api.com/
- https://www.coindesk.com/coindesk-api
- https://github.com/1Forge/javascript-forex-quotes

- https://github.com/ContinuumIO/tranquilizer

- https://hoppscotch.io/
- https://pokeapi.co/
- https://api.nasa.gov/
- https://spaceflightnewsapi.net/

* Fake api

- https://official-joke-api.appspot.com/random_joke
- https://source.unsplash.com/random
- https://swapi.dev/api/people/5/   The Star Wars API


- https://jsonplaceholder.typicode.com/

```js
	fetch('https://jsonplaceholder.typicode.com/todos/1')
	.then(response => response.json())
	.then(json => console.log(json))
	
	async function fetchData() {
		const result = await fetch('http://reqres.in/api/users/2')
	const jsonResult = await result.json()
	console.log(jsonResult.first_name) // Lucille
	}
```

```js
    document.addEventListener("click", function (event) {
    // Checking if the button was clicked
    if (!event.target.matches("#button")) return;

    fetch("https://official-joke-api.appspot.com/random_joke")
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch(() => renderError());
    });
```

* SEND GET REQUEST
Any properties that may have spaces or special characters in them should be passed into the encodeURIComponent() to encode it.

```html
<form id="post">
	<label for="title">Title</label>
	<input type="text" name="title" id="title" value="Go to the beach">  
```

```js
// Get the form data
let form = document.querySelector('form');
let data = new FormData(form);

// Submit the form data
fetch('https://jsonplaceholder.typicode.com/posts', {
	method: 'POST',
	body: new URLSearchParams(data).toString(),
	headers: {
		'Content-type': 'application/x-www-form-urlencoded'
	}
}).then(function (response) {
	if (response.ok) {
		return response.json();
	}
	throw response;
}).then(function (data) {
	console.log(data);
}).catch(function (error) {
	console.warn(error);
});
```

* SEND POST REQUEST
```js

function serialize (data) {
  // Serialize form data into an object
	let obj = {};
	for (let [key, value] of data) {
		if (obj[key] !== undefined) {
			if (!Array.isArray(obj[key])) {
				obj[key] = [obj[key]];
			}
			obj[key].push(value);
		} else {
			obj[key] = value;
		}
	}
	return obj;
}

// Get the form data
let form = document.querySelector('form');
let data = new FormData(form);

// Submit to the API
fetch('https://jsonplaceholder.typicode.com/posts', {
	method: 'POST',
	body: JSON.stringify(serialize(data)),
	headers: {
		'Content-type': 'application/json; charset=UTF-8'
	}
}).then(function (response) {
	if (response.ok) {
		return response.json();
	}
	throw response;
}).then(function (data) {
	console.log(data);
}).catch(function (error) {
	console.warn(error);
});
```

::::
## Request Pipeline

Add middlewares
hello.js
module.exports = (req, res, next) => {
  res.header('X-Hello', 'World')
  next()
}

::::
download.page(api/doc/_doc.md)
::::
download.page(api/architecture/_architecture.md)
::::
download.page(api/controllers.md)
download.page(api/middleware.md)
::::
download.page(api/rest.md)
::::
download.page(api/graphql.md)
::::   
download.page(api/serializing/_serializing.md)
::::
download.page(api/grpc.md)
::::
download.page(api/performances.md)
::::
download.page(api/cors.md)
::::   
download.page(api/engines/_engines.md)
::::
download.page(api/open_api/_open_api.md)
::::
download.page(api/health_check.md)
::::
download.page(api/testing/_testing.md)
::::
download.page(api/webhooks.md)
::::
download.page(api/payment/_payment_api.md)
::::
download.page(api/communication_ways.md)
::::
download.page(api/security.md)


- [Low level ASP.NET Core example web server](https://github.com/benaadams/Ben.Http)
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5


## More

URL shortening service like bit.ly or goo.gl
- https://github.com/abhinavdhasmana/tinyUrl
- https://medium.com/@adhasmana/system-design-create-a-url-shortening-service-part-1-overview-26aae5597914
- https://github.com/abhinavdhasmana/ratelimiter
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://auth0.com/blog/how-to-build-and-secure-web-apis-with-aspnet-core-3/
- https://www.tutorialsteacher.com/webapi/consuming-web-api-in-dotnet-using-httpclient
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://devblogs.microsoft.com/aspnet/creating-discoverable-http-apis-with-asp-net-core-5-web-api/
- https://snipcart.com/blog/integrating-apis-introduction
- [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)