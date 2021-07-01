## OAuth

OAuth is intended for delegated authorization.
HTTP-based protocols for authorization

http://auth0.com/
https://oauth.net/
https://oauth.net/2
industry-standard protocol for authorization.

https://medium.com/pragmatic-programmers/understanding-security-basics-1c2b1d5371d8

OAuth is a set of standards focused on authorization. OpenID is a set of standards focused on authentication. OpenID Connect is the identity layer built on top of the OAuth access control specification
 
OAuth (authentication and authorization) is a common API security solution because it offers quite a number of authentication workflows (called grant types) to fit various levels of security and interaction needs. An important feature of OAuth is that it supports what’s called three-legged authentication. This means the actual authentication event happens at the provider service, which provides an authentication token that’s then used by the client (application or API) to present to the actual service.


![](assets/books/security/assets/token_01.png)

1. The client application makes a request to an OAuth provider service to get a valid token. This is where the username and password are supplied by the client application. For machine-to-machine APIs, we’ll supply the client ID and the client secret (more on this later).
2. The OAuth provider validates the login identity and returns a special encoded token. This token is what the client application will use when making requests to the API service.
3. The client application sends a request to the API service (for example, GET http://api.example.org/company/132435). The client application includes the token it got from the OAuth provider in the Authorization HTTP header.
4. The API service accepts the request and the token from the client application and sends the token to the OAuth provider to ask if that token is valid.
5. The OAuth provider validates the token and returns it to the API service.
6. The API service, having determined this is a valid token for this request, returns the requested resource response that the client application asked for in Step 3.

