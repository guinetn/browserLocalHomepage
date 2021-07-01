## factory 

CREATIONAL PATTERN

Permet de créer des instances dérivées d"un classe mère
Creates an instance of several derived classes
Define an interface for creating an object, but let subclasses decide which class to instantiated. Factory Method lets a class defer instantiation to subclasses.

Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

ype safety problem
The original GoF pattern requires downcast from Product to a ConcreteProduct in order to invoke the specific methods of the ConcreteProduct. (This problem is not mentioned in the GoF book.)
Complexity problem
The class structure of the original GoF pattern is complicated. (This problem is mentioned at p.113,line.1-3 in the GoF book.)
Used programming technique(s)

Implementation selection for Product and Creator.

Consequences

(+) Downcasts are no longer needed.
(+) Class structure is not complicated.
(-) This solution is applicable only if just one implementation of Product and Creator is used in a program.

Cacher la nature des objets créés par des interfaces et faciliter la conception par une règle.

Intention
la classe sollicité appelle des méthode abstraites ...il suffit de sous-classerOn utilise le FactoryMethod lorsque :• une classe ne peut anticiper la classe de l'objet qu'elle doit construire• une classe délègue la responsabilité de la création à ses sous-classes, tout en concentrant l'interface dans une classe unique
Motivation

Solution

![](assets/books/computer_science/software_design_rules/design_patterns/factory.png)


```js
public interface HeXaneNodeFactory {
        public Node getNode( String type );
}

public class ConreteHeXaneNodeFactory implements HeXaneNodeFactory {
        public Node getNode( String type ) {
         if ( "Component".equals( type ) )
   return new ComponentNode();
         else
         if ( "Link".equals( type ) ) 
   return new LinkNode();
         else
   return new DefaultNode();
        }
}
```