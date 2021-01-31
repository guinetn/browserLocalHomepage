# C# 3.0 - 2008 #

|||
|---|---|
|Auto-implemented properties||
|Anonymous types| new {c.Name, c.Age} |
|Query expressions| from … where … select …|
|Expression trees| Expression<T> |
|Extension methods  | static void dump(this object o)|
|Lambda expressions | c=>c.Name|
|Implicitly typed local variables | var x = 5;|
|Partial methods| |
|Object and collection initializers | new Point {x=1, y=2}; int[] numbers = { 1, 3, 5, 7, 9 }; |


•	Implicitly typed local variables, which permit the type of local variables to be inferred from the expressions used to initialize them.
•	Extension methods, which make it possible to extend existing types and constructed types with additional methods.
•	Lambda expressions, an evolution of anonymous methods that provides improved type inference and conversions to both delegate types and expression trees.
•	Object initializers, which ease construction and initialization of objects.
•	Anonymous types, which are tuple types automatically inferred and created from object initializers.
•	Implicitly typed arrays, a form of array creation and initialization that infers the element type of the array from an array initializer.
•	Query expressions, which provide a language integrated syntax for queries that is similar to relational and hierarchical query languages such as SQL and XQuery.
•	Expression trees, which permit lambda expressions to be represented as data (expression trees) instead of as code (delegates).



Les nouveautés de C# 3.0
C# vers un langage fonctionnel de plus en plus déclaratif. 


## Type inference with "var"

var remplace le type dans une déclaration car celui-ci sera deviné automatiquement en fonction de celui de
l’expression (inférence du type). Une fois le type attribué il ne sera pas modifiable et la
variable se comporte exactement comme si elle avait été déclarée de façon traditionnelle.
A la compilation à une déclaration de type tout à fait classique.

var est aussi le seul moyen de déclarer des variables avec un type anonyme
ne peut être utilisé qu’à l’intérieur d’une portée locale

Code plus lisible: évite d'écrire deux fois « MonTypeObjet » :
	MonTypeObjet unObjet = new MonTypeObjet() ;
	var unObject = new MonTypeObjet() ;

var a = 3 ; // a sera de type int
var b = "Salut !" ; // b sera de type string
var q = 52.8 ; // q sera un double
var z = q / a ; // z aussi
var m = b.Length() ; // m sera un int
decimal d ; var f = d ; // f sera un decimal
var o = default(string) ; // o sera un string. retourne la valeur nulle par défaut pour le type considéré
var t = null ; // Interdit ! // le type ne peut pas être inféré…



## Expressions Lambda

prolongement des méthodes anonymes de C#2.0 
Simplicité et élégance pour un code plus lisible, plus flexible et plus puissant

méthode anonyme: méthode… sans nom, morceau de code représentant le corps d’une méthode qu’on peut placer là où un pointeur de code (un delegate) est attendu, et ce, dans le respect de la déclaration du delegate 

    x => x + 1						// Implicitly typed, expression body
    x => { return x + 1; }			// Implicitly typed, statement body
    (int x) => x + 1				// Explicitly typed, expression body
    (int x) => { return x + 1; }	// Explicitly typed, statement body
    (x, y) => x * y					// Multiple parameters
    () => Console.WriteLine()		// No parameters


C# 2.0

public class DemoDelegate
{
  delegate T Func<T>(T a, T b);
  static T Agreger<T>(List<T> l, Func<T> f)
  {
    T result = default(T);
    bool premierPassage = true;
    foreach (T value in l) 
    {
     if (premierPassage)
      {
	result = value;
	premierPassage = false;
      }
      else
      {
	result = f(result, value);
      }
   }
   return result;
  }

public static void LancerDemo()
{
  int somme;
  List<int> lesEntiers = new List<int> {1,2,3,4,5,6,7,8,9};
  somme = DemoDelegate.Agreger(lesEntiers, delegate(int a, int b) { return a + b; } );
  Console.WriteLine("La somme = {0}", somme);
}

}
static void Main(string[] args)
{
  DemoDelegate.LancerDemo();
}

