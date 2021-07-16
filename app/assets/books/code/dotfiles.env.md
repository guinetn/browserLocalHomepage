# Dotenv - .env files

## APPLICATION SECRETS
Keep secret Keys and Tokens off of source code/version control
Leaked package registry credentials pose a significant security risk.

- TOKENS
- KEYS 
  * SECRET KEYS 
  Used for a database or API connection.
  KEPT HIDDEN, should never leave your private server (or service, like Netlify or Travis CI). 
  * PUBLIC KEYS 
    Shared freely, included in browser requests
    Used for analytics services, crash report analytics...

## APPLICATION SECRETS MANAGEMENT

Eliminate leaking secrets from your code
Storing configuration in the environment separate from code is based on The Twelve-Factor App methodology.

Handling application secrets safely steps:
❌ use hard-coded keys in your code
❌ use appsettings.json to store keys
✔️ development: use environment variables / secret manager app (Secret Manager ASP.NET Core)
✔️ production: use a vault, more secure 

Environment variable 
- its value is set outside the program, ex process.env.SECRET_API_KEY
- managed by 
  * operating system built in functionality 
  * service    

Dotfiles: storing configuration 
- stored app settings as plain text: `.gitconfig`
- hidden by the system: ls -a, ls -a | grep "^\."

## .env
The .env file is for storing secrets for your app outside source code/version control
- contains secrets settings
- must not be pushed to a repository
- often one file per environment 
    Add the .env into your .gitignore file
    
.env
```conf
DB_USER=root 		      → process.env.DB_USER + .gitignore 
DB_HOST=localhost
A=3
NAME=VALUE
```

⚠️ DO NOT REFERENCE SENSITIVE DATA IN YOUR PROJECT. To not be at risk add to your project a `.gitignore` file with 
  * `*.env`     
  * `*.ssh`  Don't push your .ssh folder to github
  * ...      Don't push your files containing API tokens


  
## APPLICATION SECRETS MANAGERS

- Dotnet Secret manager tool (Microsoft)
Stores sensitive data in secrets.json readed by the default ASP.NET Core configuration builder 
ASP.NET CORE reads configuration settings from a variety of sources. The configuration values are read in a particular hierarchy/order, such that if the same configuration setting is read again it replaces the setting found earlier. By default, the order is as such:

- appsettings.json
- appsettings.{environment}.json
- secrets.json
- environment variables
- command line arguments
Therefore, an environment variable will overwrite a setting in secrets.json that overwrites a setting in appsettings.json

dotnet user-secrets init
dotnet user-secrets set "Auth0:Domain" "some-domain.eu.auth0.com"
dotnet user-secrets set "Auth0:ClientId" "ABC123someClientId"
dotnet user-secrets set "Auth0:ClientSecret" "some_random_string_of_letters"

* Enabled secret for your ASP.NET Core project
>dotnet user-secrets init    
- project file change: <UserSecretsId>5e6f813f-e0e5-435d-a201-8031565450a3</UserSecretsId>
- adds a directory with the same name as your UserSecretsId. It contains secrets.json, used to store your secrets.

* Set and list secrets
>dotnet user-secrets list
>dotnet user-secrets set "WebApiOptions:ApiKey" "12345"   → {  "WebApiOptions:ApiKey": "12345" }
  WebApiOptions: section's name
  ApiKey: variable's name



Bind it to the app with the Options Pattern
```c#
public class WebApiOptions
{
    public string ApiKey { get; set; }
}

public void ConfigureServices(IServiceCollection services)
{
    services.AddOptions()
        .Bind(Configuration.GetSection(nameof(WebApiOptions)))
        .ValidateDataAnnotations();
    }
}

and use it

public class IndexModel : PageModel
{
    private readonly WebApiOptions _webApiOptions;

    public IndexModel(IOptions<WebApiOptions> webApiOptionsAccessor)
    {
        _webApiOptions = webApiOptionsAccessor.Value;
    }

    public void OnGet()
    {
        var apiKey = _webApiOptions.ApiKey;
    }
}
```

- Node dotenv: .env → process.env.xxxx
[dotenv](https://github.com/motdotla/dotenv#dotenv)
  - zero-dependency module 
  - loads environment variables from a .env file into process.env

>npm install dotenv
>yarn add dotenv

Have a .env file in the root directory. Add environment-specific variables on new lines in the form of NAME=VALUE:
```conf
DB_HOST=localhost
DB_USER=root
DB_PASS=s1mpl3
```
`process.env` now has the keys and values you defined in your .env file

```js
require('dotenv').config()
const db = require('db')
db.connect({
  host: process.env.DB_HOST,
  username: process.env.DB_USER,
  password: process.env.DB_PASS
})		
```

* ENVIRONMENTS

  With the --production flag (or when the NODE_ENV environment variable is set to production), npm will not install modules listed in devDependencies.

    ...if (process.env.NODE_ENV === 'development') {
        console.warn('This warning will dissapear on production build!');
      }

    var ENV = process.env.NODE_ENV;

    "scripts": {
      "start": "NODE_ENV=development webpack-dev-server",
      "build": "NODE_ENV=production webpack"
    }

    // secrets implementation
  if (process.env.NODE_ENV !== 'production') require('./secrets')


- Flutter dotenv

https://pub.dev/packages/flutter_dotenv


- Python dotenv

download.page(assets\books\code\langs\python\code\variables_env_vars.py)

- Azure App Services
each app service has application settings, see them is in the Azure Portal.  
add the production API Key as an application setting and it will be read in by the configuration builder and override the dummy value in appsettings.json just like we did with secrets using the secret manager tool.

- Azure Key Vault service
Store application secrets in production mode  

https://docs.microsoft.com/fr-fr/azure/key-vault/general/overview  

More secure way of storing secrets for your applications. It takes slightly more work to use Key Vault with ASP.NET Core as you will need to add it as a configuration source. However, once you configure your ASP.NET Core web application to use Key Vault, it transparently reads sensitive configuration data into your web application from Key Vault as it reads configuration data from secrets, environment variables, etc.

- Kubernetes Secrets

- Docker Vault: For containerized environments 

- Secret Manager (AWS)
https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html    

- Secret Manager (Google)
is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. Secret Manager provides a central place and single source of truth to manage, access, and audit secrets across Google Cloud.

- https://www.softfluent.fr/blog/comment-stocker-des-secrets-en-developpement/
- https://betterprogramming.pub/how-to-hide-your-api-keys-c2b952bc07e6
- https://www.freecodecamp.org/news/technical-dive-into-owasp/
- https://github.blog/2021-06-08-securing-open-source-supply-chain-scanning-package-registry-credentials/




https://12factor.net/	
	software is commonly delivered as a service: called web apps, or software-as-a-service. The twelve-factor app is a methodology for building software-as-a-service apps that:
	Use declarative formats for setup automation, to minimize time and cost for new developers joining the project;
	Have a clean contract with the underlying operating system, offering maximum portability between execution environments;
	Are suitable for deployment on modern cloud platforms, obviating the need for servers and systems administration;
	Minimize divergence between development and production, enabling continuous deployment for maximum agility;
	And can scale up without significant changes to tooling, architecture, or development practices.