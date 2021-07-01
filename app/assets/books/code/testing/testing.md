# TESTING


## Testing
Executing the software with data to ensure that the software works correctly.
## Unit testing
Testing by the developer.
## Integration testing
Testing during the integration of the software.
## System testing
Testing software in an environment that matches the operational environment.

## Behavior testing

## E2E testing

## Alpha testing
Testing by the customer at the developer’s site.
## Beta testing
Testing by the customer at the customer’s site.
## Acceptance testing
Testing to satisfy the purchaser.
## Regression testing
Saving tests from the previous version to ensure that the new version retains the previous capabilities


https://www.maxcode.net/blog/how-to-reevaluate-the-testing-efficiency-by-understanding-what-a-testing-framework-can-offer/
Black box technique	White box technique	Gray box technique

http://www.westerndevs.com/bdd-vs-tdd/
https://waml.io/
http://assertselenium.com/2012/11/05/difference-between-tdd-bdd-atdd/
http://www.infoq.com/news/2011/08/bdd-net

http://mherman.org/blog/2015/04/09/testing-angularjs-with-protractor-and-karma-part-1/#.Vpqu0xXhCHs
http://stackoverflow.com/questions/478340/clear-file-cache-to-repeat-performance-testing

# 7 principles in software testing:
https://www.geeksforgeeks.org/software-engineering-seven-principles-of-software-testing/

# Testing shows presence of defects
# Exhaustive testing is not possible
# Early testing
# Defect clustering
# Pesticide paradox
# Testing is context dependent
# Absence of errors fallacy

# TYPES OF TESTING
# UNIT TESTING
# INTEGRATION TESTING
# TOP DOWN INTEGRATION TESTING
# BOTTOM UP INTEGRATION
# SANDWICH TESTING
# REGRESSION TESTING
# SMOKE TESTING
# OBJECT-ORIENTED TESTING

# FUNCTIONAL TESTING
# Les tests fonctionnels, qui interviennent couramment lorsqu'une fonctionnalité est quasiment prête à être livrée, permettent de tester les composantes de l'interface utilisateur et s'assurer qu'une fonctionnalité ou l'application entière marche correctement.


# TEST AUTOMATION 
# The use of special software (separate from the software being tested) to control the execution of tests and the comparison of actual outcomes with predicted outcomes

# MODEL-BASED TESTING 
# A software testing technique in which the test cases are derived from a model that describes the functional aspects of the System Under Test (SUT). Visual models can be used to represent the desired behavior of a SUT, or to represent testing strategies and a test environment. From that model manual tests, test data, and automated tests can be generated automatically.


# STAGING ENVIRONMENT 
# Used to test the newer version of your software before it’s moved to live production. Staging is meant to replicate as much of your live production environment as possible, giving you the best chance to catch any bugs before you release your software.

# PRODUCTION 
# The final stage in a deployment pipeline where the software will be used by the intended audience.

# CONTINUOUS TESTING 
# The process of executing unattended automated tests as part of the software delivery pipeline across all environments to obtain immediate feedback on the quality of a code build.

# Ex: https://github.com/reddit/reddit-mobile/issues/247
# Test setup: 2013 Moto X. On 4G (HSPA+). Chrome Dev Channel.
# Load reddit.com
# Tap on the big blue link to load the mobile site.
# Wait until the site feels loaded.
• Expectation: Site should load and give me the frontpage items and images in < 5 seconds.
• Result: Site came up with items and image placeholders within 3 seconds. It took 45 seconds to show images.
• First impression


writing modular, loosely coupled code is that your code becomes vastly easier to test

# Creating and Editing Tests
# Managing Tests
# Running Tests
# Test Results and Analysis


ccNode_Hero+-+The+complete+Node.js+tutorial+series+from+RisingStack.p
• test runner: mocha, alternatively tape 
• assertion library: chai, alternatively the assert module (for asserting) 
• test spies, stubs and mocks: sinon (for test setup).
# Spies
# You can use spies to get information on function calls, like how many times they were called, or what arguments were passed to them.

