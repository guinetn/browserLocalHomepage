# C# 9 (.net 5) #

.NET 5 is paired with C# 9, which brings many new features to the language. Here are a few highlights:

* Records
Immutable reference types that BEHAVE LIKE VALUE TYPES (objects that are considered identical because they have the same values in their properties, not because they share a primary key or location in memory), and introduce the new with keyword into the language.
* Relational pattern matching
Extends pattern matching capabilities to relational operators for comparative evaluations and expressions, including logical patterns - new keywords and, or, and not.
* Top-level statements
As a means for accelerating adoption and learning of C#, the Main method can be omitted and application as simple as the following is valid: System.Console.Write("Hello world!");
* Function pointers
Language constructs that expose the following intermediate language (IL) opcodes: ldftn and calli.


download.page(dotnet/types/ref/record.md)

## INIT ONLY SETTER: { set; } --> { init; }

get rid of a lot of boilerplate code because no need of a constructor to set properties that can be set only one time with 'init' that makes it immutable or read-only

```c#
    public struct WeatherObservation
    {
        public DateTime RecordedAt { get; init; }
        public decimal TemperatureInCelsius { get; init; }
        public decimal PressureInMillibars { get; init; }

        public override string ToString() =>
            $"At {RecordedAt:h:mm tt} on {RecordedAt:M/d/yyyy}: " +
            $"Temp = {TemperatureInCelsius}, with {PressureInMillibars} pressure";
    }

    // Callers use property initializer to set values while keeping immutability:
    var now = new WeatherObservation 
    { 
        RecordedAt = DateTime.Now, 
        TemperatureInCelsius = 20, 
        PressureInMillibars = 998.0m 
    };

    // Error! CS8852.
    now.TempetureInCelsius = 18;
```

### Top-level statements - instructions de niveau supérieur

eliminate the boilerplate code and start coding the logic right away.
Un seul fichier de votre application peut utiliser des instructions de niveau supérieur
Pour documents pédagogiques.
expérience de type script pour les expérimentations similaires à celles fournies par les blocs-notes Jupyter. 
Les instructions de niveau supérieur sont idéales pour les petits programmes et utilitaires de console. 
Azure Functions est un cas d’usage idéal pour les instructions de niveau supérieur.
To identifies entry point, if C# 9 have a class file with the top-level statement, then it is assumed to be the entry point of the application. Top-level statements are great for small console programs, snippets, and utilities. It makes life simpler.

The program has to occur after the use and before any type or namespace declarations in the file

```c#
using System;
Console.WriteLine("Hello World!");
```

```c#
using System.Console;
using System.Threading.Tasks;
WriteLine("Hello ", args[0]);
WriteLine( Add(x:4, y:8) );
await Task.Delay(1000);
return 0

// Local functions ~ statement are permitted but cannot be called outside of the top-level statement section
static double Add(double x, double y) { 
    return x+y; 
}
```

A simple C# program requires a considerable amount of boilerplate code, ie consider the canonical 'Hello World!' program:
```c#
using System;
public class Program {
    
    public static void Main(string[] args) {
        Console.WriteLine("Hello World!");
    }
}
```

### AMÉLIORATIONS DES CRITÈRES SPÉCIAUX


### ENTIERS DIMENSIONNÉS NATIFS


### POINTEURS FONCTION


### SUPPRIMER L’ÉMISSION DE L’INDICATEUR LOCALSINIT

```c#
private List<WeatherObservation> _observations = new();
```

Le type de cible nouveau peut également être utilisé lorsque vous devez créer un nouvel objet à passer en tant que paramètre à une méthode. Envisagez une ForecastFor() méthode avec la signature suivante :

```c#
public WeatherForecast ForecastFor(DateTime forecastDate, WeatherForecastOptions options)
var forecast = station.ForecastFor(DateTime.Now.AddDays(2), new());
```

Une autre utilisation intéressante de cette fonctionnalité est de l’associer aux propriétés init only pour initialiser un nouvel objet. Les parenthèses sur new sont facultatives :
```c#
WeatherStation station = new() { Location = "Seattle, WA" };
```

### TARGET-TYPED ‘NEW’ EXPRESSIONS - NOUVELLES EXPRESSIONS TYPÉES CIBLES

