# Express

Express generator
>npx express-generator --view=pug --git <app-name>
>npm install

START THE APP
ran npm start with an environment variable called DEBUG with a value of app-name:*, which instructs the server to do verbose debug.
Linux:   DEBUG=nodejs-express:* npm start
Windows: set DEBUG=nodejs-express:* & npm start

Open http://localhost:3000 

Stop the server: Ctrl+C

Dockerize the app: https://blog.logrocket.com/node-js-docker-improve-dx/
 
- https://expressjs.com/en/starter/generator.html
- https://blog.logrocket.com/documenting-your-express-api-with-swagger/