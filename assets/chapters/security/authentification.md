# authentification

https://medium.com/@adhasmana/auth-token-management-with-node-js-observer-pattern-e51a63d945b2

https://www.c-sharpcorner.com/article/basic-authentication-in-swagger-open-api-net-5/

## TYPE OF AUTHENTICATION
- Custom credential database
- ASP.NET Identity
- Identity Server
- Commercial Identity Provider (e.g. Azure AD, Auth0, Ping Identity, Okta etc.)
- Social Providers (Facebook, Google ID, Apple ID etc.)
- Windows or Kerberos authentication
- Azure AD B2C
- Azure Easy Auth
- Any other authentication system

## OpenID 
https://openid.net/

Federated authentication: A client accepts an identity assertion from any provider (although clients are free to whitelist or blacklist providers). 
HTTP-based protocols for authentication and/or authorization
Allows to sign with an existing account into multiple websites without creating new passwords.
Choose to associate information (name, email...) with your OpenID that can be shared with the websites you visit
Your password is only given to your identity provider, and that provider then confirms your identity to the websites you visit.

OpenID Connect

## OAuth

OAuth is intended for delegated authorization.
HTTP-based protocols for authorization

https://oauth.net/2
industry-standard protocol for authorization.

## WebAuthn - Web Authentication 

W3C official API specification web standard for passwordless login since March 2019
Supported by all major desktop and mobile browsers.

* Relying Party (web server)
web application
use web authentication API to register and authenticate users.
↑
↓
A web browser’s role 
* Exchange data between authenticators and relying parties
* Provide a user interface for authenticators if needed
* Manage error handling

↑
↓
* Authenticators
Devices generating a cryptographic key-pair and register it with the relying party. An authenticator can be a device with TouchID, FaceID, Windows Hello, or a USB or Bluetooth security key.


When the authenticator generates a new private-public key pair for a website, the browser sends the public key and a random credential ID to the server, but the private key is stored securely on the user’s device. This makes passwordless authentication much more secure as there is no need to store or remember passwords anymore, and the public key is not secret and cannot be used without the corresponding private key.


## Okta
https://developer.okta.com/
https://developer.okta.com/blog/2020/12/18/how-to-use-webauthn-csharp-dotnet