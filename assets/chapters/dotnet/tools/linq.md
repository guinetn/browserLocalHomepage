# Linq

Enumerable.Range(1, 5).Select(i => {})

* Sort a string
var s = "zacb";
var s2 = String.Concat(s.OrderBy(c => c)); // abcz
var s2 = String.Concat(s.OrderBy(c => c).Distinct()); // remove duplicates


## More

- https://www.ezzylearning.net/tutorial/introduction-to-language-integrated-query-linq