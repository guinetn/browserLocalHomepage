# Linq To SQL

API for working with SQL Server databases
generates object-relational mapping (ORM) implementation to seamlessly maps tables and columns to classes and properties with the help of mapping attributes

Ex:
New Console Application 
Right click on your project name (Solution Explorer)
Add > New Item > Data > LINQ to SQL Classes template
Give the file same name as the database as SampleDB.dbml

Drag the Categories and Products table to the designer surface 

SampleDB.dbml 
SampleDB.designer.cs
 
[System.Data.Linq.Mapping.DatabaseAttribute(Name="SampleDB")]
public partial class SampleDBDataContext : System.Data.Linq.DataContext
{
 
}
[Table(Name="dbo.Categories")]
public partial class Category : INotifyPropertyChanging, INotifyPropertyChanged
{
 
}
[Column(Storage="_CategoryName", DbType="NVarChar(50) NOT NULL", CanBeNull=false)]
public string CategoryName
{
 
}

string constr = @"Server=Waqas\SQLEXPRESS; Database=SampleDB; uid=sa; pwd=123;";
SampleDBDataContext db = new SampleDBDataContext(constr);
var query = from c in db.Categories
            orderby c.CategoryID
            select c;
 
foreach (var item in query)
{
    Console.WriteLine(item.CategoryID + " : " + item.CategoryName);
}

## More

- https://www.ezzylearning.net/tutorial/introduction-to-linq-to-sql