```c#
Person person = new Person("Bill", "Wagner");
Person person = new("Bill", "Wagner");

Point p[] = { new(1,2), new(3,4) };
```


### FONCTIONS ANONYMES STATIQUES

### EXPRESSIONS CONDITIONNELLES TYPÉES CIBLE

### TYPES DE RETOUR COVARIANT

### PARAMÈTRES D’ABANDON LAMBDA

### ATTRIBUTS SUR DES FONCTIONS LOCALES

### INITIALISEURS DE MODULE

### NOUVELLES FONCTIONNALITÉS POUR LES MÉTHODES PARTIELLES

générateurs de code analysent le code et écrivent de nouveaux fichiers de code source dans le cadre du processus de compilation. Un générateur de code standard recherche des attributs ou d’autres conventions dans le code.



Init-only properties, object initializers to the client of a type are extremely flexible and readable format to build an object, and they are especially great for nested object creation where a whole tree of objects is created in one go.
Object initializers are developer's delight and free the type author from writing hassles of complexity. After all, that is required is to write simple properties!

## Data members
Immutable, with init-only public properties, Records can be non-destructively modified through with-expressions. Records often change the defaults to optimize for that common case.
It makes up for explicit record declarations.
It makes for beautiful and clear record declarations. In case the requirement is of a single field, you can just clearly add the private modifier.

### Pattern Matching
New and, or, and not Keywords for the pattern which afford more flexibility and robustness with conjunctive, disjunctive, and negated patterns

match a value (or an object) with certain patterns to pick a branch/block of the code.

C# 7.0 Switch statement
```c#
int myValue = 10;
switch(myValue) {
    case int value when value <=0:
        WriteLine("Less than/equal to 0");
        break;
    case int value when value > 0 && value <=10:
        WriteLine( "More then 0 and less/equal to 10");
        break;    
    default:
        WriteLine("More than 10");
}
```

C# 8.0 Switch Expressions
```c#
int myValue = 10;
var messae = myValue switch {
    int value when value <=0 => "Less than/equal to 0";
    int value when value >=0 && value <=10 => "More then 0 and less/equal to 10";
    _ => "More than 10"    
}
```

C# 9.0 Relational patterns: allow to use < > <= and >= in patterns
```c#
int myValue = 10;
var message = myValue switch {
    <=0 => "Less than/equal to 0";
    1 or 2 => "More than 1 or equal to 1";
    >2 and <=20: "More then 2 and less/equal to 20";
    _ => "More than 10"    
}
```

### Logical patterns
If you want to minimize confusion in the operators used in expressions, logical operators such as "and, or and not" should be spelled out.

### Records
Declaration form for C# class and struct types which amalgamates benefits of same features with a way to declare a datatype by describing members of the aggregate as well as extra code or deviations from boilerplate, if any.
Type Inference for the New Keyword

Target-typed new expression proposal has been adopted into C### 9; such boilerplate code will no longer be necessary.

 Improved target typing

 When the expression gets its type from the context of where it is being used, Target typing comes in place. Typical examples would be null and lambda which are target typed.

 When it comes to C#, expressions not previously target typed can now be guided by their context.

 Covariant returns

 It is useful to express that a method override in a derived class has a more specific return type than the declaration in the base type.

 Top-level programs

 When it comes to C#, even writing a simple program can be an arduous task with too much of boilerplate code.

 This adds to the level of code and ultimately clutter in the code. But this problem is all set to get resolved. With C#9, it is relatively simple to write the main program at the top level.

 Local functions are typically a form of statement and allowed in top-level program. It is an error to call from anywhere outside of the top-level statement section.

 Improved pattern matching

 Several different kinds of patterns have been incorporated in C 9.0. Let's look at the context of code snippet.

 Simple type patterns: a type pattern needs to declare an identifier when the type matches

 Relational patterns: patterns corresponding to the relational operators <, <=

 Logical patterns: combine patterns with logical operators and, or and not, spelt out as words to avoid confusion with the operators used in expressions.



https://docs.microsoft.com/fr-fr/dotnet/csharp/whats-new/csharp-9
https://medium.com/swlh/an-introduction-to-the-new-features-in-c-9-305dc8fb74d2
https://anthonygiretti.com/