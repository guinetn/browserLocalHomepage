## TYPES

Method
Boolean
Numeric
String
Array
Slice
Struct
Pointer
Function
Interface
Map
Channel
Rune. handle both slices and strings. Runes are Unicode code points and can therefore parse strings and slices equally.

### Conversions

i := 55      //int
j := 67.8    //float64
sum := i + int(j) //j is converted to int

### check type

Type Switch 
- to check a variable’s type at runtime. 
- evaluates variables by type rather than value
Each Switch contains at least one case, which acts as a conditional statement, and a default case, which executes if none of the cases are true.
For example, you could create a Type Switch that checks if the interface value i contains the type int or string:

```go
package main
import "fmt"
func do(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Printf("Double %v is %v\n", v, v*2)
    case string:
        fmt.Printf("%q is %v bytes long\n", v, len(v))
    default:
        fmt.Printf("I don't know  type %T!\n", v)
    }
}
func main() {
    do(21)
    do("hello")
    do(true)
}
```


### concatenate strings

```go
package main
import "fmt"
func main() { 
    
    // Creating and initializing strings using var keyword 
    var str1 string 
    str1 = "Hello "
    var str2 string 
    str2 = "Reader!"
    
    // Using + operator 
    fmt.Println("New string 1: ", str1+str2) 
    
    // Creating and initializing strings using shorthand declaration 
    str3 := "Welcome"
    str4 := "Educative.io"
    
    // Concatenating strings Using + operator 
    result := str3 + " to " + str4 
    fmt.Println("New string 2: ", result) 
}
```


## Lvalue / Rvalue

* Lvalue
Refers to a memory location
Represents a variable identifier
Mutable
May appear on the left or right side of the = operator
For example, in the statement x =20, x is an lvalue and 20 is an rvalue.

* Rvalue
Represents a data value stored in memory
Represents a constant value
Always appears on the = operator's right side.

For example, the statement 10 = 20 is invalid because there is an rvalue (10) left of the = operator.