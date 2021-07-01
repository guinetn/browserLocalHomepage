## Covariance / Contravariance

.NET 4.0 feature
Covariance and contravariance allow us to be flexible when dealing with class hierarchy.

```cs
// Contravariance (applied to parameters): Enables to use a more generic (less derived) type than originally specified
Action<object> broadAction = (object data) => { Console.WriteLine(data); };
Action<string> narrowAction = broadAction;

// Covariance: use a more derived type than originally specified
Func<string> narrowFunction = () => Console.ReadLine();
Func<object> broadFunction = narrowFunction;

// Contravariance and covariance combined
Func<object, string?> func1 = (object data) => data.ToString();
Func<string, object?> func2 = func1;
```



Implicit reference conversion for array types, delegate types, generic type arguments
Covariance preserves assignment compatibility and contravariance reverses it.

Covariance and contravariance are terms that refer to the ability to use a more derived type (more specific) or a less derived type (less specific) than originally specified. Generic type parameters support covariance and contravariance to provide greater flexibility in assigning and using generic types.
Covariance and contravariance provide flexibility for matching a delegate type with a method signature.

Assume a base class named Base and a derived class named Derived.

* Invariance (before .Net 4)
Means that you can use only the type originally specified; so an invariant generic type parameter is neither covariant nor contravariant.
You cannot assign an instance of List<Base> to a variable of type List<Derived> or vice versa.

* Covariance
Covariance permits a method to have a return type that is more derived than that defined in the delegate. 
Enables you to use a more derived type than originally specified.
You can assign an instance of IEnumerable<Derived> to a variable of type IEnumerable<Base>
IEnumerable<Derived> d = new List<Derived>();
IEnumerable<Base> b = d;

* Contravariance
permits a method that has parameter types that are less derived than those in the delegate type.
Enables you to use a more generic (less derived) type than originally specified.
You can assign an instance of Action<Base> to a variable of type Action<Derived>

Action<Base> b = (target) => { Console.WriteLine(target.GetType().Name); };
Action<Derived> d = b;
d(new Derived());




 	MIX COVARIANCE / CONTRAVARIANCE

 		public delegate TResult Func<in T, out TResult>(T args);

 		Func<object, string> f1 = s=>s.ToString();
 		Func<string, object> f2 = s=>s.ToString();


## Sample 

```xml
<?xml version="1.0" encoding="utf-8" ?>
<root>
  <!-- comment 1 -->
  <foo>foo 1</foo>
  <bar>bar 1</bar>
  <!-- comment 2 -->
  <foo>foo 2</foo>
  <bar>2</bar>
  <!-- comment 3 -->
</root>

Transform to (all 'bar' child elements of 'root' node have been removed)

<?xml version="1.0" encoding="utf-8" ?>
<root>
  <!-- comment 1 -->
  <foo>foo 1</foo>
  <!-- comment 2 -->
  <foo>foo 2</foo>
  <!-- comment 3 -->
</root>
```

```cs
XDocument doc1 = XDocument.Load(@"XMLFile1.xml");
XDocument doc2 = new XDocument(
    new XElement(doc1.Root.Name, 
                 doc1.Root.Nodes().Except(doc1.Root.Elements("bar").Cast<XNode>())));
doc2.Save(Console.Out);
```

***Before .Net 4.0, generic interfaces were invariant:***
Inheritance: Object → XObject → XNode → XContainer → XElement
***Error: Cannot convert 
    from 'System.Collections.Generic.IEnumerable<System.Xml.Linq.XElement>' 
    to   'System.Collections.Generic.IEnumerable<System.Xml.Linq.XNode>'***
Reason:                 
- Nodes() returns an IEnumerable<XNode> 
- Except() needs an IEnumerable<XNode>
- Elements("bar") gives IEnumerable<XElement>
With generic interfaces being invariant in .NET 3.5 we can't pass that IEnumerable<XElement> in for an IEnumerable<XNode>, although XElement is a class derived from XNode.
It seems desirable that you would not need that Cast<XNode>() call.