expressions Lambda pour réécrire le code de la méthode LancerDemo :
public static void LancerDemoCS3()
{
  int somme; 
  List<int> lesEntiers = new List<int> {1,2,3,4,5,6,7,8,9};
  somme = DemoDelegate.Agreger(lesEntiers, (int x, int y) => { return x + y; });
  Console.WriteLine("La somme = {0}", somme);
}

Expression = « étant donné les paramètres x et y de type entier, retourner la somme de x et y. »
Les expressions lambda supportent le typage implicite des paramètres: (x, y) => { return x + y; }
L’inférence des types est effectuée à la compilation, bien entendu, et non à l’exécution.

=> « Tel Que » si prédicat (expression booléenne généralement utilisée pour créer un filtre )
=> « Deviens » si projection (expression retournant un type différent de son unique paramètre)

somme = DemoDelegate.Agreger(lesEntiers, (x, y) => x + y );


Encore plus simple:

public delegate T Func2<T>(T x);
public static T Agreger2<T>(List<T> l, Func2<T> f)
{
 T result = default(T);
 foreach (T value in l) result = f(value);
 return result;
}

public static void LancerDemoCS3v4()
{
 Single somme=0f;
 List<Single> lesSimples = new List<Single> { 1.5f, 2.6f, 3.7f, 4.8f, 5.9f, 6.0f, 7.1f, 8.2f, 9.3f };
 somme = DemoDelegate.Agreger2(lesSimples, (x) => somme += x);
 Console.WriteLine("La somme = {0}", somme);
}

elle peut se permettre d’utiliser la variable locale somme à l’intérieur même de sa définition. 
En effet, somme est une locale de la méthode contenant l’expression et sa portée ainsi que sa durée de vie sont étendues à l’instance de la méthode anonyme définit par l’expression Lambda.

Lorsqu’il n’y a qu’un seul paramètre on peut omettre les parenthèses qui l’entourent: x => somme += x

Que des petits bouts de code et non des pages entières :  filtres ou autres fonctions de ce type ne réclamant que quelques instructions au maximum. 


Code de type filtrage (prédicat):
public class DemoPredicat
{
 public static void AfficheListe<T>(T[] items, Func<T, bool> leFiltre)
 {
  foreach (T item in items) if (leFiltre(item)) Console.WriteLine(item);
 }

 public static void lancerDemo()
 {
  string[] villes = { "Paris", "Berlin", "Londres", "New-york", "Barcelone", "Milan" };
  Console.WriteLine("Les villes sans 'e' dans leur nom sont:");
  AfficheListe(villes, s => !s.Contains('e'));
  Console.WriteLine("Les villes ayant 'i' dans leur nom sont:");
  AfficheListe(villes, s => s.Contains('i'));
 }
}

Les expressions Lambda rendent le code concis et clair. 
pas de delegate déclaré. Nous avons utilisé une déclaration existante dans le Framework:

• public delegate T Func< T >();
• public delegate T Func< A0, T >( A0 arg0 );
• public delegate T Func<A0, A1, T> ( A0 arg0, A1 arg1 );
• public delegate T Func<A0, A1, A2, T >( A0 arg0, A1 arg1, A2 arg2 );
• public delegate T Func<A0, A1, A3, T> ( A0 arg0, A1 arg1, A2 arg2, A3 arg3 );

Il n’y a bien entendu aucune obligation d’utiliser ces types définis dans System.Linq
(ajouté automatiquement aux projets sous VS 2008). Vous pouvez utiliser vos propres types.
Il n’y a qu’un seul cas dans lequel il faut respecter les définitions de delagate présentées cidessus
: lorsqu’on veut transformer une expression en arbre d’expression.



## Les arbres d’expression

