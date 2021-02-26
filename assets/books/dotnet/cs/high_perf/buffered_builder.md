# Buffered Builder

**Problem:** We generate a lot of temporary objects due to many operations on immutable data.
**Solution:** We create "builder" to manipulate data of immutable nature as "mutable". Ultra popular example is `StringBuilder`.
**Benefits:** A lot less pressure on the GC, better data locality (internal buffer)
**Consequences:** Slightly more complex API than just using plain immutable data.


```cs
[HttpGet]
[Route("values/concatenated/{count}")]
public string GetConcatenated(int count)
{
    Random rand = new Random();
    var result = "<Customers>";
    for (int i = 0; i <= count; i++)
    {
        result += "<Customer Id=\"";
        result += i.ToString();
        result += "\" lastUpdateDate=\"";
        result += DateTime.Now.ToString();
        result += "\" branchId=\"";
        result += i.ToString();
        result += "\" firstName=\"";
        result += i.ToString(); ;
        result += "\" lastName=\"";
        result += "A customer with the Id: ";
        result += i.ToString();
        result += "\" ranking=\"";
        result += rand.Next(100).ToString();
        result += "\"/>";
    }
    result += "</Customers>";
    return result;
}
```

```cs
[HttpGet]
[Route("values/builder/{count}")]
public string GetBuilder(int count)
{
    Random rand = new Random();
    var sb = new StringBuilder("<Customers>");
    for (int i = 0; i <= count; i++)
    {
        sb.Append("<Customer Id=\"");
        sb.Append(i.ToString());
        sb.Append("\" lastUpdateDate=\"");
        sb.Append(DateTime.Now.ToString());
        sb.Append("\" branchId=\"");
        sb.Append(i.ToString());
        sb.Append("\" firstName=\"");
        sb.Append(i.ToString());
        sb.Append("\" lastName=\"");
        sb.Append("A customer with the Id: ");
        sb.Append(i.ToString());
        sb.Append("\" ranking=\"");
        sb.Append(rand.Next(100).ToString());
        sb.Append("\"/>");
    }
    sb.Append("</Customers>");
    return sb.ToString();
}
```

For example - `BigInteger`. Proposal [Expose a BigInteger.Builder to help avoid so many copies/allocations](https://github.com/dotnet/corefx/issues/37204):

*"`System.Numerics.BigInteger` is an immutable struct that frequently works with "big data". This can cause it to be very ineffecient to use given that you need to create a new immutable struct for every operation. As such, I propose we expose a new `BigInteger.Builder` type which allows for multiple operations to be performed on a mutable class before ultimately serializing the final result back to a regular `BigInteger`"*

```cs
public sealed class Builder : ...
{
	public static Builder Abs(Builder value);
	public static Builder Add(Builder left, Builder right);
	public static Builder Divide(Builder dividend, Builder divisor);
	public static Builder Multiply(Builder left, Builder right);
	public static Builder Negate(Builder value);
	public static Builder Pow(Builder value, int exponent);
	public static Builder Remainder(Builder dividend, Builder divisor);
	...
	public BigInteger ToBigInteger();
}
```

---

```cs
public ref struct ValueStringBuilder
{
	private char[] _arrayToReturnToPool;
	private Span<char> _chars;
	private int _pos;

	public ValueStringBuilder(Span<char> initialBuffer)
	{
		_arrayToReturnToPool = null;
		_chars = initialBuffer;
		_pos = 0;
	}
	
	public ref char this[int index] => ref _chars[index];
	
	public void Append(char c)
	{
		int pos = _pos;
		if (pos < _chars.Length)
		{
			_chars[pos] = c;
			_pos = pos + 1;
		}
		else
			GrowAndAppend(c);
	}
	
	private void GrowAndAppend(char c)
	{
		Grow(1);
		Append(c);
	}
	...
```

???

Combination of this and #4 and #5: ValueStringBuilder (stacklloc internal buffer)

```cs
	...
	private void Grow(int requiredAdditionalCapacity)
	{
		Debug.Assert(requiredAdditionalCapacity > 0);
		char[] poolArray = ArrayPool<char>.Shared.Rent(Math.Max(_pos +
							requiredAdditionalCapacity, _chars.Length * 2));
		_chars.CopyTo(poolArray);
		char[] toReturn = _arrayToReturnToPool;
		_chars = _arrayToReturnToPool = poolArray;
		if (toReturn != null)
		{
			ArrayPool<char>.Shared.Return(toReturn);
		}
	}
	
	public void Dispose()
	{
		char[] toReturn = _arrayToReturnToPool;
		if (toReturn != null)
		{
			ArrayPool<char>.Shared.Return(toReturn);
		}
	}	

	public void Append(string str)
	{
		foreach (char c in str)
			Append(c);
	}	
	
	public override string ToString() => new string(_chars.Slice(0, _pos));

	...
}
```

`ValueStringBuilder` example usage:

```cs
static string UseValueStringBuilder(string data)
{
	Span<char> initialBuffer = stackalloc char[32];
	using var builder = new ValueStringBuilder(initialBuffer);
	builder.Append("<tag>");
	builder.Append(data);
	builder.Append("</tag>");
	return builder.ToString();
}
```

```bash
|                Method |     Mean | Gen 0/1k Op | Gen 1 | Gen 2 | Allocated/Op |
|---------------------- |---------:|------------:|------:|------:|-------------:|
| UseValueStringBuilder | 44.23 ns |      0.0134 |     - |     - |         56 B |
|      UseStringBuilder | 51.53 ns |      0.0459 |     - |     - |        192 B |
```