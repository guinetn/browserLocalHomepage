# ASP NET CORE

Can be hosted in
- InProcess
    One web server
    Application hosted in the IIS worker process
    Requests to the application are handled by Asp.net core module
    Asp.net core module forwards requests to 
        IIS HTTP Server: server runnning in-process with IIS
        This results in great perf (bypasses built-in Kesterl web server of asp.net core)
- OutOfProcess
    Two web servers
    Internal: kestrel 
        cross-platform web server included by default in asp.net core project  process used to host the app is dotnet.exe
    External: IIS, Apache, NGinx

System.Diagnostics.Process.GetCurrentProcess().ProcessName
    w3wp/iisexpress (InProcess)
    dotnet/project_name (OutOfProcess)

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

## ASP.NET Core data-protection system 
It encrypts and decrypts sensitive data such as the authentication cookie.
Symmetric-key encryption to protect data. A key containing random data is used to encrypt the data, and the same key is used to decrypt the data.
It assumes that it will be the same app or application decrypting the data as encrypted it. That implies it has access to the same key, and knows the parameters used to encrypt the data.
The data-protection keys are designed to expire and be rotated
https://andrewlock.net/an-introduction-to-the-data-protection-system-in-asp-net-core/

## Startup
ASP.NET Core application must include Startup class. It is like Global.asax
https://www.tutorialsteacher.com/core/aspnet-core-startup
- https://www.tutorialsteacher.com/core/aspnet-core-program

public class Program
{
    public static void Main(string[] args)
    {
        BuildWebHost(args).Run();
    }

    public static IWebHost BuildWebHost(string[] args)
    {
        WebHost.CreateDefaultBuilder(args)
            .UseStartup<Startup>()
            .Build();
    }
}

## Servers

- [Low level ASP.NET Core example web server](https://github.com/benaadams/Ben.Http)
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5

download.page(web/back/servers/kestrel.md)
## Tutorial

https://www.youtube.com/watch?v=BfEjDD8mWYg
https://www.youtube.com/watch?v=C5cnZ-gZy2I&t=217s

## More

- [Good intro](https://www.youtube.com/watch?v=BfEjDD8mWYg)

- https://www.ezzylearning.net/tutorial/how-to-consume-third-party-web-apis-in-asp-net-core
- https://www.ezzylearning.net/tutorial/introduction-to-asp-net-core-middleware
- https://www.ezzylearning.net/tutorial/a-step-by-step-guide-to-asp-net-core-dependency-injection
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://developer.okta.com/blog/2019/03/21/build-secure-microservices-with-aspnet-core
- https://developer.okta.com/blog/2019/03/11/build-a-crud-app-with-aspnet-mvc-and-entity-framework
- [InProcess hosting model in asp.net core](https://www.youtube.com/watch?v=LxnjX-ZjQ64)
- https://blog.elmah.io/how-to-send-push-notifications-to-a-browser-in-asp-net-core
- https://blog.elmah.io/how-to-secure-asp-net-core-with-oauth-and-json-web-tokens
- https://blog.elmah.io/cookie-authentication-with-social-providers-in-asp-net-core
- https://blog.elmah.io/export-data-to-excel-with-asp-net-core
- https://blog.elmah.io/the-asp-net-core-security-headers-guide
- https://blog.elmah.io/oauth-authentication-with-facebook-and-aspnet-core
- https://github.com/benaadams/practical-aspnetcore
- https://makolyte.com/aspdotnet-how-to-use-a-backgroundservice-for-long-running-and-periodic-tasks/
- https://www.ezzylearning.net/tutorial/13-reasons-to-learn-asp-net-core-in-2021-infographic
- https://www.tutorialsteacher.com/core/aspnet-core-startup
- https://www.tutorialsteacher.com/core/aspnet-core-program
- https://andrewlock.net/avoiding-startup-service-injection-in-asp-net-core-3/
- https://intellitect.com/quickly-configure-asp-net-core-api-to-work-with-vue-cli-3/
- https://www.ezzylearning.net/tutorial/a-developers-guide-for-creating-web-apis-with-asp-net-core-5
- https://medium.com/swlh/consuming-wsdl-services-using-asp-net-core-141fbc77924f

