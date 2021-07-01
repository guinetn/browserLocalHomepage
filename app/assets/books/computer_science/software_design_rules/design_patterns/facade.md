## facade 

STRUCTURAL PATTERN

Provide a unified interface to a set of interfaces in a subsystem. Façade defines a higher-level interface that makes the subsystem easier to use.

abstracts the underlying complexity and provides a convenient high-level interface.

Interfaces unifiées
Masque la complexité d'un système. Permet la modularité et la réutilisation
A single class that represents an entire subsystem
Provide a unified interface to a set of interfaces in a subsystem. Facede defines a higher-level interface that makes the subsystem easier to use.
Regrouper les intéractions avec une API dans une classe ou façade.

Intention
cache une structure complexeOn utilise Facade lorsque on veut :• fournir une interface simple à un système complexe• introduire une interface pour découpler les relations entre deux systèmes complexes• construire le système en couche
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/facade.png)


```js
// Facade for the dynamix API
public class DynamixFacade {
        // Merge data and the model to produce output
        public void transform( Hashtable data, String model, String output ) {
    ...
        }
}
```