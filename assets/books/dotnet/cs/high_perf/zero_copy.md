## ZERO COPY - Avoid copying

**Problem:** Oparations on "sub-data" require a temporary object to represent it, which introduces a lot of short-living objects. Typical examples are `string.Substring()` or sub-arrays/sub-lists.
**Solution:** Introduce special types that allow *slicing* - represnting sub-regions without a memory copy.
**Benefits:** You can operate on subset of data without overhead of memory copy - especially useful in various "descendant" parsers.
**Consequences:** API and code is being polluted with technical-specific types, instead of using generic, intuitive ones.


download.page(dotnet/types/val/span.md)

Other examples:
* System.IO.Pipelines
* `ref` returning and argument passing

ref returning collection
```cs
public class RefValueBookCollection
{
	public ValueBook[] books = {
		new ValueBook { Title = "Call of the Wild, The", Author = "Jack London" },
		new ValueBook { Title = "Tale of Two Cities, A", Author = "Charles Dickens" } };
	private ValueBook nobook = default;
	public ref ValueBook GetBookByTitle(string title)
	{
		for (int ctr = 0; ctr < books.Length; ctr++)
			if (title == books[ctr].Title)
				return ref books[ctr];
		return ref nobook;
	}

	public static void Run()
	{
		var collection = new RefValueBookCollection();
		ref var book = ref collection.GetBookByTitle("Call of the Wild, The");
		book.Author = "Konrad Kokosa";
		Console.WriteLine(collection.books[0].Author);
	}
}
```
