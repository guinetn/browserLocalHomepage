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

# CYPRESS

https://github.com/cypress-io/cypress
https://www.lambdatest.com/blog/cypress-vs-selenium-comparison

open source automation testing and web app testing.

# SELENIUM

https://www.lambdatest.com/blog/selenium-with-python

```js
> Launch a Selenium chrome driver
from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
### Open a webpage (i.e. google.com),
driver.get('http://www.google.com')
### Get an element (‘q’ means something),
driver.find_element_by_name('q')           # via name
driver.find_element_by_id('q')             # via id
driver.find_element_by_class_name('q')     # via class
>via css format: i.e. <input type="password" />
driver.find_element_by_css_selector('input[type='password']') 
>via xpath: i.e. <input name="username" type="text" />
driver.find_elements_by_xpath('//input[@name='username']')
### Write in a text box and submit
query = 'something'           # things we want to post
box.send_keys(query)
box.submit()
### Click a button
btn.click()
Scrolling down the page,
driver.execute_script("window.scrollTo(0, 10000);")
Quit the driver,
driver.quit()
```