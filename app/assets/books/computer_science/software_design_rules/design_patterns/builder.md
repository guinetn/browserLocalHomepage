## builder 

CREATIONAL PATTERN

Créer un objet complexe à partir d'objets plus simples
Séparer la construction d'un objet complexe de sa représentation
Separate the construction of a complex object from its representation so that the same construction process can create different representations
Extensibility problem
Adding new methods to Builder and ConcreteBuilder classes is impossible without modifying the source code.

Used programming technique(s)

Method addition to Builder and ConcreteBuilder classes.

Consequences

(+) New methods can be added to Builder and ConcreteBuilder classes without modifying the source code.
(-) Addition of both a new method and a new ConcreteBuilder requires a complementary module; however, if default behavior
of the method can be implemented in Builder, e.g. default behavior is to do nothing, no complementary module is required.

Separate the construction of a complex object from its representation so that the same construction process can create different representations

Déléguer la construction d'un objet sur d'autres classes.

Separates object construction from its representation

Intention
passe en paramètre un objet qui sait construire l'objet à partir d'une descriptionOn utilise le Builder lorsque :• l'algorithme pour créer un objet doit être indépendant des parties qui le compose et de la façon de les assembler • le processus de construction permet différentes représentations de l'objet construit
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/builder.png)


```js
public interface RepositoryBuilder {
        public void buildContent();
        public RepositoryContent getContent();
}

public class ConcreteRepositoryBuilder implements RepositoryBuilder {
        public void buildContent() { files = ( new File( "." ) ).list();  }
        public getContent() { return new RepositoryContent( files );      }
        String[] files;
}

```