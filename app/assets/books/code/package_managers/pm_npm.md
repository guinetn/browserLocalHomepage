# NPM - NODE PACKAGE MANAGER


	windows  		npm list | find "<package name>"
	Linux 			npm list | grep <package name> 
	PowerShell 		npm list | sls <package name>
	                ($env:path.split(';')) | where {$_ -like '*flut*'}


    * access, adduser, audit
    * bin, bugs
    * c, cache, ci, cit, clean-install, clean-install-test, completion, config, create
    * ddp, dedupe, deprecate, dist-tag, docs, doctor
    * edit, explore
    * fund
    * get
    * help, help-search, hook
    * i, init, install, install-ci-test, install-test, it
    * link, list, ln, login, logout, ls
    * org, outdated, owner
    * pack, ping, prefix, profile, prune, publish
    * rb, rebuild, repo, restart, root, run, run-script
    * s, se, search, set, shrinkwrap, star, stars, start, stop
    * t, team, test, token, tst
    * un, uninstall, unpublish, unstar, up, update
    * v, version, view, whoami

	npm <command> -h  quick help on <command>
	npm -l            display full usage info
	npm help <term>   search for help on <term>
	npm help npm      involved overview

	
	C:\Users\nguin\node_modules             ← npm install -g <pname>
	C:\Users\nguin\AppData\Roaming\npm      ← cli's "exe" are here
		npm.exe
		npx.cmd
		browser-sync.cmd
		svelte.cmd
		...
	
	npm root -g 		tell you where that exact location is on your machine
	C:\Users\nguin\AppData\Roaming\npm\node_modules      ← cli's sources are here...and others '-g' modules
	
	C:\Users\nguin\AppData\Roaming\npm-cache
	C:\Users\nguin\AppData\Roaming\npm-cache\_npx


	A node module is a .js file that contains export functions
	Export functionality by assigning 'module.exports' or 'exports'
		module.exports = function (n) { return n * 111 }
		module.exports = [  {name: 'The Revolver', price: 15}, {name: 'The Heavy Duty', price: 65}]
		
	BACK-END PACKAGE MANAGER (bower is a client-side/front-end package manager)
	Make developing things easier by installing needed modules
	Extend node by downloading & installing modules
	Package manager for node.js: Thousands modules available on npm.org
	Language agnostic task-runner (scripts)

	Packages are installed to `./node_modules`
	Bins are installed to     `./node_modules/.bin`

	var http = require('http');         http moduke, to set up a web server. Include with node.js
    var test = require('./test');       use test.js (relative path to same folder)
    var test = require('../test');      use test.js (relative path to parent folder)
    var express = require('express');   Will use express.js, by convention it is in 'node_modules' folder

						   ___ look for 'http.js'
						  |
	var http = require('http');     Use http.js
									By convention it is in 'node_modules' folder
								   	Search a 'node_modules' folder in parent folders if missing...
	var test = require('./test');  // use test.js (relative path to same folder)

	dependencies		required to run
	devDependencies		Only to develop, e.g.: unit tests, Coffeescript to Javascript transpilation, minification, ...

# RESOURCES

	http://npm.org 				List of modules
	https://www.npmjs.org
	https://docs.npmjs.com 		Help
	https://docs.npmjs.com/files/package.json
	https://medium.freecodecamp.com/8-npm-tricks-you-can-use-to-impress-your-colleagues-dbdae1ef5f9e
	http://browsenpm.org/help#linkinganynpmpackagelocally
	https://www.npmjs.com/package/browserify : 'require()' in the browser. Make a bundle file of all require() detected.


