# Dictionary 

System.Collection.Generic: Generic collection 
Dictionary<TKey, TValue> stores key-value pairs in no particular order.
Implements IDictionary<TKey, TValue> interface.
Keys must be unique and cannot be null.
Values can be null or duplicate.
Values can be accessed by passing associated key in the indexer e.g. myDictionary[key]
Elements are stored as KeyValuePair<TKey, TValue> objects.

```cs
IDictionary<int, string> numberNames = new Dictionary<int, string>();
numberNames.Add(1,"One"); //adding a key/value using the Add() method
numberNames.Add(2,"Two");
numberNames.Add(3,"Three");

//The following throws run-time exception: key already added.
//numberNames.Add(3, "Three"); 

foreach(KeyValuePair<int, string> kvp in numberNames)
    Console.WriteLine("Key: {0}, Value: {1}", kvp.Key, kvp.Value);
		
//creating a dictionary using collection-initializer syntax
// <= C# 5.0
var cities = new Dictionary<string, string>(){
	{"UK", "London, Manchester, Birmingham"},
	{"USA", "Chicago, New York, Washington"},
	{"India", "Mumbai, New Delhi, Pune"}
};

// C# 6.0
var cities = new Dictionary<string, string>(){
	["UK"] = "London, Manchester, Birmingham",
	["USA"] = "Chicago, New York, Washington",
	["India"] = "Mumbai, New Delhi, Pune"}
};
         
private static void Print(IEnumerable<KeyValuePair<string, ConsoleColor>> items)
{
    foreach (KeyValuePair<string, ConsoleColor> item in items)    
        Console.WriteLine("Key: {0}, Value: {1}", item.Key, item.Value);            
}
		
foreach(var kvp in cities)
    Console.WriteLine("Key: {0}, Value: {1}", kvp.Key, kvp.Value);
In the above example, numberNames is a Dictionary<int, string> type dictionary, so it can store int keys and string values. In the same way, cities is a Dictionary<string, string> type dictionary, so it can store string keys and string values. Dictionary cannot include duplicate or null keys, whereas values can be duplicated or null. Keys must be unique otherwise, it will throw a runtime exception.

Access Dictionary Elements
The Dictionary can be accessed using indexer. Specify a key to get the associated value. You can also use the ElementAt() method to get a KeyValuePair from the specified index.

Example: Access Dictionary Elements
var cities = new Dictionary<string, string>(){
	{"UK", "London, Manchester, Birmingham"},
	{"USA", "Chicago, New York, Washington"},
	{"India", "Mumbai, New Delhi, Pune"}
};

Console.WriteLine(cities["UK"]); //prints value of UK key
Console.WriteLine(cities["USA"]);//prints value of USA key
//Console.WriteLine(cities["France"]); // run-time exception: Key does not exist

//use ContainsKey() to check for an unknown key
if(cities.ContainsKey("France")){  
    Console.WriteLine(cities["France"]);
}

//use TryGetValue() to get a value of unknown key
string result;

if(cities.TryGetValue("France", out result))
{
    Console.WriteLine(result);
}

//use ElementAt() to retrieve key-value pair using index
for (int i = 0; i < cities.Count; i++)
{
    Console.WriteLine("Key: {0}, Value: {1}", 
                                            cities.ElementAt(i).Key, 
                                            cities.ElementAt(i).Value);
}


cities["UK"] = "Liverpool, Bristol"; // update value of UK key
cities["USA"] = "Los Angeles, Boston"; // update value of USA key
//cities["France"] = "Paris"; //throws run-time exception: KeyNotFoundException

if(cities.ContainsKey("France")){
    cities["France"] = "Paris";
}

cities.Remove("UK"); // removes UK 
```


```cs
 static IReadOnlyDictionary<string, string> DefaultConfigurationStrings{get;} = new Dictionary<string, string>() {
      ["Profile:UserName"] = Environment.UserName,
      [$"AppConfiguration:ConnectionString"] = DefaultConnectionString,
      [$"AppConfiguration:MainWindow:Height"] = "400",
      [$"AppConfiguration:MainWindow:Width"] = "600",
      [$"AppConfiguration:MainWindow:Top"] = "0",
      [$"AppConfiguration:MainWindow:Left"] = "0",
    };
```
