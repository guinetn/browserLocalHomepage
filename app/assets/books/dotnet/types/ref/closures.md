## Closures

Provide a context for a function which can be used to provide it with additional information without the need to use additional parameters (because function signature isn’t under your control)

Special functions that 'remember/are linked' the environment in which they were created.
Preserve state; hence the name closure - it closes over state
Allow to access variables that would otherwise be out of scope

This allows closure functions to use variables from that referencing environment, despite these values not being within the closure's scope.
When the function is created, the external variables that it uses are "closed over", meaning that they are bound to the closure function in a way that makes them accessible. Often this means that copies of their values are made when the closure is defined.

C# closures are created using anonymous methods or lambda expressions

```cs
int nonLocal = 1;
Action closure = delegate { Console.WriteLine("{0} + 1 = {1}", nonLocal, nonLocal + 1); };
closure();  // 1 + 1 = 2
```

```cs
MyHelloDelegateType1[] Count = new MyHelloDelegateType1[10];
for(int i=0;i<10;i++)
 Count[i] = ()=> { MessageBox.Show(i.ToString()); };
Displays the value 10 for each delegate

MyHelloDelegateType1[] Count=new
MyHelloDelegateType1[10];
for(int i=0;i<10;i++)
{
  // j is recreated each time through the loop and each delegate captures its own copy  
  int j = i;
  Count[i] = delegate() { MessageBox.Show(j.ToString()); };
};
```

Calling each delegate in turn will displays 0,1,2... reflecting the value of i at the time the delegate was created.
j is out of scope when the loop ends so you can’t discover what its current value is – only the captured copies survive the loop

### Use #1 - No control

### Use #2 - Event pattern

In an event oriented environment the linear flow of actions is often made unclear by the need to pause processing until an event occurs


```cs
using System;
class Test
{
    static void Main()
    {
        Action action = CreateAction();
        action();
        action();
    }

    static Action CreateAction()
    {
        int counter = 0;
        return delegate
        {
            // Yes, it could be done in one statement;
            // but it is clearer like this.
            counter++;
            Console.WriteLine("counter={0}", counter);
        };
    }
}
```
Action returned by CreateAction still has access to the counter variable, and can indeed increment it, even though CreateAction itself has finished.

## Closures and Out-Of-Scope Variables

```cs
class Program
{
    static Action _closure;
    
    static void Main(string[] args)
    {
        SetUpClosure();
        _closure();     // 1 + 1 = 2
    }
    
    private static void SetUpClosure()
    {
        int nonLocal = 1;
        _closure = () =>
        {
            Console.WriteLine("{0} + 1 = {1}", nonLocal, nonLocal + 1);
        };
    }
}
```

The "nonLocal" variable was captured, or "closed over", by the delegate code, causing it to remain in scope beyond the normal limits. In fact, it will remain available until the no further references to the delegate remain.				

## JS CLOSURE

```js
function getEmployeeFactory() {
  let employeeNumber = 1;
  return function(name, country) {
    return { employeeNumber: employeeNumber++, name, country };
  };
}
 
const getEmployee = getEmployeeFactory();
 
const employeeOne = getEmployee('Robin', 'Germany');
const employeeTwo = getEmployee('Markus', 'Canada');
 
const employees = [employeeOne, employeeTwo];
 
console.log(employees);
 
// [
//   { employeeNumber: 1, name: 'Robin', country: 'Germany' },
//   { employeeNumber: 2, name: 'Markus', country: 'Canada' },
// ]
```

## More

- http://www.blackwasp.co.uk/CSharpClosures.aspx
- [Closures in C# and why you NEED to know about them](https://www.youtube.com/watch?v=h3MsnBRqzcY)
When it comes time to optimize your code for memory allocations, closures tend to be the usual suspect for a big chunck of your allocated memory.