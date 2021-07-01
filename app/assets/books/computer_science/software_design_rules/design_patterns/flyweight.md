## flyweight 

STRUCTURAL PATTERN

Use sharing to support large numbers of fine-grained objects efficiently.

Autorise le partage de nombreux objets de petite granularité
A fine-grained instance used for efficient sharing

Minimiser le nombre d'instance and distinguant deux états dans un objet :

Etat personnel ( lié à chaque objet )
Etat global ( indépendant de l'objet )
Ex : Caractères dans un traitement de texte, avec le code ASCII pour l'état personnel et la position du caractère pour l'état global

Intention
petits objets destinés à être partagésOn utilise Flyweight lorsque :
• on utilise beaucoup d'objets, et
• les coûts de sauvegarde sont élevés, et
• l'état des objets peut être externalisé (extrinsic), et
• de nombreux groupes d'objets peuvent être remplacés par quelques objets partagés un fois que les états sont externalisés, et
• l'application ne dépend pas de l'identité des objetsMotivation
Solution

![](assets/books/computer_science/software_design_rules/design_patterns/flyweight.png)


```js
public class CaracterView extends View {
        public void draw() {
    ...
        }

        // Personal state       
        char c;
}

public void Editor {
        public void initCars() {
    ... 
    // Reset carView for all caracters once
        }

        public void addCaracterView( char c ) {
    cars.addElement( carView.get( c ) );  
        }

        public void draw() {
    // Compute the global state       

    // Paint using cars View
        }

        Hashtable carView = new Hastable();
        Vector cars = new Vector();
}
```