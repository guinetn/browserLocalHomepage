# HASHTABLE

non-generic collection: so you must TYPE CAST VALUES while retrieving it.
stores key-value pairs ~ generic Dictionary<TKey, TValue> 
It optimizes lookups by computing the hash code of each key and stores it in a different bucket internally and then matches the hash code of the specified key at the time of accessing values.

System.Collection namespace
Implements IDictionary interface
Keys must be unique and cannot be null.
Values can be null or duplicate.
Values can be accessed by passing associated key in the indexer e.g. myHashtable[key]
Elements are stored as DictionaryEntry objects.

```cs
Hashtable numberNames = new Hashtable();
numberNames.Add(1,"One"); //adding a key/value using the Add() method
numberNames.Add(2,"Two");
numberNames.Add(3,"Three");
numberNames.Add(3, "Three"); // run-time exception: key already added.

foreach(DictionaryEntry de in numberNames)
    Console.WriteLine("Key: {0}, Value: {1}", de.Key, de.Value);
		
//creating a Hashtable using collection-initializer syntax
var cities = new Hashtable(){
	{"UK", "London, Manchester, Birmingham"},
	{"USA", "Chicago, New York, Washington"},
	{"India", "Mumbai, New Delhi, Pune"}
};
		
foreach(DictionaryEntry de in cities)
    Console.WriteLine("Key: {0}, Value: {1}", de.Key, de.Value);

// Update
string citiesOfUK = (string) cities["UK"];      // non-generic: need to cast values to string
string citiesOfUSA = (string) cities["USA"];    // cast to string
Console.WriteLine(citiesOfUK);
cities["UK"] = "Liverpool, Bristol"; // update value of UK key
Console.WriteLine(citiesOfUK);

if(!cities.ContainsKey("France")){
    cities["France"] = "Paris";    
    
cities.Remove("UK"); // removes UK 
    
// Add Dictionary in Hashtable    
Dictionary<int, string> dict = new Dictionary<int, string>();
dict.Add(1, "one");
dict.Add(2, "two");
dict.Add(3, "three");

Hashtable ht = new Hashtable(dict);    
```    

### Hashtable vs Dictionary

|Hashtable|Dictionary|
|---|---|
|Hashtable is included in the System.Collections namespace|	Dictionary is included in the System.Collections.Generic namespace|
|Hashtable is a loosely typed (non-generic) collection, this means it stores key-value pairs of any data types|Dictionary is a generic collection. So it can store key-value pairs of specific data types|
|Hashtable is thread safe|	Only public static members are thread safe in Dictionary|
|Hashtable returns null if we try to find a key which does not exist|	Dictionary throws an exception if we try to find a key which does not exist|
|Data retrieval is slower than dictionary because of boxing-unboxing|	Data retrieval is faster than Hashtable|