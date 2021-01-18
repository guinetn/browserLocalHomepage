# C# 6 (.Net 4.6)


Static imports
Exception filters
Auto-property initializers
Expression bodied members
Null propagator
String interpolation
nameof operator
Index initializers
Await in catch/finally blocks
Default values for getter-only properties

Roslyn the compiler as a service. The C# compiler is now written in C#, and you can use the compiler as part of your programming efforts.


csharpcodingguidelines.com
https://csharpguidelines.codeplex.com/downloads/get/540283
csharpguidelines

# Improve daily coding, lighter code
http://www.toptal.com/dot-net/tips-and-practices
https://quizlet.com/137612626/miscellaneous-development-flash-cards/


* Auto-property initializers 
* Using static members 
* Extension methods
* Expression-bodied members 
* Indexer initializer 
* Dictionary initializer							
* Await in catch/finally 
* Exception filters 
* Null propagation 
* String interpolation 
* Parameterless struct ctors						
* Struct with parameterless ctors						
* nameof operator 
* #pragma 


??
* Getter-only auto-properties 
* Ctor assignment to getter-only autoprops 
* Extension Add in collection initializers 
* Improved overload resolution 




## AUTO-PROPERTY INITIALIZERS

	public int X { get; set; } = x;		
	public int X { get = 2; };		
	Before: can init at declaration level, only at constructor level			
	Now   : can init at declaration level

	public class Customer
	{
	    public string First { get; set; } = "Jane";
	    public string Last { get; set; } = "Doe";
	}
	complete old notions
	getter-only -  allow you to omit a setter
	public class Customer
	{
		public string First { get; } = "Jane";
		public string Last { get; } = "Doe";
	}

	Getter-only auto-properties						
	public int Y { get; } = y;		
	assignment at declaration or ctor level		Y = 15											

## USING STATIC MEMBERS							
	using System.Console; 	now just… Write(4);	  no Console.Write(...)					
	using static System.Math;
	double distance = Sqrt(x * x + y * y);  // and not Math.Sqrt !!

    using ra = Microsoft.ML.Probabilistic.Models;  // Fix Le nom de type 'Range' n'existe pas dans le type 'Range'
    var game = new ra.Range(winnerData.Length);

## Extension methods
	using System.Linq.Enumerable; // Just the type, not the whole namespace
	class Program
	{ 
		static void Main() 
		{ 
			var range = Range(5, 17); // Ok: not extension 
			var odd = Where(range, i => i % 2 == 1); // Error, not in scope
			var even = range.Where(i => i % 2 == 0); // Ok 
		} 
	}

## EXPRESSION-BODIED MEMBERS			

## If a method is short, define it without braces			

		public double Dist => Sqrt(X * X + Y * Y);		
		public int Double(int x) => Add(x,x);		
		public Point Move(int dx, int dy) => new Point(X + dx, Y + dy);
		Simplify methods/pties made of a single return

## INDEX INITIALIZERS
	var numbers = new Dictionary<int, string> { [7] = "seven", [9] = "nine", [13] = "thirteen" }; // set values to keys through any indexer that the new object has:

## DICTIONARY INITIALIZER
	JObject { ["x"] = 3, ["y"] = 7 }				
	Dictionary<string, string> newWay = new Dictionary<string, string>()
	{
	    // Look at this!
	    ["Afghanistan"] = "Kabul", // and not like in c#3: { "Afghanistan", "Kabul" },
	    ["Iran"] = "Tehran",
	    ["India"] = "Delhi"
	};
	Works with any type having an indexer
 
