# API

/api/v1
X-MyGreatApi-Token : apiKey
Rate Limits: 30... API calls/second. Else Status Code 429


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

- https://hoppscotch.io/
- https://pokeapi.co/
- https://api.nasa.gov/
- https://spaceflightnewsapi.net/

Fake api
- https://jsonplaceholder.typicode.com/
```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))
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
download.page(api/rest.md)
  
download.page(api/soap.md)
::::   
download.page(api/graphql.md)
::::   
download.page(api/json.md)
::::
download.page(api/jsonp.md)
::::
download.page(api/grpc.md)
::::
download.page(api/performances.md)
::::
download.page(api/cors.md)
::::   
download.page(api/engines/_engines.md)
::::
download.page(api/open_api.md)
::::
download.page(api/health_check.md)
::::
download.page(api/testing/_testing.md)
::::
download.page(api/webhooks.md)
::::
## More

URL shortening service like bit.ly or goo.gl
- https://github.com/abhinavdhasmana/tinyUrl
- https://medium.com/@adhasmana/system-design-create-a-url-shortening-service-part-1-overview-26aae5597914
- https://github.com/abhinavdhasmana/ratelimiter
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://auth0.com/blog/how-to-build-and-secure-web-apis-with-aspnet-core-3/
- https://www.tutorialsteacher.com/webapi/consuming-web-api-in-dotnet-using-httpclient
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5