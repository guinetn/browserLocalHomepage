## abstract factory

CREATIONAL PATTERN

Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

Création agnostique de classes différentes
Creates an instance of several families of classes
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

In order to add new kinds of products, new creation methods should be added to AbstractFactory and ConcreteFactory classes. (This problem is mentioned at p.90,line.4-9 in the GoF book.)

Used programming technique(s)
abstract method addition to AbstractFactory.
Consequences

(+) New kinds of products can be added without modifying the source code.
(-) Addition of both a new kind of products and a new concrete factory requires a complementary module.

Cacher la nature des objets créés par des interfaces tout en maintenant leurs cohérences.

Intention
on passe un paramètre à la création qui définit ce qu'on va créerOn utilise l'AbstractFactory lorsque :• un système doit être indépendant de la façon dont ses produits sont créés, assemblés, représentés• un système repose sur un produit d'une famille de produits• une famille de produits doivent être utilisés ensemble, pour renforcer cette contrainte• on veut définir une interface unique à une famille de produits concrets Motivation

Solution

![](assets/books/computer_science/software_design_rules/design_patterns/abstract_factory.png)

```js
public interface AbstractFactory {
        public Engine getEngine();
        public Tyre getTyre();
}

public class ConcreteFactorySNECMA implements AbstractFactory {
    public Engine getEngine() { return new EngineSNECMA();  }
    public Tyre getTyre() { return new TyreSNECMA(); }
}

```