ces ajouts au langage ont été faits surtout pour faciliter l’implémentation de Linq… 
Linq impose de pouvoir transformer une expression en un arbre facilement navigable pour transformer les
requêtes Linq C# en syntaxe SQL (Linq to ADO.NET)  conforme à la base cible. Cette dernière dépendant de la connexion et de la base cible, de son langage, des champs, Linq a besoin d’interpréter les arbres à ce moment et non à la compilation.
	expression Lambda binaire: compilée code IL
	arbre expression : une représentation mémoire dynamique (modifiable notamment), runtime.

Expression trees permit lambda expressions to be represented as data structures instead of executable code. A lambda expression that is convertible to a delegate type D is also convertible to an expression tree of type System.Query.Expression<D>. Whereas the conversion of a lambda expression to a delegate type causes executable code to be generated and referenced by a delegate, conversion to an expression tree type causes code that creates an expression tree instance to be emitted. Expression trees are efficient in-memory data representations of lambda expressions and make the structure of the expression transparent and explicit.
The following example represents a lambda expression both as executable code and as an expression tree. Because a conversion exists to Func<int,int>, a conversion also exists to Expression<Func<int,int>>.

Func<int,int> f = x => x + 1;					// Code
Expression<Func<int,int>> e = x => x + 1;		// Data

Delegate f references a method that returns x+1
Expression tree e references a data structure that describes the expression x+1



## Les méthodes d’extension (class helpers)
Pouvoir ajouter des méthodes à une classe sans modifier la dite classe…
Pour simplifier la syntaxe de Linq, la rendre plus lisible et plus concise.

public struct Article
{
 public int Code;
 public string Désignation;
 public override string ToString()  { return Code + ", " + Désignation; }
 public Article(int code, string designation)  { Code = code; Désignation = designation; }
}

public struct Client
{
 public int Code;
 public string Société;
 public override string ToString() { return Code + ", " + Société; }
 public Client(int code, string société)  { Code = code; Société = société; }
}

public static class DemoHelpers
{
 public static void LanceDemo()
 {
  Article a = new Article(101, "Zune 20 Go");
  Client c = new Client(5800, "E-Naxos");
  a.Affiche(); // appel « magique » à Affiche
  c.Affiche(); 
 }
}

// déclaré non imbriqué dans une autre classe
public static class Afficheur
{
  public static void Affiche(this object o)
  { Console.WriteLine(o.ToString()); }
}

Article et Client ne partageant rien en commun. 
Les paramètres de Affiche, et l’utilisation de this, en font automatiquement un class helper.
C’est ce qui permet d’appeler Affiche depuis des instances de Article ou de Client. 
Si void Affiche(Article): seule la classe Article aurait pu utiliser Affiche 


namespace Acme.Utilities
{
	public static class Extensions
	{
		public static int ToInt32(this string s) {
			return Int32.Parse(s);
		}
		public static T[] Slice<T>(this T[] source, int index, int count) {
			if (index < 0 || count < 0 || source.Length – index < count)
				throw new ArgumentException();
			T[] result = new T[count];
			Array.Copy(source, index, result, 0, count);
			return result;
		}
	}
}




## Les expressions d’initialisation des objets

C# 1.0 proposait déjà quelques facilités syntaxiques, pour rappel :
string s = "Bonjour" ;
single x = 10.0f ;
Synthé synthé = new Synthé("Prophet",5,"Sequential Circuit") ; // Cette Approche oblige à coder les surcharges du ctor

C#3.0:


public class Point
{
	int x, y;
	public int X { get { return x; } set { x = value; } }
	public int Y { get { return y; } set { y = value; } }
}
var a = new Point { X = 0, Y = 1 };

which has the same effect as
var a = new Point(); a.X = 0; a.Y = 1;


public class Rectangle
{
	Point p1, p2;
	public Point P1 { get { return p1; } set { p1 = value; } }
	public Point P2 { get { return p2; } set { p2 = value; } }
}

var r = new Rectangle {
	P1 = new Point { X = 0, Y = 1 },
	P2 = new Point { X = 2, Y = 3 }
};



int i = 5;
string s = "Hello";
double d = 1.0;

