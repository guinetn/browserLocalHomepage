## MONADS

Container types which encapsulate some kind of functionality
On top of that, they provide a way to combine two containers into one
hide the implementation details from the client, but provide a proper way to use the hidden functionality
often monads provide the way to avoid imperative code in favor of functional style.

monadic types as containers that hold any generic type. 
As long as the container holds the data type, it is possible to chain as many expressions as necessary
Elevate basic C# types and unlock functional patterns. 
Allows doting into expressions while remaining inside the abstraction

- https://mikhail.io/2016/01/monads-explained-in-csharp/


```c#
public class Monad<T>
{
    public Monad(T instance)
    {
    }
}

// Monads can be chained to create new monad
public class Monad<T>
{
    public Monad<TO> Bind<TO>(Func<T, Monad<TO>> func)
    {
    }
}

// Power of monads comes when we compose several of them in one chain:
initialValue
    .Return()
    .Bind(v1 => produceV2OutOfV1(v1))
    .Bind(v2 => produceV3OutOfV2(v2))
    .Bind(v3 => produceV4OutOfV3(v3))
    //...

// extension method to enable fluent syntax of monad creation:
public static class MonadExtensions
{
    public static Monad<T> Return<T>(this T instance) => new Monad<T>(instance);
}
```

Common Maybe implementations implements IEnumerable which allows a more C#-idiomatic binding composition

```c#
public class Maybe<T> where T : class
{
    private readonly T value;

    public Maybe(T someValue)
    {
        if (someValue == null)
            throw new ArgumentNullException(nameof(someValue));
        this.value = someValue;
    }

    private Maybe()
    {
    }

    public Maybe<TO> Bind<TO>(Func<T, Maybe<TO>> func) where TO : class
    {
        return value != null ? func(value) : Maybe<TO>.None();
    }

    public static Maybe<T> None() => new Maybe<T>();
}

public static class MaybeExtensions
{
    public static Maybe<T> Return<T>(this T value) where T : class
    {
        return value != null ? new Maybe<T>(value) : Maybe<T>.None();
    }
}
```

Use case. 
```c#
public interface ITraditionalRepository
{
    Customer GetCustomer(int id);
    Address GetAddress(int id);
    Order GetOrder(int id);
}

// client loading data one by one and tries to find a shipper:

Shipper shipperOfLastOrderOnCurrentAddress = null;
var customer = repo.GetCustomer(customerId);
if (customer?.Address != null)
{
    var address = repo.GetAddress(customer.Address.Id);
    if (address?.LastOrder != null)
    {
        var order = repo.GetOrder(address.LastOrder.Id);
        shipperOfLastOrderOnCurrentAddress = order?.Shipper;
    }
}
return shipperOfLastOrderOnCurrentAddress;
```

Same with monad code is fluent and linear
```c#

public interface IMonadicRepository
{
    Maybe<Customer> GetCustomer(int id);
    Maybe<Address> GetAddress(int id);
    Maybe<Order> GetOrder(int id);
}

Maybe<Shipper> shipperOfLastOrderOnCurrentAddress =
    repo.GetCustomer(customerId)
        .Bind(c => c.Address)
        .Bind(a => repo.GetAddress(a.Id))
        .Bind(a => a.LastOrder)
        .Bind(lo => repo.GetOrder(lo.Id))
        .Bind(o => o.Shipper);

```