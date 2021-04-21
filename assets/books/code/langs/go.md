# Go

Designed by Google as a ‘better C++’
Good at running across large networks like the server farms that power the world’s number one search engine. In comparison, coping with the cluster farms of even the largest banks is a piece of cake.

https://github.com/twpayne/chezmoi/blob/master/main.go
use a github command

Golang: This language is by Google and its code is extremely easy to write and maintain. Go programmers are among the highest paid programmers in the marker as per stackoverflow. The development of web, desktop and mobile apps all are supported in Go.

## PACKAGES

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

Aliasing
```go
package main

import (
 f "fmt"          // Printf refer now as f.Printf rather than fmt.Printf
  "math/rand"
)

func main() {
  for i := 0; i < 10; i++ {
    f.Printf("%d) %d\n", i, rand.Intn(25))
  }
}
```

***Installing Packages***
>go get github.com/gobuffalo/flect
Find the package on GitHub in this case, and install it into your $GOPATH
$GOPATH/src/github.com/gobuffalo/flect
>go get -u github.com/gobuffalo/flect     To update package

## More
- https://github.com/twpayne
- https://www.digitalocean.com/community/tutorials/importing-packages-in-go