Starting with .NET 4.0 the type parameter T of IEnumerable<T> is covariant meaning where an IEnumerable<T> of a certain type T is expected we can always pass in an IEnumerable<T2> where T2 is type derived from T, as in our example where XElement is a subclass of XNode (or subsubclass to be precise).
Thus with .NET 4.0 the following compiles and works fine:
XDocument doc2 = new XDocument(
    new XElement(doc1.Root.Name, 
                 doc1.Root.Nodes().Except(doc1.Root.Elements("bar")));
                 
## Variance modifiers: out, in

|                |     INVARIANCE     |     COVARIANCE      |   CONTRAVARIANCE  |
|----------------|--------------------|---------------------|-------------------|
|                |                    |         A → B       |         A → B     |   
|                |                    |      T<A> ← T<B>    |      T<A> → T<B>  |   
|                |    class Box<T>    |    class Box<out T> |   class Box<in T> |   
|    Number      |    Box<Number>     |      Box<Number>    |     Box<Number>   |
|      ↑         |       ↑✘↓          |          ↑          |         ↓         |  
|     int        |    Box<int>        |       Box<int>      |      Box<int>     | 

Number is derived from int
 
### Covariance  A → B  =>  T<A> ← T<B>
Method can have more derived return type 
Allow to pass a derived type where a base type is expected
Covariance can be applied on delegate, generic, array, interface, etc.
You can use either the type you specified or any type that is more derived

Variance: Base class and other derived classes are considered to be the same kind of class that adds extra functionalities to the base type. So covariance allows you to use a derived class where a base class is expected (rule: can accept big if small is expected).

'out' word allow generic covariance
object ← string
List<object> ← List<string>


interface IElement<out T> {}
class Elements<T>: IElement<T> {}
class a {}
class b:a {}

IElement<b> bs = new Elements<b>();
IElement<a> as = bs;
IElement<object> o = bs;   // covariance: a ← b   List<a> ← List<b>

In C# 4.0, interface IEnumerable<T>  is changed to interface IEnumerable<out T> to allow
List<string> sl = new List<string>();
List<object> ol = sl;


class GrandFather {}
class      Son : GrandFather {}
class GrandSon : GrandFather {}

GrandFather father = new Son();
father   = new GrandSon();
IEnumerable<GrandFather> fathers = new List<Son>();		► will throw exception prior to version 4.0
                                                            isn’t it somehow violate polymorphism :)
                                                            
                                                            
                                                                  
                                                                  
IEnumerable<T> is covariant: where IEnumerable<T> is expected we can always pass in IEnumerable<T2> where T2 is type derived from T
 
Covariance for arrays enables implicit conversion of an array of a more derived type to an array of a less derived type. But this operation is not type safe:
```cs
object[] array = new String[10];  
array[0] = 10; // run-time exception: implicit conversionnot type safe operation  
```

```cs
IEnumerable<string> strings = new List<string>();  
// An object that is instantiated with a more derived type argument
// is assigned to an object instantiated with a less derived type argument.
// Assignment compatibility is preserved.
IEnumerable<object> objects = strings;  
```

```cs
class Cells {}  
class Human : Cells {}  
  
class Program  
{  
    // Define the delegate.  
    public delegate Cells HandlerMethod();  
  
    public static Cells CellsHandler()  
    {  
        return null;  
    }  
  
    public static Human HumanHandler()  
    {  
        return null;  
    }  
  
    static void Test()  
    {  
        HandlerMethod handlerCells = CellsHandler;  
  
        // Covariance enables this assignment.  
        HandlerMethod handlerHuman = HumanHandler;  
    }  
}  
```


delegate expects a return type of small (base class) but we can still assign Method1 that returns Big (derived class) and also Method2 that has same signature as delegate expects.
Thus, covariance allows you to assign a method to the delegate that has a less derived return type.
```cs

public class Small { }
public class Big: Small { }
public class Bigger : Big { }

public delegate Small covarDel(Big mc);

public class Program
{
    public static Big Method1(Big bg)
    {
        Console.WriteLine("Method1");    
        return new Big();
    }
    public static Small Method2(Big bg)
    {
        Console.WriteLine("Method2");    
        return new Small();
    }
        
    public static void Main(string[] args)
    {
        // A base class can hold a derived class 
        Small s1 = new Small();
        Small s2 = new Big();
        Small s3 = new Bigger();
        // But a derived class cannot hold a base class
        Big b1 = new Bigger();
        Big b2 = new Small(); // ERROR
        
        covarDel del = Method1;
        Small sm1 = del(new Big());
        del= Method2;
        Small sm2 = del(new Big());
    }
}
```


