# Arrays

Stores a fixed number of strongly typed elements. 
Its size must be specified at the time of initialization.
Performs faster than ArrayList because it is strongly typed.

public static T Find<T>(T[] array, Predicate<T> match);
public static T[] FindAll<T>(T[] array, Predicate<T> match)
public static T FindLast<T>(T[] array, Predicate<T> match)

```cs
using System; // array

int[] arr = new int[5]
int[] arr = new int[5]{1, 2, 3, 4, 5};
int[] arr = {1, 2, 3, 4, 5};

int[] numbers = new int[] {1, 2, 3};
int[] numbers = { 1, 3, 5, 7, 9 };
foreach (var n in numbers) 
    Console.WriteLine(n);
    
Array.ForEach<int>(numbers, n => Console.WriteLine(n)); //[1,2,3,4]

// Array Size
int[,] arr = new int[4,5]; // two dimentional array
int[,] arr = new int[,] {{2,3,4},{11,12,24}};
int elem = arr[0,0]; //elem=2
int elem2 = arr[1,1]; //elems=12
int num = arr.Length; // Get the total number of the array: 6
int dim = arr.Rank; // Get the dimension of the array: 2
int len = arr.GetLength(1); // Get the length of a given dimension: 3

var totalElements = numbers.Count(); // 5
var totalEvenNums = numbers.Count(n => n%2==0);

var a = new[] { 1, 10, 100, 1000 };				// int[]
var b = new[] { 1, 1.5, 2, 2.5 };				// double[]
var c = new[] { "hello", null, "world” };		// string[]

List<int> digits = new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

var contacts = new[] {
	new {
		Name = "Chris Smith",
		PhoneNumbers = new[] { "206-555-0101", "425-882-8080" }
	},
	new {
		Name = "Bob Harris",
		PhoneNumbers = new[] { "650-555-0199" }
	}

// Searches 
string[] names = { "Steve", "Bill", "Bill Gates", "Ravi", "Mohan", "Salman", "Boski" };
var stringToFind = "Bill";
var result = Array.Find(names, element => element == stringToFind); // returns "Bill"
var result = Array.Find(names, element => element.StartsWith("B")); // returns Bill
var result = Array.Find(names, element => element.Length >= 5); // returns Steve
var stringToFind = "bill";
string[] result = Array.FindAll(names, element => element.ToLower() == stringToFind); // return Bill, 
var result = Array.FindLast(names, element => element.Contains(stringToFind)); 

string[] animals = { "Cat", "Alligator", "fox", "donkey", "Cat", "alligator" };
var animalsWithCapitalLetter = animals.Count(s => { return Regex.IsMatch(s, "^[A-Z]"); });

Array.Reverse(animals);
```

### Array Binary Search
Searches a one-dimensional SORTED Array for a value, using a binary search algorithm.
O(n log n)
https://www.tutorialspoint.com/Binary-search-in-Chash
https://docs.microsoft.com/en-us/dotnet/api/system.array.binarysearch?view=net-5.0

```cs
using System;

public class SamplesArray
{
    public static void Main()
    {
        // Creates and initializes a new Array.
        Array myIntArray = Array.CreateInstance(typeof(Int32), 5);

        myIntArray.SetValue(8, 0);
        myIntArray.SetValue(2, 1);
        myIntArray.SetValue(6, 2);
        myIntArray.SetValue(3, 3);
        myIntArray.SetValue(7, 4);

        // Do the required sort first
        Array.Sort(myIntArray);

        // Displays the values of the Array.
        Console.WriteLine( "The Int32 array contains the following:" );
        PrintValues(myIntArray);

        // Locates a specific object that does not exist in the Array.
        object myObjectOdd = 1;
        FindMyObject( myIntArray, myObjectOdd );

        // Locates an object that exists in the Array.
        object myObjectEven = 6;
        FindMyObject(myIntArray, myObjectEven);
    }

    public static void FindMyObject(Array myArr, object myObject)
    {
        int myIndex=Array.BinarySearch(myArr, myObject);
        if (myIndex < 0)
        {
            Console.WriteLine("The object to search for ({0}) is not found. The next larger object is at index {1}.", myObject, ~myIndex );
        }
        else
        {
            Console.WriteLine("The object to search for ({0}) is at index {1}.", myObject, myIndex );
        }
    }

    public static void PrintValues(Array myArr)
    {
        int i = 0;
        int cols = myArr.GetLength(myArr.Rank - 1);
        foreach (object o in myArr)
        {
            if ( i < cols )            
                i++;            
            else
            {
                i = 1;
                Console.WriteLine();
            }
            Console.Write( "\t{0}", o);
        }
        Console.WriteLine();
    }
}
// This code produces the following output.
//The Int32 array contains the following:
//        2       3       6       7       8
//The object to search for (1) is not found. The next larger object is at index 0
//The object to search for (6) is at index 2.
```

