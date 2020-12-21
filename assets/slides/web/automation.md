# Web UI Automation

Automating tasks to be performed on webpage elements

Virtual browser: act as a browser without actually having a GUI

## Browsers Drivers  
Abstract the interaction with the browser.  
To communicate with the corresponding web browser.  
Every browser has its own browser driver, and the same needs to be installed on the machine where automation testing will be performed.
When the browser driver receives any command (or request), it is executed on the respective browser, and the response of execution is sent to the web driver as an HTTP response.

WebDrivers
Firefox https://github.com/mozilla/geckodriver/releases
Chrome http://chromedriver.chromium.org/downloads
Internet Explorer https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver
Microsoft Edge https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

HEADLESS WEBSITE TESTING 	Run functional tests with frameworks such as Jasmine, QUnit, Mocha, Capybara, WebDriver
		SCREEN CAPTURE 				Programmatically capture web contents, including SVG and Canvas. Create web site screenshots with thumbnail preview
		PAGE AUTOMATION 			Access and manipulate webpages with the standard DOM API, or with usual libraries like jQuery.
		NETWORK MONITORING 			Monitor page loading and export as standard HAR files. Automate performance analysis using YSlow and Jenkins. Learn more

### https://www.lambdatest.com/blog/selenium-webdriver-with-python