int[] numbers = new int[] {1, 2, 3};
int[] numbers = { 1, 3, 5, 7, 9 };
foreach (var n in numbers) Console.WriteLine(n);
var a = new[] { 1, 10, 100, 1000 };				// int[]
var b = new[] { 1, 1.5, 2, 2.5 };				// double[]
var c = new[] { "hello", null, "world” };		// string[]

var contacts = new[] {
	new {
		Name = "Chris Smith",
		PhoneNumbers = new[] { "206-555-0101", "425-882-8080" }
	},
	new {
		Name = "Bob Harris",
		PhoneNumbers = new[] { "650-555-0199" }
	}


List<int> digits = new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
Dictionary<int,Order> orders = new Dictionary<int,Order>();






## Les types anonymes

An anonymous object initializer declares an anonymous type and returns an instance of that type. An anonymous type is a nameless class type that inherits directly from object. The members of an anonymous type are a sequence of read/write properties inferred from the object initializer(s) used to create instances of the type. 

* The name of an anonymous type is automatically generated by the compiler and cannot be referenced in program text.

new { p1 = e1 , p2 = e2 , … pn = en } declares an anonymous type of the form
class __Anonymous1
{
	private T1 f1 ;
	private T2 f2 ;
	…
	private Tn fn ;
	public T1 p1 { get { return f1 ; } set { f1 = value ; } }
	public T2 p2 { get { return f2 ; } set { f2 = value ; } }
	…
	public T1 p1 { get { return f1 ; } set { f1 = value ; } }
}

* Two anonymous object initializers that specify a sequence of properties of the same names and types in the same order will produce instances of the same anonymous type. 

var p1 = new { Name = "Lawnmower", Price = 495.00 };
var p2 = new { Name = "Shovel", Price = 26.95 };
p1 = p2; // permitted assignment because p1 and p2 are of the same anonymous type



var truc = new { Couleur = Color.Red, Forme = "Carré" };
var bidule = new { Marque = "Intel", Type = "Xeon", Coeurs = 4 };
Console.WriteLine("la couleur du truc est " + truc.Couleur +" et sa forme est un " + truc.Forme);
Console.WriteLine("le processeur est un " + bidule.Type + " de chez " + bidule.Marque + " avec " + bidule.Coeurs + " coeurs.");

Output:
la couleur du truc est Color [Red] et sa forme est un Carré
le processeur est un Xeon de chez Intel avec 4 coeurs.

C# créé bien des classes (un type) pour truc et bidule 
GetType() donne
truc est   <>f__AnonymousType0`2[System.Drawing.Color,System.String]
bidule est <>f__AnonymousType1`3[System.String,System.String,System.Int32]

Si nous créons un objet trucbis définit de la même façon que l’objet truc et que nous inspectons les types, 
nous trouverons le même type que l’objet truc, ce qui les rend compatibles pour d’éventuelles manipulations groupées !

Les propriétés doivent être définies dans le même ordre, si nous inversions Couleur et Forme, un nouveau type sera créé par le compilateur.
Linq a besoin de pouvoir créer de types qui n’existent pas, par exemple créer un objet qui représente chaque ligne du résultat d’un SELECT, 
et il a besoin de faire la différence dans l’ordre des champs puisque dans un SELECT l’ordre peut avoir une importance.

## Query expressions

Query expressions provide a language integrated syntax for queries that is similar to relational and hierarchical query languages such as SQL and XQuery.

A query expression 
- begins with a ***from*** clause
- ends with either a ***select or group*** clause

The initial from clause can be followed by zero or more from, let, or where clauses. Each from clause is a generator that introduces one or more iteration variables ranging over a sequence or a join of multiple sequences, each let clause computes a value and introduces an identifier representing that value, and each where clause is a filter that excludes items from the result. The final select or group clause specifies the shape of the result in terms of the iteration variable(s). The select or group clause may be preceded by an orderby clause that specifies an ordering for the result. Finally, an into clause can be used to “splice” queries by treating the results of one query as a generator in a subsequent query.

C# 3.0 translates query expressions into invocations of methods that adhere to the query expression pattern. Specifically, query expressions are translated into invocations of methods named Where, Select, SelectMany, Join, GroupJoin, OrderBy, OrderByDescending, ThenBy, ThenByDescending, GroupBy, and Cast that are expected to have particular signatures and result types
These methods can be instance methods of the object being queried or extension methods that are external to the object, and they implement the actual execution of the query

from Customer c in customers where c.City == "London" select c
is translated into
from c in customers.Cast<Customer>() where c.City == "London" select c
the final translation of which is
customers.Cast<Customer>().Where(c => c.City == "London")


from c in customers group c by c.Country into g select new { Country = g.Key, CustCount = g.Count() }
is translated into
from g in from c in customers group c by c.Country select new { Country = g.Key, CustCount = g.Count() }
the final translation of which is
customers.GroupBy(c => c.Country).Select(g => new { Country = g.Key, CustCount = g.Count() })

from x1 in e1 join x2 in e2 on k1 equals k2
is translated into
from * in (	from x1 in e1 join x2 in e2 on k1 equals k2 select new { x1 , x2 })
A from clause followed by a join clause with an into followed by something other than a select clause
from x1 in e1 join x2 in e2 on k1 equals k2 into g
is translated into
from * in (	from x1 in e1 join x2 in e2 on k1 equals k2 into g select new { x1 , g } )

from c in customers join o in orders on c.CustomerID equals o.CustomerID select new { c.Name, o.OrderDate, o.Total }
 has the final translation
customers.Join(orders, c => c.CustomerID, o => o.CustomerID, (c, o) => new { c.Name, o.OrderDate, o.Total })

from c in customers join o in orders on c.CustomerID equals o.CustomerID into co
let n = co.Count()
where n >= 10
select new { c.Name, OrderCount = n }
is translated into
from * in
	from c in customers
	join o in orders on c.CustomerID equals o.CustomerID into co
	select new { c, co }
let n = co.Count()
where n >= 10 
select new { c.Name, OrderCount = n }
the final translation of which is
customers.GroupJoin(orders, c => c.CustomerID, o => o.CustomerID, (c, co) => new { c, co }).Select(x => new { x, n = x.co.Count() }).Where(y => y.n >= 10).Select(y => new { y.x.c.Name, OrderCount = y.n)


A from clause immediately followed by a let clause
from x in e let y = f
is translated into
from * in (from x in e select new { x , y = f })

A from clause immediately followed by a where clause
from x in e where f
is translated into
from x in ( e ) . Where ( x => f )

from o in orders let t = o.Details.Sum(d => d.UnitPrice * d.Quantity)
where t >= 1000
select new { o.OrderID, Total = t }
is translated into
from * in
	from o in orders
	select new { o, t = o.Details.Sum(d => d.UnitPrice * d.Quantity) }
where t >= 1000 
select new { o.OrderID, Total = t }
the final translation of which is
orders.Select(o => new { o, t = o.Details.Sum(d => d.UnitPrice * d.Quantity) }).
Where(x => x.t >= 1000).Select(x => new { x.o.OrderID, Total = x.t })

from x1 in e1 from x2 in e2 select v
is translated into
from t in (e1).SelectMany ( x1 => from x2 in e2 select v ) select t


from x1 in e1 from x2 in e2 …
is translated into
from * in (
	from x1 in e1 from x2 in e2 … select new { x1 , x2 … }
)
The translations in the following sections assume that queries have only one from clause.
The example
from c in customers
from o in c.Orders
select new { c.Name, o.OrderID, o.Total }
is translated into
from t in
	customers.SelectMany(c =>
		from o in c.Orders
		select new { c.Name, o.OrderID, o.Total }
	)
select t
the final translation of which is
customers.
SelectMany(c =>
	c.Orders.
	Select(o => new { c.Name, o.OrderID, o.Total })
)
The example
from c in customers
from o in c.Orders
orderby o.Total descending
select new { c.Name, o.OrderID, o.Total }
is translated into
from * in
	from c in customers
	from o in c.Orders
	select new { c, o }
orderby o.Total descending
select new { c.Name, o.OrderID, o.Total }
the final translation of which is
customers.
SelectMany(c =>
	c.Orders.
	Select(o => new { c, o })
).
OrderByDescending(x => x.o.Total).
Select(x => new { x.c.Name, x.o.OrderID, x.o.Total })



from x in e orderby k1 , k2 …
is translated into
from x in (e).OrderBy(x => k1).ThenBy(x => k2 ) …

from o in orders orderby o.Customer.Name, o.Total descending select o
has the final translation
orders.OrderBy(o => o.Customer.Name).ThenByDescending(o => o.Total)


from x in e select v
is translated into
( e ) . Select ( x => v )
except when v is the identifier x, the translation is simply
( e )

from c in customers select c
is simply translated into
customers

from x in e group v by k
is translated into
( e ) . GroupBy ( x => k , x => v )
except when v is the identifier x, the translation is
( e ) . GroupBy ( x => k )

from c in customers group c.Name by c.Country
is translated into
customers.GroupBy(c => c.Country, c => c.Name)


Transparent identifiers

from c in customers
from o in c.Orders
orderby o.Total descending
select new { c.Name, o.Total }
is translated into
from * in
	from c in customers
	from o in c.Orders
	select new { c, o }
orderby o.Total descending
select new { c.Name, o.Total }
which is further translated into
customers.SelectMany(c => c.Orders.Select(o => new { c, o })).OrderByDescending(* => o.Total).Select(* => new { c.Name, o.Total })
which, when transparent identifiers are erased, is equivalent to
customers.SelectMany(c => c.Orders.Select(o => new { c, o })).OrderByDescending(x => x.o.Total).Select(x => new { x.c.Name, x.o.Total })


from c in customers
join o in orders on c.CustomerID equals o.CustomerID
join d in details on o.OrderID equals d.OrderID
join p in products on d.ProductID equals p.ProductID
select new { c.Name, o.OrderDate, p.ProductName }

customers.Join(orders, c => c.CustomerID, o => o.CustomerID, (c, o) => new { c, o }).
Join(details, * => o.OrderID, d => d.OrderID, (*, d) => new { *, d }).
Join(products, * => d.ProductID, p => p.ProductID, (*, p) => new { *, p }).
Select(* => new { c.Name, o.OrderDate, p.ProductName })
the final translation of which is
customers.Join(orders, c => c.CustomerID, o => o.CustomerID, (c, o) => new { c, o }).Join(details, x => x.o.OrderID, d => d.OrderID, (x, d) => new { x, d }).Join(products, y => y.d.ProductID, p => p.ProductID, (y, p) => new { y, p }).Select(z => new { z.y.x.c.Name, z.y.x.o.OrderDate, z.p.ProductName })
where x, y, and z are compiler generated identifiers that are otherwise invisible and inaccessible.



query-expression:
    from-clause   query-body

from-clause:
    from   typeopt   identifier   in   expression   join-clausesopt

join-clauses:
    join-clause
    join-clauses   join-clause

join-clause:
    join   typeopt   identifier   in   expression   on   expression   equals   expression
    join   typeopt   identifier   in   expression   on   expression   equals   expression   into   identifier

query-body:
    from-let-where-clausesopt   orderby-clauseopt   select-or-group-clause   query-continuationopt

from-let-where-clauses:
    from-let-where-clause
    from-let-where-clauses   from-let-where-clause

from-let-where-clause:
    from-clause
    let-clause
where-clause

let-clause:
    let   identifier   =   expression

where-clause:
    where   boolean-expression

orderby-clause:
    orderby   orderings

orderings:
    ordering
    orderings   ,   ordering

ordering:
    expression    ordering-directionopt

ordering-direction:
    ascending
    descending

select-or-group-clause:
    select-clause
    group-clause

select-clause:
    select   expression

group-clause:
    group   expression   by   expression

query-continuation:
    into   identifier   join-clausesopt   query-body