### Contravariance  A → B  =>  T<A> → T<B>
Contravariane is applied to parameters
Method can have less derived parameter types  
Allows a method with the parameter of a base class to be assigned to a delegate that expects the parameter of a derived class.

'in' word allow generic contravariance (works on parameters)
object ← string
List<object> → List<string>

                 
Like variance, contravariance methods that have parameters of a type that are base types of the delegate signature parameter type.

```cs
// Event handler that accepts a parameter of the EventArgs type.  
private void MultiHandler(object sender, System.EventArgs e)  
{  
    label1.Text = System.DateTime.Now.ToString();  
}  
  
public Form1()  
{  
    InitializeComponent();  
  
    // You can use a method that has an EventArgs parameter,  
    // although the event expects the KeyEventArgs parameter.  
    this.button1.KeyDown += this.MultiHandler;  
  
    // You can use the same method
    // for an event that expects the MouseEventArgs parameter.  
    this.button1.MouseClick += this.MultiHandler;  
  
}  
```
 
Method3 has a parameter of Small class whereas delegate expects a parameter of Big class. 
Still, you can use Method3 with the delegate. 
```cs
delegate Small covarDel(Big mc);

class Program
{
    static Big Method1(Big bg)
    {
        Console.WriteLine("Method1");
        return new Big();
    }
    static Small Method2(Big bg)
    {
        Console.WriteLine("Method2");
        return new Small();
    }

    static Small Method3(Small sml)
    {
        Console.WriteLine("Method3");
        
        return new Small();
    }
    static void Main(string[] args)
    {
        covarDel del = Method1;
        del += Method2;
        del += Method3;

        Small sm = del(new Big());
}
```

Covariance and Contravariance
```cs
delegate Small covarDel(Big mc);

class Program
{

    static Big Method4(Small sml)
    {
        Console.WriteLine("Method3");
    
        return new Big();
    }

    static void Main(string[] args)
    {
        covarDel del = Method4;
    
        Small sm = del(new Big());
    }
}
```




Delegates have two more important concepts:
Covariance
Contravariance
A delegate can refer to a method with the same return type and signature, however, variance eases this requirement. 
Covariance and contravariance provide flexibility for matching a delegate type with a method signature.
Covariance permits a method to have a return type that is more derived than that defined in the delegate. 
                    an IEnumerable<T> of a certain type T is expected we can always pass in an IEnumerable<T2> where T2 is type derived from T
Contravariance permits a method that has parameter types that are less derived than those in the delegate type.

	public class Animal
    {
        protected int age;
        protected void displayAge(int age)
        {
            this.age = age;
            Console.WriteLine(this.age);
        }
    }
    public class Dog : Animal
    {
        public string color;
        public void displayColor()
        {
            displayAge(99);
            Console.WriteLine(this.color);
        }
    }
}

The Dog class inherits the Animal class. So using covariance, a delegate with type Animal can refer to the Dog type. 
We are creating a delegate with return type of Animal and assigning a reference of Dog type below
This is possible due to the covariance feature of delegates.

public delegate Animal AnimalDelegate();
static void Main(string[] args)
{
    AnimalDelegate an = newDog;
    an();
    Console.ReadKey(true);
}
static Dog newDog()
{
    Dog d = new Dog();
    d.color = "white";
    d.displayColor();
    return d;
}


 
 
 ## More
 
- https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance
- http://www.tutorialsteacher.com/csharp/csharp-covariance-and-contravariance
- http://zetcode.com/lang/csharp/csharp4/
- https://www.i-programmer.info/programming/other-languages/12478.html








