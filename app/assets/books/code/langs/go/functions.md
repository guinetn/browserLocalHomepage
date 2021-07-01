## Functions

### return multiple values from a function

A Go function can return multiple values, each separated by commas in the return statement.

```go
package main
import "fmt"
func foo() (string, string) {
   return "two", "values"
}
func main() {
   fmt.Println(foo())
}
```