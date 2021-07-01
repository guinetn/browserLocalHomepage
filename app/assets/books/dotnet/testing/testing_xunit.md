# XUnit

Tool for unit testing

- JUnit: Java
- PyUnit: Python
- PHPUnit: PHP
- xUnit.net (.NET Core / ASP.NET Core)

- https://xunit.github.io/docs/getting-started-dotnet-core
- https://andrewlock.net/creating-strongly-typed-xunit-theory-test-data-with-theorydata/
- https://github.com/dotnet/samples/tree/master/csharp/unit-testing/XUnit.TestProject

xUnit.net support for two different major types of unit tests: 

* Facts
are tests which are always true. They test invariant conditions. CodeLens add an icon 'test' near the method

```c#
using xUnit;
public class MyTests {
    [Fact]
    public void add(x,y) {
        Assert.True(true)
    }
    [Fact]
    public void add(x,y) {
        Assert.Throw<InvalidOperationException>(
            ()=> account.MakeWithDrawal(1000, DateTime.Now, "Attempt to overdraw"));
    }
}
```

```c#
public int Convert(string option)
{
   if (option == "No") return 0;
   else if (option == "Yes") return 1;
   else return -1;
}

[InlineData("No", 0)]
[InlineData("Yes", 1)]
[InlineData("Invalid", -1)]
public void VerifyConvert(string option, int expectedValue)
{
   var actualResult = Convert(option);
   Assert.Equal(expectedValue, actualResult);
}
```

* Theories
are tests which are only true for a particular set of data.


  [Theory]
  [InlineData("goodnight moon", "moon", true)]
  [InlineData("hello world", "hi", false)]
  public void Contains(string input, string sub, bool expected)
  {
      var actual = input.Contains(sub);
      Assert.Equal(expected, actual);
  }



  // figure out the minimal number of invocations to cover all possible combinations:
  [Theory, PairwiseData]
  public void CheckValidAge(bool p1, bool p2, bool p3)
      // Pairwise generates these 4 test cases:
      // false false false
      // false true  true
      // true  false true
      // true  true  false
  }





  using Xunit;

  namespace XUnit.Project
  {
      [TestCaseOrderer("XUnit.Project.Orderers.AlphabeticalOrderer", "XUnit.Project")]
      public class ByAlphabeticalOrder
      {
          public static bool Test1Called;
          public static bool Test2Called;
          public static bool Test3Called;

          [Fact]
          public void Test1()
          {
              Test1Called = true;

              Assert.False(Test2Called);
              Assert.False(Test3Called);
          }

          [Fact]
          public void Test2()
          {
              Test2Called = true;

              Assert.True(Test1Called);
              Assert.False(Test3Called);
          }

          [Fact]
          public void Test3()
          {
              Test3Called = true;

              Assert.True(Test1Called);
              Assert.True(Test2Called);
          }
      }
  }






# Strongly typed data with TheoryData
The TheoryData<> types provide a series of abstractions around the IEnumerable<object[]> required by theory tests. It consists of a TheoryData base class, and a number of generic derived classes TheoryData<>. The basic abstraction looks like the following:

public abstract class TheoryData : IEnumerable<object[]>
{
    readonly List<object[]> data = new List<object[]>();

    protected void AddRow(params object[] values)
    {
        data.Add(values);
    }