Next we come to the question of whether an array, considered as a transformation on the type of its element, is covariant, contravariant or invariant.

    Array<Int>: Array<Object>    derived class (make Array covariant)
    Array<Object> : Array<Int>   super class (make Array contravariant)
    Array<Int> has no relationship with Array<Object> (make Array invariant)


    in and out modifiers
         Allow you to mark type parameters as contravariant or covariant

	Covariance enables you to pass a derived type where a base type is expected. Co-variance is like variance of the same kind. 
	The base class and other derived classes are considered to be the same kind of class that adds extra functionalities to the base type. 
	So covariance allows you to use a derived class where a base class is expected (rule: can accept big if small is expected).
	Covariance can be applied on delegate, generic, array, interface, etc.

	Polymorphism extensions to array types,	delegate types, and generic types
	Allowing you to do things in your code that previously you where surprised you could not 
    Covariance preserves assignment compatibility between parent and Child relationship during dynamic polymorphism
    https://www.youtube.com/watch?v=jtzPBYBub5Y


			Suppose we have two types A and B and we have a modification, or transformation G,  that we can make to both of them to give new types G(A) and G(B).

			If G is a covariant transformation we have A>B implies G(A)>G(B). Outputs are covariant. 

			If G is a contravariant transformation then we have A>B implies G(A)<G(B). Inputs are contravariant.

			It is also possible that neither relationship applies. That is A>B doesn't imply anything about the relationship between G(A) and G(B). In this case G is referred to as invariant – which isn't really a good name.

			In the case of our example we had two transformations G1, which converted the type into the input parameter – a contravariant transform, and G2, which converted the type into the return result – a covariant transform. 

	Earlier versions of C# support covariance and contravariance in assignments, parameter types and return types. 
	C# version 4.0 brings covariance for generics and delegate types.

	upcast:  Fruit ← Apple
	dncast:  Fruit → Apple

    * Invariant types are not able to convert (Invariance)
		They are their own type and not related to anything else in the hierarchy.

	* variant type	A ← B
 					Generic are not variant: List<A> = new List<B>();  // failed

	* covariant types	
		A ← B 	 	T<A> ← T<B>
		arrows in same direction

		Covariance enables you to pass a derived type where a base type is expected.
		covariance allows you to assign a method to the delegate that has a less derived return type

		covariant types convert from a wider type to narrower type. (ex: from double to float) 
		Covariance • Pass collection of sub-class to a collection of base class 

		using System;
		public class Covariance
		{
		    static void Main()
		    {
		        object[] langs = {"C#", "Python", "PHP", "Java"};
		        Console.WriteLine(langs[0]);
		    }
		}

	contravariant types (paramters)
		A ← B  		T<A> → T<B>
		Accept base parameters where derived where expected
		Contravariant types convert from a narrower type to a wider type. (ex: short to int) 
		Contravariance • Pass collection of base class to a collection of sub-class 

		using System;
		using System.Collections.Generic;

		public class Contravariance
		{
		    static void Main()
		    { 
		        Action<string> del = ShowMessage; 
		        del("Proximity alert");         
		    }

		    static void ShowMessage(object message) 
		    { 
		        Console.WriteLine(message);
		    }
		}		

	Before c#4 Generic was not covariant (A ← B then T<A> ← T<B>)
	    Lack of covariance hinder reusability
	    class Animals {}    class Bear : Animal {}
	    Stack<Bear> bears = new Stack<Bear>();
	    Stack<Animal> animals = bears; // compil time error

	    void wash(Stack<Animal> animals) {...}

	    wash(bears); → compil time error, so:
	    void wash(Stack<T> animals) where T: Animal {}

### Sample 1

class  Animal {}
class  Dog:Animal {}
class  Cat:Animal {}
Animal objAninal = new Dog(); // valid statetement 
objAninal 		 = new Cat(); // valid statetement 
IEnumerable<Animal> animals = new List<Dog>>(); 	            Can group of Animals point to group of dogs?
Error Cannot convert type to 'System.Collections.Generic.List<Dog>' to 'System.Colleections.Generic.List<Animal>'
  Switch from 3.5 to .Net 4.0 -> Error disapeard
  .net 4.0 implements variance for generic interfaces and delegates using in and out key words
