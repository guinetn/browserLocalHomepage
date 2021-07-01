## strategy 

BEHAVIOURAL PATTERN

The strategy design pattern allows you to replace the algorithm at runtime.
The pattern allows encapsulating algorithms into separate objects, which improves reusability, unit testing and maintainability.
A strategy is better to implement with an interface when it defines a group of methods.
A strategy can be implemented using a delegate if the strategy has a single method.


Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Encapsulates an algorithm inside a class
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Allow to modify an algorithm transparently (sorting...)
Strategy lets the algorithm vary independently from clients that use it.
Wider than the "state" pattern, allows you to choose an algorithm adapted to the context.

Intention
On utilise Strategy lorsque :
• de nombreuses classes associées ne diffèrent que par leur comportement. Stratégie offre un moyen de configurer une classe avec un comportement parmi plusieurs.
• on a besoin de plusieurs variantes d'algorithme.• un algorithme utilise des données que les clients ne doivent pas connaitre.Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/strategy.png)


```js
public class IndentDocument {
 public void setIndenter( Indenter indenter );

 // Depend on the context
 public void indent( Document doc ) {
 indenter.indent( doc );  
 }
}

// Indent document strategy
public interface Indenter {
 public void indent( Document doc );
}
```

- https://levelup.gitconnected.com/3-ways-to-implement-strategy-design-pattern-in-c-a58548d8a4ad