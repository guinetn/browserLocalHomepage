## RECORD - ENREGISTREMENTS - Value Objects

In Short: 'class' avoiding lot of code when copying immutable objects

Identical objects have same values in their properties (struct), not because they share a primary key or location in memory (class). In DDD copied value objects are spread and risk to drift apart when updated. So value objects are made immutable (requires more code to set up in .NET), that actually makes copying the data a bigger problem: You now have data that is guaranteed to be identical taking up twice as much space as necessary. C# 9 record are value object that does everything you want 


```C#
public record Person
{
   string LastName;        ←→ public string LastName { get; init; }
   string FirstName;
}

Address addr = new Address {Street = "Kensignton", City = "London" }
Address addr = new ( "Kensignton", "London") // target typing
```

Immutable référence type qui fournit des méthodes synthétisées pour FOURNIR UNE SÉMANTIQUE DE VALEUR → POUR L’ÉGALITÉ ←

Records define an immutable reference type and behave like a value type. Once the record is defined, we can’t modify the values of any properties of the record instances.
To make the entire object immutable, an init keyword must be defined on each of the properties in case of implicit parameterless constructors are used.


Immutable reference types that BEHAVE LIKE VALUE TYPES (objects that are considered identical because they have the same values in their properties, not because they share a primary key or location in memory), and introduce the new with keyword into the language.

Combine different kinds of data into an aggregate. They cannot be null and come with default comparison and equality.
Records are comparable and equatable:

One of the key features of C#9 would be records. Init-only properties can work wonders for individual properties immutable and behave like a value, then declaring it as a record. Records are "values" and not mere objects.
They depict change by creating new records which signify new state and are defined not by identity, but by their contents.

creating a copy of an object (assigning a value from one object to another):  
- Structs (and other value types): assigning a value from one struct to another copies the data
- classes: assigning one variable to another just copies pointers around and both variables end up pointing to the same object in memory rather than getting their own copies of the data

The problem with creating a copy of a value object is that the two copies can have separate changes made to them -- what started off as two identical objects drift apart. As a result, value objects are often made to be immutable, something that requires a fair amount of code to set up in .NET. That actually makes copying the data a bigger problem: You now have data that is guaranteed to be identical taking up twice as much space as necessary.



Type référence qui fournit des méthodes synthétisées pour FOURNIR UNE SÉMANTIQUE DE VALEUR POUR L’ÉGALITÉ
Members are implicitly public in records if you don’t precise it


Why?
In domain driven design one of the key concepts are "value objects": objects that are considered identical because they have the same values in their properties, not because they share a primary key or location in memory. An address is a good example of a value object: two addresses are the same if they have identical city/street/etc. even if they're from two different customers and one is a "Shipping" address while the other is a "Billing" address.

