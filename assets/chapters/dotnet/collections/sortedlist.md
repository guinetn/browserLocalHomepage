# SortedList

Store key-value pairs that are sorted by the keys based on the associated IComparer implementation. 
Generic and non-generic SortedList
Generic SortedList<TKey, TValue> performs faster and less error-prone than the non-generic SortedList.

SortedList<TKey, TValue> is an array of key-value pairs sorted by keys.
Sorts elements as soon as they are added. Sorts primitive type keys in ascending order and object keys based on IComparer<T>.
Comes under System.Collection.Generic namespace.
A key must be unique and cannot be null.
A value can be null or duplicate.
A value can be accessed by passing associated key in the indexer mySortedList[key]
Contains elements of type KeyValuePair<TKey, TValue>
It uses less memory than SortedDictionary<TKey,TValue>.
It is faster in the retrieval of data once sorted, whereas SortedDictionary<TKey, TValue> is faster in insertion and removing key-value pairs.

```cs
//SortedList of int keys, string values 
SortedList<int, string> numberNames = new SortedList<int, string>();
numberNames.Add(3, "Three");
numberNames.Add(1, "One");
numberNames.Add(2, "Two");
numberNames.Add(4, null);
numberNames.Add(10, "Ten");
numberNames.Add(5, "Five");

//The following will throw exceptions
//numberNames.Add("Three", 3); //Compile-time error: key must be int type
//numberNames.Add(1, "One"); //Run-time exception: duplicate key
//numberNames.Add(null, "Five");//Run-time exception: key cannot be null
In the above example, a generic SortedList<TKey, TValue> object is created by specifying the type of keys and values it is going to store. The SortedList<int, string> will store keys of int type and values of string type.

The Add() method is used to add a single key-value pair in a SortedList. Keys cannot be null or duplicate. If found, it will throw a run-time exception. Values can be duplicate and null if the type is nullable.

Use the collection-initializer syntax to initialize a SortedList with multiple key-value pairs at the time of instantiating, as shown below.

//Creating a SortedList of string keys, string values 
//using collection-initializer syntax
SortedList<string,string> cities = new SortedList<string,string>()
                                    {
                                        {"London", "UK"},
                                        {"New York", "USA"},
                                        { "Mumbai", "India"},
                                        {"Johannesburg", "South Africa"}
                                    };
The SortedList rearranges key-value pairs in the ascending order of keys as soon as a key-value pair added. The following example displays all the keys and values using foreach loop.

Example: SortedList Elements Default Sorting Order
SortedList<int,string> numberNames = new SortedList<int,string>()
                                    {
                                        {3, "Three"},
                                        {5, "Five"},
                                        {1, "One"}
                                    };

Console.WriteLine("---Initial key-values--");

foreach(KeyValuePair<int, string> kvp in numberNames)
    Console.WriteLine("key: {0}, value: {1}", kvp.Key , kvp.Value );

numberNames.Add(6, "Six");
numberNames.Add(2, "Two");
numberNames.Add(4, "Four");

Console.WriteLine("---After adding new key-values--");

foreach(var kvp in numberNames)
    Console.WriteLine("key: {0}, value: {1}", kvp.Key , kvp.Value );
Output:
---Initial key-values--
key: 1, value: One
key: 3, value: Three
key: 5, value: Five
---After adding new key-values--
key: 1, value: One
key: 2, value: Two
key: 3, value: Three
key: 4, value: Four
key: 5, value: Five
key: 6, value: Six
ADVERTISEMENT

Accessing SortedList
Specify a key in the indexer sortedList[key], to get or set a value in the SortedList.

Example: Access SortedList Values
SortedList<int,string> numberNames = new SortedList<int,string>()
                                    {
                                        {3, "Three"},
                                        {1, "One"},
                                        {2, "Two"}
                                    };

Console.WriteLine(numberNames[1]); //output: One
Console.WriteLine(numberNames[2]); //output: Two
Console.WriteLine(numberNames[3]); //output: Three
//Console.WriteLine(numberNames[10]); //run-time KeyNotFoundException

numberNames[2] = "TWO"; //updates value
numberNames[4] = "Four"; //adds a new key-value if a key does not exists
Above, numberNames[10] will throw a KeyNotFoundException because specified key 10 does not exist in a sortedlist. To prevent this exception, use ContainsKey() or TryGetValue() methods, as shown below.

Example: ContainsKey() and TryGetValue()
SortedList<int, string> numberNames = new SortedList<int,string>()
                                    {
                                        {3, "Three"},
                                        {1, "One"},
                                        {2, "Two"}
                                    };
if(numberNames.ContainsKey(4)){
    numberNames[4] = "four";
}

int result;
if(numberNames.TryGetValue(4, out result))
    Console.WriteLine("Key: {0}, Value: {1}", 4, result); 
Output:
Key:4, Value: Four
Use Keys and Values properties if you want to iterate a SortedList using a for loop.

Example: Iterate SortedList using For Loop
SortedList<int, string> numberNames = new SortedList<int,string>()
                                    {
                                        {3, "Three"},
                                        {1, "One"},
                                        {2, "Two"}
                                    };
for (int i = 0; i < numberNames.Count; i++)
{
    Console.WriteLine("key: {0}, value: {1}", numberNames.Keys[i], numberNames.Values[i]);
}
Output:
key: 1, value: One
key: 2, value: Two
key: 3, value: Three
Remove Elements from SortedList
Use the Remove(key) and RemoveAt(index) methods to remove key-value pairs from a SortedList.

Example: Remove Elements
SortedList<int,string> numberNames = new SortedList<int,string>()
                                    {
                                        {3, "Three"},
                                        {1, "One"},
                                        {2, "Two"},
                                        {5, "Five"},
                                        {4, "Four"}
                                    };
    
numberNames.Remove(1);//removes key 1 pair
numberNames.Remove(10);//removes key 1 pair, no error if not exists

numberNames.RemoveAt(0);//removes key-value pair from index 0 
//numberNames.RemoveAt(10);//run-time exception: ArgumentOutOfRangeException

foreach(var kvp in numberNames)
	Console.WriteLine("key: {0}, value: {1}", kvp.Key , kvp.Value );
```cs
    