    public IEnumerator<object[]> GetEnumerator()
    {
        return data.GetEnumerator();
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}
This class implements IEnumerable<object[]> but it has no other public members. Instead, the generic derived classes TheoryData<> provide a public Add<T>() method, to ensure you can only add rows of the correct type. For example, the derived class with three generic arguments looks likes the following:

public class TheoryData<T1, T2, T3> : TheoryData
{
    /// <summary>
    /// Adds data to the theory data set.
    /// </summary>
    /// <param name="p1">The first data value.</param>
    /// <param name="p2">The second data value.</param>
    /// <param name="p3">The third data value.</param>
    public void Add(T1 p1, T2 p2, T3 p3)
    {
        AddRow(p1, p2, p3);
    }
}
This type just passes the generic arguments to the protected AddRow() command, but it enforces that the types are correct, as the code won't compile if you try and pass an incorrect parameter to the Add<T>() method.

Using TheoryData with the [ClassData] attribute
First, we'll look at how to use TheoryData<> with the [ClassData] attribute. You can apply the [ClassData] attribute to a theory test, and the referenced type will be used to load the data. In the previous post, the data class implemented IEnumerable<object[]>, but we can alternatively implement TheoryData<T1, T2, T3> to ensure all the types are correct, for example:

public class CalculatorTestData : TheoryData<int, int, int>
{
    public CalculatorTestData()
    {
        Add(1, 2, 3);
        Add(-4, -6, -10);
        Add(-2, 2, 0);
        Add(int.MinValue, -1, int.MaxValue);
        Add(1.5, 2.3m, "The value"); // will not compile!
    }
}
You can apply this to your theory test in exactly the same way as before, but this time you can be sure that every row will have the correct argument types:

[Theory]
[ClassData(typeof(CalculatorTestData))]
public void CanAdd(int value1, int value2, int expected)
{
    var calculator = new Calculator();
    var result = calculator.Add(value1, value2);
    Assert.Equal(expected, result);
}
The main thing to watch out for here is that that the CalculatorTestData implements the correct generic TheoryData<> - there's no compile time checking that you're referencing a TheoryData<int, int, int> instead of a TheoryData<string> for example.

Using TheoryData with the [MemberData] attribute
You can use TheoryData<> with [MemberData] attributes as well as [ClassData] attributes. Instead of referencing a static property that returns an IEnumerable<object[]>, you reference a property or method that returns a TheoryData<> object with the correct parameters.

For example, we can rewrite the Data property from the start of this post to use a TheoryData<int, int, int> object:

public static TheoryData<int, int, int> Data
{
    get
    {
        var data = new TheoryData<int, int, int>();
        data.Add(1, 2, 3);
        data.Add(-4, -6, -10 );
        data.Add( -2, 2, 0 );
        data.Add(int.MinValue, -1, int.MaxValue );
        data.Add( 1.5, 2.3m, "The value"); // won't compile
        return data;
    }
}
This is effectively identical to the original example, but the strongly typed TheoryData<> won't let us add invalid data.

That's pretty much all there is to it, but if the verbosity of that example bugs you, you can make use of collection initialisers and expression bodied members to give:

public static TheoryData<int, int, int> Data =>
    new TheoryData<int, int, int>
        {
            { 1, 2, 3 },
            { -4, -6, -10 },
            { -2, 2, 0 },
            { int.MinValue, -1, int.MaxValue }
        };
As with the [ClassData] attribute, you have to manually ensure that the TheoryData<> generic arguments match the theory test parameters they're used with, but at least you can be sure all of the rows in the IEnumerable<object[]> are consistent!

# Summary
<https://github.com/AArnott/Xunit.Combinatorial> a library that produces equivalent functionality to NUnit's [Values] attribute called Xunit.Combinatorial:
It allows you to specify parameter-level values:
[Theory, CombinatorialData]
public void CheckValidAge([CombinatorialValues(5, 18, 21, 25)] int age, bool friendlyOfficer)
{
    // This will run with all combinations:
    // 5  true
    // 18 true
    // 21 true
    // 25 true
    // 5  false
    // 18 false
    // 21 false
    // 25 false
}



// use of XUnit's TheoryData<,> generic types
// must be public & static for MemberDataAttr to use
public static TheoryData<int, bool, string> DataForTest1 = new TheoryData<int, bool, string> {
    { 1, true, "First" },
    { 2, false, "Second" },
    { 3, true, "Third" }
};

[Theory(DisplayName = "My First Test"), MemberData(nameof(DataForTest1))]
public void Test1(int valA, bool valB, string valC)
{
    Debug.WriteLine($"Running {nameof(Test1)} with values: {valA}, {valB} & {valC} ");
}






$ mkdir MyFirstUnitTests
$ cd MyFirstUnitTests
$ dotnet new classlib                                        ←  creates a .NET Standard class library
The template "Class library" was created successfully

Change .csproj to target dotnet core:

<Project Sdk="Microsoft.NET.Sdk">
    <PropertyGroup>
    <TargetFramework>netcoreapp2.1</TargetFramework>
    </PropertyGroup>
    <ItemGroup>
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="15.7.0" />
    <PackageReference Include="xunit" Version="2.3.1" />
    <PackageReference Include="xunit.runner.visualstudio" Version="2.3.1" />
    </ItemGroup>
</Project>

To run tests against multiple targets (we pluralize <TargetFramework> to <TargetFrameworks>):
    <PropertyGroup>
    <TargetFrameworks>net452;netcoreapp2.1</TargetFrameworks>
    </PropertyGroup>
    Since we changed the .csproj file, we need to remember to re-run '$dotnet restore' before trying to run our unit tests. 