## AWAIT IN CATCH/FINALLY							
	try … catch { await someCall } finally { await someCall }		
	await (C# 5) permet d'interrompre l'exécution d'une méthode asynchrone en attendant la fin d'une tâche, et de reprendre plus tard là où on en était, 
	quand la tâche attendue est terminée.

## EXCEPTION FILTERS								
	catch(E e) if (e.Count > 5) { … }			
	lets you specify a condition for a catch block.
	try
	{
	    throw new Exception("Me");
	}
	catch (Exception ex) if (ex.Message == "You")
	{
	    // this one will not execute.
	}
	catch (Exception ex) if (ex.Message == "Me")
	{
	    // this one will execute
	}	

## NULL CONDITIONAL
	Safe members access in deep object graphs
	parent.child?.ToString()								
	customer?.Orders?[5]?.$price	
	int? length = customers?.Length; // null if customers is null 
	Customer first = customers?[0]; // null if customers is null
	if (predicate?.Invoke(e) ?? false) { … }
	PropertyChanged?.Invoke(this, args); // to check for null before you trigger an event

	string city = order?.Customer?.Address?.City;
	If one of these element is null, the result will be null

## STRING INTERPOLATION							
	easily format strings
	C#5:  var s = String.Format("{0} is {1} year{{s}} old", p.Name, p.Age);
							↓
	C#6:  var s = "\{p.Name} is \{p.Age} year{s} old";
		  var s = $"{p.First} {p.Last} is {p.Age} years old."
		  var s = $"{p.Name,20} is {p.Age:D3} year{{s}} old";	

	Tip: use () to use quotes in string interpolation
		 var s= $"Result = {p.Name} {(p.name.Length>0? "s" : "")}" 


## STRUCT WITH PARAMETERLESS CTORS

	Before struct cannot have parameterles ctor (implicit to init fields)						
	struct Person 
	{ 
		public string Name { get; } 
		public int Age { get; } 
		public Person(string name, int age) { Name = name; Age = age; } 
	  	public Person() : this("Jane Doe", 37) { }  ← 
	}

## NAMEOF OPERATOR		
	To get the name of a member from code							
	string s = nameof(Console.Write);	// s = Write. Evite chaines en dur, doit exister			
	WriteLine(nameof(person.Address.ZipCode)); // prints "ZipCode"

#pragma										    
	#Disable Warning BC40008						

# Extension Add in collection initializers														

# Improved overload resolution

# Declaration expressions		 					if (!long.TryParse(Request.QureyString["Id"], out long id)) { … }															







    http://www.csharpstar.com/top-10-new-features-of-csharp6/
    https://msdn.microsoft.com/en-us/magazine/dn802602.aspx

    Expression-bodied property      
                                public bool property => method();
                                a new syntax to create computed properties in the same way as you would create a lambda expression.

                                Expression bodied property

                                    => used in property is an expression body. 
                                    Shorter and cleaner way to write a property with only getter

                                    public string Text =>  $"{TimeStamp}: {Process} - {Config} ({User})";

                                    public bool MyProperty => myMethod();
                                    is translated to
                                    public bool MyProperty { get { return myMethod(); } }

                                    private sealed class DapperTable
                                    {
                                        private string[] fieldNames;
                                        internal string[] FieldNames => fieldNames;
                                        public int FieldCount => fieldNames.Length;

                                Expression bodied functions
                                    public int TwoTimes(int number) => 2 * number;
                                    public override string ToString() => string.Format("{0}, {1}", First, Second);

                                    static bool TheUgly(int a, int b)
                                    {
                                        if (a > b) return true;
                                        else return false;
                                    }
                                    static bool TheNormal(int a, int b) { return a > b; }
                                    static bool TheShort(int a, int b) => a > b; // beautiful, isn't it?

## String Interpolation                public string FullName => $"{FirstName} {LastName}";

                                        specify a format stringwith a colon (:): var aNumberAsString = $"{aDoubleValue:0.####}";

    Dictionary Initializer              var BookDictionary = new Dictionary<int,string> { 
                                        [1] = "ASP.net", [2] = "C#.net", [3] = "ASP.net Razor", [4] = "ASP.net MVC5" }

    Null-Conditional Operator
                                        return value?.Substring(0, Math.Min(value.Length, length));

                                        OnTemperatureChanged?.Invoke(this, value)       Checking for Null Before Invoking a Delegate

                                        List<string> linesOfCode = ParseSourceCodeFile("Program.cs");s
                                        return linesOfCode?.Count ?? 0;

                                         public static IEnumerable<T> GetValueTypeItems<T>( IList<T> collection, params int[] indexes) where T : struct
                                        {
                                            foreach (int index in indexes)
                                            {
                                                T? item = collection?[index];
                                                if (item != null) yield return (T)item;
                                            }
                                        }

    Getter-only Auto Properties         public DateTime BirthDate { get; } // true readonly auto implemented properties
                                        (in C# 5 and lower, you must provide a get and set)

    await in catch and finally block    try { // code that might throw exception }
                                        catch(Exception ex) { await LogExceptionAsync(ex); }

    Exception Filters
                                        try { throw new customexception("Test Exception") }
                                        catch(customexception ex) if (ex.Message=="Not Test") { //Control will not come here because exception name is not test }
                                        catch(customexception ex) if (ex.Message=="Test Exception") { //Control will come here because exception name is Test Exception }                                    
    Auto Property Initializer
                                        class customer
                                        {
                                            public string Firstname{get; set;} = "Csharpstar";
                                            public string Lastname{get; set;} = "Admin";
                                            public int Age{get;} = 20;
                                            Public DateTime BirthDate { get; set; }
                                        }






