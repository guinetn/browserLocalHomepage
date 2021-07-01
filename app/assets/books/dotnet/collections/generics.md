# Generics

Generic means not specific to a particular data type.
- Increases the reusability: don't need to write code to handle different data types
- Generics are type-safe. You get compile-time errors if you try to use a different data type than the one specified in the definition.
- Generic has a performance advantage because it removes the possibilities of boxing and unboxing.
Declared by specifying a type parameter in an angle brackets
 
C# allows you to define generic classes, interfaces, abstract classes, fields, methods, static methods, properties, events, delegates, and operators 
Use the type parameter: 
- a placeholder for a particular type specified when creating an instance of the generic type
- It is not required to use T as a type parameter

```cs
static T[] Shuffle<T>(T[] array)
{
    Random rand = new Random();
    for (int i = 0; i < array.Length; i++)
    {
        int r = i + rand.Next(array.Length - i);
        T temp = array[r];
        array[r] = array[i];
        array[i] = temp;
    }
    return array;
}

int[] randomIndices = Shuffle(Enumerable.Range(0, (int)Rows.Count).ToArray());
```

```cs

class DataStore<T>
{
    public T Data { get; set; }
}

// multiple type parameters separated by a comma
class KeyValuePair<TKey, TValue>
{
    public TKey Key { get; set; }
    public TValue Value { get; set; }
}

DataStore<string> store = new DataStore<string>();
store.Data = "Hello World!";
//obj.Data = 123; //compile-time error
```

Generic Method in Non-generic Class
```cs
class Printer
{
    public void Print<T>(T data)
    {
        Console.WriteLine(data);
    }
}

Printer printer = new Printer();
printer.Print<int>(100);
printer.Print(200); // type infer from the specified value
printer.Print<string>("Hello");
printer.Print("World!"); // type infer from the specified value
```

Generic Fields
```cs
class DataStore<T>
{
    public T data;
    public T[] data = new T[10];
}
```

Generic Methods
```cs
class DataStore<T>
{
    private T[] _data = new T[10];
    
    public void AddOrUpdate(int index, T item)
    {
        if(index >= 0 && index < 10)
            _data[index] = item;
    }

    public T GetData(int index)
    {
        if(index >= 0 && index < 10)
            return _data[index];
        else 
            return default(T);
    }
}

DataStore<string> cities = new DataStore<string>();
cities.AddOrUpdate(0, "Mumbai");
cities.AddOrUpdate(1, "Chicago");
cities.AddOrUpdate(2, "London");

DataStore<int> empIds = new DataStore<int>();
empIds.AddOrUpdate(0, 50);
empIds.AddOrUpdate(1, 65);
```

## constraints
GenericTypeName<T> where T  : contraint1, constraint2

Restrict client code to specify certain types while instantiating generic types. It will give a compile-time error if you try to instantiate a generic type using a type that is not allowed by the specified constraints.

```cs
class DataStore<T> where T : class
{
    public T Data { get; set; }
}

DataStore<string> store = new DataStore<string>(); // valid
DataStore<MyClass> store = new DataStore<MyClass>(); // valid
DataStore<IMyInterface> store = new DataStore<IMyInterface>(); // valid
DataStore<IEnumerable> store = new DataStore<IMyInterface>(); // valid
DataStore<ArrayList> store = new DataStore<ArrayList>(); // valid
//DataStore<int> store = new DataStore<int>(); // compile-time error 


class DataStore<T> where T : struct
{
    public T Data { get; set; }
}
DataStore<int> store = new DataStore<int>(); // valid
DataStore<char> store = new DataStore<char>(); // valid
DataStore<MyStruct> store = new DataStore<MyStruct>(); // valid
//DataStore<string> store = new DataStore<string>(); // compile-time error 
//DataStore<IMyInterface> store = new DataStore<IMyInterface>(); // compile-time error 
//DataStore<ArrayList> store = new DataStore<ArrayList>(); // compile-time error 


class DataStore<T> where T : class, new()
{
    public T Data { get; set; }
}

DataStore<MyClass> store = new DataStore<MyClass>(); // valid
DataStore<ArrayList> store = new DataStore<ArrayList>(); // valid
//DataStore<string> store = new DataStore<string>(); // compile-time error 
//DataStore<int> store = new DataStore<int>(); // compile-time error 
//DataStore<IMyInterface> store = new DataStore<IMyInterface>(); // compile-time error 

// BaseClass constraint
class DataStore<T> where T : IEnumerable
{
    public T Data { get; set; }
}

DataStore<ArrayList> store = new DataStore<ArrayList>(); // valid
DataStore<List> store = new DataStore<List>(); // valid
//DataStore<string> store = new DataStore<string>(); // compile-time error 
//DataStore<int> store = new DataStore<int>(); // compile-time error 
//DataStore<IMyInterface> store = new DataStore<IMyInterface>(); // compile-time error 
//DataStore<MyClass> store = new DataStore<MyClass>(); // compile-time error 
```

|Constraint|Description|
|---|---|
|class  |  The type argument must be any class, interface, delegate, or array type|
|class?  |  The type argument must be a nullable or non-nullable class, interface, delegate, or array type|
|struct  |  The type argument must be non-nullable value types such as primitive data types int, char, bool, float, etc|
|new()  |  The type argument must be a reference type which has a public parameterless constructor. It cannot be combined with struct and unmanaged constraints|
|notnull  |  Available C# 8.0 onwards. The type argument can be non-nullable reference types or value types. If not, then the compiler generates a warning instead of an error|
|unmanaged  |  The type argument must be non-nullable unmanged types|
|base class name  |  The type argument must be or derive from the specified base class. The Object, Array, ValueType classes are disallowed as a base class constraint. The Enum, Delegate, MulticastDelegate are disallowed as base class constraint before C# 7.3|
|<base class name>?  |  The type argument must be or derive from the specified nullable or non-nullable base clas|
|<interface name>  |  The type argument must be or implement the specified interface|
|<interface name>?  |  The type argument must be or implement the specified interface. It may be a nullable reference type, a non-nullable reference type, or a value typ|
|where T: U  |  The type argument supplied for T must be or derive from the argument supplied for U|



```cs
class ItemList<T>: List<T>
{
	public int Sum<T>(Func<T,int> selector) {
		int sum = 0;
		foreach (T item in this) sum += selector(item);
		return sum;
	}
	public double Sum<T>(Func<T,double> selector) {
		double sum = 0;
		foreach (T item in this) sum += selector(item);
		return sum;
	}
}
```

The ItemList<T> class has two Sum methods. Each takes a selector argument, which extracts the value to sum over from a list item. The extracted value can be either an int or a double and the resulting sum is likewise either an int or a double.
The Sum methods could for example be used to compute sums from a list of detail lines in an order.

```cs
class Detail
{
	public int UnitCount;
	public double UnitPrice;
	...
}
void ComputeSums() {
	ItemList<Detail> orderDetails = GetOrderDetails(...);
	int totalUnits = orderDetails.Sum(d => d.UnitCount);
	double orderTotal = orderDetails.Sum(d => d.UnitPrice * d.UnitCount);
	...
}
```