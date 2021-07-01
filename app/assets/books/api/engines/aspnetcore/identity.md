## Identity

Configure Passwordless Authentication in ASP.NET Core Web App
- https://developer.okta.com/blog/2020/12/18/how-to-use-webauthn-csharp-dotnet
- https://docs.microsoft.com/en-us/aspnet/identity/
- https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity
- https://www.youtube.com/watch?v=Fhfvbl_KbWo&list=PLOeFnOV9YBa7dnrjpOG6lMpcyd7Wn7E8V&index=1
- https://andrewlock.net/an-introduction-to-the-data-protection-system-in-asp-net-core/
- https://andrewlock.net/introduction-to-authentication-with-asp-net-core/

***ASP.NET 4.x*** → HttpContext.User:IPrincipal represents request's current user
Authorisation was Role-based (a user may belong to one or more roles) and different sections of your app may require a user to have a particular role in order to access it
IsInRole()

***ASP.NET Core*** →  HttpContext.User:ClaimsPrincipal which implements IPrincipal
Shift to claims-based authentication (role-based authorisation can be used for backward compatibility)

### Claims-based authentication

claims = 'statement about/property of' a particular identity. A name and a value
DateOfBirth claim, FirstName claim, EmailAddress claim, IsVIP... the "Who", NOT the "IT CAN"

Identities in ASP.NET Core are a ClaimsIdentity
```cs
public class ClaimsIdentity: IIdentity
{
    // Method used to authenticate the user and to determine the claims associated with an identity
    public string AuthenticationType { get; }  // string: Cookies, Bearer, Google...Passport or DriversLicense
     
    public bool IsAuthenticated { get; }       // indicates whether an identity is authenticated or not
    public IEnumerable<Claim> Claims { get; }  // all the claims associated with an identity

    public Claim FindFirst(string type) { /*...*/ }
    public Claim HasClaim(string type, string value) { /*...*/ }
}
```

HttpContext.User is a ClaimsPrincipal (not a ClaimsIdentity)
Principal can have multiple identities, these identities can have multiple claims, and the ClaimsPrincipal inherits all the claims of its Identities.
you are the principal, and you have two forms of identity: passport, driver license. The principal inherit all the claims from all your identities
```cs
public class ClaimsPrincipal :IPrincipal
{
    public IIdentity Identity { get; }                      //  IPrincipal implement, Identities[0]
    public IEnumerable<ClaimsIdentity> Identities { get; }  // a single ClaimsPrincipal can consist of multiple Identities
    public IEnumerable<Claim> Claims { get; }

    public bool IsInRole(string role) { /*...*/ }
    public Claim FindFirst(string type) { /*...*/ }
    public Claim HasClaim(string type, string value) { /*...*/ }
}
```

Creating a new principal
```cs
public async Task<IActionResult> Login(string returnUrl = null)
{
    const string Issuer = "https://gov.uk";

    // 1. Create claims
    // obtain the claim values from a database or some other source
    // http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name
    var claims = new List<Claim> {
        new Claim(ClaimTypes.Name, "Joe", ClaimValueTypes.String, Issuer),
        new Claim(ClaimTypes.Surname, "Black", ClaimValueTypes.String, Issuer),
        new Claim(ClaimTypes.Country, "UK", ClaimValueTypes.String, Issuer),
        new Claim("PreferedCurrency", "Dollar", ClaimValueTypes.String)
    };

    // 2. Create a new ClaimsIdentity passing in your claim list, and specifying the AuthenticationType
    var userIdentity = new ClaimsIdentity(claims, "Passport");  // Now IsAuthenticated=true

    // 3. Create a new ClaimsPrincipal using your identity
    var userPrincipal = new ClaimsPrincipal(userIdentity);

    // 4. Sign the user in, telling the AuthenticationManager to use the "Cookie" authentication handler
    await HttpContext.Authentication.SignInAsync("Cookie", userPrincipal,    
        new AuthenticationProperties
        {
            ExpiresUtc = DateTime.UtcNow.AddMinutes(20),
            IsPersistent = false,
            AllowRefresh = false
        });

    return RedirectToLocal(returnUrl);
}
```