Structs (and other value types) work that way when compared, but with structs, assigning a value from one struct to another copies the data (it's different with classes: assigning one variable to another just copies pointers around and both variables end up pointing to the same object in memory rather than getting their own copies of the data).

The problem with creating a copy of a value object is that the two copies can have separate changes made to them -- what started off as two identical objects drift apart. As a result, value objects are often made to be immutable, something that requires a fair amount of code to set up in .NET. That actually makes copying the data a bigger problem: You now have data that is guaranteed to be identical taking up twice as much space as necessary.
But, in C# 9, you can just create a record and get a value object that does everything you want

```C#
        class (check IL)
          ↓
public record Person
{
   public string LastName { get; }
   public string FirstName { get; }

   public Person(string first, string last) => (FirstName, LastName) = (first, last);
}
```

```C#
public record Person
{
   public string LastName { get; init; }  // init → no constructor needed
   public string FirstName { get; init;}
}
```

Records introduce public init-only auto-property that is a shorthand of the previous declaration:
```C#
public record Person
{
   string LastName;        ←→ public string LastName { get; init; }
   string FirstName;
}
```


Elle est immuable: aucune des propriétés ne peut être modifiée une fois qu’elle a été créée. 
When record is used, le compilateur synthétise plusieurs autres méthodes pour vous :
- Méthodes pour les comparaisons d’égalité basées sur des valeurs
- Remplacer pour GetHashCode()
- Copier et cloner des membres
- PrintMembers et ToString()
- Méthode Deconstruct

```C#
public record Teacher : Person
{
  public string Subject { get; }
  public Teacher(string first, string last, string sub) : base(first, last) => Subject = sub;
}
```

Sceller les enregistrements pour éviter toute dérivation supplémentaire :
```C#
public sealed record Student : Person
{
  public int Level { get; }
  public Student(string first, string last, int level) : base(first, last) => Level = level;
}
```

By default, regular classes are equal when they underlying reference. Its behavior changes if you declare your class as a record. As opposed to comparing the object reference, the RECORDS ARE COMPARED BY VALUE. IT MEANS TWO DIFFERENT OBJECTS HOLDING THE SAME VALUES WILL BE CONSIDERED EQUAL AND HASHCODE WILL BE THE SAME. Contents will able to define the Records, not by identity.

```C#
public record Address
{
   public string Street { get; }
   public string City { get; }        
   public Address()
   {
      this.Street = string.Empty;
      this.City = string.Empty;
   }
   public Address(string Street, string City)
   {
      this.Street = Street;
      this.City = City;
   }
}

Address addr1 = new Address("Ridout", "London");
Address addr2 = new Address("Ridout", "London");
```

Looks like I'm creating a reference type. 
BUT when you compare the two record objects, they're compared like value types -- it's the value of the properties that matter (provided the two objects are of the same type). So, in this code, the test will pass because the Street and City properties have the same values in both of the objects:

```c#
(addr1 == addr2)    // True addresses are the same
addr1.Equals(addr2) // True and same hashCode
```

On the other hand, when you assign variables, records work like reference types: pointers are moved around but no data is copied. In this code, the addr1 and addr2 variables both point at the same object in memory:

```c#
Address addr1 = new Address("Ridout", "London");
Address addr2 = addr1;
```

# Controlling and Defining Properties in Records

init of a property: indicate a readonly property (can be set when an object is instantiated)
```C#
public record Address
{
   public string Street { get; init; }
   public string City { get; init; }
}
Address addr = new Address {Street = "Kensignton", City = "London" }
Address addr = new ( "Kensignton", "London") // "TARGET TYPING": The same (reduce the amount of typing)

// Force a copy to be created by using the `with` keyword:
Address newAddress = addr1 with { City = "Liverpool" }

// Deconstructing a record
// A Deconstruct method accepts an out parameter for each individual variable that will be returned and then, in the method's body, assigns values to those parameters (typically from the properties in the record but you can do whatever you want).
// Extract record's properties into individual variables:
var (street, city) = addr;
MessageBox.Show("The city is " + city);

// Custom record deconstruction
public void Deconstruct(out string city)
{
  city = City;
}

// Short definition
public record Address(string Street, string City);  // Note ended ;

// adds a body to the record and makes the Street property writeable
public record Address(string Street, string City)
{
   public string Street {get; set; } // writeable property 
}
```

## TARGET TYPING

```C#
Address addr = new Address {Street = "Kensignton", City = "London" }
Address addr = new ( "Kensignton", "London") // "TARGET TYPING": The same (reduce the amount of typing)
```

Microsoft calls this "target typing" and it works almost everywhere 
Pays off when you're loading multiple copies of the same type into a collection:

```C#
List<Address> addrs = new();
addrs.Add(new( "Ridout", "London" ), new( "Shore", "London" ), new( "St. Patrick", "Goderich" ));
```

```C#
PrintAddress (new("Ridout", "London"));
…
public void PrintAddress(Address addr)
{...}
```


## Positional records - Enregistrements positionnels

There is value in adopting a more positional approach to a record and its contents are given via constructor arguments and can be extracted with positional deconstruction. It is entirely possible to define your own constructor and deconstructor in a record:


```C#
public record Person
{
   public string LastName { get; init;}
   public string FirstName { get; init;}

   public Person(string first, string last) => (FirstName, LastName) = (first, last);
   public void Deconstruct(out string first, out string last) => (firstName, lastName) = (First, Last);
}
```

Shorter, declares public init-only auto-properties and constructor() and deconstructor()
```C#
public record Person(string First, string LastName);
var person = new Person('Joe','Black'); // positional construction
var (f,l) = person;                     // positional deconstruction
//let you write:

```

Le compilateur produit une `Deconstruct()` méthode pour les enregistrements positionnels. 
La Deconstruct méthode a des paramètres qui correspondent aux noms de toutes les propriétés publiques dans le type d’enregistrement. 
La Deconstruct méthode peut être utilisée pour déconstruire l’enregistrement dans ses propriétés de composant :

```C#
var person = new Person("Bill", "Wagner");

var (first, last) = person;
Console.WriteLine(first);
Console.WriteLine(last);
```

## 'with' expressions
Non—Destructive mutation = create new value from immutable data to represent the new state 
Creates an updated copy of a record but with some properties modified:  
Calls the copy constructor and applies the object initializer at the top to change the properties accordingly

```c#
var person = new Person("Bill", "Wagner");
var brother = person with { FirstName = "Paul" };
```




## F# records #

```C#
type ContactCard =
    { Name: string
      Phone: string
      ZipCode: string }

// Create a new record
{ Name = "Joe"; Phone = "(555) 555-5555"; ZipCode = "90210" }
```

- https://devblogs.microsoft.com/dotnet/c-9-0-on-the-record/