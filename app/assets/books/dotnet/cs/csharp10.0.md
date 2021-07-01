# C# 10 (.NET 6) #

slim down unnecessary code: Global using, file-scoped namespaces

valuable low-hanging fruit of language optimization. Large studies examining the cause of catastrophic programming failures suggest that the same easily avoidable mistakes happen again and again, not because the concepts in the code are too complex, but because reading code is tiring and humans have finite attention spans. Reducing the length of code reduces the time you need to review it, the cognitive load you need to process it, and the odds that you’ll skip over an actual bug because your attention has faded.


# Global using: cleaning up vertical waste

Define namespace imports across an entire project using the global keyword
It’s recommended that you place your global imports in a separate file (one for each project), possibly named usings.cs or imports.cs:
global using System;
global using System.Collections.Generic;
global using System.Linq;
global using System.Threading.Tasks;

# File-scoped namespaces: cleaning up horizontal waste

A file-scoped namespace applies automatically to your entire file, with no need to indent anything.

namespace LoggingTestApp
{
    public class Startup
    {
        ...
    }
}

           ↓

namespace LoggingTestApp;
public class Startup
{
    ...
}

# Null parameter checking

public UpdateAddress(int personId, Address newAddress)
{
    if (newAddress == null)
    {
        throw new ArgumentNullException("newAddress");
    }
    ...
}

↓  !! at the end of your parameter name = ask C# to insert this null check for you automatically

public UpdateAddress(int personId, Address newAddress!!)
{
    ...  if you pass a null value in the place of an Address object, the ArgumentNullException is thrown automatically.
}

# Required properties

public record Employee
{
    public string Name { get; init; }
    public decimal YearlySalary { get; init; }
    public DateTime HiredDate{ get; init; }
}
// create instances quickly with object initializer syntax:
var theNewGuy = new Employee
{
    Name = "Dave Bowman",       ← When object doesn’t make sense unless certain properties are set
    YearlySalary = 100000m,
    HiredDate = DateTime.Now()
};

public record Employee
{
    public required string Name { get; init; }   allow to creates an Employee but doesn’t set the Name property
    public decimal YearlySalary { get; init; }
    public DateTime HiredDate{ get; init; }
}

# field keyword

use the field keyword to access the backing field in a get, set, or init procedure.

Autoimplemented properties are great, but they can only take you so far. When they don’t suit, you’re forced to add the backing field to your class and write the usual property methods like you’re back in C# version 2. But in C# 10, there’s a new backdoor with the field keyword, which exposes the automatically created backing field.
For example, let’s say you want to create a record that does a little bit of processing to an initial property value. Here’s a revision of the Employee class that makes sure the HiredDate field only contains the date information from the DateTime object, and no time information:


public record Employee
{
    // three immutable properties using the get and init keywords. The data is stored in three private fields, but these fields are created for you automatically, and managed without your intervention. You never see them:

    public required string Name { get; init; }
    public decimal YearlySalary { get; init; }
    public DateTime HiredDate{ get; init => field = value.Date(); }
}

private string _firstName;
public string FirstName
{
    get
    {
        return _firstName;
    }
    set
    {
        if (value.Trim() == "")
            throw new ArgumentException("No blank strings");
        _firstName = value;
    }
}
Now you can use an autoimplemented property and field:
public string FirstName {get;
    set
    {
        if (value.Trim() == "")
            throw new ArgumentException("No blank strings");
        field = value;
    }
}