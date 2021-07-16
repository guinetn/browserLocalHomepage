# API CREATION

https://auth0.com/docs/quickstart/spa/vanillajs
npm init -y
npm install express
npm install -D nodemon   server can be restarted on any code changes
package.json
{
  // ...
  "scripts": {
    "start": "node server.js",        'npm start' run the application as normal
    "dev": "nodemon server.js"        'npm run dev' run the application using nodemon, watching for changes as we modify files
  },
  // ...
}

Express generator
>npm install -g express-generator
>express myExpressApp --view pug --git

>npx express-generator --view=pug --git <app-name>
>npm install

create a new project using the official Svelte starter template:
>npx degit sveltejs/template svelte-crypto-tracker
- npx comes built-in with NodeJS
- degit is a project scaffolding tool
- sveltejs/template is the official template
- svelte-crypto-tracker is the name of our project (feel free to rename it)
>cd svelte-crypto-tracker
>npm install
>npm run dev
Open up localhost:5000 in your browser

pip list | findstr Django      !! findstr is case sensitive
pip install django           
django-admin startproject helloworld
cd helloworld
code .
  > python manage.py runserver            → http://127.0.0.1:8000/  
  > python manage.py runserver 8080

asp.net
https://docs.microsoft.com/fr-fr/learn/modules/build-web-api-aspnet-core/3-exercise-create-web-api
https://www.red-gate.com/simple-talk/dotnet/c-programming/build-a-rest-api-in-net-core/


dotnet new webapi --no-https
dotnet new webapi -o api01 --no-https     → http://localhost:5000
dotnet new webapi -o api01                → https://localhost:5001  
dotnet add package Microsoft.EntityFrameworkCore.InMemory

dotnet new sln
dotnet new webapi --no-https
dotnet sln add .

  Controllers/	Contient des classes avec des méthodes publiques exposées en tant que points de terminaison HTTP.
  Program.cs	Contient une méthode Main, qui est le point d’entrée managé de l’application.
  Startup.cs	Configure des services et le pipeline des requêtes HTTP de l’application.
  ContosoPizza.csproj	Contient des métadonnées de configuration pour le projet.
dotnet build
dotnet run
http://localhost:5000/weatherforecast

  * REPL (Read-Eval-Print-Loop) HTTP .NET
  >dotnet tool install -g Microsoft.dotnet-httprepl
  >httprepl http://localhost:5000                         connect http://localhost:5000
  >ls                                                     Explorez les points de terminaison disponibles
  >cd WeatherForecast
  >get
  >exit   CTRL+C

NextJS: https://nextjs.org/learn/basics/create-nextjs-app/setup
>npx create-next-app <app-name>
>npx create-next-app nextjs-blog --use-npm --example "https://github.com/vercel/next-learn-starter/tree/master/learn-starter"

serverless
https://app.serverless.com/guinetn/apps/new

npx create-react-app my-app
yarn create react-app my-app
https://github.com/facebook/create-react-app


Blazor
  dotnet new blazorserver -o Auth0BlazorServer
  cd Auth0BlazorServer
  dotnet run

  https://andrewlock.net/adding-authentication-to-a-blazor-server-app-using-auth0
  dotnet add package Microsoft.AspNetCore.Authentication.OpenIdConnect