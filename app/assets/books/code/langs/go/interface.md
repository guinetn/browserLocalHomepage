## Go Interfaces

Special Go type  
Define a set of method signatures but do not provide implementations.   
Values of type interface can hold any value that implements those methods.

Interfaces essentially act as placeholders for methods that will have multiple implementations based on what object is using them.

For example, you could implement a geometry interface that defines that all shapes that use this interface must have an implementation of area() and perim().

```go
type geometry interface {
    area() float64
    perim() float64
}
```