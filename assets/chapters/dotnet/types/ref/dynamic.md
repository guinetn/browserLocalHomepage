# dynamic

dynamic data = "Hi";
Console.WriteLine(data);
data = (double)data.Length;
Console.WriteLine(data);
data = data * 3.5 + 28.6;
Console.WriteLine(data);

dynamic person = DynamicXml.Parse(
@"<Person>
<FirstName>Joe</FirstName>
<LastName>Black</LastName>
</Person>");
Console.WriteLine($"{ person.FirstName } { person.LastName }");
