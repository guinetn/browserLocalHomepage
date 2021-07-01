# NUnit

Unit-testing framework for all .Net languages
https://nunit.org/
https://github.com/nunit/nunit-csharp-samples

NUnit features 
- "fluent assertions" syntax (BDD, assert=affirmation) 
- parameterized, generic and theory tests
- user-extensible test
- number of runners 

## Install
Via NuGet: Tools -> Library Package Manager -> Manage NuGet Packages
Install-Package NUnit
Install-Package NUnitLite

Install the "NUnit Test Adapter" extension to run NUnit tests inside Visual Studio
## Configure

<ItemGroup>
  <PackageReference Include="Microsoft.NET.Test.Sdk" Version="15.5.0" />
  <PackageReference Include="NUnit" Version="3.9.0" />
  <PackageReference Include="NUnit3TestAdapter" Version="3.9.0" />
</ItemGroup>

## Execute NUnit tests
Number of runners from 
- NUnit project
- Third parties

1. .NET Core CLI test command
> dotnet test .\test\NetCore10Tests\NetCore10Tests.csproj

2. NUnit Console   
nunit-console.exe   
fast, non interactive

3. NUnit GUI
nunit.exe          
select tests to runs, graphical feedback

4. Visual Studio


## SAMPLES

```cs
public class Rectangle
{
    protected int _width;
    protected int _height;
    public int Width  { get { return _width; }    }
    public int Height { get { return _height; }   }

    public virtual void SetWidth(int width)
    { _width = width;  }

    public virtual void SetHeight(int height)
    { _height = height; }
}

public class Square: Rectangle
{
    public override void SetWidth(int width)
    {  _width = width;
        _height = width;
    }

    public override void SetHeight(int height)
    {
        _height = height;
        _width = height;
    }
}


[TestFixture]
public class RectangleTests
{
    [Test]
    public void AreaOfRectangle()
    {
        Rectangle r = new Square();
        r.SetWidth(5);
        r.SetHeight(2);

        // Will Fail – r is a square and sets width and height equal to each other.
        Assert.IsEqual(r.Width * r.Height,10);
    }
}
```

## QUICK START (is not a good example of Test-Driven Development)

1. WRITE YOUR BUSINESS CLASS

```cs
namespace Bank
{
  public class InsufficientFundsException : ApplicationException
  {
  }

  public class Account
  {
    private decimal balance;
    public decimal Balance        {  get { return balance; }     }
    private decimal minimumBalance = 10m;
    public decimal MinimumBalance {  get{ return minimumBalance; }

    public void Deposit(decimal amount)   {     balance += amount;   }
    public void Withdraw(decimal amount)   {   balance -= amount;    }
    public void TransferFunds(Account destination, decimal amount)
    {       
      if(balance-amount < minimumBalance)
        throw new InsufficientFundsException();
      destination.Deposit(amount);
      Withdraw(amount);
    }
  }
}
```

2. WRITE A TEST FOR THIS CLASS

```cs
namespace Bank
{
  using NUnit.Framework;

  [TestFixture]                     Indicate that the class contains test code (fixture=fixation,installation)
  public class AccountTest          The class . must be public (no restrictions on its superclass)
  {                                           . has to have a default constructor.  
    Account source, destination;

    [SetUp]                         Common initialization code. void+parameterless
    public void Init()
    {
      source = new Account();         init  test objects  
      source.Deposit(200m);           execute business methods

      destination = new Account();
      destination.Deposit(150m);
    }

    [Test]                          Indicate that it is a test method (void+parameterless)
    public void TransferFunds()
    {
      source.TransferFunds(destination, 100m);

                                  Check the state of the business objects   
                                  Assert class has a collection of methods used to check post-conditions

      Assert.AreEqual(250m, destination.Balance);
      Assert.AreEqual(100m, source.Balance);
    }

    [Test]
    [ExpectedException(typeof(InsufficientFundsException))]   indicate the test is expecting an exception of a certain type
    public void TransferWithInsufficientFunds()               Test will fail if not thrown 
    {
      source.TransferFunds(destination, 300m);
    }

    [Test]
    [Ignore("Decide how to implement transaction management")]    temporarily ignore this test
    public void TransferWithInsufficientFundsAtomicity()          Displayed in “Tests Not Run”
    {
      try
      {
        source.TransferFunds(destination, 300m);
      }
      catch(InsufficientFundsException expected)
      {
      }

      Assert.AreEqual(200m, source.Balance);
      Assert.AreEqual(150m, destination.Balance);
    }
  }
}
```