Sort
```cs
// SORT
string[] animals = { "Cat", "Alligator", "Fox", "Donkey", "Bear", "Elephant", "Goat" };
Array.Sort(animals); // Result: ["Alligator", "Bear", "Cat","Donkey","Elephant","Fox","Goat"]
// Sort the Portion of Array
Array.Sort(animals, 0, 3); // Result: ["Alligator","Cat","Fox", "Donkey", "Bear", "Elephant", "Goat"]

// Sort an Array using LINQ
var sortedStr = from name in animals orderby name select name;
Array.ForEach<string>(sortedStr.ToArray<string>(), s => Console.WriteLine(s)); 
```

// Duplicates
```cs
// Remove duplicate from built-in types 
int[] nums = { 1, 2, 3, 4, 3, 55, 23, 2 };
int[] dist = nums.Distinct().ToArray();

// Remove duplicate from custom objects: implement either IEquatable or IEqualityComparer.
Person[] people = {
        new Person(){ FirstName="Steve", LastName="Jobs"},
        new Person(){ FirstName="Bill", LastName="Gates"},
        new Person(){ FirstName="Steve", LastName="Jobs"},
        new Person(){ FirstName="Lary", LastName="Page"}
    };        
var dist = people.Distinct(new PersonNameComparer()).ToArray();

class PersonNameComparer : IEqualityComparer<Person>
{       
    public bool Equals(Person x, Person y)
    {
        return x.FirstName == y.FirstName && x.LastName == y.LastName;
    }
 
    public int GetHashCode(Person obj)
    {
        return obj.Id.GetHashCode() ^ (obj.FirstName == null ? 0 : obj.FirstName.GetHashCode()) ^ (obj.LastName == null ? 0 :obj.LastName.GetHashCode());
    }
}
or to do "var dist = people.Distinct().ToArray();"
class Person : IEquatable<Person>
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
 
    public bool Equals(Person other)
    {
        return FirstName.Equals(other.FirstName) && LastName.Equals(other.LastName);
    }
 
    public override int GetHashCode()
    {
        return Id.GetHashCode() ^ (FirstName == null ? 0 : FirstName.GetHashCode()) ^ (LastName == null ? 0 : LastName.GetHashCode());
    }
}
```


Combine
```cs
// Combine
int[] num1 = { 1, 2, 3, 4, 3, 55, 23, 2 };           
int[] num2 = { 55, 23, 45, 50, 80 };
var all = num1.Union(num2).ToArray();
// If an array contains objects of a custom class, then you need to implement IEquatable<T> or IEqualityComparer<T>
class Person : IEquatable<Person>
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
 
    public bool Equals(Person other)
    {
        return FirstName.Equals(other.FirstName) && LastName.Equals(other.LastName);
    }
 
    public override int GetHashCode()
    {
        return Id.GetHashCode() ^ (FirstName == null ? 0 : FirstName.GetHashCode()) ^ (LastName == null ? 0 : LastName.GetHashCode());
    }
}

Person[] people1 = {
        new Person(){ FirstName="Steve", LastName="Jobs"},
        new Person(){ FirstName="Bill", LastName="Gates"},
        new Person(){ FirstName="Steve", LastName="Jobs"},
        new Person(){ FirstName="Lary", LastName="Page"}
    };
 
    Person[] people2 = {
        new Person(){ FirstName="Steve", LastName="Jobs"},
        new Person(){ FirstName="Lary", LastName="Page"},
        new Person(){ FirstName="Bill", LastName="Gates"}
    };    
var allp = people1.Union(people2).ToArray();
Array.ForEach(allp, p => Console.WriteLine(p.FirstName));
```

