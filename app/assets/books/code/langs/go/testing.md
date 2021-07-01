# testing with Golang
Golang supports automated testing of packages with custom testing suites.
To create a new suite, create a file that ends with _test.go and includes a TestXxx function, where Xxx is replaced with the name of the feature you're testing. For example, a function that tests login capabilities would be called TestLogin.
You then place the testing suite file in the same package as the file you wish to test. The test file will be skipped on regular execution but will run when you enter the go test command.