    it's legal to have something like 
    <TargetFrameworks>net452;net461;net47;netcoreapp1.0;netcoreapp2.0;netcoreapp2.1</TargetFrameworks>

Test

class1.cs

    using Xunit;
    namespace MyFirstUnitTests
    {
        public class Class1
        {
            [Fact]
            public void PassingTest()
            {
                Assert.Equal(4, Add(2, 2));
            }

            [Fact]
            public void FailingTest()
            {
                Assert.Equal(5, Add(2, 2));
            }

            int Add(int x, int y)
            {
                return x + y;
            }

            [Theory]
            [InlineData(3)]
            [InlineData(5)]
            [InlineData(6)]                         ← this test will fail
            [InlineData(int.MinValue, -1, int.MaxValue)]
            public void MyFirstTheory(int value)
            {
                Assert.True(IsOdd(value));
            }

            bool IsOdd(int value)
            {
                return value % 2 == 1;
            }
        }
    }

$ dotnet test
    Build started, please wait...
    Build completed.

# Running tests with Visual Studio

If you're having problems discovering or running tests, you may be a victim of a corrupted runner cache inside Visual Studio. 
To clear this cache
• shut down all instances of Visual Studio
• delete the folder %TEMP%\VisualStudioTestExplorerExtensions
Also make sure your solution is only linked against a single version of the Visual Studio runner NuGet package (xunit.runner.visualstudio).

You can run your xUnit.net tests within Visual Studio's built-in test runner (named Test Explorer)
Test > Windows > Test Explorer
Click the 'Run All'














# SAMPLES


[Theory]
[InlineData("goodnight moon", "moon", true)]
[InlineData("hello world", "hi", false)]
public void Contains(string input, string sub, bool expected)
{
var actual = input.Contains(sub);
Assert.Equal(expected, actual);
}



// figure out the minimal number of invocations to cover all possible combinations:
[Theory, PairwiseData]
public void CheckValidAge(bool p1, bool p2, bool p3)
{
// Pairwise generates these 4 test cases:
// false false false
// false true  true
// true  false true
// true  true  false
}



<https://github.com/AArnott/Xunit.Combinatorial> a library that produces equivalent functionality to NUnit's [Values] attribute called Xunit.Combinatorial:
# It allows you to specify parameter-level values:
[Theory, CombinatorialData]
public void CheckValidAge([CombinatorialValues(5, 18, 21, 25)] int age, bool friendlyOfficer)
{
// This will run with all combinations:
// 5  true
// 18 true
// 21 true
// 25 true
// 5  false
// 18 false
// 21 false
// 25 false
}



// use of XUnit's TheoryData<,> generic types
// must be public & static for MemberDataAttr to use
public static TheoryData<int, bool, string> DataForTest1 = new TheoryData<int, bool, string> {
{ 1, true, "First" },
{ 2, false, "Second" },
{ 3, true, "Third" }
};

[Theory(DisplayName = "My First Test"), MemberData(nameof(DataForTest1))]
public void Test1(int valA, bool valB, string valC)
{
Debug.WriteLine($"Running {nameof(Test1)} with values: {valA}, {valB} & {valC} ");
}





Package (xunit) is what's called a meta-package:
packages.config
<?xml version="1.0" encoding="utf-8"?>
<packages>
    <package id="xunit" version="2.2.0" targetFramework="net452" />
    <package id="xunit.abstractions" version="2.0.1" targetFramework="net452" />
    <package id="xunit.assert" version="2.2.0" targetFramework="net452" />
    <package id="xunit.core" version="2.2.0" targetFramework="net452" />
    <package id="xunit.extensibility.core" version="2.2.0" targetFramework="net452" />
    <package id="xunit.extensibility.execution" version="2.2.0" targetFramework="net452" />
</packages>

Facts       are tests which are always true. They test invariant conditions.
Theories    are tests which are only true for a particular set of data.

[Theory]
[InlineData(3)]
[InlineData(5)]
[InlineData(6)]
public void MyFirstTheory(int value) {Assert.True(IsOdd(value)); }
bool IsOdd(int value) {return value % 2 == 1; }

Running tests with Visual Studio: 
    Manage NuGet Packages → install a package named "xunit.runner.visualstudio"
    Then you can see tests in VS

[Theory(Skip = "cause build fail")]     to skip a test...


https://xunit.github.io/
https://xunit.github.io/docs/getting-started-desktop.html
works:
D:\vsts-agent\_work\7\s\packages\xunit.runner.console\tools\xunit.console.exe D:\vsts-agent\_work\7\s\tests\Business.Tests.dll D:\vsts-agent\_work\7\s\tests\Domain.Tests.BDD.dll D:\vsts-agent\_work\7\s\tests\Domain.Tests.dll D:\vsts-agent\_work\7\s\tests\Domain.Tests.Lan.dll D:\vsts-agent\_work\7\s\tests\OndeoSystems.Tests.dll D:\vsts-agent\_work\7\s\tests\Services.Tests.BDD.dll D:\vsts-agent\_work\7\s\tests\Services.Tests.dll -nologo -parallel none -noshadow -xml D:\vsts-agent\_work\7\s\tests\xunit.xml
D:\vsts-agent\_work\7\s\packages\xunit.runner.console\tools\xunit.console.exe D:\vsts-agent\_work\7\s\tests\OndeoSystems.Tests.dll -nologo -parallel none -noshadow -xml D:\vsts-agent\_work\7\s\tests\xunit.xml


Error build:
    Tests.TeleoperationServices.ReferentGatewayServiceTest.TestGetReferentGateway [FAIL]
        System.IO.FileLoadException : Could not load file or assembly 'FakeItEasy, Version=4.0.0.0, Culture=neutral, PublicKeyToken=eff28e2146d5fd2c' or one of its dependencies. The located assembly's manifest definition does not match the assembly reference. (Exception from HRESULT: 0x80131040)
Fix:
    2 project use 2 differents fakeiteasy.dll causing conflict because only one is used in "D:\vsts-agent\_work\7\s\tests"

https://www.hanselman.com/blog/ReferencingNETStandardAssembliesFromBothNETCoreAndNETFramework.aspx
Can't load Could not load file or assembly 'Microsoft.EntityFrameworkCore, Version=2.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60'or one of its dependencies. The system cannot find the file specified.