# NPM frequent modules

	__filename  	file path of the currently executing file
	__dirname  		directory path of the currently executing file
	global  		top-level scope object (window)
	process
	Buffer

	npm install --save commander 	to parse inputs from the client
	npm install --save shortid  	small lib to create IDs
	npm install --save request 		lib to make it easier for us to make HTTP calls. 

	[assert](https://www.npmjs.com/package/assert)
	[buffer](https://www.npmjs.com/package/buffer)
	[console](https://www.npmjs.com/package/console-browserify)
	[constants](https://www.npmjs.com/package/constants-browserify)
	[crypto](https://www.npmjs.com/package/crypto-browserify)
	[domain](https://www.npmjs.com/package/domain-browser)
	[events](https://www.npmjs.com/package/events)
	[http](https://www.npmjs.com/package/stream-http)
	[https](https://www.npmjs.com/package/https-browserify)
	[os](https://www.npmjs.com/package/os-browserify)
	[path](https://www.npmjs.com/package/path-browserify)
	[punycode](https://www.npmjs.com/package/punycode)
	[querystring](https://www.npmjs.com/package/querystring-es3)
	[stream](https://www.npmjs.com/package/stream-browserify)
	[string_decoder](https://www.npmjs.com/package/string_decoder)
	[timers](https://www.npmjs.com/package/timers-browserify)
	[tty](https://www.npmjs.com/package/tty-browserify)
	[url](https://www.npmjs.com/package/url)
	[util](https://www.npmjs.com/package/util)
	[vm](https://www.npmjs.com/package/vm-browserify)
	[zlib](https://www.npmjs.com/package/browserify-zlib)
	https://yargs.js.org/docs/
		parse optstrings
		build interactive command line tools by parsing arguments and generating an elegant user interface
		https://github.com/theonlymikeever/obey-the-coin-cli/blob/master/cli.js

	https://auth0.com/blog/react-tutorial-building-and-securing-your-first-app/

	body-parser: 	you will use to convert the body of incoming requests into JSON objects.
	cors: 			you will use to configure Express to add headers stating that your API accepts requests coming from other origins. This is also known as Cross-Origin Resource Sharing (CORS).
	express: 		Express itself.
	helmet: 		helps to secure Express apps with various HTTP headers.
	morgan: 		adds some logging capabilities to your Express app.
	[dotenv](https://github.com/motdotla/dotenv#dotenv)   DB_USER=root → process.env.DB_USER + .gitignore 

		## NPM MODULES INSTALLED

		* 11ty
		* angular
		* apiconnect
		* azure-cli
		* babel-cli
		* bower
		* brunch
		* create-react-app
		* docute-cli
		* elm-upgrade
		* eslint
		* express
		* express-generator
		* firebase-functions
		* firebase-tools
		* flux
		* gatsby-cli
		* generator-angular-fullstack
		* generator-aspnet
		* generator-bootstrap
		* generator-dotnetcore
		* generator-espress
		* generator-express
		* generator-react-component
		* generator-vuejs
		* gh-pages
		* gulp
		* hexo-cli
		* ionic
		* jshint
		* less
		* nativescript
		* node
		* node-sass
		* nodemon
		* now
		* npm
		* npx
		* nvm
		* parcel-bundler
		* pug
		* pug-cli
		* puppeteer
		* react
		* react-fullstack
		* serve
		* server
		* styled-components
		* surge
		* to
		* tslint
		* typescript
		* typings
		* update
		* vue
		* vue-cli
		* vue-loader
		* vue-resource
		* vuetify
		* vuex
		* webpack
		* weex-toolkit
		* yarn
		* yo


# NPM SECURITY

	https://github.com/lirantal/is-website-vulnerable
	npx is-website-vulnerable https://example.com [--json] [--js-lib]
	Finds publicly known security vulnerabilities in a website's frontend JavaScript libraries


# NPM COMMANDS

	npm <command>

	where <command> is one of:
	    access, add-user, adduser, apihelp, author, bin, bug cache, completion, config, ddp, dedupe, deprecate, d dist-tags, docs, edit, explore, faq, find, find-dupe
	    help, help-search, home, i, info, init, install, iss link, list, ll, ln, login, logout, ls, outdated, own pack, ping, prefix, prune, publish, r, rb, rebuild,
	    repo, restart, rm, root, run-script, s, se, search, show, shrinkwrap, star, stars, start, stop, t, tag, test, tst, un, uninstall, unlink, unpublish, unstar,
	    update, upgrade, v, verison, version, view, whoami

## C:\Program Files\nodejs\node_modules\npm\

	.	Command             Shorthand           Action
    ---------------------------------------------------------------------------------------------------

	npm audit
 		Generates a report of vulnerabilities, simple-to-run npm commands and recommendations to resolve them, and links to web pages with more details.
 		To analyze your code and its dependencies against the Node Security Platform database of JavaScript vulnerabilities. 

    INSTALL
    	two ways to install npm packages: locally or globally (and dev mode or not)
    	npm can install modules locally in a project ( by default in node_modules ) or globally to be used by multiple projects.
		In large projects the way to specify dependencies is by creating a file called 'package.json' which contains a list of dependencies.
		That list is recognized by npm when you run 'npm install', which then downloads and installs them for you.

	npm install             	npm i               Install Node packages listed in package.json. npm detect module dependencies (listed in package.json) and install needed modules automatically
	npm install --production  						Install Node packages listed in package.json except devDepencies
	npm install <packagename>	npm i pkg 			LOCAL INSTALL 	Install a package in 'node_modules' local folder
	npm install <packagename> -dev 					Install also development packages
	npm i --global pkg 	 		npm i -g pkg 		GLOBAL INSTALL 	Install a package globally in C:\Users\<username>\AppData\Roaming\npm\node_modules\<modulename>   
													Ex: C:\Users\nguin_000\node_modules
													Will download 'modulename' and create 'node_modules' directory if it doesn´t exists: C:\Users\<username>\AppData\Roaming\npm\node_modules\
													Global install of the module: it will be usable by any node application on the system andnot only the app in the local directory
													For the global install with -g , OSX/Linux users may need to prefix the command with 'sudo'
	npm i --save pkg 	 		npm i -S pkg 		Install a package and save it as a dependency in package.json (create the 'package.json' file if not existing) → "dependencies": { "express": "^4.0.0", …    PROD DEPENDENCIES
	npm i --save-dev pkg 		npm i -D pk 		Install a package and save it as a devDependency (development package: tests,debug…)							 "devDependencies": { "mocha": "^1.18.2", …  DEV DEPENDENCIES    npm i <
						 							npm will not install modules listed in devDependencies.
	
	npm uninstall <your_library>

	Semver convention
	npm install eslint@1.0.0 						Install a specific version
	npm install eslint~4.17.1 						look for 4.17.1 but if a newer PATCH release exists say 4.17.9 then use it
	npm install eslint^4.17.1 						look for 4.17.1 but if a newer MINOR release exists say 4.18.1 then use it
	npm install eslint~4.17.1
	npm install eslint~4.17.1

	npm init  										Create package.json with prompt
	npm init -y 									Create package.json without prompt
	npm test 					npm t 				Run test
	npm run 										List scripts
	npm ls --depth 0 								Installed packages
	npm ls -g --depth 0
	npm i -g npm 									to update npm. npm> 5.2 has 'npx'
	npm it 											to run install and test ???
	
	UNINSTALL
	npm uninstall modulename						Remove a package from your node_modules directory
 	npm uninstall --save modulename					To remove it from the dependencies in package.json
	npm uninstall --no-save <your_library> 			Remove it from the node modules but not from the package.json

 	npm uninstall quinoa
 	npm uninstall quinoa -g   						if globally installed
	npm uninstall -g node.io && npm uninstall node.io

	INCREMENT "version": "1.0.0",
	npm version patch  		patch can be used as hotfix that doesn't imply breaking changes and doesn't introduce new features
	npm version minor 		minor can be used to tag versions introducing new features and minor non-breaking changes
	npm version major  		major is used for versions that introduce breaking changes

	FIND PACKAGE VERSION
	npm list 						returns versions of all modules and dependencies.
	npm list -g 
	npm list --depth=0 				list locally installed packages without their dependencies
	npm list -g angular
	npm list -g --depth=0
	npm view <package> version  	returns the latest available version on the package (not the installed)
	npm info YOUR_PACKAGE version   returns the latest available version on the package (not the installed)
	npm list --depth=0  			returns versions of all installed modules without dependencies.

	Linux 			npm list | grep <package name> 
	windows  		npm list | find "<package name>"
	PowerShell 		npm list | sls <package name>

	{
	  "name": "...project name...",
	  "version": "...project version...",
	  "description": "...some description...",
	  "main": "...startup JavaScript file...",
	  "dependencies": {},
	  "devDependencies": {},
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1"
	  },
	  "author": "...your name...",
	  "license": "ISC"
	}

	Use NPM's init command to set it up 
	>npm init 			ask questions
	{
	  "name": "my app",
	  "version": "1.0.0",
	  "description": "ssss",
	  "main": "index.js",
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1"
	  },
	  "author": "",
	  "license": "ISC"
	}

	>npm init -y 		--yes or -y: doesn't ask questions (app name is the currrent's folder name)
	{
	  "name": "Temp",
	  "version": "1.0.0",
	  "description": "",
	  "main": "index.js",
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1"
	  },
	  "keywords": [],
	  "author": "",
	  "license": "ISC"
	}
		
	prune: remove packages that are not listed on the parent package's dependencies list.
	npm prune [[<@scope>/]<pkg>...] [--production]

	

	* shrinkwrap
	
	    npm shrinkwrap
		Lock down dependency versions by generating	**npm-shrinkwrap.json**
		{
		  "name": "A",
		  "version": "1.1.0",
		  "dependencies": {
		    "B": {
		      "version": "1.0.1",
		      "from": "B@^1.0.0",
		      "resolved": "https://registry.npmjs.org/B/-/B-1.0.1.tgz",
		      "dependencies": {
		        "C": {
		          "version": "1.0.1",
		          "from": "org/C#v1.0.1",
		          "resolved": "git://github.com/org/C.git#5c380ae319fc4efe9e7f2d9c78b0faa588fd99b4"
		        }
		      }
		    }
		  }
		}
		shrinkwrap locked down the dependencies based on what's currently installed in node_modules

		locks down the versions of a package's dependencies so that you can control exactly which versions of each dependency will be used when your package is installed.

		By default, npm install recursively installs the target's dependencies listed in package.json, choosing the latest available version that satisfies the dependency's semver pattern
		In some situations, particularly when shipping software where each change is tightly managed, it's desirable to fully specify each version of each dependency recursively so that subsequent builds and deploys do not inadvertently pick up newer versions of a dependency that satisfy the semver pattern.

# .gitignore

 	Exclude node_modules from source control

## Add node_modules to your .gitignore file to exclude it and all installed packages from getting committed to source control.

    node_modules/
    typings/
    dist/
    *.log

# package.json

	package.json : https://docs.npmjs.com/files/package.json

	{
	    "name": "mon-app", 			← required
	    "version": "0.1.0",		    ← required
	    "author": "nguinet",
	    "main": "foo_package.js" 	a module ID that is the primary entry point to your program. That is, if your package is named foo, and a user 
	    							installs it, and then does require("foo"), then your main module's exports object will be returned.
	    							npm start resolving the package at that point. 
	    							If there is no "main" field, it will look for an "index.js"
	}

# NPM WORKFLOW

	1. INIT

	npm init 		→ prompt... → package.json 			Create the package.json file (ask for the fields)
	npm search 										List modules available or go on https://www.npmjs.com
	npm init -y    no prompt questions

	2. DEVELOPPEMENT
	npm run <script_name>

	3. TESTS
	npm run <test script_name>

	4. PRODUCTION
	npm prune [[<@scope>/]<pkg>...] [--production]     	remove packages that are not listed on the parent package's dependencies list. prune: tailler, elaguer, emonder
	npm install --production  							doesn't install “devDependencies”

	5. UPDATE
	npm -v
	npm install npm@latest -g
	npm install npm -g 					Update npm itself (npm gets updated more frequently than Node does). Not working on Windows
	 									reinstalling npm according to the documentation: "You can download a zip file from https://npmjs.org/dist/, and unpack it in the same folder where node.exe lives." https://nodejs.org/en/download/

	npm update              			Search all packages updates. Run it in the same directory as your package.json
	npm outdated 						Check versions

# NPM Variables

	{
	  "scripts": {
	    "start": "http-server dist -p 8000",
	    ...
	  }
	}
	
	
	to be able to easily change the port:

	{
	

# NPM Scripts: build/test system

## C:\Program Files\nodejs\node_modules\npm\doc\misc\npm-scripts.md

	npm run    			list of the commands interfaced by npm scripts
 	npm run myscript  	call custom script


	"scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1",
	    "start": "nodemon index.js 3000"
	 },

	"scripts": {
   		 "start": "node index.js"
  	}

	"scripts" property is a dictionary containing script commands that are run at various times in the lifecycle of your package. 
    language agnostic task-runner
	The key is the lifecycle event, and the value is the command to run at that point.
	Common ones are the start and the test scripts
	 npm run <your-custom-script>
	Predefined scripts names
	 	npm start
	 	npm test
	 	npm run
		npm run postinstall 


	npm will default some script values based on package contents.
	* `"start": "node server.js"`:

	* prepublish:	 			Run BEFORE the package is packed and published, as well as on local `npm install` without any arguments.
	* prepare:		 			Run both BEFORE the package is packed and published, and on local `npm install` without any arguments. This is run AFTER `prepublish`, but BEFORE `prepublishOnly`
	* prepublishOnly:		  	Run BEFORE the package is prepared and packed, ONLY on `npm publish`. (See below.)
	* prepack:				  	run BEFORE a tarball is packed (on `npm pack`, `npm publish`, and when  installing git dependencies)
	* postpack:				  	Run AFTER the tarball has been generated and moved to its final destination.
	* publish, postpublish:		Run AFTER the package is published.
	* preinstall:				Run BEFORE the package is installed
	* install, postinstall:		Run AFTER the package is installed.
	* preuninstall, uninstall:	Run BEFORE the package is uninstalled.
	* postuninstall:			Run AFTER the package is uninstalled.
	* preversion:				Run BEFORE bumping the package version.
	* version:				  	Run AFTER bumping the package version, but BEFORE commit.
	* postversion:				Run AFTER bumping the package version, and AFTER commit.
	* pretest, test, posttest:				Run by the `npm test` command.
	* prestop, stop, poststop:				Run by the `npm stop` command.
	* prestart, start, poststart:			Run by the `npm start` command.
	* prerestart, restart, postrestart:		Run by the `npm restart` command. Note: `npm restart` will run the stop and start scripts if no `restart` script is provided.
	* preshrinkwrap, shrinkwrap, postshrinkwrap:				  Run by the `npm shrinkwrap` command.

	Additionally, arbitrary scripts can be executed by running `npm run-script <stage>`. 
	*Pre* and *post* commands with matching  names will be run for those as well (e.g. `premyscript`, `myscript`,`postmyscript`). 
	Scripts from dependencies can be run with `npm explore <pkg> -- npm run <stage>`.


	package.json file:
	{
	  "name": "mypackage",
	  "author": "webkid.io"
	  "scripts": {               ← add some entries to the scripts section
	    "test": "ava"            ← 'npm test' to run ava 
	  },                           if you don't have the folder ./node_modules/.bin exported to your PATH, you
	  "devDependencies": {         will end up calling ava as   ./node_modules/.bin/ava 
		"ava": "^0.20.0"
	  }
	}

	{
	    "name": "mon-app", 			← required
	    "version": "0.1.0",		    ← required
	    "author": "nguinet",
	    "main": "app.js", 			← simply crank up the server with typing 'nodemon' in the CLI. Default is 'index.js'
	    "scripts": {
	    	“start”: “node index.js”,
	        "test": "echo \"Error: no test specified\" && exit 1",
			“testm”: “mocha test”,
			“your-custom-script”: “echo npm”
			"watch": "watchify main.js -o public/bundle.js -dv",
	        "postinstall": "node_modules/.bin/tsd update",
	        "postinstall": "node_modules/.bin/tsd install",
	        "build": "node node_modules/typescript/bin/tsc",
	        "run": "node node_modules/http-server/bin/http-server -o"
    }	

	{
	    "name": "mon-app",
	    "version": "0.1.0",		    
	    "main": "app.js",
	    "scripts": {
	    	“start”: “node index.js”,
	        "test": "echo \"Error: no test specified\" && exit 1",
				“testm”: “mocha test”,
				“your-custom-script”: “echo npm”
	        "postinstall": "node_modules/.bin/tsd update",
	        "postinstall": "node_modules/.bin/tsd install",
	        "build": "node node_modules/typescript/bin/tsc",
	        "run": "node node_modules/http-server/bin/http-server -o"
	    }			

	* HOOKS

	npm install --save-dev husky                gives you git hooks like precommit
	{
  	"scripts": {
    "precommit": "npm test",
    ...
  	}
	}
	This will run npm test every time you enter git commit and it will proceed committing the changes only if the script exits with a 0 exit-code, 
	meaning no error occurred. You can of course decide to run other scripts than npm test or to hook another command instead of commit.

# Npm run script - Command Line Tools with Node

	http://website.simplx.fr/blog/2017/05/23/creer-une-interface-en-ligne-de-commande-avec-npm/

	npm run-script <command> [--silent] [-- <args>...]        runs a command from a package's "scripts" object
	npm run (alias)

	npm run adds node_modules/.bin to the PATH provided to scripts. 
	Any binaries provided by locally-installed dependencies can be used without the node_modules/.bin prefix. 

	"scripts": {"test": "tap test/\*.js"}
	instead of
	"scripts": {"test": "node_modules/.bin/tap test/\*.js"}  
	npm run sets the NODE environment variable to the node executable with which npm is executed. 

	https://docs.npmjs.com/cli/run-script

	https://javascriptplayground.com/blog/2015/03/node-command-line-tool/
	npm init
	package.json
	{
	  "name": "filesearch",
	  "version": "1.0.0",
	  "description": "searches for files",
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1"
	  },
	  "author": "JavaScript Playground",
	  "license": "ISC",
	  "preferGlobal": true,          warn installers that the module is designed to be installed globally (-g)
	  "bin": {
	    "filesearch": "index.js"     maps commands to files. when module is install, npm will set up
	  } 							 the filesearch executable to execute index.js
	}


	index.js
		#! /usr/bin/env node
		console.log('This is the filesearch script.');

	Installing the Script
		npm link 	(from your project): install the script on your system. 
					Creates a symlink to your project so that you can run the project whilst working on it, with no need to keep reinstalling it over and over again.

	Then you should be able to run `filesearch` on the command line and see the string printed back
		~/git/filesearch > filesearch
		This is the filesearch script.

## Processing Arguments

	index.js
		console.log(process.argv);

	~/git/filesearch > filesearch foo
	[ 'node', '/Users/jackfranklin/.nvm/v0.10.32/bin/filesearch', 'foo']
		↓				↓                                           ↓
		↓               ↓                                   following arguments are ones of the user
		↓			second argument is the path to the file that has been executed. 
	 First argument is always node

	index.js
		var exec = require('child_process').exec;
		var userArgs = process.argv.slice(2);  // slice to get an array of just the arguments we need
		var searchPattern = userArgs[0];
		var child = exec('ls -a | grep ' + searchPattern, function(err, stdout, stderr) {
	  	console.log(stdout);
		});

	~/git/filesearch > filesearch package
		package.json	

	npm adduser and follow the prompts to set up and authenticate yourself.
	npm publish to push it onto npm
	Have good semver, Readme
	Once published, users can then install your module using npm install --global filesearch.




	     

	    official Node.js's package manager (automatically installed when you install Node.js)
	    Use npm through the command line to 
	    install, uninstall, update, manage packages for your Node.js application
	    It can also be used to install packages locally or globally to provide functionality on the command line and not necessarily within your Node.js application.

# Scoped / Private Packages :  @myorg/mypackage

	https://docs.npmjs.com/misc/scope

	$ npm init 
	$ npm init --scope=simplx       scoped !

	Originally NPM had a global shared namespace for module names - with more than 250.000 modules in the registry most of the simple names are already taken. 
	Also, the global namespace contains public modules only. NPM addressed this problem with the introduction of scoped packages. 
	
	Scoped packages has the following naming pattern: @myorg/mypackage

	You can install scoped packages the same way as you did before:
	npm install @myorg/mypackage --save-dev
	
	It will show up in your package.json in the following way:
	“dependencies”: {
	 “@myorg/mypackage”: “^1.0.0”
	 }

	Requiring scoped packages works as expected:
	 npm install @myorg/mypackage --save-dev 

	[NPM scoped module docs](https://docs.npmjs.com/misc/scope)    	
					
# TIPS

	[Most commonly used functionalities in our team](https://blog.webkid.io/npm-tips-and-scripts)	
    - npm scripts
	- npm variables
    - Handle package-lock.json and yarn.lock files      
	- Release and Tagging
		Shorthand for creating a new release of your package and keeping track of your versions at the same time. The command should be used to follow the Semantic Versioning paradigm.
		In order to keep track of version numbers, we use the npm version command. Each time we merge the develop branch into the master we run one of the following commands:
		npm version patch  		patch can be used as hotfix that doesn't imply breaking changes and doesn't introduce new features
		npm version minor 		minor can be used to tag versions introducing new features and minor non-breaking changes
		npm version major  		major is used for versions that introduce breaking changes

		These will increment the parts version in package.json:
		{
  			"name": "webpack2-basics",
  			"version": "1.0.0",

		Followed by a git push --tags
		This will bump the version number in the package.json and create a new git tag for the latest version number.

	    ### 1: Install packages locally
	    npm install <package_name>
	    installs a package and any packages it depends on into a folder named "node_modules" within the current working directory.

	    ### 2: Install packages globally
	    npm install -g <package_name>
	    Install packages and have them available anywhere
	    This will install packages in {prefix}/lib/node_modules, where {prefix} is usually something like /usr/local.

	    ### 3: Install packages as dependencies
	    npm install <package_name> --save
	    add the package in packages.json's "dependencies" object  -> To use "npm install" later

	    "dependencies": {
	      "express": "^4.0.0",
	      "body-parser": "^1.0.2"
	    }

	    This is critical when deploying your application to production. 
	    In most cases you won’t be deploying your node_modules folder so it will need to know what packages your application depends on so they can be installed.

	    This is also useful when working with other developers who may get a copy of your source code but not the node_modules folder. By having these dependencies listed, they can simply run "npm install" from within the application folder to have npm install all the necessary packages.

	    ### 4: Install packages as dev env dependencies
	    npm install <package_name> --save-dev
	    add the package in packages.json's "devDependencies" object  -> To use "npm install" later

	    "devDependencies": {
	        "mocha": "^1.18.2"
	    }

	    Useful for packages for test runners, debugging, and more but not have them install in production.

	    ### 5: Install packages as exact version dependencies rather than based on a range or approximate
	    npm install <package_name> --save --save-exact

	    ### 6: Save time with Nodemon
	    monitor for any changes in your source and automatically restart your server.
	    Install it globally so I can use it for all projects, but you can remove the -g to install it locally instead.
	    npm install -g nodemon

	    instead of "node server.js" to run your application
	    use        "nodemon server.js"

	    ### 7: Enable debugging with Node Inspector
	    Node Inspector is a debugger interface for Node.js applications that uses the Blink Developer Tools. 
	    works almost exactly as the Chrome Developer Tools.

	    Some of the things you can do with Node Inspector are:

	        Navigate in your source files
	        Set breakpoints (and specify trigger conditions)
	        Step over, step in, step out, resume (continue)
	        Inspect scopes, variables, object properties
	        Hover your mouse over an expression in your source to display its value in a tooltip
	        Edit variables and object properties
	        Continue to location
	        Break on exceptions
	        Disable/enable all breakpoints

	    npm install -g node-inspector
	    Run it using the following command. This will start the debugger and open your browser.
	    node-debug server.js

	    ### 8: Exclude node_modules from source control

	    add node_modules to your .gitignore file to exclude it and all installed packages from getting committed to source control.


	    hostname :""
	    hash :""
	    host :""
	    origin :"null"
	    href :"file:///D:/Users/s0053232/Desktop/MD/aaa.html"
	    protocol :"file:"

# Lockfiles (package-lock.json, yarn-lock.json)

	lock the version number in stone and will guarantee that the same package version is installed on every subsequent installation.

	package-lock.json. NPM uses this file to make sure that anyone else using your project 
	(or even yourself in other environments) will always get versions compatible with those 
	that you are installing now.
	Not using lockfiles?
	If you are willing to spend time debugging what changed from your CI/environment deployment to what you ran on your local machine that’s totally fine. 
	If you’re not, and your goal is to get reproducible deploys, then you should be using lockfiles (either with npm or yarn).

    To understand the package-lock and even package.json, you have to understand semantic versioning (semver).  
    http://semver.org/  
    http://blog.npmjs.org/post/115305091285/introducing-the-npm-semantic-version-calculator  
    When you install a package with npm (and save it), an entry is added to your package.json containing the package name, and the semver that should be used. npm supports some wildcards in this semver definition however. By default, npm installs the latest version, and prepends a caret e.g. “^1.2.12”. This signifies that at a minimum, version 1.2.12 should be used, but any version higher than that is OK, as long as it has the same major version, 1. Since minor and patch numbers only represent bugfixes and non-breaking additions, you should be safe to use any higher same-major version.
    ! Where things might go wrong...  
    npm install express — save` (4.15.4 At the time of writing)  
    npm install ... later get the latest fixed 4.15.5 but maybe that bugfix affected functionality that we are using, and our application would produce different results when run with express version 4.15.4 compared to 4.15.5.  
    ** purpose of the package-lock is to avoid the situation described above where installing modules from the same package.json results in two different installs.**

    **The Format**
		Package-lock is a large list of each dependency listed in your package.json, the specific version that should be installed, the location of the module (URI), a hash that verifies the integrity of the module, the list of packages it requires, and a list of dependencies.

## The idea then becomes that instead of using package.json to resolve and install modules, npm will use the package-lock.json. Because the package-lock specifies a version, location and integrity hash for every module and each of its dependencies, the install it creates will be the same, every single time.

    **The Controversy**
    Some people thought that the package.json should be the source of truth, some people thought that since package-lock is what npm uses to create the install, that should be considered the source of truth. The resolution to this controversy lies in npm PR #17508. Npm maintainers added a change that causes package.json to overrule the package-lock if package.json has been updated. 

    package-lock
	    ~ more verbose package.json
	    auto created
	    npm>5 
        Ensure a consistent install and compatible dependencies
        You SHOULD commit your package-lock to source control
        No more deleting that package-lock just to run `npm install` and regenerate it
        Use semver if your app offers an API, and adhere to the rules of semver.


	Yarn and npm 5 introduced lockfiles, supposed to be commited to your git repository:
	It is highly recommended to commit the generated package lock to source control: this will allow anyone else in your team, your deployments, your CI/continuous integration, and anyone else who runs npm install in your package source to get the exact same dependency tree that you were developing on.
	Unfortunately this is causing a lot of trouble


	In production you should still use this:
		#!/bin/sh
		git checkout .
		git pull origin master
		rm -f package-lock.json && npm install

### Letting package-lock.json decide the versions still leaves your apps crippled once and again.



# NPX
	npm package runner that runs (load, call and delete) directly from the npm registry (or local/global if present)	
	npx is a new utility available in npm 5 or above that executes local binaries/scripts to avoid global installs

	npx supports executing CLIs even when they are not installed yet. Simply run npx create-flex-plugin and it will download it into a cache if it can't find a locally- or globally-installed version.
		
	npx is an utility that comes with npm v5.2.0 and that is designed to make it easy to run CLI utilities and executables hosted in the npm registry. For example, it allows developers to use locally installed executables without having to use the npm run scripts.
		
	https://www.npmjs.com/package/npx
	https://github.com/zkat/npx
	https://medium.com/@sibeeshvenu/npm-vs-npx-f737dea2fb4
	https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b

	npm install -g npx@latest
	npm > 5.2.0

	npx [options] <command>[@version] [command-arg]...
	npx [options] [-p|--package <pkg>]... <command> [command-arg]...
	npx [options] -c '<command-string>'
	npx --shell-auto-fallback [shell]

	Install windows issue: Command failed: C:\"Program Files"\nodejs\node.exe C:\Program Files\nodejs\node_modules\npm\bin\npm-cli.js config get cache --parseable
	Fix: 
		1. C:\Program Files\nodejs\node_modules\npm\package.json →  "libnpx": "~9.2.0", to "libnpx": "^9.2.0",
		2. npm update
		3. npx -v
	
	
	npx lets you execute npm package binaries without installing them globally
	npx <package> will install and run the package
		When it’s done, the installed package won’t be anywhere in your globals
		All of this is done internally. What npx does is use npm to install into $npm_cache/_npx and then prepends that temporary install directory to your running $PATH, so you’ll see the binaries in it.
        npx isolates runs, then completely removes the temporary directory on process exit, so there’s nothing to clean.
        If you wanna be really sure nothing’s left, you can do $ rm -rf $(npm config get cache)/_npx, and you’ll -definitely- no longer have any of npx’s internal goo lying around, but that shouldn’t be necessary. :)
        it’s a cache and you can rm -rf ~/.npm/_npx to clear it

  		npx is
        A npm package runner
        Use the packages directly from npm registry
        No global or local installation required
        Using the globally/locally installed package if it is installed. That means, global or local installed package gets the priority

	$ npx cowsay wow
	$ npx babel script.js

	$ npx create-react-app my-cool-new-app
	installs a temporary create-react-app and calls it, without polluting global installs or requiring more than one step!
	https://github.com/facebookincubator/create-react-app

	we can create a simple react application with the help of Create-React-App from FaceBook

      npm i -g create-react-app
      create-react-app my-new-app
      npm start           you’re in business with a fully functional, hot reloading dev server. 

      or more simply: npx create-react-app

      Npx? Create-React-App from FaceBook is used only for creating the application, and once we create the application, and we are no longer needed this. 
      If you use npm, you will have to install this package either globally or locally before you use this, or else you will get an error.
      Isn’t it good, if we can just use this create-react-app package from the npm registry and create the application in our local machine? And that’s where npx stands. With the  help of npx, we can reduce the size of our node_modules and I strongly believe that this is a huge benefit. And we can even execute the packages and command simultaneously like below.
      It is smart enough to identify whether the package you are trying to get from the npm registry is already there in your machine, either globally or locally. If the package is available in your machine, it will take it from there.

      npx is,
        A npm package runner
        Use the packages directly from npm registry
        No global or local installation required
        Using the globally/locally installed package if it is installed. That means, global or local installed package gets the priority
	
	https://github.com/js-n/awesome-npx
	https://npm.im/happy-birthday
	https://npm.im/benny-hill
	https://npm.im/workin-hard
	https://npm.im/cowsay
	https://npm.im/yo
	https://npm.im/create-react-app
	https://npm.im/npm-check

	A server! 
	Easily try out APIs! Also a 1-liner w/ #npx:
	npx json-server https://raw.githubusercontent.com/typicode/jsonplaceholder/master/data.json

	npx is cool!
	common to use gist.github.com to share all sorts of utility scripts, instead of setting up entire git repos, releasing new tools, etc.
	With npx, you can take it a step further: since npx accepts any specifier that npm itself does, you can create a gist that people can invoke directly, with a single command!
	npx https://gist.github.com/zkat/4bc19503fe9e9309e2bfaa2c58074d32
		• readme.md
			Hi! try passing the URL for this gist to npx
		• index.js
			#!/usr/bin/env node
			console.log('yay gist')
		• package.json
		{"name": "npx-is-cool", "version": "0.0.0", "bin": "./index.js"}
	N:\projects\@tools\web\@node_based__gulp_etc\npx>npx https://gist.github.com/zkat/4bc19503fe9e9309e2bfaa2c58074d32
	npx: installed 1 in 3.954s
	Path must be a string. Received undefined
	npx: installed 1 in 3.66s                      will install it in:
	C:\Users\nguin\AppData\Roaming\npm-cache\_npx\11732\node_modules\npx-is-cool\index.js
	yay gist                                       will delete folder _npx\11732\node_modules\npx-is-cool




	
	Executes <command> from $PATH or in the local project binaries
	If <command> is not found, it will be installed prior to execution.
	All npm package may be used with npx, including git specifiers, remote tarballs, local directories, or scoped packages.

	npx <command> 
	when <command> isn’t already in your $PATH will automatically install a package with that name from the npm registry for you, and invoke it. 
	When it’s done, the installed package won’t be anywhere in your globals, so you won’t have to worry about pollution in the long-term.

	Fun packages with npx: happy-birthday, benny-hill, workin-hard, cowsay, yo, create-react-app, npm-check.
	https://github.com/js-n/awesome-npx

	Running a project-local bin
	$ npm i -D webpack
	$ npx webpack ...
	$ npx github:piuccio/cowsay
	$ npx git+ssh://my.hosted.git:cowsay.git#semver:^1
	$ npx -p lolcatjs -p cowsay -c \ 			Execute a full shell command using one npx call w/ multiple packages
  	  'echo "$npm_package_name@$npm_package_version" | cowsay | lolcatjs'

	npm it 		to run install and test...works because npm run-script adds local binaries to path
				but...no fast/convenient way to invoke local binaries interactively
				Some fix, but none are quite ideal:
				. add those tools to your scripts, remember to pass arguments using --
				. shell tricks like alias npmx=PATH=$(npm bin):$PATH
				. path manually: ./node_modules/.bin/mocha. 

	makes it easy to use CLI tools and other executables hosted on the registry. It greatly simplifies a number of things that, until now, required a bit of ceremony to do with plain npm:

	to run a package just once, without installing it globally on your machine or locally in your project, you can try npx. 
	to run the locally installed executables. You can drop it inside of an npm run script or you may instead execute with the relative path instead. 

	Let's say we want to try the git-changelog command:
	npx git-changelog -t false -a "My nice application"
	
	This can of course be integrated in the npm scripts section for tasks that don't run that often.


	with npm>5.2, or $ npm install -g npx

	$ npx http-server    to start an http server in the current directory

	Shorthand for Calling Local Binaries
	Normally, if you want to run a binary that’s installed locally with your project instead of globally on the machine, you’d have to type the following:
	$ ./node_modules/.bin/jest      	In this example we're running the locally-installed jest binary
	
	Well, no more! With npx it’s now as simple as running the following:
	$ npx jest

# NPM TESTING

## Create a 'npm' folder

 	Create 'npmtest.js'
 			console.log("Hello World");

### Enter node a.js → It Works

 		Enter 'npm install'

			C:\Temp\npm>npm install
			npm ERR! install Couldnt read dependencies
		 	npm ERR! Error: ENOENT, open 'C:\Temp\npm\package.json'
		 	+ npm has created  'npm-debug.log'

## Update 'npmtest.js'

		var http = require('http');
		var server = http.createServer(function (req, res)
		{
			res.writeHead(200, {'Content-Type': 'text/plain'});
			res.write("...body...");
		    res.end('Hello World\n');
		});
		server.listen(1337, '127.0.0.1');
		console.log('Server running at http://127.0.0.1:1337');

		Enter node a.js → It Works
	 	Enter 'npm install'

			C:\Temp\npm>npm install
			npm ERR! install Couldnt read dependencies

	Update 'npmtest.js'
		var http = require('http');
		var os = require('os');
		var markdown = require('markdown');

		var server = http.createServer(function (req, res)
		{
			console.log(os.hostname());
		  	console.log(os.platform());
		  	console.log(markdown.toHTML('A **markdown** paragraph!'));

			res.writeHead(200, {'Content-Type': 'text/plain'});
			res.write("...body...");
		    res.end('Hello World\n');
		});
		server.listen(1337, '127.0.0.1');
		console.log('Server running at http://127.0.0.1:1337');

		Enter a.js → FAILED
							module.js:340
							    throw err;
							          ^
							Error: Cannot find module 'markdown'
							at Function.Module._resolveFilename (module.js:338:15)
					    	at Function.Module._load (module.js:280:25)

### Enter 'npm install'

		C:\Temp\npm>npm install
		npm ERR! install Couldnt read dependencies



		C:\Temp\npm>npm search markdown
		npm WARN Building the local index for the first time, please be patient
		npm http GET https://registry.npmjs.org/-/all
		…

		npm search markdown >> ModulesListForNpm.txt

		NAME                  DESCRIPTION                                                   AUTHOR                DATE              VERSION     KEYWORDS
		active-markdown       A tool for generating reactive documents from markdown source. =alecperkins         2013-05-04 08:23  0.3.2
		add-less-import       Add an `@import` statement into a .less file at a specific point.  =jonschlinkert   2014-06-02 18:26  0.1.2       docs documentation generate generator markdown templates verb
		adoc2gfm              A adoc markdown syntax to GFM syntax                          =ksky521              2014-11-27 01:51  0.0.3       adoc gfm
		…
		markdown              A sensible Markdown parser for javascript                     =ashb =dom            2013-12-04 11:37  0.5.0       markdown text processing ast
		…


	Create 'package.json'
		{
		    "name": "mon-app",
		    "version": "0.1.0",
		    "dependencies": {
		        "markdown": "0.3.5",
		        "markdown": "~0.3.5",
		        "markdown": "~0.3"
		    }
		}

## Enter 'npm install'

		npm WARN package.json mon-app@0.1.0 No description
		npm WARN package.json mon-app@0.1.0 No repository field.
		npm WARN package.json mon-app@0.1.0 No README data
		npm http GET https://registry.npmjs.org/markdown
		npm http 200 https://registry.npmjs.org/markdown
		npm http GET https://registry.npmjs.org/markdown/-/markdown-0.3.1.tgz
		npm http 200 https://registry.npmjs.org/markdown/-/markdown-0.3.1.tgz
		markdown@0.3.1 node_modules\markdown

		This create
			node_modules
				.bin
					md2html
					md2html.cmd
						@IF EXIST "%~dp0\node.exe" (
						  "%~dp0\node.exe"  "%~dp0\..\markdown\bin\md2html.js" %*
						) ELSE (
						  node  "%~dp0\..\markdown\bin\md2html.js" %*
						)
				markdown
					package.json
					README.markdown
					bin
						md2html.js
					lib
						index.js
						markdown.js
					test
					
# NPM - NODE MODULE SYSTEM

## C:\Program Files\nodejs\node_modules\npm\

	http://www.codemag.com/article/1709061

	npm 	Node Package Manager
			Node modules provide a way to re-use code in your Node application ~ class
			Extend node by downloading & installing modules
			Thousands modules available on npm.org

								   ___ look for 'http.js'
								  |
			const http = require('http');     Use http.js (by convention it is in 'node_modules' folder)
			  \				\			   	Search a 'node_modules' folder in parent folders if missing...
			   \ 			 \___ Bring a module into scope 
                \
                 \___ prevents variable from being overwritten in the calling code. 

			const test = require('./test');  // use test.js (relative path to same folder)

			const path = require('path');
			console.info(path.extname('index.js'));

			Internally, require is an abstraction around an internal function, _load() wich
				Check Module._cache for a cached copy
				Create a new Module instance if not found in cache
				Save it to the cache
					Ensures that I don’t accidentally load multiple copies of a module
				 	Reference to the loaded module is returned if the module was already loaded. Each module has only a single instance in memory. A new instance won’t be created each time you require() a module because require() may return a cached instance based on the identifier it’s passed
				Load contents of the model
					/, ../ or ./ assumes a relative path and attempts to load the module at that path. 
					If the identifier isn’t a relative path, the following locations are searched:
						Node core modules (installed with Node. If core module not found, Node assumes the identifier refers to a Node package)
						Node_modules directory, checks recursively by traversing the directory structure to the root directory
						Path pointed to by NODE_PATH (points to the global package location)
						$HOME/.node_modules
						$HOME/.node_libraries
						$PREFIX/lib/node_modules
				Compile the contents into a closure
				If there was an error, delete from the cache
				Return module.exports

	Modules 
		Is a .js file with 'export' functions
		Make developing things easier
		Based on CommonJS modules
		Cached after the first time they are loaded
		require() return an 'module.exports' object
			Use both `exports` and 'module.exports' to import code into your application		
			 	var module = {};
		  		var exports = module.exports = {};
			   	var require = function(path) { …						
		    		return module.exports;
		  		};
		
		Think required files as functions that return a single object, and you can add properties (strings, numbers, arrays, functions…) to the object that's returned by setting them on `exports`.
	
		* Set `exports` to have the require() object returned to be an object with properties/functions ~ class

			\hello\hello.js
			exports.world = function() {console.log('Hello World'); }

			main.js
			var hello = require('./hello');
			hello.world();
			$ node main.js

			many node users are overwriting the `exports` object directly like so: 
			module.exports = function() {...}
			will directly cause the require function to return the assigned function
			useful if you're doing object oriented programming, where each file exports the constructor of one class.

		*  Set 'module.exports' to have the require() object returned to be a function you can call rather than just an object with properties
			
			// test.js
			var name = 'william';
			module.exports = function(){console.log(name); }
			module.exports = () => 'Hi, world!'

			// index.js
			var test = require('./test');
			test();
		
		Using node modules

			var os = require('os'); 		// 'os.js' is the required module
											// By convention it is in 'node_modules' folder
											// Nodde will search a 'node_modules' folder in parent folders if missing...
		  	console.log(os.hostname());
		  	console.log(os.platform());

			* Absolute path   /
				require('/...') 				prefixed with '/' is an absolute path to the file
				require('/home/marco/foo.js') 	will load the file at /home/marco/foo.js

			* Relative path  ./  ../	
				require('./circle') 			'./' is relative to the file calling require()
												circle.js must be in the same directory as foo.js

			* Core module / node_modules
				Without a leading '/', './', or '../' to indicate a file, the module must either be Core module/node_modules folder

			* Non-core modules
				var mysql = require('mysql');
				node.js will walk up the directory tree, moving through each parent directory in turn, checking in each to see if there is a folder called 'node_modules'. 
				If such a folder is found, node.js will look into this folder for a file called 'mysql.js'. If no matching file is found and the directory root '/' is reached, node.js will give up and throw an exception.


		* We accessed an exported object and made certain that private state isn't available outside the 'module.exports'
		* Node has a pretty cool module system (require('http')) where a module can be compared to classes like we have in C# or Java.
		* If the given path does not exist, require() will throw an Error with its code property set to 'MODULE_NOT_FOUND'.
		* Modules are cached after the first time they are loaded. every "require('foo')"" will get exactly the same object returned, if it would resolve to the same file.

### NodeJS module mechanism is based on CommonJS modules which are supported in many other implementations like RequireJS, but also SproutCore, CouchDB, Wakanda, OrientDB, ArangoDB, RingoJS, TeaJS, SilkJS, curl.js, or even Adobe Photoshop.

		module.exports = () => 'Hi, world!'

		module.exports = [
	    {    
	        name: 'The Revolver',
	        price: 15,
	        description: 'Easy to carry, perfect while roaming.',
	        sku: '1',
	        image: 'https://snipcart.com/media/10191/nerf-1.jpg'
	    },
	    {    
	        name: 'The Heavy Duty',
	        price: 65,
	        description: 'Spray and pray.',
	        sku: '2',
	        image: 'https://snipcart.com/media/10192/nerf-2.jpg'
	    },
	    {    
	        name: 'The One Hit Wonder',
	        price: 70,
	        description: 'One shot, one opportunity',
	        sku: '3',
	        image: 'https://snipcart.com/media/10193/nerf-3.jpg'
		    }
		]

	* Install module with npm

		npm detect module dependencies (listed in package.json) and install needed modules automatically

		Find a module about...
			npm search postgresql
			npm search email

		package.json does not only list dependency names, but also dependency versions. Of course one is able to allow more modern versions of packages, but in general packages tend to specify versions as exact as possible. This minimizes the risk of facing breaking changes
		npm install --save-dev gulp-uglify
		http://www.codeproject.com/Articles/865943/An-introduction-to-Gulp

	* npm link: developing your own npm modules without tears

		http://browsenpm.org/help#linkinganynpmpackagelocally

		Package linking: Linking a npm package to your system is a two-step process:
	 	cd http-server/
	    npm	link 								(in package dir). Linking any npm package locally
	    										Our local version of http-server is "linked" on our local machine
		cd new-app/
		npm link [<@scope>/]<pkg>[@<version>]   (in project dir)

		1. npm link                 IN A PACKAGE FOLDER 
									Create a symlink (symbolic link) in {prefix}/lib/node_modules/<package> that links to the package where the npm link command was executed
		                            
		                            similar to npm install -g except 
		                            • no package download
		                            • current folder becomes the global package
	    2. npm link package-name    IN SOME OTHER LOCATION 
	    							Create a symlink from globally-installed package-name to node_modules/ of the current folder.
	                                package-name is taken from package.json, not from directory name.

	   // in 2 steps
	   cd ~/projects/node-redis    # go into the package directory
	   npm link                    # creates global link for node-redis
	   cd ~/projects/node-bloggy   # go into some other package directory
	   npm link redis              # link-install the package

	   // in one step
	   cd ~/projects/node-bloggy  # go into the dir of your main project
	   npm link ../node-redis     # link the dir of your dependency

		npm unlink http-server 		Unlinking a npm package from an application
		
		cd http-server/				Unlinking a npm package from your system
	 	npm unlink

	dependencies
		required to run

	devDependencies

### Only to develop, e.g.: unit tests, Coffeescript to Javascript transpilation, minification, ...

		npm init 							→ create package.json, list dependency names & versions
		npm install --save-dev gulp 		→ installed a project-local version of gulp
						↓
					added gulp to the project´s dependencies in package.json
					we need another local version of Gulp to ensure that each project has exactly the version of Gulp it requires
					in general packages tend to specify versions as exact as possible. This minimizes the risk of facing breaking changes.



		https://docs.npmjs.com/files/package.json
		dependencies are installed on both:
		npm install from a directory that contains package.json
		npm install $package on any other directory

		devDependencies are:
			also installed on npm install on a directory that contains package.json
			not installed on npm install "$package" on any other directory, unless you give it the --dev option.
		peerDependencies are
			always installed if missing, like dependencies, but unlike dependencies raise an error
			if multiple incompatible versions of the dependency would be used by different dependencies.

		If you are going to develop a package, you download it (e.g. via git clone), go to its root
		which contains package.json, and run: npm install
		Since you have the actual source, it is clear that you want to develop it, so by default both
		dependencies (since you must of course run to develop) and devDependency dependencies are also installed.

		If however you are only an end user who just wants to install a package to use it, you will do from any
		directory:	npm install "$package"
		In that case, you normally don´t want the development dependencies, so you just get what is needed to use
		the package: dependencies.

		If you really want to install development packages in that case, you can set the dev config option to true,
		possibly from the command line as:

		npm install "$package" --dev
		The option is false by default since this is a much less common case.

# NPM MODULE CREATION

	- Don't use the same name as a core Node module (Don't put "js" or "node" in the name)
	- Publish your package to npm
	- Make a new directory outside of your project and cd into it
	- npm install <package>
	- Create a test.js file which requires the package and calls the method
	- node test.js 	The message should be output.


 	myfirstmodule.js
		module.exports.name = function() { return "Joe"; }  // an object with a single property 'name'

									
								   ___ relative path module, require() look in same directory as the currently executing module
								  /	
	const firstModule = require('./firstmodule');
	console.log('Results: ' + firstModule.name());

	Not specifying the .js suffix is a common convention in Node. It does create some ambiguity as to what will be loaded, though. It could refer to:
		myfirstmodule as a file
		myfirstmodule.js as a file
		myfirstmodule.json as a file
		myfirstmodule/index.js as a directory with a file in it
	Node looks at all of the above options when attempting to load a file.

# MODULE DESIGN PATTERNS





##NPM

```js
    npm install <package_name>              → packages + dep → current_dir/node_modules                 LOCAL INSTALL    
    npm install -g <package_name>           →                → /usr/local/lib/node_modules              GLOBAL INSTAKK
    npm install <package_name> --save       → packages.json "dependencies": { "express": "^4.0.0", …    PROD DEPENDENCIES
                                                                ↓
                                                        npm install → packages → node_modules → node server.js
    npm install <package_name> --save-dev   → packages.json "devDependencies": { "mocha": "^1.18.2", …  DEV DEPENDENCIES (tests,debug…)
    npm install <package_name> -D           → -D = --save-dev

    npm install <package_name> --save --save-exact
    npm install -g nodemon                  → nodemon server.js → restart server when source code changes
    npm install -g node-inspector
    .gitignore
        node_modules/
        typings/
        dist/
        *.log



    official Node.js's package manager (automatically installed when you install Node.js)
    Use npm through the command line to 
    install, uninstall, update, manage packages for your Node.js application
    It can also be used to install packages locally or globally to provide functionality on the command line and not necessarily within your Node.js application.


    ### 1: Install packages locally
    npm install <package_name>
    installs a package and any packages it depends on into a folder named "node_modules" within the current working directory.

    ### 2: Install packages globally
    npm install -g <package_name>
    Install packages and have them available anywhere
    This will install packages in {prefix}/lib/node_modules, where {prefix} is usually something like /usr/local.

    ### 3: Install packages as dependencies
    npm install <package_name> --save
    add the package in packages.json's "dependencies" object  -> To use "npm install" later

    "dependencies": {
      "express": "^4.0.0",
      "body-parser": "^1.0.2"
    }

    This is critical when deploying your application to production. 
    In most cases you won’t be deploying your node_modules folder so it will need to know what packages your application depends on so they can be installed.

## This is also useful when working with other developers who may get a copy of your source code but not the node_modules folder. By having these dependencies listed, they can simply run "npm install" from within the application folder to have npm install all the necessary packages.

    ### 4: Install packages as dev env dependencies
    npm install <package_name> --save-dev
    add the package in packages.json's "devDependencies" object  -> To use "npm install" later

    "devDependencies": {
        "mocha": "^1.18.2"
    }

## Useful for packages for test runners, debugging, and more but not have them install in production.

    ### 5: Install packages as exact version dependencies rather than based on a range or approximate
    npm install <package_name> --save --save-exact

    ### 6: Save time with Nodemon
    monitor for any changes in your source and automatically restart your server.
    Install it globally so I can use it for all projects, but you can remove the -g to install it locally instead.
    npm install -g nodemon

    instead of "node server.js" to run your application
    use        "nodemon server.js"

    ### 7: Enable debugging with Node Inspector
    Node Inspector is a debugger interface for Node.js applications that uses the Blink Developer Tools. 
    works almost exactly as the Chrome Developer Tools.

## Some of the things you can do with Node Inspector are:

        Navigate in your source files
        Set breakpoints (and specify trigger conditions)
        Step over, step in, step out, resume (continue)
        Inspect scopes, variables, object properties
        Hover your mouse over an expression in your source to display its value in a tooltip
        Edit variables and object properties
        Continue to location
        Break on exceptions
        Disable/enable all breakpoints

    npm install -g node-inspector
    Run it using the following command. This will start the debugger and open your browser.
    node-debug server.js

    ### 8: Exclude node_modules from source control

    add node_modules to your .gitignore file to exclude it and all installed packages from getting committed to source control.


    hostname :""
    hash :""
    host :""
    origin :"null"
    href :"file:///D:/Users/s0053232/Desktop/MD/aaa.html"
    protocol :"file:"
```




