## Attributes

```cs
[System.AttributeUsage(System.AttributeTargets.Class |  
                       System.AttributeTargets.Struct,
                       AllowMultiple = true)  // multiuse attribute 
]  
public class AuthorAttribute : System.Attribute  
{  
    private string name;  
    public double version;  
  
    public AuthorAttribute(string name)  
    {  
        this.name = name;  
        version = 1.0;  
    }  
}  

[Author("P. Ackerman", version = 1.1)]  
class SampleClass  
{  
    // P. Ackerman's code goes here...  
}  

[Author("P. Ackerman", version = 1.1)]  
[Author("R. Koch", version = 1.2)]  
class SampleClass  
{  
    // P. Ackerman's code goes here...  
    // R. Koch's code goes here...  
}  

// or
Author anonymousAuthorObject = new Author("P. Ackerman");  
anonymousAuthorObject.version = 1.1;  

// 2. Accessing Attributes (Reflection)

var t = typeof(SampleClass);
System.Attribute[] attrs = System.Attribute.GetCustomAttributes(t);  // Reflection.  

// Displaying output.  
foreach (System.Attribute attr in attrs)  
{  
    if (attr is Author)  
    {  
        Author a = (Author)attr;  
        System.Console.WriteLine("   {0}, version {1:f}", a.GetName(), a.version);  
    }  
}  

```

## Obsolete Attribute 

 Attribute read at compile time to generate a warning/an error
 To make sure programmers use newer versions of your methods. 
 Marks classes, methods, properties, fields, delegates... code deprecated or obsolete
 
Without arguments: generic compile-time warning
Take one or two optional parameters: Message and IsError

```c#
// Mark Method1 obsolete without a message
[ObsoleteAttribute]
public static string Method1() => return "You have called Method1.";

// Mark Method2 obsolete + a warning message
[ObsoleteAttribute("This method will soon be deprecated. Use MethodNew instead.")]
public static string Method2() => return "You have called Method2.";

// Mark Method3 obsolete + an error message
[ObsoleteAttribute("This method has been deprecated. Use MethodNew instead.", true)]
public static string Method3() => return "You have called Method3.";

public static string MethodNew() => return "You have called MethodNew.";
```