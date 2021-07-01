## inheritance 

There is no inheritance in Golang because it does not support classes.
Mimic inheritance behavior using composition to use an existing struct object to define a starting behavior of a new object. Once the new object is created, functionality can be extended beyond the original struct.

```go
type Animal struct {
    // …
}
func (a *Animal) Eat()   { … }
func (a *Animal) Sleep() { … }
func (a *Animal) Run() { … }

type Dog struct {
    Animal
    // …
}
```

Animal struct contains Eat(), Sleep(), and Run() functions.  
These functions are embedded into the child struct Dog by simply listing the struct at the top of the implementation of Dog.