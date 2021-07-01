### CODE REVIEW

Perform, improve, make reliable, learn, give

download.page(computer_science/software_design_rules/code_review_how_to_read_code.md)


* Is There a Change in the Unit Test?
Fixing the bug in the code should be accompanied by the addition or modification of the unit test.
A pull request that contains a code change to fix a bug but does not contain a change in unit tests is a smell.

* Are We Fixing a Root Cause or Just a Symptom?
```c#
public decimal CalculateOrderPrice(int orderId)
{
   Order order = _orderRepository.GetOrder(orderId);
   decimal price = order.Price; // order is reference type: potential null reference here
}
```

the null reference exception is just a symptom of a more serious problem, such as logic of order creation. This original root cause can cause problems in different places of application, and simply adding a null check will not solve the root problem.