# Express

Incoming requests are intercepted by middlewares that processes the request and passes it onto the next middleware in chain or reject it (Chain of Responsability).

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

## Express's Forks

http://expressjs.com/en/resources/frameworks.html

<ul>
<li><strong><a href="http://feathersjs.com">Feathers</a></strong>: Build prototypes in minutes and production ready real-time apps in days.</li>
<li><strong><a href="https://www.itemsapi.com/">ItemsAPI</a></strong>: Search backend for web and mobile applications built on Express and Elasticsearch.</li>
<li><strong><a href="http://keystonejs.com/">KeystoneJS</a></strong>: Website and API Application Framework / CMS with an auto-generated React.js Admin UI.</li>
<li><strong><a href="http://jsantell.github.io/poet">Poet</a></strong>: Lightweight Markdown Blog Engine with instant pagination, tag and category views.</li>
<li><strong><a href="http://krakenjs.com/">Kraken</a></strong>: Secure and scalable layer that extends Express by providing structure and convention.</li>
<li><strong><a href="http://loopback.io">LoopBack</a></strong>: Highly-extensible, open-source Node.js framework for quickly creating dynamic end-to-end REST APIs.</li>
<li><strong><a href="http://sailsjs.org/">Sails</a></strong>: MVC framework for Node.js for building practical, production-ready apps.</li>
<li><strong><a href="https://github.com/flywheelsports/fwsp-hydra-express">Hydra-Express</a></strong>: Hydra-Express is a light-weight library which facilitates building Node.js Microservices using ExpressJS.</li>
<li><strong><a href="http://github.com/onehilltech/blueprint">Blueprint</a></strong>: a SOLID framework for building APIs and backend services</li>
<li><strong><a href="http://locomotivejs.org/">Locomotive</a></strong>: Powerful MVC web framework for Node.js from the maker of Passport.js</li>
<li><strong><a href="https://github.com/graphcool/graphql-yoga">graphql-yoga</a></strong>: Fully-featured, yet simple and lightweight GraphQL server</li>
<li><strong><a href="https://express-gateway.io">Express Gateway</a></strong>: Fully-featured and extensible API Gateway using Express as foundation</li>
<li><strong><a href="https://github.com/ParallelTask/dinoloop">Dinoloop</a></strong>: Rest API Application Framework powered by typescript with dependency injection</li>
<li><strong><a href="https://kites.nodejs.vn/">Kites</a></strong>: Template-based Web Application Framework</li>
<li><strong><a href="https://foalts.org/">FoalTS</a></strong>: Elegant and all-inclusive Node.Js web framework based on TypeScript.</li>
<li><strong><a href="https://github.com/nestjs/nest">NestJs</a></strong>: A progressive Node.js framework for building efficient, scalable, and enterprise-grade server-side applications on top of TypeScript &amp; JavaScript (ES6, ES7, ES8)</li>
<li><strong><a href="https://github.com/Zero-OneiT/expresive-tea">Expressive Tea</a></strong>: A Small framework for building modulable, clean, fast and descriptive server-side applications with Typescript and Express out of the box.</li>
</ul>