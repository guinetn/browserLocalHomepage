# BOWER

	the Bower team are suggesting using Yarn and Webpack to replace the functionality of Bower



	http://bower.io/docs/api/
	http://learn.jquery.com/jquery-ui/environments/bower/
		
	a front-end package manager (npm is a BACK-END PACKAGE MANAGER)

	A package manager for client-side code/components by Twitter´s engineers
	To make easier the frontend package management: manage your frontend dependencies (jQuery, AngularJS, underscore…)
	API and configuration is very similar to NPM from Node.js (bower.json = package.json)

 	"package" 	is the thing that you can download, and contains a component, which is a group of one or more assets
	"component" is a repo which contains some files for client-side
			    A Bower component has a bower.json file that describes the component and its dependencies

# BOWER COMMANDS

    bower <command> [<args>] [<options>]
# Commands:

	'bower help <command>' for more information on a specific command

    cache                   Manage bower cache
    help                    Display help information about Bower
    home                    Opens a package homepage into your favorite browser
    info                    Info of a particular package
    init                    Create a 'bower.json' file interactively (questions asked) 
							bower init
								name: [angular-my-directive]
								version: [0.0.0]
								main file: [] directive.js
								add commonly ignored files to ignore list? (y/n): [y] y
    install                 Install a package locally
								bower install  	

										install frontend dependencies in the folder 'bower_components'
				

							Usage:

							    bower install [<options>]
							    bower install <endpoint> [<endpoint> ..] [<options>]

							Options:

							    -F, --force-latest      Force latest version on conflict
							    -h, --help              Show this help message
							    -p, --production        Do not install project devDependencies
							    -S, --save              Save installed packages into the project's bower.json dependencies
							    -D, --save-dev          Save installed packages into the project's bower.json devDependencies
							    -E, --save-exact        Configure installed packages with an exact version rather than semver
							    Additionally all global options listed in 'bower help' are available

							Description:

							    Installs the project dependencies or a specific set of endpoints.
							    Endpoints can have multiple forms:
							    - <source>
							    - <source>#<target>
							    - <name>=<source>#<target>

							    Where:
							    - <source> is a package URL, physical location or registry name
							    - <target> is a valid range, commit, branch, etc.
							    - <name> is the name it should have locally.

							    																		

http://www.mikestreety.co.uk/blog/ignoring-libraries-in-git
http://blog.nodejitsu.com/package-dependencies-done-right/

