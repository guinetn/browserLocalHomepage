# json in C#

2 ways to work .NET objects to JSON:
- DataContractJsonSerializer 
- JsonSerializer 

## Getting the New JSON Library
If you’re targeting .NET Core. Install the latest version of the NET Core. This gives you the new JSON library and the ASP.NET Core integration.
If you’re targeting .NET Standard or .NET Framework. Install the System.Text.Json NuGet package (make sure to include previews and install version 4.6.0-preview6.19303.8 or higher). In order to get the integration with ASP.NET Core, you must target .NET Core 3.0.

```c#
class Cellphone
    {
        public string Name { get; set; }
        public float Price { get; set; }
    }
    class Program
    {
        static async Task Main(string[] args)
        {
            
            using (FileStream fs = new FileStream("cellphone.json", FileMode.OpenOrCreate))
            {
                Cellphone cellphone1 = new Cellphone { Name = "Iphone 12", Price = 750.00f };
                await JsonSerializer.SerializeAsync<Cellphone>(fs, cellphone1);
                Console.WriteLine("We are done.File has benn saved");
            }
            
            using (FileStream fs = new FileStream("cellphone.json", FileMode.OpenOrCreate))
            {
                Cellphone restoredcellphone1 = await JsonSerializer.DeserializeAsync<Cellphone>(fs);
                Console.WriteLine($"Name: {restoredcellphone1.Name}  
                                  Price: {restoredcellphone1.Price}");
            }

            Console.ReadLine();
        }
    }
```

## JsonSerializerOptions
By default, the JsonSerializer serializes objects to minified code. With an add-on package like JsonSerializerOptions, you can customize the serialization / deserialization engine using the JsonSerializerOptions properties. Some of its properties are as given below:

- IgnoreReadOnlyProperties: Similarly sets whether read-only properties are serialized
- IgnoreNullValues: Sets whether to serialize / deserialize in json objects and their properties to null
- WriteIndented: Sets whether spaces are added to json (relatively speaking, for beauty). If set correctly, extra spaces
- AllowTrailingCommas: An element whether to add a comma after the last one to json. If equal is true, a comma is added

```c#
class Cellphone
{
    [JsonPropertyName("NameOfCellPhone")]
    public string Name { get; set; }
    [JsonIgnore]
    public float Price { get; set; }
}
class Program
{
    static void Main(string[] args)
    {
        Cellphone cellphone1 = new Cellphone() { Name = "Iphone 12", Price = 750.00f };
        string json = JsonSerializer.Serialize<Cellphone>(cellphone1);
        Console.WriteLine(json);
        Cellphone restoredPerson = JsonSerializer.Deserialize<Cellphone>(json);
        Console.WriteLine($"CellPhone: {restoredPerson.Name}
                          Price: {restoredPerson.Price}");

        Console.ReadLine();
    }
```

## More
- https://www.codeproject.com/Tips/5295019/Working-With-JSON-In-Csharp