    <package id="FakeItEasy" version="4.0.0" targetFramework="net452" />
    <package id="FsCheck" version="2.9.0" targetFramework="net452" />
    <package id="FsCheck.Xunit" version="2.9.0" targetFramework="net452" />
    <package id="FSharp.Core" version="4.2.2" targetFramework="net452" />
    <package id="NLog" version="4.4.12" targetFramework="net452" />
    <package id="System.ValueTuple" version="4.4.0" targetFramework="net452" />
    <package id="xunit" version="2.2.0" targetFramework="net452" />
    <package id="xunit.abstractions" version="2.0.1" targetFramework="net452" />
    <package id="xunit.assert" version="2.2.0" targetFramework="net452" />
    <package id="xunit.core" version="2.2.0" targetFramework="net452" />
    <package id="xunit.extensibility.core" version="2.2.0" targetFramework="net452" />
    <package id="xunit.extensibility.execution" version="2.2.0" targetFramework="net452" />
    <package id="xunit.runner.console" version="2.2.0" targetFramework="net452" developmentDependency="true" />
    <package id="xunit.runner.visualstudio" version="2.2.0" targetFramework="net452" developmentDependency="true" />





    Other troubleshooting tools and techniques

## You may use a tracing application such as Process Monitor from SysInternals to monitor file activity in your system. This should give you an idea of what files are being read and written and their exact locations.

Process Explorer is another indispensable utility which can help with investigation of various system-level issues, such as permissions, threading, deadlocks, performance, etc.