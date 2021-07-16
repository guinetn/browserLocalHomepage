## A fake database in memory: Microsoft.EntityFrameworkCore.InMemory 

Microsoft.EntityFrameworkCore.InMemory 
>dotnet add package Microsoft.EntityFrameworkCore.InMemory --version 3.1.15
startup.cs
```c#
public void ConfigureServices(IServiceCollection services)
{
    services.AddDbContext<BaseControllerDBContext>(options => options.UseInMemoryDatabase("BaseController"));
    services.AddControllers();
}
```
- https://www.red-gate.com/simple-talk/dotnet/c-programming/build-a-rest-api-in-net-core/
- https://itnext.io/how-to-use-database-sharding-and-scale-an-asp-net-core-microservice-architecture-22c24916590f
- https://docs.microsoft.com/fr-fr/aspnet/core/tutorials/first-web-api?view=aspnetcore-5.0&tabs=visual-studio-code
- https://github.com/beautifulcoder/BuildRestApiNetCore


* IN-MEMORY DATABASE

- https://www.red-gate.com/simple-talk/dotnet/c-programming/build-a-rest-api-in-net-core/
>dotnet new sln
>dotnet new webapi --no-https
>dotnet sln add .
>dotnet add package Microsoft.EntityFrameworkCore.InMemory
>dotnet add package Microsoft.AspNetCore.Mvc.Versioning     set up api versioning

```c#
// inject database context in Startup class
services
  .AddDbContext<ProductContext>(opt => 
              opt.UseInMemoryDatabase("Products"));

services.AddApiVersioning(opt => opt.ReportApiVersions = true);
// https://semver.org/     using Semantic Versioning to communicate breaking changes in the API.

// Entity Framework DbContext               
public class ProductContext : DbContext
{
  public ProductContext(DbContextOptions<ProductContext> options) : base(options)
  {
  }
 
  public DbSet<Product> Products { get; set; }
}

Models/

public class Product
{
  [Key]
  [Required]
  [Display(Name = "productNumber")]
  public string ProductNumber { get; set; }
 
  [Required]
  [Display(Name = "name")]
  public string Name { get; set; }
 
  [Required]
  [Range(10, 90)]
  [Display(Name = "price")]
  public double? Price { get; set; }
 
  [Required]
  [Display(Name = "department")]
  public string Department { get; set; }
}

// extension method to help iterate through seed items
public  static class EnumerableExtensions
{
  public static IEnumerable<T> Times<T>(this int count, Func<int, T> func)
  {
    for (var i = 1; i <= count; i++) yield return func.Invoke(i);
  }
}

// initial seed:  list of 900 items
public static class ProductSeed
{
  public static void InitData(ProductContext context)
  {
    var rnd = new Random();
 
    var adjectives = new [] { "Small", "Ergonomic", "Rustic", 
                                        "Smart", "Sleek" };
    var materials = new [] { "Steel", "Wooden", "Concrete", "Plastic",
                                       "Granite", "Rubber" };
    var names = new [] { "Chair", "Car", "Computer", "Pants", "Shoes" };
    var departments = new [] { "Books", "Movies", "Music", 
                                       "Games", "Electronics" };
 
    context.Products.AddRange(900.Times(x =>
    {
      var adjective = adjectives[rnd.Next(0, 5)];
      var material = materials[rnd.Next(0, 5)];
      var name = names[rnd.Next(0, 5)];
      var department = departments[rnd.Next(0, 5)];
      var productId = $"{x, -3:000}";
 
      return new Product
      {
        ProductNumber = 
           $"{department.First()}{name.First()}{productId}",
        Name = $"{adjective} {material} {name}",
        Price = (double) rnd.Next(1000, 9000) / 100,
        Department = department
      };
    }));
 
    context.SaveChanges();
  }
}


// ProductsController
[ApiController]
[ApiVersion("1.0")]
[Route("v{version:apiVersion}/[controller]")]
[Produces("application/json")]
public class ProductsController : ControllerBase
{
  private readonly ProductContext _context;
 
  public ProductsController(ProductContext context)
  {
    _context = context;
 
    if (_context.Products.Any()) return;
 
    ProductSeed.InitData(context);
  }
}

[HttpGet]
[Route("")]
[ProducesResponseType(StatusCodes.Status200OK)]
public ActionResult<IQueryable<Product>> GetProducts()
{
  var result = _context.Products as IQueryable<Product>;
 
  return Ok(result
    .OrderBy(p => p.ProductNumber));
}
```
>dotnet watch run
>curl -i -X GET "http://localhost:5000/v1/products" -H "accept: application/json"
