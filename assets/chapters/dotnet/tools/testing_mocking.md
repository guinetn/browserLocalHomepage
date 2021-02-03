# Mocking

## nsubstitute
.NET mocking libraries
Succinct syntax
https://nsubstitute.github.io/

>Install-Package NSubstitute

Optional packages to help detect potential misuses of the NSubstitute API:
> Install-Package NSubstitute.Analyzers.CSharp

```c#

public interface ICalculator
{
    int Add(int a, int b);
    string Mode { get; set; }
    event EventHandler PoweringUp;
}

//Create:
var calculator = Substitute.For<ICalculator>();

//Set a return value:
calculator.Add(1, 2).Returns(3);
Assert.AreEqual(3, calculator.Add(1, 2));

//Check received calls:
calculator.Received().Add(1, Arg.Any<int>());
calculator.DidNotReceive().Add(2, 2);

//Raise events
calculator.PoweringUp += Raise.Event();
```

Helpful exceptions
ReceivedCallsException : Expected to receive a call matching:
Add(1, 2)
Actually received no matching calls.
Received 2 non-matching calls (non-matching arguments indicated with '*' characters):
Add(*4*, *7*)
Add(1, *5*)