# FLUENT ASSERTIONS

https://fluentassertions.com/introduction

.NET extension methods to more naturally specify the expected outcome of a TDD or BDD-style unit test.
Simple intuitive syntax 

// Verify that a string begins, ends and contains a particular phrase
using FluentAssertions;
string actual = "ABCDEFGHI";
actual.Should().StartWith("AB").And.EndWith("HI").And.Contain("EF").And.HaveLength(9);

// Verify that all elements of a collection match a predicate and that it contains a specified number of elements
IEnumerable numbers = new[] { 1, 2, 3 };
numbers.Should().OnlyContain(n => n > 0);
numbers.Should().HaveCount(4, "because we thought we put four items in the collection");

var recipe = new RecipeBuilder()
                    .With(new IngredientBuilder().For("Milk").WithQuantity(200, Unit.Milliliters))
                    .Build();
Action action = () => recipe.AddIngredient("Milk", 100, Unit.Spoon);
action
                    .Should().Throw<RuleViolationException>()
                    .WithMessage("*change the unit of an existing ingredient*")
                    .And.Violations.Should().Contain(BusinessRule.CannotChangeIngredientQuantity);
                    
dictionary.Should().ContainValue(myClass).Which.SomeProperty.Should().BeGreaterThan(0);
someObject.Should().BeOfType<Exception>().Which.Message.Should().Be("Other Message");
xDocument.Should().HaveElement("child").Which.Should().BeOfType<XElement>().And.HaveAttribute("attr", "1");                    