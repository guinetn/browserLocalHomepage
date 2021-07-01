## DEFAULT-VALUES

|Type | value |
|---|---|
| Any reference type | null| 
| Any built-in integral numeric type | 0 (zero)| 
| Any built-in floating-point numeric type | 0 (zero)| 
| bool | false| 
| char | '\0' (U+0000)| 
| enum | Value produced by (E)0, where E is the enum identifier| 
| struct | Value produced by setting all value-type fields to their default values and all reference-type fields to null|
| Any nullable value type | An instance for which the HasValue property is false and the Value property is undefined. That default value is also known as the null value of a nullable value type|

Use the default operator to produce the default value of a type, as the following example shows:

int a = default(int);
Beginning with C# 7.1, you can use the default literal to initialize a variable with the default value of its type:

int a = default;
For a value type, the implicit parameterless constructor also produces the default value of the type, as the following example shows:

var n = new System.Numerics.Complex();
Console.WriteLine(n);  // output: (0, 0)

https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/default-values