## Struct of Arrays

**Problem:** Processing a lot of data is not efficient due to the memory access time.
**Solution:** Design data structures and processing steps to leverage data locality and sequential access. Most typically, in the form of plain arrays of data.
**Benefits:** Much better memory access performance.
**Consequences:** Much worse design, violating object-oriented principles like encapsulation. Can be slightly worked around with the help of ECS.


"Array of Structs":
```cs
class CustomerClassRepository
{
  List<Customer> customers = new List<Customer>();
  public void UpdateScorings()
  {
    foreach (var customer in customers)
      customer.UpdateScoring();
  }
}
public class CustomerClass
{
  private double Earnings;
  private DateTime DateOfBirth;
  private bool IsSmoking;
  private double Scoring;
  private HealthData Health;
  private AuxiliaryData Auxiliary;
  private Company Employer;
  public void UpdateScoring()
  {
    Scoring = Earnings * (IsSmoking ? 0.8 : 1.0) * ProcessAge(DateOfBirth);
  }
  private double ProcessAge(DateTime dateOfBirth) => ...;
}
```

![](assets/books/dotnet/cs/assets/soa01.png)


"Array of Structs" (better++):
```cs
class CustomerValueRepository
{
  List<CustomerValue> customers = new List<CustomerValue>(); 
  public void UpdateScorings()
  {
    foreach (var customer in customers)
      customer.UpdateScoring();
  }
}
   
[StructLayout(LayoutKind.Sequential)]
public struct CustomerValue
{
  double Earnings;
  double Scoring;
  int YearOfBirth;
  bool IsSmoking;
  int HealthDataId;
  int AuxiliaryDataId;
  int EmployerId;  

  public void UpdateScoring()
  {
    Scoring = Earnings * (IsSmoking ? 0.8 : 1.0) * ProcessAge(YearOfBirth);
  }
  private double ProcessAge(int yearOfBirth) => ...;
}
```

"Array of Structs" (better):
![](assets/books/dotnet/cs/assets/soa02.png)


Struct of Arrays
```cs
class CustomerRepositoryDOD
{
  int NumberOfCustomers;
  double[] Scoring;
  double[] Earnings;
  bool[] IsSmoking;
  int[] YearOfBirth;
  DateTime[] DateOfBirth;
  public void UpdateScorings()
  {
     for (int i = 0; i < NumberOfCustomers; ++i)
        Scoring[i] = Earnings[i] * (IsSmoking[i] ? 0.8 : 1.0) 
		             * ProcessAge(YearOfBirth[i]);
  }
  public double ProcessAge(int yearOfBirth) => ...;
}
```
![](assets/books/dotnet/cs/assets/soa03.png)

```cs
       Method |       Mean | Allocated | LlcMisses/Op | LlcReference/Op |
------------- |-----------:|----------:|-------------:|----------------:|
  ObjectStyle | 2,152.5 us |       0 B |        24680 |           30031 |
  StructStyle | 1,442.0 us |       0 B |         1986 |            3937 |
     DoDStyle |   213.9 us |       0 B |          272 |             816 |
```

***10x faster***

Extensions:
* tree processing - flatten tree navigating it in pre-order depth-first manner...
* Entity Component System 


Struct of Arrays (Entity Component System)
.center[![:scale 60%](assets/books/dotnet/cs/assets/hperf_struct_of_arrays_01.png)]

Struct of Arrays (Entity Component System)
.center[![:scale 100%](assets/books/dotnet/cs/assets/hperf_struct_of_arrays_02.png)]

.center[![:scale 100%](assets/books/dotnet/cs/assets/hperf_struct_of_arrays_03.png)]

Examples from the real-world:
* Unity ECS
* Entitas

