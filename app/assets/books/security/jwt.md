# JWT - JSON Web Token

For authentication, sharing information by claims (entity details)
Traditional authentication strategy (sessions, cookies) maintained some kind of state on the server → can't scale easily
JWT: 
- a JSON object
- stateless authentication solution, easy to scale a stateless app


![jwt.io](https://jwt.io): tools to create, decode check jwt tokens. 
Brought by Auth0: a cloud service, APIs, tools that eliminate the friction of identity for your applications

[JSON Web Token specification](https://tools.ietf.org/html/rfc7519)

[OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)

![](assets/books/security/assets/jwt01.png)

- https://auth0.com/docs/quickstart/spa/vanillajs/01-login
- https://www.loginradius.com/blog/async/invalidating-jwt/
## JWT structure: header.payload.signature

 	token = encodeBase64(header) + '.' + encodeBase64(payload) + '.' + encodeBase64(signature) 
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJb….gzSraSYS8EXBxL…"
    dot separated                                ↑     ↑   

                   ┌──── alg   Algorithm used to sign the JWT
                   |	
                   |	• none 		for no signature at all, supported by all algorithms
                   |				if 'alg' is changed to 'none', some implementations can accept the jwt as "correctly signed"
                   |	• HS256 	(default algorithm). Use symmetric encryption: algorithm (uses a secret key to sign and verify each message)
                   |				Tools for cracking jwt
                   |				HMAC uses the same key for signing and verifying
                   |	• RS256 	Use Asymmetric encryption: private key to sign messages, public key to verify them
                   |				if 'alg' is changed from RS256 to HS256, an attaker can correctly sign such messages with public key
                   |                
                   |                  
                   |         
                {  |                 
                 "alg": "HS256",     
                 "typ": "JWT"       ────── typ   Type of token. 'JWT'  
                }
	   ┌ JSON object encoded in base64 
	   |
       |
	HEADER.PAYLOAD.SIGNATURE
			|  		|
			|  		|___ (JWS) check integrity (server generated)
	        |            signature = HEADER + PAYLOAD (BASE64) + HASH(SECRET_KEY)
            |                      = sha256(base64URL(head) + "." + base64URL(body))
	        |                  cryptographic signature, for example a HMAC over the data  
	        |    						key = 'secretkey'
			|	 						unsignedToken = encodeBase64(header) + '.' + encodeBase64(payload)
			|	  						signature = HMAC-SHA256(key, unsignedToken)
			|	   
			└──	Contains the claims, information you want to pass into it, the data that’s transferred
				 	a JSON object, base64 encoded
					a set of attributes about a user, mapped to the underlying user store. 
					must not be a sensible data (unless hard encrypted)
					
                    {
                        "sub": "90129920",
                        "uuid": "sfgdsrfg434fdt535fg",
                        "iat": 1516239022,
                        "exp": 1545926973,
                    }

					In this context, "claim" can be something like 
						a 'command'
						a one-time authorization
						any other scenario that you can word as: Hello Server B, Server A told me that I could <claim goes here>, and here's the (cryptographic) proof

					ex: user email
						user id

                        The body may contain special attributes (standard accepted by OAuth services)
						- exp
						-iat (issued at)

						{useremail: test2@nect.com}
						{userid: 2}
						{userid: 2, admin: true}...
						{
						  "sub": "1234567890",
						  "name": "John Doe",
						  "admin": true,
						  "iat": 1516239022
						}
						{"loggedInAs":"admin", "iat":1422779638}
												 ↓
											timestamp (JWT spec) called iat (issued at)
						- `iat` (issued at) claim included by default unless `noTimestamp` is specified. 
						If `iat` is inserted in the payload, it will be used instead of the real timestamp for calculating other things like `exp` 

			            - `expiresIn`, `notBefore`, `audience`, `subject`, `issuer`. 
                        These claims can also be provided in the payload directly with `exp`, `nbf`, `aud`, `sub` and `iss` 




## JWT authentication mechanism

The token with user_id is given to the client
The client 
- sends the token back to the server 
    - every time the client makes an HTTP request to the server
    - in the authorization header as Bearer {token}
- store the token in the browser 
    - local storage: keep the user signed in until the token expires
    - session storage: keep the user logged in until the browser tab is closed

### with Vue.js
https://www.loginradius.com/blog/async/implementing-authentication-on-vuejs-using-jwt/
### with Node.js
npm i express jsonwebtoken mongoose body-parser bcrypt
root
   -app.js
   -user.js
   -key.js     private key. Better: in .env

### with Angular

https://ankitsharmablogs.com/policy-based-authorization-in-angular-using-jwt/     create an HTTP interceptor service to send the authorization token in the header of each API request

### with asp.net core

https://codeburst.io/jwt-auth-in-asp-net-core-148fb72bed03
### with .net

- https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/
- https://github.com/davidfowl/Todos/blob/davidfowl/todo-blazor/TodoBasicWithAuth/AuthApi.cs ***
- https://codyanhorn.tech/blog/blazor/2020/09/06/Blazor-Server-Get-Access-Token-for-User.html  + OpenId
- https://codyanhorn.tech/blog/blazor/2020/09/05/Blazor-Get-Access-Token-for-User.html

	using System.Threading.Tasks;
	using Microsoft.AspNetCore.Authorization;
	using Microsoft.AspNetCore.Components;
	using Microsoft.AspNetCore.Components.WebAssembly.Authentication;

	[Authorize]
	public partial class Index : ComponentBase
	{
	    [Inject]
	    IAccessTokenProvider TokenProvider { get; set; }

	    public string AccessToken { get; set; }

	    protected override async Task OnInitializedAsync()
	    {
	        var accessTokenResult = await TokenProvider.RequestAccessToken();
	        AccessToken = string.Empty;

	        if (accessTokenResult.TryGetToken(out var token))
	        {
	            AccessToken = token.Value;
	        }
	    }
    }


## More
- https://blog.bitsrc.io/understanding-json-web-token-authentication-a1febf0e15
- https://dev.to/deleteman123/jwt-authentication-best-practices-3lf9
- https://dev.to/nilanth/how-to-secure-jwt-in-a-single-page-application-cko
- https://dev.to/deleteman123/jwt-authentication-best-practices-3lf9
- http://www.primaryobjects.com/2015/05/08/token-based-authentication-for-web-service-apis-in-c-mvc-net/  
- http://website.simplx.fr/blog/2016/09/27/authentification-api-via-jwt-et-cookies/
- https://auth0.com/learn/
- https://auth0.com/docs/quickstart/webapp
- https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp
- https://github.com/auth0-blog/nodejs-jwt-authentication-sample
- https://speakerdeck.com/genehack/json-web-tokens-will-improve-your-life-2
- http://cryto.net/~joepie91/blog/2016/06/19/stop-using-jwt-for-sessions-part-2-why-your-solution-doesnt-work/
- https://blog.codecentric.de/en/2017/08/use-json-web-tokens-services/
- https://medium.com/vandium-software/5-easy-steps-to-understanding-json-web-tokens-jwt-1164c0adfcec
- https://dzone.com/articles/jwtjson-web-tokens-are-better-than-session-cookies
- http://cryto.net/~joepie91/blog/2016/06/13/stop-using-jwt-for-sessions/
- https://www.oreilly.com/ideas/session-management-with-microservices
- https://medium.com/studioarmix/learn-restful-api-design-ideals-c5ec915a430f
- [Force Expiring of JWTs with Refresh Tokens](https://medium.com/studioarmix/expiring-jwts-with-refresh-tokens-cf54057fe727)
- https://scotch.io/tutorials/the-anatomy-of-a-json-web-token
- https://scotch.io/tutorials/the-ins-and-outs-of-token-based-authentication   **