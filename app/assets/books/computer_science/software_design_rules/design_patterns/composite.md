## composite 

STRUCTURAL PATTERN

Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
Makes sure the group of objects behaves in the same way as an individual object.

Pour créer des structures arborescentes d'objets ayant une relation tout/parties
Pouvoir faire évoluer des classes d'abstraction (ex: une fenêtre) sans toucher au niveau implémentation (ex: une fenêtre pour window).

Pas de différentiation entre un aggrégat d'objets et un objet.

Ex : Dans un logiciel de dessin vectoriel un groupe d'objets lié est un nouvel objet.

A tree structure of simple and composite objects
Intention
basé sur des objets primitifs et composantsOn utilise Composite lorsque on veut :• représenter une hiérarchie d'objets• ignorer la différence entre un composant simple et un composant en contenant d'autres. (interface uniforme)
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/composite.png)


```js
public class GroupComponent extends Component {
        public void addComponent( Component component ) {
    ...
        }

        public void removeComponent( Component component ) {
    ...
        }

        public void paint( Graphics gc ) {
    // Paint each sub component
        }
}
```