3. EXECUTE TESTS

* Start the NUnit Gui
* File->Open -> bank.dll
  you will see a test tree structure in the left panel and a collection of status panels on the right
* Click the Run button
“Errors and Failures” panel says
    TransferFunds : expected <250> but was <150>
Fix...
  public void TransferFunds(Account destination, decimal amount)
  {
      destination.Deposit(amount);
      Withdraw(amount);
  }


## TIPS

A. The benefit in using NUnit is having multiple tests under the same Test method.

  [TestMethod]               
  public void Test_Trending()
  {
      var result = TrendingRunner.WhatsTrending(1);
      Assert.AreEqual("Paul Walker", result);

      result = TrendingRunner.WhatsTrending(2);
      Assert.AreEqual("Cory Monteith", result);

      result = TrendingRunner.WhatsTrending(3);
      Assert.AreEqual("RoyalBaby", result);
  }

  Purists will say you should only have 1 assert per test: ignore, them, or break our tests into three methods, 
  and this is where things start to get ugly, and repetitions

* NUnit #1

    public class NUnitTest
    {
        [TestCase]                  // this mark the method as a test in Nunit
        public void Test_Trending()
        {
            var result = TrendingRunner.WhatsTrending(1);
            Assert.AreEqual("Paul Walker", result);
        }
    }

* NUnit #2 - test is called three times, with different parameters

    [TestCase(1, Result = "Paul Walker")]
    [TestCase(2, Result = "Cory Monteith")]
    [TestCase(3, Result = "RoyalBaby")]
    public string Test_Trending(int anIndex)
    {
        return TrendingRunner.WhatsTrending(anIndex);
    }

    // More details?
    var result = TrendingRunner.WhatsTrending(anIndex);
    Console.Out.WriteLine("Call \t-> \tresult :\r\n  {0} \t-> \t\"{1}\"", anIndex, result );
    return result;

B. FLUENT ASSERTIONS (BDD)

  http://www.codeproject.com/Articles/784791/Introduction-to-Unit-Testing-with-MS-tests-NUnit-a

  [TestCase]
  public void Test_MSTest_Fluent_OK()
  {
      var result = TrendingRunner.WhatsTrending(1);
      result.Should().Be("Paul Walker");

      // another fluid assertion
      result.Should().NotBeEmpty("because it should have a value");
  }

  [TestCase]
  public void Test_MSTest_Fluent_Fail()
  {
      var result = TrendingRunner.WhatsTrending(1);

      result.Should().Contain("Paul");     // Will pass
      result.Should().Be("Paul Talker");  // Will fail because of typo
  }




https://github.com/dotnet/samples/blob/master/csharp/unit-testing/NUnit.TestProject/ByOrder.cs

using NUnit.Framework;

namespace NUnit.Project
{
    public class ByOrder
    {
        public static bool Test1Called;
        public static bool Test2ACalled;
        public static bool Test2BCalled;
        public static bool Test3Called;

        [Test, Order(5)]
        public void Test1()
        {
            Test3Called = true;

            Assert.IsTrue(Test1Called);
            Assert.IsFalse(Test2ACalled);
            Assert.IsTrue(Test2BCalled);
        }

        [Test, Order(0)]
        public void Test2B()
        {
            Test2BCalled = true;

            Assert.IsTrue(Test1Called);
            Assert.IsFalse(Test2ACalled);
            Assert.IsFalse(Test3Called);
        }

        [Test]
        public void Test2A()
        {
            Test2ACalled = true;

            Assert.IsTrue(Test1Called);
            Assert.IsTrue(Test2BCalled);
            Assert.IsTrue(Test3Called);
        }

        [Test, Order(-5)]
        public void Test3()
        {
            Test1Called = true;

            Assert.IsFalse(Test2ACalled);
            Assert.IsFalse(Test2BCalled);
            Assert.IsFalse(Test3Called);
        }
    }
}      



