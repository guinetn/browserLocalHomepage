# F#  #

Functional programming
Interop with C#, .NET
Use NuGet

## F# 1.0  #
## F# 2.0  #

## F# 3.0  #

## F# 4.0  #

## F# 5.0  #


### Variables
let numbers = [0 .. 10]
numbers
numbers.[3]
Take the numbers from 2nd index to the 5th
numbers.[2..5]    .[start .. end] to slice a subset of the data 

let s1 = "Hello"
let s2 = "World"
s1 + ", " + s2 + "!"
"""A triple-quoted string can contain quotes "like this" anywhere within it"""

(1, "fred", Math.PI)   Tuples
struct (1, Math.PI)    Struct tuples for performance

Record: combine different kinds of data into an aggregate. They cannot be null and come with default comparison and equality. Records are comparable and equatable:
type ContactCard =
    { Name: string
      Phone: string
      ZipCode: string }
// Create a new record
{ Name = "Alf"; Phone = "(555) 555-5555"; ZipCode = "90210" }
// . to access a record
let alf = { Name = "Alf"; Phone = "(555) 555-5555"; ZipCode = "90210" }
alf.Phone
let showContactCard contact = contact.Name + " - Phone: " + contact.Phone + ", Zip: " + contact.ZipCode
    showContactCard alf

### Data structures

* Arrays: are mutable
let firstTwoHundred = [| 1 .. 200 |]
firstTwoHundred.[197..]
// Filter the previous list of numbers and sum their squares.
firstTwoHundred |> Array.filter (fun x -> x % 3 = 0) |> Array.sumBy (fun x -> x * x)

* Lists: linear sequences of values of the same type
[0 .. 10]

let thisYear = DateTime.Now.Year
let fridays =
    [
        for month in 1 .. 10 do
            for day in 1 .. DateTime.DaysInMonth(thisYear, month) do
                let date = DateTime(thisYear, month, day)
                if date.DayOfWeek = DayOfWeek.Friday then
                    date.ToShortDateString()
    ]
// Get the first five fridays of this year
fridays |> List.take 5
fridays.[..4]    First five


### Functions
let sampleFunction x = 2*x*x - 5*x + 3             infered types
let sampleFunction' (x: int) = 2*x*x - 5*x + 3     figure out
sampleFunction 5
sampleFunction' 12

* Functions composition
let negate x = -x
let square x = x * x
let print x = printfn "The number is %d" x

let squareNegateThenPrint x = print (negate (square x))
squareNegateThenPrint 5

* Pipeline operator |>
let squareNegateThenPrint x = x |> square |> negate |> print
squareNegateThenPrint 5


Parallel Programming
#!time
let bigArray = [| 0 .. 100_000 |]
let rec fibonacci n = if n <= 2 then n else fibonacci (n-1) + fibonacci (n-2)
// We'll use the '%A' print formatter for F# constructs for these results, since they are enormous
let results =
    bigArray
    |> Array.Parallel.map (fun n -> fibonacci (n % 25))
printfn "%A" results
#!time
​

## more

- https://hub-binder.mybinder.ovh/user/dotnet-interactive-cb9ukwlm/lab/tree/fsharp/Introduction%20to%20F%23.ipynb