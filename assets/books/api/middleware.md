# Middleware

When we have to process on each request (log...)

Middleware is a function which is called before the route handler. Middleware functions have access to the request and response objects, and the next() middleware function in the application’s request-response cycle

Middleware functions can perform the following tasks:
- execute any code.
- make changes to the request and the response objects.
- end the request-response cycle.
- call the next middleware function in the stack.
- if the current middleware function does not end the request-response cycle, it must call next() to pass control to the next middleware function. Otherwise, the request will be left hanging.

**Middleware skeleton**

```c#
using Microsoft.AspNetCore.Http;
using System;
using System.Threading.Tasks;
namespace YourNamespace.CustomMiddleware
{
    public class CustomMiddleware
    {
        private readonly RequestDelegate _next;
        public CustomMiddleware(RequestDelegate next)
        {
            _next = next;
        }
        public async Task Invoke(HttpContext httpContext)
        {
            // code sur le chemin ALLER
            await _next(httpContext);
            // code sur le chemin RETOUR
        }
    }
}
```

## more 
- https://expressjs.com/en/guide/using-middleware.html
- https://docs.microsoft.com/fr-fr/aspnet/core/fundamentals/middleware/?view=aspnetcore-5.0
- https://www.ctrl-alt-suppr.dev/2021/06/14/les-middlewares/