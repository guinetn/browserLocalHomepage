## NULLABLE REFERENCE TYPES

    string s = null;
    WriteLine($"The first letter of {s} is {s[0]}"); // "null reference exception"

Nullable reference types feature intends to warn you about null-unsafe behavior in the code. 

myproject.csproj
```cs
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp3.1</TargetFramework>
  </PropertyGroup>

  <PropertyGroup>
    <Nullable>enable</Nullable>
    or
    <NullableReferenceTypes>true</NullableReferenceTypes>     turn them on
  </PropertyGroup>

</Project>
```


mycode.cs
```c#    
        string? s = null;
        WriteLine($"The first letter of {s} is {s[0]}");                        Warning
        if (s != null) WriteLine($"The first letter of {s} is {s[0]}");         Fix 1
        WriteLine($"The first letter of {s} is {s?[0] ?? '?'}");                Fix 2
                                                    ↓     ↓
                                                    ↓   Null-coalescing operator ??   '?' replaces a null value with the char '?'. Avoid null dereferences
                                                    ↓                                                 
                                            Null conditional indexing operator s?[0]
                                                * avoids the dereference 
                                                * produces a null if s is null (has nullable char?) 
```

## null references = Defensive programming

Defensive design intended to ensure the continuing function of a piece of software under unforeseen circumstances.
Logical branches leading to hypothetical test scenarios.
Adding a catch block for NullReferenceException.
Added responsibilities on the consumers of the class/the block of code to deal with null v

- Enforce NULL checks at compiler time
C# 8.0 introduce Nullable and Non-Nullable Reference Types to enforce a project wide rule for all or any reference type objects to follow null checks.

```cs
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp3.1</TargetFramework>
  </PropertyGroup>

  <PropertyGroup>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

- Using Option Types to avoid NULL types altogether

completely avoid the NullReferenceException from your application
Use [LanguageExt.Core](https://github.com/louthy/language-ext) nuget library for implementing Option Types  
Provides a type named `Option<>` that allows you to simply define your functions’ return types as option types. 

Either returns the cache object if it the key matches (Some) or returns Option<TResult>.None if the key doesn’t match.
```cs
public class CacheProvider : ICacheProvider
{
        private readonly ObjectCache _objectCache;

        public CacheProvider()
        {
                _objectCache = new MemoryCache("CustomerCache");
        }

        public Option<TResult> Get<TResult>(string key)
        {
                return _objectCache.Contains(key) ? (TResult) _objectCache[key] : Option<TResult>.None;
        }

        public void Add<TResult>(string key, TResult item)
        {
                _objectCache.Add(key, item, DateTimeOffset.Now.AddHours(1));
        }
}
```

Easier for the CacheProvider's consumers to validating the response:
```cs
[HttpGet("{id}")]
public IActionResult Get([FromRoute] string id)
{
  var customer = _cacheProvider.Get<Customer>(id);

  if (customer == null)
  {
    NotFound();
  }

  return Ok(customer);
}

// provide an appropriate response to the API consumers instead of adding a null check and then responding based on that (last line)
[ApiController]
[Route("api/customers")]
public class CustomerController : ControllerBase
{
	private readonly ICacheProvider _cacheProvider;

	public CustomerController(ICacheProvider cacheProvider)
	{
		_cacheProvider = cacheProvider;
	}

	[HttpGet("{id}")]
	public IActionResult Get([FromRoute] string id)
	{
		var customer = _cacheProvider.Get<Customer>(id);

		return customer.Match<IActionResult>(c => Ok(c), NotFound);
	}
}
```

Easier tests
Unit testing the CacheProvider becomes equally simpler as we are not focusing on writing tests for null reference checks here.
```cs
[TestFixture]
public class CacheProviderShould
{
	private const string KeyThatExists = "KEY_THAT_EXISTS";
	private const string KeyThatDoesNotExist = "KEY_THAT_DOES_NOT_EXIST";

	private Customer CreateNewCustomer()
	{
		return new Customer
		{
			FirstName = "Vighneshwar",
			LastName = "Madas"
		};
	}

	[Test]
	public void Not_Provide_A_CacheObject_When_An_Item_With_Matching_Key_Is_Not_Found()
	{
		//Arrange
		var cacheProvider = new CacheProvider();
		cacheProvider.Add(KeyThatExists, CreateNewCustomer());

		//Act
		var actual = cacheProvider.Get<Customer>(KeyThatDoesNotExist);

		//Assert
		actual.IsNone.Should().BeTrue();
	}

	[Test]
	public void Provide_A_CacheObject_When_An_Item_With_Matching_Key_Is_Found()
	{
		//Arrange
		var cacheProvider = new CacheProvider();
		cacheProvider.Add(KeyThatExists, CreateNewCustomer());

		//Act
		var actual = cacheProvider.Get<Customer>(KeyThatExists);

		//Assert
		actual.IsSome.Should().BeTrue();
	}
}
```