interface System.Collections.Generic.IEnumerable<out T>. T is covariant
Covariance preserves assignment compatibility between parent and Child relationship during dynamic polymorphism


### Sample 2

public interface ICovariant<out T> { }             remark <out ...>   used in dotnet core ILogger<MyClass>
public interface IContravariant<in T> { }          remark <in  ...>

public class Covariant<T> : ICovariant<T> { }
public class Contravariant<T> : IContravariant<T> { }

public class Fruit { }
public class Apple : Fruit { }

public class TheInsAndOuts
{
    public void Covariance()
    {
        ICovariant<Fruit> fruit = new Covariant<Fruit>();
        ICovariant<Apple> apple = new Covariant<Apple>();

        Covariant(fruit);
        Covariant(apple); //apple is being upcasted to fruit, without the 'out' keyword this will not compile
    }

    public void Contravariance()
    {
        IContravariant<Fruit> fruit = new Contravariant<Fruit>();
        IContravariant<Apple> apple = new Contravariant<Apple>();

        Contravariant(fruit); //fruit is being downcasted to apple, without the 'in' keyword this will not compile
        Contravariant(apple);
    }

    public void Covariant(ICovariant<Fruit> fruit)
    {}

    public void Contravariant(IContravariant<Apple> apple)
    {}
}
ICovariant<Fruit> apple = new Covariant<Apple>(); //bc it's covariant
IContravariant<Apple> fruit = new Contravariant<Fruit>(); //bc it's contravariant



	“covariance and contravariance enable implicit reference conversion for array types, delegate types, and generic
	type arguments. Covariance preserves assignment compatibility and contravariance reverses it.”
	In simple words, we can say Covariance and Contravariance are the polymorphism extensions to array types,
	delegate types, and generic type

	Ability to define types, such as the new IEnumerable<T>, that admit conversions among themselves when
	the type parameters in question bear some relationship to one another

	This is called covariance, because the arrows in each of the two examples point in the same direction
					 Manager → Employee
		IEnumerable<Manager> → IEnumerable<Employee>

	This is called contravariance because the arrow got reversed this time:
		             Manager → Employee
		IComparable<Manager> ← IComparable<Employee>


		IEnumerable<Manager> ms = GetManagers();
		IEnumerable<Employee> es = ms; 				Fails in 3.0, not in 4.0

	You can add the keyword in or out whenever you define a type parameter, and doing so gives you free extra conversions. 
	limitations: works with generic interfaces and delegates only



	“covariance and contravariance enable implicit reference conversion for array types, delegate types, and generic type arguments.
	 . Covariance preserves assignment compatibility
	 . Contravariance reverses it”
	In simple words, Covariance and Contravariance are the polymorphism extensions to array types, delegate types, and generic type

 	GENERIC VARIANCE

 		object ← string 					// yes, but...
 		List<object> = new List<string>();  // failed. ex:    object[] langs = {"C#", "Python", "PHP", "Java"};

 		This generic variance is solved in C# 4.0:




 

### IEnumerable<GrandFather> fathers = new List<Son>();		► will work fine with version 4.0

		Array Covariance
			This is nothing but implicit conversion of an array of a more derived type to an array of a less derived type.
			Unfortunately this is not type safe.

			object[] strArray = new string[10];
			strArray[0] = 1; // throw runtime exception, not compile time exception
			In above example, our object array is of string type but we are assigning integer value to one of its element,
			it will not throw any compile-time exception but, it will throw runtime exception.

		Delegate Covariance (method group variance)
			you can assign to delegates not only methods that have matching signatures, but also methods that return more derived types (covariance)
			or that accept parameters that have less derived types (contravariance) than that specified by the delegate type.
			This includes both generic and non-generic delegates.

			static string Parental() { return "Grandfather name is: Lala Bhagwan Das"; }

			Func<object> parentalLambda = () => Parental(); //lambda expression
			Func<object> parentalFunc = Parental; //Grouped

			static string ParentalObject(object obj) {	//method signature }
			Contravariance. A delegate specifies a parameter type as string, but can assign a method that takes an object.
			Action<String> parentalDel = ParentalObject;