# Code coverage




# Test FRAMEWORKS


## Unit Tests 			QUnit, JsUnit, Jasmine, JsTestDriver, Mocha, WallabyJs, etc.

	Functional Test 	Selenium, HTMLUnit, Watir, karma, Protractor, coded-ui, Selenium WebDrive

## Integration tests


# The test pyrami
ccNode_Hero+-+The+complete+Node.js+tutorial+series+from+RisingStack.pdf

# EndtoEnd
# Integration tests
# Unit tests


# TESTING TYPES

## UNIT TESTING

		Automated tests where you write logic to test discrete parts of your application
   		A way to specify and verify the behavior of individual classes
		Simple to create and run, are brilliantly precise when you are working on algorithms, business logic, or other back-end infrastructure
		Validates a software system at its most basic level and in preferred isolation
		Unit tests are perfect for testing controllers and other js components

		Unit testing key
			a. the tests are short
			b. the tests run quickly
			c. the tests are run often
			d. the tests act as documentation for the code that it is testing.

## unit tests
a test process by which each unit of source code is tested to determine if it is ready for use
It​ is basically testing a small piece of code or a function/method to check whether it is working fine or not
unit tests are narrow, simple and generally written by the developer or the person writing the same piece of code


## INTEGRATION TESTING

Testing how the different parts of an application work together
integrates the parts of an application and then test them as a whole
complex and harder as it requires a lot of setups. That’s why integration tests are difficult to write and test than unit tests
combination of united tests
Done by a separate team of testers
Integration testing monitors the Integration between software modules.
Test methodology that integrates and measures individual units of a system as a group
Test stubs and test drivers are used for the integration testing. Usually Top down method and Bottom up method are been used to perform the integration testing.
 

		Complement to unit testing
		Validating the behavior of individual components
		involves multiple tiers of your application (for example, how components communicate between one another).
		A way to specify and verify the behavior of multiple components working together, up to and including the entire web application.

			Understanding Integration Testing

				integration testing lets you create tests that are client-focused, re-creating the actions of a user
				Integration testing takes more time. It takes longer to create the tests and longer to perform them.

				UI AUTOMATION
					refers to simulating or automating a web browser to exercise the application’s entire technology stack by reproducing the
					actions that a user would perform, such as clicking buttons, following links, and submitting forms

					Automation testing experience
					- Selenium - webdriver, GRID, TestNG
					- Jenkins, Maven and ANT

				open source browser automation options for .NET developers:
				• Selenium RC (http://seleniumhq.org/)
				  a Java “server” application that can send automation commands to Internet Explorer, Firefox, Safari, or Opera, plus clients for .NET, Python, Ruby,
			          and multiple others so that you can write test scripts in the language of your choice. Selenium is powerful and mature; its only drawback is that
				  you have to run its Java server.
				• WatiN (http://watin.sourceforge.net/)
				  a .NET library that can send automation commands to Internet Explorer or Firefox. Its API isn’t as powerful as Selenium, but it comfortably handles
				  most common scenarios and is easy to set up (you need to reference only a single dynamic-link library)

## END TO END TESTING (E2E - SYSTEM TESTING) 

		Unit tests are perfect for testing controllers and other components of our application written in JavaScript, but they can´t easily test DOM manipulation or the wiring of our application. For these, an end-to-end test is a much better choice.
	
		https://docs.angularjs.org/api/ngRoute/service/$route    see protactor.js


		Ensure the whole CLIENT SIDE application (views…) are displaying and behaving correctly.
		Test DOM manipulation / the wiring of our application.
    	It does this by simulating real user interaction with the real application (test DOM manipulation / application wiring) running in the browser.
		Tools: Selenium, protractor

	  
	  unit tests then E2E ends
	  https://docs.angularjs.org/guide/e2e-testing
	  As applications grow in size and complexity, it becomes unrealistic to rely on manual testing to verify the correctness of new features, catch bugs and notice regressions. Unit tests are the first line of defense for catching bugs, but sometimes issues come up with integration between components which can't be captured in a unit test. End-to-end tests are made to find these problems. E2E testing is a complement to Unit testing



	BETA TESTING
		manual testing whereby you give your software to a subset of your desired audience and have them try out your software

	Web Test
		A Web test, also called a declarative Web test, consists of a series of HTTP requests.
		Web tests work at the protocol layer by issuing HTTP requests. Web tests do not run JavaScript.
		However, you can simulate JavaScript actions at runtime by using Web test plug-ins, Web test request plug-ins,
		extraction rules, or coded Web tests.
		http://msdn.microsoft.com/en-us/library/ms182537(v=vs.80).aspx

	ACCEPTANCE TESTING - FUNCTIONAL TEST - CUSTOMER TEST
		application is verified from your customers standpoint
		Tools: FIT, Selenium

		Formal description of the behaviour of a software product, generally expressed as an example or a usage scenario
		Binary result, pass or fail; a failure suggests "though it does not prove" the presence of a defect in the product
		The terms "functional test", "acceptance test" and "customer test" are used more or less interchangeably.

		Extreme Programming has always talked about writing acceptance tests, sometimes also called functional tests to describe what
		the customer expects to be done at the end of an iteration.



# TOOLS


## TDD Tools

		NUnit	http://nunit.org
		MSUnit 	http://msdn.microsoft.com/en-us/library/ms243147(v=vs.80).aspx
		RhinoMocks
		Moq
		qUnit   js Unit testing http://qunitjs.com/
		VS Tools Menu → Extensions and Updates... menu and searching for "JavaScript Unit Testing"
		Chutzpah 	open source Visual Studio extension and JavaScript test runner
		http://nilsnaegele.com/codeedge/javascripttdd1.html
		https://github.com/mantoni/mochify.js   TDD with Browserify, Mocha, PhantomJS and WebDriver

	

	To see
		http://www.browserswarm.com
		https://saucelabs.com

### F:\@Projects\Web\mob.angular-seed-karma-jasm-protractor\readme.txt:

# C++ UNIT TESTING (ASSERT class)

# VISUAL STUDIO UNIT TESTING (ASSERT class)

		Click in the body of a method → Menu 'Tests' → Run → Tests in current context
														   → All Tests in solution
		  [Test]
		  public void AbsoluteValue()
		  {
		    Assert.AreEqual(4,Math.Abs(-4));
		    Assert.AreEqual(3,Math.Abs(3));
		  }

### Testing exceptions is easy, simply add the ExpectedException attribute.

		  [Test, ExpectedException(typeof(FileNotFoundException))]
		  public void AbsoluteValue()
		  {
		    File.OpenRead("filedoesnotexist.txt");
		  }


		ASSERT CLASS
			Central element for Unit Testing
			Static methods to check true assumptions
			Assert failed if condition is false

			AreEqual  				Vérifie que les valeurs spécifiées sont égales.
			AreNotEqual  			Vérifie que des valeurs spécifiées ne sont pas égales.
			AreNotSame  			Vérifie que des variables objets spécifiées font référence à des objets différents.
			AreSame  				Vérifie que des variables objets spécifiées font référence au même objet.
			Equals  				N´utilisez pas cette méthode.
			Fail  					Fait échouer une assertion sans vérifier les conditions.
			Inconclusive  			Indique qu´une assertion ne peut pas être prouvée true ou false. Permet également d´indiquer une assertion qui n´a pas encore été implémentée.
			IsFalse  			 	Vérifie qu´une condition spécifiée est false.
			IsInstanceOfType  		Surchargé. Vérifie qu´un objet spécifié est une instance d´un type spécifié.
			IsNotInstanceOfType  	Surchargé. Vérifie qu´un objet spécifié n´est pas une instance d´un type spécifié.
			IsNotNull  	 			Vérifie qu´un objet spécifié n´est pas nullptr.
			IsNull 					Vérifie qu´un objet spécifié est null.
			IsTrue					Vérifie qu´une condition spécifiée est true.
			ReplaceNullChars  		Dans une chaîne, remplace des caractères null ("\0") par "\\0."


# JS TESTING

http://jstest.jcoglan.com/


# JAVASCRIPT 'NATIVE' TESTING WITH ASSERT

		http://www.slideshare.net/simonguest
		https://github.com/angular/angular-seed    Good global sample

		assert() is not a native javascript function

		 	sol #1
				a modern browser or nodejs, you can use console.assert(expression, object)
				var add = function(x,y)
				{
					var res = x+y;
					console.assert(res, "an error occured. refresh (X should not be null)");
					return res;
				}

		 	sol #2

				function assert(condition, message) {
				    if (!condition) {
				        message = message || "Assertion failed";
				        if (typeof Error !== "undefined") {
				            throw new Error(message);
				        }
				        throw message; // Fallback
				    }
				}
				assert(1===1); // executes without problem
				assert(false, "Expected true"); // yields "Error: Assert failed: Expected true" in console

		 	sol #3

			 	<!DOCTYPE HTML>
				<html lang="en-US">
				<head>
				    <meta charset="UTF-8">
				    <title>Easy JavaScript Testing </title>
				    <style>
				        .pass:before {
				            content: 'PASS: ';
				            color:  blue;
				            font-weight: bold;
				        }

				        .fail:before {
				            content: 'FAIL: ';
				            color: red;
				            font-weight: bold;

				        }
				    </style>
				</head>
				<body>

				<ul id="output"></ul>

				<script>
				var output = document.getElementById('output');

				function assert( outcome, description ) {
					// outcome: A boolean, which references whether your test passed or failed
					// description: A short description of your test.
				    var li = document.createElement('li');
				    li.className = outcome ? 'pass' : 'fail';
				    li.appendChild( document.createTextNode( description ) );

				    output.appendChild(li);
				};
				</script>

				Run Tests:
				function add(num1, num2) { return num1 + num2; }

				var result = add(5, 20);
				assert( result == 24, 'Checking the add function');

				// OR
				assert( add( 5, 20 ) == 24, 'Checking the add function');

# QUNIT

		http://qunitjs.com/
		http://nilsnaegele.com/codeedge/javascripttdd1.html
		http://lostechies.com/chadmyers/2008/08/29/getting-started-with-jquery-qunit-for-client-side-javascript-testing/


		JavaScript unit testing framework.
		It is used by the jQuery, jQuery UI and jQuery Mobile projects
		Capable of testing any generic JavaScript code
		github.com/simonguest/gids/tree/master/testing/tests/qunit

# KARMA (old TESTACULAR)

		http://karma-runner.github.io/0.10/index.html
		https://www.npmjs.com/package/karma

		bring a productive testing environment to developers
		Test on Real Devices
		Run test when it detects change on files
		Continuous integration with Jenkins, Travis or Semaphore.
		Testing Framework Agnostic Describe your tests with Jasmine, Mocha, QUnit, or write a simple adapter for any framework you like.

		Karma is not a testing framework, nor an assertion library.
		Karma just launches a HTTP server, and generates the test runner HTML file you probably already know from your
		favourite testing framework:
			Jasmine
			Mocha
			QUnit
			…

## JASMINE

		http://pivotal.github.io/jasmine


# PROTRACTOR

		github.com/angular/protractor
		Testing framework for Angular JS or any application
		Support Jasmine tests by default
		selenium compatible
			script to support selenium installation
			install selenium dependencies
			npm install -g protractor
			webdriver-manager update
			webdriver-manager start

### See sample ANGULAR-SEED PROJECT

# SELENIUM

		seleniumhq.org
		Browser automation framework
		Web Application testing platform
		Basic test recorder

		SELENIUM WEBDRIVER
			w3c webdriver protocol
			remote control for browser (invoke&drive browser)
		
		SELENIUM GRID
			instantiate browsers on remote machine

			Tests (Jasmine written)
			     ▲ ▼
			  Protractor 			invoke tests
			  WebDriverJS 			test results sent to selenium server using WebDriver protocol
			  Selenium Host 		selenium invoking Chrome to run tests
			  Browser (Chrome...)
			     ▲ ▼
			Application to test




# E2E TESTING

   	Unit tests then E2E 

	  https://docs.angularjs.org/guide/e2e-testing
	  As applications grow in size and complexity, it becomes unrealistic to rely on manual testing to verify the correctness of new features, catch bugs and notice regressions. 
	  Unit tests are the first line of defense for catching bugs, but sometimes issues come up with integration between components which can't be captured in a unit test. 
	  End-to-end tests are made to find these problems. 
	  E2E testing is a complement to Unit testing


## End-to-end tests written in Jasmine, run with the Protractor End-to-End test runner.

	Protractor simulates interaction with our web app and verifies that the application responds correctly.
	Therefore, our web server needs to be serving up the application, so that Protractor can interact with it.
	npm start // start the web server 'http-server' installed with npm

	In addition, since Protractor is built upon WebDriver we need to install this
	npm run update-webdriver   //This will download and install the latest version of the stand-alone WebDriver tool.

	Once you have ensured that the development web server hosting our application is up and running and WebDriver is updated,
	you can run the end-to-end tests using the supplied npm script:
	npm run protractor 	// This script will execute the end-to-end tests against the application being hosted on the development server.

		. protractor.conf.js

			exports.config = {
			  allScriptsTimeout: 11000,

			  specs: ['*.js'],

			  capabilities: {
			    'browserName': 'chrome'
			  },

			  baseUrl: 'http://localhost:8000/app/',

			  framework: 'jasmine',

			  jasmineNodeOpts: {
			    defaultTimeoutInterval: 30000
			  }
			};

		. scenarios.js

				'use strict';
				/* https://github.com/angular/protractor/blob/master/docs/toc.md */
				describe('my app', function() {

				  browser.get('index.html');

				  it('should automatically redirect to /view1 when location hash/fragment is empty', function() {
				    expect(browser.getLocationAbsUrl()).toMatch("/view1");
				  });


				  describe('view1', function() {

				    beforeEach(function() {
				      browser.get('index.html#/view1');
				    });


				    it('should render view1 when user navigates to /view1', function() {
				      expect(element.all(by.css('[ng-view] p')).first().getText()).
				        toMatch(/partial for view 1/);
				    });

				  });


				  describe('view2', function() {

				    beforeEach(function() {
				      browser.get('index.html#/view2');
				    });


				    it('should render view2 when user navigates to /view2', function() {
				      expect(element.all(by.css('[ng-view] p')).first().getText()).
				        toMatch(/partial for view 2/);
				    });

				  });
				});

# A/B Testing

	The idea behind A/B testing is to facilitate choice by measuring the user engagement for each of the options

	A/B testing (sometimes called split testing) is comparing two versions of a web page to see which one performs better. 
	You compare two web pages by showing the two variants (let's call them A and B) to similar visitors at the same time. 
	The one that gives a better conversion rate, wins!
		
	1. Visual Website Optimizer probably the best A/B testing tool
	2. Optimizely
	3. Google website optimizer (Free)


# UNIT TEST NAMING CONVENTIONS	

# Which one would you choose?

[Test]
# ShouldGetAllUsersByAge()
{
}

[Test]
# Should_Get_All_Users_By_Age()
{
}

[Test]
should_get_all_users_by_age()
{
}

# Choose number 3:

# It’s the closest we’ll get to an English sentence without using spaces.
# It’s lowercase which reduces the cognitive load of reading.
# Pascal case is a lot harder to read.
# It uses given when then (or would do in more complex examples, infact they all do).




## More 
- https://intellitect.com/decoupling-csharp-testable/
- https://www.educba.com/unit-test-vs-integration-test/?source=leftnav

