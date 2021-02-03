# TUPLE

- .Net 4.0 / c#7

An ordered sequence, immutable, fixed-size and of heterogeneous
An ordered sequence, immutable, fixed-size collection of heterogeneous objects, i.e.,
each object being of a specific type: allows us to group multiple kind of data type	objects.

Ordered sequence	The order of items in a tuple follows the order used at the time of its creation.
Immutable 			All properties are read-only tuple, i.e., once created, it cannot be changed.
Fixed size			The size is set at the time of its creation. If it was created with three items, you cannot add new items.
heterog. objects	Each item has a specific and independent of the type of the other item.

***Advantages***
    It provides a way to aggregate models without creating new class (ViewModel)
    For Return of Methods: a quick way to group multiple values into a single result, which can be very useful when used as a return of function
    For Composite Key in a Dictionary
***Disadvantages***
    Tuples is fixed size maximum limit of 8 items.
    As Tuples don’t have an explicit semantic meaning, your code becomes unreadable.
    Value is passes as item1, item2.....It is difficult to identify the arguments just by seeing the code.
    Not a great intellisense support in Visual Studio.

```cs
Create<T1>(T1)
Create<T1, T2>(T1, T2)
…
Create<T1, T2, T3, T4, T5, T6, T7, T8>(T1, T2, T3, T4, T5, T6, T7, T8)

Tuple<int, string, DateTime> _cliente = Tuple.Create(1, "Frederico", new DateTime(1975, 3,24));
var t8 = new Tuple<int,int,int,int,int,int,int,int>(1, 2, 3, 4, 5, 6, 7, 8);
var t8 = new Tuple<int,int,int,int,int,int,int,Tuple<int>> (1, 2, 3, 4, 5, 6, 7, Tuple.Create(8));
var Item8 = t8.Rest.Item1;
To create a tuple with more than 8 items, we do as follows:
    var t12 = new Tuple<int,int,int,int,int,int,int,Tuple<int,int,int,int, int>>
    (1, 2, 3, 4, 5, 6, 7, new Tuple<int,int,int, int,int>(8,9,10, 11, 12));
    <>var Item10 = t12.Rest.Item3;

// a tuple which is having lists of courses, faculties and students
public ActionResult TupleDemo()
{
    var allModels = new Tuple <List <Course>,
    List <Faculty>,  List <Student>>
    (_repository.GetCourses(), _repository.GetFaculties(),  _repository.GetStudents()) { };
        return View(allModels);
}
```


```cs
public static void Main()
{
    string root = Directory.GetCurrentDirectory();
    string searchPattern = "*";

    IEnumerable<string> fileList = Directory.EnumerateFiles(root, searchPattern);
    IEnumerable<(string FileName, long Size)> items = fileList.Select(file =>
        {
            FileInfo fileInfo = new FileInfo(file);
            return ( FileName: fileInfo.Name, Size: fileInfo.Length );
        });

    ListItems(items);
}

private static void ListItems(IEnumerable<(string FileName, long Size)> items)
{
    foreach((string FileName, long Size) item in items)    
        Console.WriteLine($"File: '{item.FileName}', Size:{item.Size}");    
}
```