bootstrap-filestyle/bower.json
																						{
  "name": "bootstrap-filestyle",
  "version": "1.2.1",
  "homepage": "https://github.com/markusslima/bootstrap-filestyle",
  "authors": [
    "Markus Lima @markusslima"
  ],
  "description": "Bootstrap FileStyle is a quick and simple plugin to help style your form's file upload inputs.",
  "main": "src/bootstrap-filestyle.js",
  "keywords": [
    "bootstrap",
    "fileupload",
    "filestyle"
  ],
  "license": "MIT",
  "ignore": [
    "**/.*",
    "node_modules",
    "bower_components",
    "test",
    "tests"
  ]
}↓
																					can be change with '.bowerrc' file
																					.bowerrc
																					{
																			 		 "directory": "inc/",
																			 		 "json": "bower.json"
																					}

								bower install <package>

									bower install jquery										Registered package. Take latest version on github.com/components/jquery.git
									bower install jquery#2.0.0 									A tag allow to choose the github version
									bower install desandro/masonry								GitHub shorthand
									bower install git://github.com/user/package.git 			Git endpoint
									bower install git@github.com:components/jquery.git#2.0.0 	Git endpoint + version
									bower install http://example.com/script.js 					URL

									The package/component will be downloaded, cached, and then copied to a 'components' directory in the CURRENT WORKING DIRECTORY    

									 
									 SEMVER (Semantic Versioning specification)
									 	"dependencies": { "angular": "~1.0.6"…
									 		~ means "install the highest 1.0.x version."
									 		the lowest version number (also called the "patch" number) is for fixes that dont change APIs in a way that is not backwards compatible
		
									bower install btford/angular-socket-io.git 							install from Github 
									bower install git@github.com:btford/angular-socket-io.git 			use a private register on Github

    link                    Symlink a package folder
    list                    List local packages - and possible updates
    lookup                  Look up a package URL by name
    prune                   Removes local extraneous packages
    register                Register a package
    search                  Search for a package by name
    							
    							. http://bower.io/search/

								. bower search angular
									Search results:
									  - angular git://github.com/angular/bower-angular.git
									  - angular-resource git://github.com/angular/bower-angular-resource.git
									  - angular-mocks git://github.com/angular/bower-angular-mocks.git
									  - angular-cookies git://github.com/angular/bower-angular-cookies.git
									  - angular-sanitize git://github.com/angular/bower-angular-sanitize.git
									  - angular-scenario git://github.com/angular/bower-angular-scenario.git
									  - angular-unicorn-directive git://github.com/btford/angular-unicorn-directive.git
									  ...

								. bower search angular | grep "phonegap"   ← search with multiple keywords
									  - angular-phonegap-ready git://github.com/btford/angular-phonegap-ready.git
									  - angular-phonegap-geolocation git://github.com/btford/angular-phonegap-geolocation.git
									  - angular-phonegap-accelerometer git://github.com/btford/angular-phonegap-accelerometer.git
									  - angular-phonegap-notification git://github.com/btford/angular-phonegap-notification.git
    update                  Update a local package
    							bower update knacss 				update a dependency
    uninstall               Remove a local package
    							bower uninstall <package-name> 		To uninstall a locally installed package:
    							To uninstall a locally installed package:
								bower uninstall <package-name>
    version     -v          Bump a package version

# Options:

    -f, --force             Makes various commands more forceful
    -j, --json              Output consumable JSON
    -l, --log-level         What level of logs to report
    -o, --offline           Do not hit the network
    -q, --quiet             Only output important information
    -s, --silent            Do not output anything, besides errors
    -V, --verbose           Makes output more verbose
    --allow-root            Allows running commands as root
    --version               Output Bower version




# SAMPLE

bower init
bower install angular
bower install bootstrap   (include jquery)
bower list
bower update
bower install angular-strap --save
bower install angular-bootstrap --save
bower install angular-material --save
    <!-- Angular Material Dependencies -->
    <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/angular_material/0.7.1/angular-material.min.css">
    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.6/angular.min.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.6/angular-animate.min.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.6/angular-aria.min.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/angular_material/0.7.1/angular-material.min.js"></script>
touch readme.md


# Yeoman 

	Angular-Gulp-Bower generator
    	http://techiedreams.com/yeoman-angular-gulp-bower-generator/
	    npm install -g generator-angular-gulp-bower

	    In Yeoman, Bower is used to install and update libraries like AngularJS...
	     						    managing the versions of various libraries for your app
	     						    you can use Bower to find, install, update, and even publish your own reusable components


# QUICKSTART

npm install -g bower 		Install bower
npm update -g bower 		Update bower

# Bower configuration file  <http://bower.io/docs/config/>
	↓
.bowerrc 									
{
  "directory": "app/components/",
  "analytics": false,
  "timeout": 120000,
  "registry": {
    "search": [
      "http://localhost:8000",
      "https://bower.herokuapp.com"
    ]
  }
}

bower.json 		File specifying a list of dependencies
				Describe the component and its dependencies
				{
				  "name": "angular-my-directive",
				  "version": "0.0.0",
				  "main": "directive.js",
				  "ignore": [
				    "**/.*",
				    "node_modules",
				    "components"
				  ],
				  "dependencies": {
				    "angular": "~1.0.6"
				  }
				}








# Bower is used together with other tools to integrate with all sorts of setups and workflows.
				Grunt
				Gulp
				Yeoman
				RequireJS
				SublimeText



# WHAT IS BOWER?

	A package manager for the front end (you no longer have to manually download and manage your scripts)
	Bower allow to install/update/remove all the depencies your projects need
	You can use Bower to download libraries like jQuery UI from the command line, without having to manually download each project from their respective sites

	Manual web library management:
			Create folder, visit tool´s website, upload and copy files, then update <script>..tedious

	Bower works by fetching and installing packages from all over, taking care of hunting, finding, downloading, and saving the
	stuff you’re looking for. Bower keeps track of these packages in a manifest file, bower.json. How you use packages is up to you.

 	And npm ? Node Packaged Modules: to developp node.js apps but it has a “back” orientation







## DIFFERENCE BETWEEN BOWER AND NPM?

 		colleagues use bower and npm interchangeably in their project

		npm is used for managing Node.js modules but it works for the front-end too when combined with Browserify and/or $ npm dedupe
		Bower is created solely for the front-end and is optimized with that in mind. The biggest difference is that npm does nested dependency tree (size heavy) while Bower requires a flat dependency tree (puts the burden of dependency resolution on the user).
		The reason many projects use both is that they use Bower for front-end packages and npm for developer tools like Yeoman, Grunt, Gulp, JSHint, CoffeeScript, etc.


		npm
		It is much harder to avoid dependency conflicts without nesting dependencies. This is fundamental to the way that npm works, and has proven to be an extremely successful approach.
		project root
		[node_modules]
		 -> dependency A
		 -> dependency B
		    -> dependency A

		 -> dependency C
		    -> dependency B
		       -> dependency A
		    -> dependency D

		Bower:
		Bower is optimized for the front-end. Bower uses a flat dependency tree, requiring only one version for each package, reducing page load to a minimum.
		project root
		[bower_components]
		 -> dependency A
		 -> dependency B
		 -> dependency C
		 -> dependency D



	INSTALL BOWER
		Bower depends on Node.js (nodejs.org/download), npm and Git (git-scm.com/downloads must be installed as some bower packages require it to be fetched and installed)

		cmd > npm install -g bower

		Check if the dos variable 'path' contains NPM & Git paths:
			'C:\Users\***\AppData\Roaming\npm; C:\Program Files (x86)\Git\bin'
			'C:\Program Files (x86)\Git\bin' or 'C:\Progra~2\Git\bin'
			If No, add it by Config Panel > System > Advanced


	CONFIGURATION
		By defautlt bower install package in a 'bower_components' folder. This can be changed with a '.bowerrc' JSON´s file
		bower.io/docs/config

		.bowerrc
			{
			  "directory": "app/bower_components"
			}

		.bowerrc
			{
	 		 "directory": "inc/",
	 		 "json": "bower.json"
			}

	SETUP PROJECT
	
	bower init

	C:\Tmp\P215\PA15>bower init
	? name: PA15
	? version: 0.0.0
	? description: Website of hotel les palmiers F83230
	? main file: readme.md
	? what types of modules does this package expose?:
	  amd es6 node yui
	? keywords: hotel bormes palmiers restaurant
	? authors: nguinet <me@me.com>
	? license: MIT
	? homepage: http://www.hotellespalmiers.com
	? set currently installed components as dependencies?: No
	? add commonly ignored files to ignore list?: Yes	
	? would you like to mark this package as private which prevents it from being ac published to the registry?: No

## INSTALL PACKAGES VIA BOWER

		bower install <package>
		based on the {"name":"url"} of https://bower.herokuapp.com/packages

		bower install jquery										Registered package. Take latest version on github.com/components/jquery.git
		bower install jquery#2.0.0 									A tag allow to choose the github version
		bower install desandro/masonry								GitHub shorthand
		bower install git://github.com/user/package.git 			Git endpoint
		bower install git@github.com:components/jquery.git#2.0.0 	Git endpoint + version
		bower install http://example.com/script.js 					URL


		PROJECT VERSION MANAGED:
			Manage conflicts version with the 'component.json' file (if it is present on the github project)

		Installing packages and dependencies from a 'bower.json' file
			bower install 									Install dependencies listed in bower.json
			bower install <package> --save 					install a package and add it to bower.json
			bower install <package>#<version> --save 		install specific version of a package and add it to bower.json

			bower.json
			{
			    "name": "projet",
			    "dependencies": {
			        "knacss": "latest",
			        "html5shiv": "latest",
			        "box-sizing-polyfill": "latest",
			        "modernizr": "latest",
			        "jquery": "1.10.2"
			    }
			}


			bower.json
			{
			 "name": "Marionette-Boilerplate",
			  "version": "0.0.1",
			 "dependencies": {
			   "jquery": "2.0.0",
			    "backbone": "1.0.0",
			    "marionette": "1.0.2",
			    "underscore": "1.4.4",
			    "requirejs": "2.1.5",
			    "requirejs-text": "2.0.6",
			    "mustache": "latest",
			    "hogan": "latest",
			    "bootstrap": "latest",
			    "less.js": "latest"
			  }
			}


			cmd >   cd myfolder
					bower install knacss      	(small css framework)
					bower install knacss#2.9.1 	install a specific version
					bower update knacss 		update dependency
			 									update my dependencies
			 									   |
					bower.json file         _______|
							{
							    "name": "projet",
							    "dependencies": {
							        "knacss": "latest",
							        "html5shiv": "latest",
							        "box-sizing-polyfill": "latest",
							        "modernizr": "latest",
							        "jquery": "1.10.2"
							    }
							}

	USING PACKAGES
		How you use packages is up to you but we discourage using bower components statically for performance and security
		reasons (if component has an upload.php file that is not ignored, that can be easily exploited to do malicious stuff).
		The best approach is to process components installed by bower with build tool (like Grunt or gulp), and serve them concatenated
		or using module loader (like RequireJS).

### Use Bower together with Grunt, RequireJS, Yeoman, and lots of other tools or build your own workflow with the API.

		TOOLS
			Bower is used together with other tools to integrate with all sorts of setups and workflows.
				Grunt
				Gulp
				SublimeText
						Plugin for sublime text: benschwarz/sublime-bower
						http://germanforblack.com/post/46734908388/i-built-a-plugin-for-sublime-text-that-integrates
						G:\Roaming\st3\bower_components




# REGISTER YOU DEPENCY IN BOWER REPOSITORY (http://bower.io/search/)

	A. Conditions: 	1. On GitHub
					2. 'bower.json' must be present at the project´s root


## B. Register process:

	bower register knacss
	git@github.com:raphaelgoetter/KNACSS.git


## C. Sample of 'bower.json' for KNACSS depency:

	{
	  "name": "KNACSS",
	  "version": "2.9.1",
	  "homepage": "http://www.knacss.com/",
	  "authors": [
	    "Raphaël GOETTER, Alsacreations"
	  ],
	  "description": "KNACSS is a minimalist, responsive and extensible style sheet to kick-start your HTML / CSS projects. It relies on common best practices and experience on the topic.",
	  "main": "css/knacss.css",
	  "keywords": [
	    "css", "framework", "reset", "responsive", "rwd", "boilerplate", "workflow"
	  ],
	  "license": "WTFPL",
	  "ignore": [
	    "**/.*",
	    "node_modules",
	    "bower_components",
	    "test",
	    "less/knackLESS.zip",
	    "tests",
	    "README.md"
	  ]
	}










## Bower vs npm



			npm / bower → similar functions
			    npm -v
			    npm update              Search all updates
			    npm search              List modules available

			    npm detect module dependencies (listed in package.json) and install needed modules automatically

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

			    npm install         Will download all the Node packages needed (found in 'package.json')

			    npm install css-sprite --save
			                              ↓
			                              Local download + ADD depencies in 'package.json'
			    npm install css-sprite -g
			                            ↓
			                            To use css-sprite on your cli. Usage: css-sprite <out> <src>... [options]

			    var http = require('http');         http moduke, to set up a web server. Include with node.js
			    var test = require('./test');       use test.js (relative path to same folder)
			    var test = require('../test');      use test.js (relative path to parent folder)
			    var express = require('express');   Will use express.js, by convention it is in 'node_modules' folder



	npm 
		is most commonly used for managing Node.js modules, but it works for the front-end too when combined with Browserify and/or $ npm dedupe.
		It is much harder to avoid dependency conflicts without nesting dependencies. 
		This is fundamental to the way that npm works, and has proven to be an extremely successful approach.

		project root
		[node_modules]
		 -> dependency A
		 -> dependency B
		    -> dependency A

		 -> dependency C
		    -> dependency B
		       -> dependency A 
		    -> dependency D
		As you can see it installs some dependencies recursively. Dependency A has three installed instances!

	Bower 
		is created solely for the front-end and is optimized with that in mind. 
		optimized for the front-end. 
		Bower uses a flat dependency tree, requiring only one version for each package, reducing page load to a minimum.
		To manage your frontend dependencies. Libraries like jQuery, AngularJS, underscore, etc. Similar to npm it has a file in which you can specify 
		a list of dependencies called bower.json. In this case your frontend dependencies are installed by running bower install which by default installs 
		them in a folder called bower_components.

		project root
		[bower_components]
		 -> dependency A
		 -> dependency B
		 -> dependency C
		 -> dependency D

	So, why bother using NPM?
	Maybe dependency B requires a different version of dependency A then dependency C. 
	NPM installs both versions of this dependency so it will work anyway, but Bower will give you a conflict because 
	it does not like duplication (because loading the same resource on a webpage is very inefficient and costly). 
	You will have to manually pick which version you want to install. This can have the effect that one of the dependencies will break.

	The biggest difference is that npm does nested dependency tree (size heavy) while Bower requires a flat dependency tree (puts the burden of dependency resolution 
		on the user).
	A nested dependency tree means that your dependencies can have its own dependencies which can have their own, and so on. This is really great on 
	the server where you dont have to care much about space and latency. It lets you not have to care about dependency conflicts as all your dependencies use
	e.g. their own version of Underscore. This obviously doesnt work that well on the front-end. Imagine a site having to download three copies of jQuery.

## The reason many projects use both is that they use Bower for front-end packages and npm for developer tools like Yeoman, Grunt, Gulp, JSHint, CoffeeScript, etc.


	Writing Reusable AngularJS Components with Bower
		http://briantford.com/blog/angular-bower





