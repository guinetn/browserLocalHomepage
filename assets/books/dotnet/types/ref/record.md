## RECORD - ENREGISTREMENTS

Immutable reference types that behave like value types, and introduce the new with keyword into the language.

Combine different kinds of data into an aggregate. They cannot be null and come with default comparison and equality.
Records are comparable and equatable:

One of the key features of C#9 would be records. Init-only properties can work wonders for individual properties immutable and behave like a value, then declaring it as a record. Records are "values" and not mere objects.
They depict change by creating new records which signify new state and are defined not by identity, but by their contents.


Type référence qui fournit des méthodes synthétisées pour FOURNIR UNE SÉMANTIQUE DE VALEUR POUR L’ÉGALITÉ

```C#
            ___ = class (check IL)
        /
public record Person
{
public string LastName { get; }
public string FirstName { get; }

public Person(string first, string last) => (FirstName, LastName) = (first, last);
}
```

Elle est immuable: aucune des propriétés ne peut être modifiée une fois qu’elle a été créée. 
When record is used, le compilateur synthétise plusieurs autres méthodes pour vous :
Méthodes pour les comparaisons d’égalité basées sur des valeurs
Remplacer pour GetHashCode()
Copier et cloner des membres
PrintMembers et ToString()
Méthode Deconstruct

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

## Enregistrements positionnels

```C#
public record Person(string FirstName, string LastName);
public record Teacher(string FirstName, string LastName,string Subject): Person(FirstName, LastName);
public sealed record Student(string FirstName,string LastName, int Level) : Person(FirstName, LastName);
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

les expressions: Une instruction with-expression demande au compilateur de créer une copie d’un enregistrement, mais avec les propriétés spécifiées modifiées :
Person brother = person with { FirstName = "Paul" };

## F# records #

```C#
type ContactCard =
    { Name: string
      Phone: string
      ZipCode: string }

// Create a new record
{ Name = "Alf"; Phone = "(555) 555-5555"; ZipCode = "90210" }
```

- https://devblogs.microsoft.com/dotnet/c-9-0-on-the-record/