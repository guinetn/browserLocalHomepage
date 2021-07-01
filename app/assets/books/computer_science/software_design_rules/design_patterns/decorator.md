## decorator 

STRUCTURAL PATTERN

Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

add new properties to objects by placing these objects inside wrappers
add properties to a particular object at run-time, and this does not affect any other object of the same class.

Ajout de fonctions dynamiquement
Add responsibilities to objects dynamically
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
Pouvoir enrichir dynamiquement la représentation graphique d'un objet.

Permet d'accrocher dynamiquement (à l'exécution) de nouvelles fonctions à un objet. Utilise les capacités d'autres objets. 3é voie de
L'héritage/Interface
Intention
ajoute des services à un objetOn utilise Decorator lorsque :• il faut ajouter des responsabilités dynamiquement et de manière transparente• il existe des responsabilités dont on peut se passer• des extensions sont indépendantes et qu'il serait impraticable d'implanter par sous-classage
Motivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/decorator.png)


```js
// Decorator for any rendering
public class ExtendedRenderer extends Renderer {
        public void addRenderer( Renderer renderer ) {
        ...
        }

        public void removeRenderer( Renderer renderer ) {
        ...
        }

        public void paint( Grapics gc ) {
    // Paint all renderer
    ...
        }
}

```