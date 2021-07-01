## goroutine

Function/method that executes concurrently alongside any other goroutines using a special goroutine thread. Goroutine threads are more lightweight than standard threads, with most Golang programs using thousands of goroutines at once.

Create a goroutine, add the go keyword before the function declaration:  
go f(x, y, z)

You can stop a goroutine by sending it a signal channel. 
Goroutines can only respond to signals if told to check, so you’ll need to include checks in logical places such as at the top of your for loop.

```go
package main
func main() {
  quit := make(chan bool)
  go func() {
    for {
        select {
        case <-quit:
            return
        default:
            // …
        }
  }
}()
// …
quit <- true
}
```