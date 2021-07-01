# Go

Designed by Google as a ‘better C++’
Good at running across large networks like the server farms that power the world’s number one search engine. In comparison, coping with the cluster farms of even the largest banks is a piece of cake.
Go use type composition exclusively, not inheritance

- Other languages that started as academic experiments, Go code is pragmatically designed. Every feature and syntax decision is engineered to make life easier for the programmer.
- Optimized for concurrency and works well at scale.
- Single standard code format = More readable
- Automatic concurrently garbage collection more efficient than in Java/Python

https://github.com/twpayne/chezmoi/blob/master/main.go
use a github command

Golang: This language is by Google and its code is extremely easy to write and maintain. Go programmers are among the highest paid programmers in the marker as per stackoverflow. The development of web, desktop and mobile apps all are supported in Go.

# GO SAMPLES
download.slideshow(assets/books/code/langs/go/code_samples/go01.md)

## PACKAGES - pkg

Directories within your Go workspace that contain Go source files or other packages. 
Every function, variable, and type from your source files is stored in the linked package. Every Go source file belongs to a package, which is declared at the top of the file using:
package <packagename>
You can import and export packages to reuse exported functions or types using:
import <packagename>
Golang’s standard package is fmt, which contains formatting and printing functionalities like Println().

***Standard Library Packages***
ramdom.go
```go
package main

import "math/rand"

func main() {
  for i := 0; i < 10; i++ {
    println(rand.Intn(25))
  }
}
```
>go run random.go

***Installing Packages***
>go get github.com/gobuffalo/flect
Find the package on GitHub in this case, and install it into your $GOPATH
$GOPATH/src/github.com/gobuffalo/flect
>go get -u github.com/gobuffalo/flect     To update package

download.page(assets/books/code/langs/go/types.md)
download.page(assets/books/code/langs/go/loops.md)
download.page(assets/books/code/langs/go/interface.md)
download.page(assets/books/code/langs/go/functions.md)
download.page(assets/books/code/langs/go/goroutines.md)
download.page(assets/books/code/langs/go/closure.md)
download.page(assets/books/code/langs/go/inheritance.md)
download.page(assets/books/code/langs/go/testing.md)
download.page(assets/books/code/langs/go/concurrency_parallelism.md)


## More
- https://github.com/twpayne
- https://www.digitalocean.com/community/tutorials/importing-packages-in-go
- [Distributed Services with Go](https://medium.com/pragmatic-programmers/table-of-contents-9cb9895df519)
- [GO INTERVIEWS](https://betterprogramming.pub/how-to-crack-the-top-25-golang-interview-questions-a94396d6c808)
- https://betterprogramming.pub/how-to-become-a-golang-developer-a-6-step-career-guide-ce8274dd0eb3
- https://pro.academind.com/p/golang-the-practical-guide
- https://www.bogotobogo.com/GoLang/GoLang_Closures_Anonymous_Functions.php