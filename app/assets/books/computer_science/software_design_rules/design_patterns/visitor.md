## visitor

BEHAVIOURAL PATTERN

Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

Classe définissant une opération sur une autre classe
L'objet visité publie une méthode ayant en paramètre la classe du visiteur.
Defines a new operation to a class without change
Represent operation to be performed on the elements of an object structure.
Visitor lets you define a new operation without changing the classes of the elements on which it operates.
Lors du parcours d'une structure, pouvoir concentrer les actions hors de l'élément de la structure.

Intention
On utilise Visitor lorsque :
• une structure d'objets contient de nombreuses classes avec des interfaces différentes et on veut appliquer des operations diverses sur ces objets.
• les structures sont assez stables, et les opération sur leurs objets évolutives.
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/visitor.png)


```js
public interface Visitor {
 public void actionForAllNode( Node node );
 public void actionForCustomNode( CustomNode node );
}

public class Node {
 public void accept( Visitor visitor ) {
  visitor.actionForAllNode( this );
 }
}

public class CustomNode extends Node {
 public void accept( Visitor visitor ) {
  visitor.actionForCustomNode( this );       
 }
}
```