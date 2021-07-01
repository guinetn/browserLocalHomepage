# MS Unit Test / UnitTestFramework

    The Unit Testing Framework supports unit testing in Visual Studio
    http://msdn.microsoft.com/en-us/library/ms243147(v=vs.80)
    http://msdn.microsoft.com/en-US/library/ms182524(v=vs.80).aspx

## C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\ReferenceAssemblies\v4.0\Microsoft.VisualStudio.QualityTools.UnitTestFramework.dll


# To generate a unit test
# In Solution Explorer, right-click a test project → Add → Visual C# → Test → Unit Test Project
# Add reference  → solution  → add your project

# Skeleton auto-generated

    using System;
    using Microsoft.VisualStudio.TestTools.UnitTesting;
    using Trending;

    namespace MSTest
    {
        [TestClass]                    // Defines a testing class
        public class MSTestExample     // name, like any other class
        {
            [TestMethod]                          // this mark the method as a test
            public void Test_Trending_MSTest_OK() // method name, like any other
            {
                /*
                 * your test goes here.
                 */
            }
        }
    }

## ADD YOUR OWN TEST

        [TestMethod]               
        public void Test_Trending_MSTest_OK()
        {
            var result = TrendingRunner.WhatsTrending(1);
            Assert.AreEqual("Paul Walker", result);
        }

    EXECUTE TESTS
        Menu → Test → Run → All Tests (CTRL+R+A)


    UNITTESTING NAMESPACE
        http://msdn.microsoft.com/en-us/library/Microsoft.VisualStudio.TestTools.UnitTesting(v=vs.80).aspx
        http://msdn.microsoft.com/en-US/library/microsoft.visualstudio.testtools.unittesting.assert_members(v=vs.80).aspx

            AreEqual                Overloaded. Verifies that specified values are equal.  
            AreNotEqual             Overloaded. Verifies that specified values are not equal.  
            AreNotSame              Overloaded. Verifies that specified object variables refer to different objects.  
            AreSame                 Overloaded. Verifies that specified object variables refer to the same object.  
            Equals                  Overloaded. (Inherited from Object.)
            Fail                    Overloaded. Fails an assertion without checking any conditions.  
            Inconclusive            Overloaded. Indicates that an assertion cannot be proven true or false. Also used to indicate an assertion that has not yet been implemented.  
            IsFalse                 Overloaded. Verifies that a specified condition is false.  
            IsInstanceOfType        Overloaded. Verifies that a specified object is an instance of a specified type.  
            IsNotInstanceOfType     Overloaded. Verifies that a specified object is not an instance of a specified type.  
            IsNotNull               Overloaded. Verifies that a specified object is not a null reference (Nothing in Visual Basic).  
            IsNull                  Overloaded. Verifies that a specified object is null.  
            IsTrue                  Overloaded. Verifies that a specified condition is true.  

## SAMPLE

            A. PROJECT

            class Program
                {
                    static void Main(string[] args)
                    {
                        Console.WriteLine(sum(5, 7));
                        Console.WriteLine(mul(5, 7));
                        Console.ReadKey();
                    }

                    static int sum(int a, int b) { return a + b; }
                    static int mul(int a, int b) { return a * b; }
                }



            B. TEST PROJECT

            [TestClass()]
            public class ProgramTest
            {

            		// TEST ATTRIBUTES

            	    // Gets or sets the test context which provides information about and functionality for the current test run.
                    public TestContext TestContext
                    {
                        get { return testContextInstance;  }
                        set { testContextInstance = value; }
                    }

                    // Use ClassInitialize to run code before running the first test in the class
                    [ClassInitialize()]
                    public static void MyClassInitialize(TestContext testContext)
                    {
                    }        

                    // Use TestInitialize to run code before running each test
                    [TestInitialize()]
                    public void MyTestInitialize()
                    {
                    }

                    // Use ClassCleanup to run code after all tests in a class have run
                    [ClassCleanup()]
                    public static void MyClassCleanup()
                    {
                    }

                    // Use TestCleanup to run code after each test has run
                    [TestCleanup()]
                    public void MyTestCleanup()
                    {
                    }

                    // TESTS

                    [TestMethod()]
                    [DeploymentItem("Computer.exe")]
                    public void sumTest()
                    {
                        int a = 10; // Initialize to an appropriate value
                        int b = 2; 
                        int expected = 12; 
                        int actual = Program_Accessor.sum(a, b);
                        Assert.AreEqual(expected, actual);
                        //Assert.Inconclusive("Verify the correctness of this test method.");
                    }

            }

## FLUENT ASSERTIONS (BDD)

### NuGet package manager → "fluent assertions" (BDD)

        [TestMethod]
        public void Test_MSTest_Fluent_OK()
        {
            var result = TrendingRunner.WhatsTrending(1);
            result.Should().Be("Paul Walker");

            // another fluid assertion
            result.Should().NotBeEmpty("because it should have a value");
        }

        [TestMethod]
        public void Test_MSTest_Fluent_Fail()
        {
            var result = TrendingRunner.WhatsTrending(1);

            result.Should().Contain("Paul");     // Will pass
            result.Should().Be("Paul Talker");  // Will fail because of typo
        }




https://github.com/dotnet/samples/blob/master/csharp/unit-testing/MSTest.Project/ByAlphabeticalOrder.cs

    using Microsoft.VisualStudio.TestTools.UnitTesting;

    namespace MSTest.Project
    {
        [TestClass]
        public class ByAlphabeticalOrder
        {
            public static bool Test1Called;
            public static bool Test2Called;
            public static bool Test3Called;

            [TestMethod]
            public void Test2()
            {
                Test2Called = true;

                Assert.IsTrue(Test1Called);
                Assert.IsFalse(Test3Called);
            }

            [TestMethod]
            public void Test1()
            {
                Test1Called = true;

                Assert.IsFalse(Test2Called);
                Assert.IsFalse(Test3Called);
            }

            [TestMethod]
            public void Test3()
            {
                Test3Called = true;

                Assert.IsTrue(Test1Called);
                Assert.IsTrue(Test2Called);
            }
        }
    }        



