# IEnumerator

To read the data in the collection, but they cannot be used to modify the underlying collection.
Base interface for all non-generic enumerators
Current			Gets the element in the collection at the current position of the enumerato
MoveNext()		Advances the enumerator to the next element of the collection.
Reset()			Sets the enumerator to its initial position, which is before the first element in the collection.

Initially, the enumerator is positioned before the first element in the collection. 
MoveNext() to advance the enumerator to the first element of the collection before reading the value of Current; otherwise, Current is undefined.
If MoveNext passes the end of the collection, the enumerator is positioned after the last element in the collection and MoveNext() returns false.

If changes are made to the collection, such as adding, modifying, or deleting elements, the behavior of the enumerator is undefined.

To guarantee thread safety during enumeration, you can either lock the collection during the entire enumeration or catch the exceptions resulting from changes made by other threads.


![](assets/books/dotnet/collections/assets/ienumerator.gif)

```cs
using System;
using System.Collections;

// Simple business object.
public class Person
{
    public Person(string fName, string lName)
    {
        this.firstName = fName;
        this.lastName = lName;
    }

    public string firstName;
    public string lastName;
}

// Collection of Person objects. This class
// implements IEnumerable so that it can be used
// with ForEach syntax.
public class People : IEnumerable
{
    private Person[] _people;
    public People(Person[] pArray)
    {
        _people = new Person[pArray.Length];

        for (int i = 0; i < pArray.Length; i++)
        {
            _people[i] = pArray[i];
        }
    }

	// Implementation for the GetEnumerator method.
    IEnumerator IEnumerable.GetEnumerator() { return (IEnumerator) GetEnumerator(); }
    public PeopleEnum GetEnumerator() { return new PeopleEnum(_people); }
}

// When you implement IEnumerable, you must also implement IEnumerator.
public class PeopleEnum : IEnumerator
{
    public Person[] _people;

    // Enumerators are positioned before the first element
    // until the first MoveNext() call.
    int position = -1;
    public PeopleEnum(Person[] list) { _people = list; }

    public bool MoveNext()
    {
        position++;
        return (position < _people.Length);
    }

    public void Reset() { position = -1; }
    object IEnumerator.Current { get { return Current; } }
    public Person Current
    {
        get {
            try { return _people[position]; }
            catch (IndexOutOfRangeException) { throw new InvalidOperationException(); }
        }
    }
}

class App
{
    static void Main()
    {
        Person[] peopleArray = new Person[3] { new Person("John", "Smith"), new Person("Jim", "Johnson"), new Person("Sue", "Rabon")};
        People peopleList = new People(peopleArray);
        foreach (Person p in peopleList)
            Console.WriteLine(p.firstName + " " + p.lastName);
    }
}
```
# IEnumerator<T>

System.Collections.Generic.IEnumerator<T>