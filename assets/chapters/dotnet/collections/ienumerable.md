# IEnumerable

Exposes an enumerator, which supports a simple iteration over a non-generic collection.
System.Collections

GetEnumerator()					Returns an enumerator that iterates through a collection.
Cast<TResult>(IEnumerable)		Casts the elements of an IEnumerable to the specified type
OfType<TResult>(IEnumerable)	Filters the elements of an IEnumerable based on a specified type
AsParallel(IEnumerable)			Enables parallelization of a query
AsQueryable(IEnumerable)		Converts an IEnumerable to an IQueryable

```cs
using static System.Console;
using static System.Linq.Enumerable;
        
namespace System.Query
{
	public static class Sequence
	{
		public static IEnumerable<S> Select<T,S>(this IEnumerable<T> source, Func<T,S> selector)
		{
			foreach (T element in source) 
				yield return selector(element);
		}
	}
    
    public class Program
    {
        static void Main()
        { }
    }
}

List<Customer> customers = GetCustomerList();
IEnumerable<string> names = customers.Select(c => c.Name);
IEnumerable<string> names = Sequence.Select(customers, c => c.Name);

// type inference for the invocation
static Z F<X,Y,Z>(X value, Func<X,Y> f1, Func<Y,Z> f2) {
	return f2(f1(value));
}
double seconds = F("1:15:30", s => TimeSpan.Parse(s), t => t.TotalSeconds);
```

# IEnumerable<T>

public interface IEnumerable<out T> : System.Collections.IEnumerable
System.Collections.Generic
T: type of objects to enumerate, this type parameter is covariant (use either the type you specified or any type that is more derived)